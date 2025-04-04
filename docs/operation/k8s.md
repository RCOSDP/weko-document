# WEKO3 deployment note on Kubernetes

This article describes how to install WEKO3 in a Kubernates environment.

## Kubernates environment

The kubernetes environment used in this article is shown below.

```
                                           [haproxy]
                                               |
      -----------------------------------------------------------------------------------------
      |                |              |               |            |            |             |
 [node-k8s-1]     [node-k8s-2]   [node-k8s-3]    [node-k8s-4] [node-k8s-5] [node-k8s-6]  [node-k8s-7]
[control-plane] [control-plane] [control-plane]  [          ] [          ] [          ]  [          ]
                                                      |            |            |             |
                                                      -----------------------------------------
                                                                          |
                                                                     [nfs server]
```

# Prepare environment

## nfs-subdir-external-provisioner

In order to use NFS as a storage, install a NFS provider.

### Create namespace

Create a yaml file for namespace of external-provisioner.

```
$ vi namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: nfs-provisioner
```

Apply a yaml file.

```
$ kubectl apply -f namespace.yaml
namespace/nfs-provisioner created
```

Check that the namespace has been created.

```
$ kubectl get ns nfs-provisioner
NAME              STATUS   AGE
nfs-provisioner   Active   62s
```

### install nfs-subdir-external-provisioner with Helm

1. Add nfs-subdir-external-provisioner repository.

```
$ helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
"nfs-subdir-external-provisioner" has been added to your repositories

```

2. Install and configure nfs-subdir-external-provisioner

```
$ helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner  --set nfs.server=<NFS Server IP Address> --set nfs.path=/var/weko3data --set storageClass.name=nfs-client --namespace nfs-provisioner
NAME: nfs-subdir-external-provisioner
LAST DEPLOYED: Sat Oct  5 16:23:11 2024
NAMESPACE: nfs-provisioner
STATUS: deployed
REVISION: 1
TEST SUITE: None

```

3. Check installation result.

```
$ kubectl get all -n nfs-provisioner
NAME                                                   READY   STATUS    RESTARTS   AGE
pod/nfs-subdir-external-provisioner-7cd5d98b97-6xxmh   1/1     Running   0          62s

NAME                                              READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/nfs-subdir-external-provisioner   1/1     1            1           92s

NAME                                                         DESIRED   CURRENT   READY   AGE
replicaset.apps/nfs-subdir-external-provisioner-7cd5d98b97   1         1         1       64s

```

4. Check installation roles.

```
$ kubectl get clusterrole | grep nfs
nfs-subdir-external-provisioner-runner                                 2024-10-05T07:25:43Z
$ kubectl get clusterrolebinding | grep nfs
run-nfs-subdir-external-provisioner                             ClusterRole/nfs-subdir-external-provisioner-runner                                 13m
$ kubectl get role -n nfs-provisioner| grep nfs
leader-locking-nfs-subdir-external-provisioner   2024-10-05T07:25:44Z
$ kubectl get rolebinding -n nfs-provisioner| grep nfs
leader-locking-nfs-subdir-external-provisioner   Role/leader-locking-nfs-subdir-external-provisioner   16m
$ kubectl get serviceaccount -n nfs-provisioner| grep nfs
nfs-subdir-external-provisioner   0         13m

```

### test nfs-subdir-external-provisioner

1. Create yaml file for persistent volume claim.

```
$ cat test-claim.yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: test-claim
spec:
  storageClassName: nfs-client
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 1Mi

```

2. Create a PVC

```
$ kubectl apply -f test-claim.yaml
persistentvolumeclaim/test-claim created

```

3. Create a yaml file for testing POD.

```
$ cat test-pod.yaml
kind: Pod
apiVersion: v1
metadata:
  name: test-pod
spec:
  containers:
  - name: test-pod
    image: busybox:stable
    command:
      - "/bin/sh"
    args:
      - "-c"
      - "touch /mnt/SUCCESS && exit 0 || exit 1"
    volumeMounts:
      - name: nfs-pvc
        mountPath: "/mnt"
  restartPolicy: "Never"
  volumes:
    - name: nfs-pvc
      persistentVolumeClaim:
        claimName: test-claim

```

4. Create a pod.

```
$ kubectl apply -f test-pod.yaml
pod/test-pod created

```

5. Get pod status.

```
$ kubectl describe pod test-pod
Name:             test-pod
Namespace:        default
Priority:         0
Service Account:  default
Node:             node-k8s-6/10.50.50.176
Start Time:       Sat, 05 Oct 2024 16:30:33 +0900
Labels:           <none>
Annotations:      cni.projectcalico.org/containerID: de8ec96a4d1cf4a18f76df3e28bb5308b36e0681c58c78aed9bfc716097ca2dd
                  cni.projectcalico.org/podIP:
                  cni.projectcalico.org/podIPs:
Status:           Succeeded
IP:               10.233.119.67
IPs:
  IP:  10.233.119.67
Containers:
  test-pod:
    Container ID:  containerd://1150736a02cfe27c59a61920d9df70e577eb26656469c347dc306ae0ca8f519d
    Image:         busybox:stable
    Image ID:      docker.io/library/busybox@sha256:c230832bd3b0be59a6c47ed64294f9ce71e91b327957920b6929a0caa8353140
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/sh
    Args:
      -c
      touch /mnt/SUCCESS && exit 0 || exit 1
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sat, 05 Oct 2024 16:30:34 +0900
      Finished:     Sat, 05 Oct 2024 16:30:34 +0900
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /mnt from nfs-pvc (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-v6jnb (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   False
  Initialized                 True
  Ready                       False
  ContainersReady             False
  PodScheduled                True
Volumes:
  nfs-pvc:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  test-claim
    ReadOnly:   false
  kube-api-access-v6jnb:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  64s   default-scheduler  Successfully assigned default/test-pod to node-k8s-6
  Normal  Pulled     0s    kubelet            Container image "busybox:stable" already present on machine
  Normal  Created    0s    kubelet            Created container test-pod
  Normal  Started    0s    kubelet            Started container test-pod

```

## Ingress-nginx

1. install ingress-nginx from github

```
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/refs/heads/main/deploy/static/provider/baremetal/deploy.yaml
namespace/ingress-nginx unchanged
serviceaccount/ingress-nginx unchanged
serviceaccount/ingress-nginx-admission unchanged
role.rbac.authorization.k8s.io/ingress-nginx unchanged
role.rbac.authorization.k8s.io/ingress-nginx-admission unchanged
clusterrole.rbac.authorization.k8s.io/ingress-nginx unchanged
clusterrole.rbac.authorization.k8s.io/ingress-nginx-admission unchanged
rolebinding.rbac.authorization.k8s.io/ingress-nginx unchanged
rolebinding.rbac.authorization.k8s.io/ingress-nginx-admission unchanged
clusterrolebinding.rbac.authorization.k8s.io/ingress-nginx unchanged
clusterrolebinding.rbac.authorization.k8s.io/ingress-nginx-admission unchanged
configmap/ingress-nginx-controller unchanged
service/ingress-nginx-controller configured
service/ingress-nginx-controller-admission unchanged
deployment.apps/ingress-nginx-controller created
job.batch/ingress-nginx-admission-create unchanged
job.batch/ingress-nginx-admission-patch unchanged
ingressclass.networking.k8s.io/nginx unchanged
validatingwebhookconfiguration.admissionregistration.k8s.io/ingress-nginx-admission configured

```

2. check running status

```
$ kubectl get pod,svc -n ingress-nginx
NAME                                            READY   STATUS      RESTARTS   AGE
pod/ingress-nginx-admission-create-8pcpf        0/1     Completed   0          19m
pod/ingress-nginx-admission-patch-mt82v         0/1     Completed   0          19m
pod/ingress-nginx-controller-54cf9c8856-6xmcw   1/1     Running     0          2m18s

NAME                                         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                      AGE
service/ingress-nginx-controller             NodePort    10.233.6.14    <none>        80:31060/TCP,443:30640/TCP   90d
service/ingress-nginx-controller-admission   ClusterIP   10.233.7.196   <none>        443/TCP                      90d

```


## PostgreSQL

1. Create yaml file for PostgreSQL

```
$ vi deploy.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: weko3pg
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: postgres-operator
  namespace: weko3pg
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: postgres-pod-config
  namespace: weko3pg
data:
  ALLOW_NOSSL: "true"
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: postgres-operator
  namespace: weko3pg
rules:
- apiGroups:
  - acid.zalan.do
  resources:
  - postgresqls
  - postgresqls/status
  - operatorconfigurations
  verbs:
  - create
  - delete
  - deletecollection
  - get
  - list
  - patch
  - update
  - watch
- apiGroups:
  - acid.zalan.do
  resources:
  - postgresteams
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - apiextensions.k8s.io
  resources:
  - customresourcedefinitions
  verbs:
  - create
  - get
  - patch
  - update
- apiGroups:
  - ""
  resources:
  - configmaps
  verbs:
  - get
- apiGroups:
  - ""
  resources:
  - events
  verbs:
  - create
  - get
  - list
  - patch
  - update
  - watch
- apiGroups:
  - ""
  resources:
  - endpoints
  verbs:
  - create
  - delete
  - deletecollection
  - get
  - list
  - patch
  - update
  - watch
- apiGroups:
  - ""
  resources:
  - secrets
  verbs:
  - create
  - delete
  - get
  - update
- apiGroups:
  - ""
  resources:
  - nodes
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - ""
  resources:
  - persistentvolumeclaims
  verbs:
  - delete
  - get
  - list
  - patch
  - update
- apiGroups:
  - ""
  resources:
  - persistentvolumes
  verbs:
  - get
  - list
  - update
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - delete
  - get
  - list
  - patch
  - update
  - watch
- apiGroups:
  - ""
  resources:
  - pods/exec
  verbs:
  - create
- apiGroups:
  - ""
  resources:
  - services
  verbs:
  - create
  - delete
  - get
  - patch
  - update
- apiGroups:
  - apps
  resources:
  - statefulsets
  - deployments
  verbs:
  - create
  - delete
  - get
  - list
  - patch
- apiGroups:
  - batch
  resources:
  - cronjobs
  verbs:
  - create
  - delete
  - get
  - list
  - patch
  - update
- apiGroups:
  - ""
  resources:
  - namespaces
  verbs:
  - get
- apiGroups:
  - policy
  resources:
  - poddisruptionbudgets
  verbs:
  - create
  - delete
  - get
- apiGroups:
  - ""
  resources:
  - serviceaccounts
  verbs:
  - get
  - create
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - rolebindings
  verbs:
  - get
  - create
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: postgres-pod
  namespace: weko3pg
rules:
- apiGroups:
  - ""
  resources:
  - endpoints
  verbs:
  - create
  - delete
  - deletecollection
  - get
  - list
  - patch
  - update
  - watch
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - get
  - list
  - patch
  - update
  - watch
- apiGroups:
  - ""
  resources:
  - services
  verbs:
  - create
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: postgres-operator
  namespace: weko3pg
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: postgres-operator
subjects:
- kind: ServiceAccount
  name: postgres-operator
  namespace: weko3pg
---
apiVersion: v1
data:
  PGPOOL_PARAMS_BACKEND_CLUSTERING_MODE: streaming_replication
  PGPOOL_PARAMS_BACKEND_FLAG0: ALWAYS_PRIMARY|DISALLOW_TO_FAILOVER
  PGPOOL_PARAMS_BACKEND_FLAG1: DISALLOW_TO_FAILOVER
  PGPOOL_PARAMS_BACKEND_HOSTNAME0: weko-postgresql.weko3pg
  PGPOOL_PARAMS_BACKEND_HOSTNAME1: weko-postgresql-repl.weko3pg
  PGPOOL_PARAMS_BACKEND_PORT0: "5432"
  PGPOOL_PARAMS_BACKEND_PORT1: "5432"
  PGPOOL_PARAMS_BACKEND_WEIGHT0: "0"
  PGPOOL_PARAMS_BACKEND_WEIGHT1: "1"
  PGPOOL_PARAMS_CHILD_LIFE_TIME: "300"
  PGPOOL_PARAMS_CHILD_MAX_CONNECTIONS: "0"
  PGPOOL_PARAMS_CLIENT_IDLE_LIMIT: "900"
  PGPOOL_PARAMS_CONNECTION_CACHE: "on"
  PGPOOL_PARAMS_CONNECTION_LIFE_TIME: "0"
  PGPOOL_PARAMS_DEBUG_LEVEL: "0"
  PGPOOL_PARAMS_ENABLE_POOL_HBA: "on"
  PGPOOL_PARAMS_FAILOVER_ON_BACKEND_ERROR: "off"
  PGPOOL_PARAMS_LISTEN_ADDRESSES: '*'
  PGPOOL_PARAMS_LOAD_BALANCE_MODE: "on"
  PGPOOL_PARAMS_MAX_POOL: "10"
  PGPOOL_PARAMS_NUM_INIT_CHILDREN: "60"
  PGPOOL_PARAMS_PCP_LISTEN_ADDRESSES: '*'
  PGPOOL_PARAMS_PCP_PORT: "9898"
  PGPOOL_PARAMS_PCP_SOCKET_DIR: /var/run/pgpool
  PGPOOL_PARAMS_PORT: "5432"
  PGPOOL_PARAMS_RELCACHE_SIZE: "10000"
  PGPOOL_PARAMS_SOCKET_DIR: /var/run/pgpool
  PGPOOL_PARAMS_SR_CHECK_PERIOD: "0"
  PGPOOL_PARAMS_SSL: "off"
kind: ConfigMap
metadata:
  labels:
    app: pgpool-config
  name: pgpool-config
  namespace: weko3pg
---
apiVersion: v1
data:
  pool_hba.conf: |-
    local   all         all                               trust
    host    all         all         127.0.0.1/32          trust
    host    all         all         ::1/128               trust
    host    all         all         0.0.0.0/0             md5
kind: ConfigMap
metadata:
  labels:
    app: pgpool-hba-config
  name: pgpool-hba-config
  namespace: weko3pg
---
apiVersion: v1
data:
  api_port: "8080"
  aws_region: eu-central-1
  cluster_domain: cluster.local
  cluster_history_entries: "1000"
  cluster_labels: application:spilo
  cluster_name_label: weko3pg
  connection_pooler_image: registry.opensource.zalan.do/acid/pgbouncer:master-16
  db_hosted_zone: db.example.com
  debug_logging: "true"
  docker_image: registry.opensource.zalan.do/acid/spilo-13:2.0-p6
  enable_ebs_gp3_migration: "false"
  enable_master_load_balancer: "false"
  enable_pgversion_env_var: "true"
  enable_replica_load_balancer: "false"
  enable_spilo_wal_path_compat: "true"
  enable_teams_api: "false"
  external_traffic_policy: Cluster
  infrastructure_roles_secret_name: weko3pg/postgresql-infrastructure-roles
  major_version_upgrade_mode: manual
  master_dns_name_format: '{cluster}.{team}.{hostedzone}'
  pdb_name_format: postgres-{cluster}-pdb
  pod_deletion_wait_timeout: 10m
  pod_environment_configmap: weko3pg/postgres-pod-config
  pod_label_wait_timeout: 10m
  pod_management_policy: ordered_ready
  pod_role_label: spilo-role
  pod_service_account_name: postgres-pod
  pod_terminate_grace_period: 5m
  ready_wait_interval: 3s
  ready_wait_timeout: 30s
  repair_period: 5m
  replica_dns_name_format: '{cluster}-repl.{team}.{hostedzone}'
  replication_username: invenio_cl
  resource_check_interval: 3s
  resource_check_timeout: 10m
  resync_period: 30m
  ring_log_lines: "100"
  secret_name_template: '{username}.{cluster}.credentials'
  spilo_allow_privilege_escalation: "true"
  spilo_privileged: "false"
  storage_resize_mode: pvc
  super_username: postgres
  watched_namespace: '*'
  workers: "8"
kind: ConfigMap
metadata:
  name: postgres-operator
  namespace: weko3pg
---
apiVersion: v1
data:
  invenio: |
    user_flags:
      - createdb
kind: ConfigMap
metadata:
  name: postgresql-infrastructure-roles
  namespace: weko3pg
---
apiVersion: v1
data:
  invenio: ZGJwYXNzMTIz
kind: Secret
metadata:
  name: postgresql-infrastructure-roles
  namespace: weko3pg
type: Opaque
---
apiVersion: v1
kind: Service
metadata:
  name: pgpool
  namespace: weko3pg
spec:
  ports:
  - name: pgpool-port
    port: 5432
    protocol: TCP
    targetPort: 5432
  selector:
    app: pgpool
---
apiVersion: v1
kind: Service
metadata:
  name: postgres-operator
  namespace: weko3pg
spec:
  ports:
  - port: 8080
    protocol: TCP
    targetPort: 8080
  selector:
    name: postgres-operator
  type: ClusterIP
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-postgresql-backup
  namespace: weko3pg
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 50Gi
  storageClassName: nfs-client
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    application: postgres-operator
  name: postgres-operator
  namespace: weko3pg
spec:
  replicas: 1
  selector:
    matchLabels:
      name: postgres-operator
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        name: postgres-operator
    spec:
      containers:
      - env:
        - name: CONFIG_MAP_NAME
          value: postgres-operator
        image: registry.opensource.zalan.do/acid/postgres-operator:v1.10.1
        imagePullPolicy: IfNotPresent
        name: postgres-operator
        resources:
          limits:
            cpu: 500m
            memory: 500Mi
          requests:
            cpu: 100m
            memory: 250Mi
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          runAsNonRoot: true
          runAsUser: 1000
      serviceAccountName: postgres-operator
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: weko-pgpool
  namespace: weko3pg
spec:
  replicas: 1
  selector:
    matchLabels:
      app: pgpool
  template:
    metadata:
      labels:
        app: pgpool
    spec:
      containers:
      - env:
        - name: POSTGRES_USERNAME
          valueFrom:
            secretKeyRef:
              key: username
              name: invenio.weko-postgresql.credentials
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              key: password
              name: invenio.weko-postgresql.credentials
        envFrom:
        - configMapRef:
            name: pgpool-config
        image: pgpool/pgpool:4.2.2
        name: pgpool
        resources:
          limits:
            cpu: 1500m
            memory: 7Gi
          requests:
            cpu: 1000m
            memory: 6Gi
        volumeMounts:
        - mountPath: /config
          name: pgpool-hba-config
      initContainers:
      - command:
        - sh
        - -c
        - until nslookup -type=a postgres-operator.weko3pg.svc.cluster.local; do echo
          waiting for myservice; sleep 2; done
        image: mhayashi55/busybox-curl:v1.0.0
        name: wait-operator
      - command:
        - sh
        - -c
        - until [ 0 != $(curl -s -L postgres-operator.weko3pg:8080/clusters/weko/weko3pg/postgresql
          | jq .PodDisruptionBudget.status.currentHealthy) ]; do echo waiting for
          postgresql; sleep 2; done
        image: mhayashi55/busybox-curl:v1.0.0
        name: wait-postgresql
      volumes:
      - configMap:
          name: pgpool-hba-config
        name: pgpool-hba-config
---
apiVersion: acid.zalan.do/v1
kind: postgresql
metadata:
  name: weko-postgresql
  namespace: weko3pg
spec:
  additionalVolumes:
  - mountPath: /var/lib/postgresql/backup
    name: pvc-postgresql-backup
    targetContainers:
    - postgres
    volumeSource:
      persistentVolumeClaim:
        claimName: pvc-postgresql-backup
        readyOnly: false
  numberOfInstances: 1
  patroni:
    initdb:
      data-checksums: "true"
      encoding: UTF8
      locale: en_US.UTF-8
    pg_hba:
    - local   all             all                                   trust
    - hostssl all             +zalandos    127.0.0.1/32       pam
    - host    all             all                127.0.0.1/32       md5
    - hostssl all             +zalandos    ::1/128            pam
    - host    all             all                ::1/128            md5
    - hostssl replication     invenio_cl all                md5
    - hostssl all             +zalandos    all                pam
    - hostssl all             invenio            all                trust
    - hostssl all             postgres           all                trust
    - hostssl all             all                all                md5
    - host    all             invenio            all                trust
    - host    all             postgres           all                trust
    synchronous_mode: true
  postgresql:
    parameters:
      log_destination: stderr
      log_statement: none
      logging_collector: "false"
      max_connections: "2000"
      max_parallel_workers: "2"
      max_parallel_workers_per_gather: "2"
      max_standby_streaming_delay: "-1"
      max_wal_senders: "10"
      max_wal_size: 4GB
      max_worker_processes: "2"
      shared_buffers: 1500MB
      wal_buffers: 16MB
      wal_keep_segments: "8"
      wal_receiver_timeout: "0"
      wal_sender_timeout: "0"
    version: "12"
  resources:
    limits:
      cpu: 1500m
      memory: 7Gi
    requests:
      cpu: 1000m
      memory: 4Gi
  sidecars:
  - env:
    - name: DATA_SOURCE_URI
      value: weko-postgresql?sslmode=disable
    - name: DATA_SOURCE_USER
      valueFrom:
        secretKeyRef:
          key: username
          name: postgres.weko-postgresql.credentials
    - name: DATA_SOURCE_PASS
      valueFrom:
        secretKeyRef:
          key: password
          name: postgres.weko-postgresql.credentials
    image: wrouesnel/postgres_exporter
    name: exporter
    ports:
    - containerPort: 9187
      name: exporter
      protocol: TCP
    resources:
      limits:
        cpu: 500m
        memory: 256M
      requests:
        cpu: 100m
        memory: 200M
  teamId: weko
  volume:
    size: 50Gi
    storageClass: nfs-client

```

2. Create postgreSQL.

```
$ kubectl apply -f deploy.yaml
namespace/weko3pg created
serviceaccount/postgres-operator created
configmap/postgres-pod-config created
clusterrole.rbac.authorization.k8s.io/postgres-operator unchanged
clusterrole.rbac.authorization.k8s.io/postgres-pod unchanged
clusterrolebinding.rbac.authorization.k8s.io/postgres-operator unchanged
configmap/pgpool-config created
configmap/pgpool-hba-config created
configmap/postgres-operator created
configmap/postgresql-infrastructure-roles created
secret/postgresql-infrastructure-roles created
service/pgpool created
service/postgres-operator created
persistentvolumeclaim/pvc-postgresql-backup created
deployment.apps/postgres-operator created
deployment.apps/weko-pgpool created
postgresql.acid.zalan.do/weko-postgresql created

```

3. Check deployment result.

```
$ kubectl get all -n weko3pg
NAME                                     READY   STATUS    RESTARTS   AGE
pod/postgres-operator-64cd687ff5-jsdvk   1/1     Running   0          3h24m
pod/weko-pgpool-55cc495c58-f8gwz         1/1     Running   0          3h24m
pod/weko-postgresql-0                    2/2     Running   0          3h24m

NAME                             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/pgpool                   ClusterIP   10.233.7.225    <none>        5432/TCP   3h25m
service/postgres-operator        ClusterIP   10.233.30.33    <none>        8080/TCP   3h25m
service/weko-postgresql          ClusterIP   10.233.61.81    <none>        5432/TCP   3h24m
service/weko-postgresql-config   ClusterIP   None            <none>        <none>     3h24m
service/weko-postgresql-repl     ClusterIP   10.233.13.110   <none>        5432/TCP   3h24m

NAME                                READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/postgres-operator   1/1     1            1           3h25m
deployment.apps/weko-pgpool         1/1     1            1           3h25m

NAME                                           DESIRED   CURRENT   READY   AGE
replicaset.apps/postgres-operator-64cd687ff5   1         1         1       3h24m
replicaset.apps/weko-pgpool-55cc495c58         1         1         1       3h24m

NAME                               READY   AGE
statefulset.apps/weko-postgresql   1/1     3h24m

NAME                                       TEAM   VERSION   PODS   VOLUME   CPU-REQUEST   MEMORY-REQUEST   AGE     STATUS
postgresql.acid.zalan.do/weko-postgresql   weko   12        1      50Gi     1000m         4Gi              3h25m   Running

```

## Elasticsearch

1. create yaml file for deployment.

```
$ vi deploy.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: weko3es
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: elasticsearch-configmap
  namespace: weko3es
data:
  ES_JAVA_OPTS: -Xms2500m -Xmx2500m -XX:NewSize=1g -XX:MaxNewSize=1g -Dlog4j2.formatMsgNoLookups=true
  cluster.name: k8s-cluster
  discovery.zen.minimum_master_nodes: "2"
  discovery.zen.ping.unicast.hosts: weko-elasticsearch-0.elasticsearch,weko-elasticsearch-1.elasticsearch,weko-elasticsearch-2.elasticsearch
---
apiVersion: v1
kind: Service
metadata:
  name: elasticsearch
  namespace: weko3es
spec:
  clusterIP: None
  ports:
  - name: elasticsearch-port
    port: 9200
    protocol: TCP
    targetPort: 9200
  selector:
    app: elasticsearch
  type: ClusterIP
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-elasticsearch-backup
  namespace: weko3es
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 100Gi
  storageClassName: nfs-client
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: weko-elasticsearch
  namespace: weko3es
spec:
  replicas: 1
  selector:
    matchLabels:
      app: elasticsearch
  serviceName: elasticsearch
  template:
    metadata:
      labels:
        app: elasticsearch
    spec:
      containers:
      - env:
        - name: node.name
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        envFrom:
        - configMapRef:
            name: elasticsearch-configmap
        image: mhayashi55/weko-elasticsearch:latest
        imagePullPolicy: Always
        lifecycle:
          postStart:
            exec:
              command:
              - sh
              - -c
              - chown elasticsearch:elasticsearch /usr/share/elasticsearch/data
        name: elasticsearch
        ports:
        - containerPort: 9200
        resources:
          limits:
            cpu: 500m
            memory: 5Gi
          requests:
            cpu: 300m
            memory: 3Gi
        volumeMounts:
        - mountPath: /usr/share/elasticsearch/backups
          name: pvc-elasticsearch-backup
        - mountPath: /usr/share/elasticsearch/data
          name: weko-elasticsearch
      restartPolicy: Always
      volumes:
      - name: pvc-elasticsearch-backup
        persistentVolumeClaim:
          claimName: pvc-elasticsearch-backup
  volumeClaimTemplates:
  - metadata:
      name: weko-elasticsearch
    spec:
      accessModes:
      - ReadWriteOnce
      storageClassName: nfs-client
      resources:
        requests:
          storage: 100Gi

```

2. deploy elasticsearch

```
$ kubectl apply -f deploy.yaml
namespace/weko3es created
configmap/elasticsearch-configmap created
service/elasticsearch created
persistentvolumeclaim/pvc-elasticsearch-backup created
statefulset.apps/weko-elasticsearch created

```

3. check running status of elasticsearch.

```
$ kubectl get all -n weko3es
NAME                       READY   STATUS    RESTARTS   AGE
pod/weko-elasticsearch-0   1/1     Running   0          70s

NAME                    TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
service/elasticsearch   ClusterIP   None         <none>        9200/TCP   74s

NAME                                  READY   AGE
statefulset.apps/weko-elasticsearch   1/1     72s

```

## RabbitMQ

1. create a yaml file for deployment.

```
$vi deploy.yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    app.kubernetes.io/component: rabbitmq-operator
    app.kubernetes.io/name: rabbitmq-system
    app.kubernetes.io/part-of: rabbitmq
  name: rabbitmq-system
---
apiVersion: v1
kind: Namespace
metadata:
  name: weko3ra
---
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.9.0
  labels:
    app.kubernetes.io/component: rabbitmq-operator
    app.kubernetes.io/name: rabbitmq-cluster-operator
    app.kubernetes.io/part-of: rabbitmq
  name: rabbitmqclusters.rabbitmq.com
spec:
  group: rabbitmq.com
  names:
    categories:
    - all
    - rabbitmq
    kind: RabbitmqCluster
    listKind: RabbitmqClusterList
    plural: rabbitmqclusters
    shortNames:
    - rmq
    singular: rabbitmqcluster
  scope: Namespaced
  versions:
  - additionalPrinterColumns:
    - jsonPath: .status.conditions[?(@.type == 'AllReplicasReady')].status
      name: AllReplicasReady
      type: string
    - jsonPath: .status.conditions[?(@.type == 'ReconcileSuccess')].status
      name: ReconcileSuccess
      type: string
    - jsonPath: .metadata.creationTimestamp
      name: Age
      type: date
    name: v1beta1
    schema:
      openAPIV3Schema:
        description: RabbitmqCluster is the Schema for the RabbitmqCluster API. Each
          instance of this object corresponds to a single RabbitMQ cluster.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object. Servers should convert recognized schemas to the latest
              internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents. Servers may infer this from the endpoint the client
              submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: Spec is the desired state of the RabbitmqCluster Custom Resource.
            properties:
              affinity:
                description: Affinity scheduling rules to be applied on created Pods.
                properties:
                  nodeAffinity:
                    description: Describes node affinity scheduling rules for the
                      pod.
                    properties:
                      preferredDuringSchedulingIgnoredDuringExecution:
                        description: The scheduler will prefer to schedule pods to
                          nodes that satisfy the affinity expressions specified by
                          this field, but it may choose a node that violates one or
                          more of the expressions. The node that is most preferred
                          is the one with the greatest sum of weights, i.e. for each
                          node that meets all of the scheduling requirements (resource
                          request, requiredDuringScheduling affinity expressions,
                          etc.), compute a sum by iterating through the elements of
                          this field and adding "weight" to the sum if the node matches
                          the corresponding matchExpressions; the node(s) with the
                          highest sum are the most preferred.
                        items:
                          description: An empty preferred scheduling term matches
                            all objects with implicit weight 0 (i.e. it's a no-op).
                            A null preferred scheduling term matches no objects (i.e.
                            is also a no-op).
                          properties:
                            preference:
                              description: A node selector term, associated with the
                                corresponding weight.
                              properties:
                                matchExpressions:
                                  description: A list of node selector requirements
                                    by node's labels.
                                  items:
                                    description: A node selector requirement is a
                                      selector that contains values, a key, and an
                                      operator that relates the key and values.
                                    properties:
                                      key:
                                        description: The label key that the selector
                                          applies to.
                                        type: string
                                      operator:
                                        description: Represents a key's relationship
                                          to a set of values. Valid operators are
                                          In, NotIn, Exists, DoesNotExist. Gt, and
                                          Lt.
                                        type: string
                                      values:
                                        description: An array of string values. If
                                          the operator is In or NotIn, the values
                                          array must be non-empty. If the operator
                                          is Exists or DoesNotExist, the values array
                                          must be empty. If the operator is Gt or
                                          Lt, the values array must have a single
                                          element, which will be interpreted as an
                                          integer. This array is replaced during a
                                          strategic merge patch.
                                        items:
                                          type: string
                                        type: array
                                    required:
                                    - key
                                    - operator
                                    type: object
                                  type: array
                                matchFields:
                                  description: A list of node selector requirements
                                    by node's fields.
                                  items:
                                    description: A node selector requirement is a
                                      selector that contains values, a key, and an
                                      operator that relates the key and values.
                                    properties:
                                      key:
                                        description: The label key that the selector
                                          applies to.
                                        type: string
                                      operator:
                                        description: Represents a key's relationship
                                          to a set of values. Valid operators are
                                          In, NotIn, Exists, DoesNotExist. Gt, and
                                          Lt.
                                        type: string
                                      values:
                                        description: An array of string values. If
                                          the operator is In or NotIn, the values
                                          array must be non-empty. If the operator
                                          is Exists or DoesNotExist, the values array
                                          must be empty. If the operator is Gt or
                                          Lt, the values array must have a single
                                          element, which will be interpreted as an
                                          integer. This array is replaced during a
                                          strategic merge patch.
                                        items:
                                          type: string
                                        type: array
                                    required:
                                    - key
                                    - operator
                                    type: object
                                  type: array
                              type: object
                            weight:
                              description: Weight associated with matching the corresponding
                                nodeSelectorTerm, in the range 1-100.
                              format: int32
                              type: integer
                          required:
                          - preference
                          - weight
                          type: object
                        type: array
                      requiredDuringSchedulingIgnoredDuringExecution:
                        description: If the affinity requirements specified by this
                          field are not met at scheduling time, the pod will not be
                          scheduled onto the node. If the affinity requirements specified
                          by this field cease to be met at some point during pod execution
                          (e.g. due to an update), the system may or may not try to
                          eventually evict the pod from its node.
                        properties:
                          nodeSelectorTerms:
                            description: Required. A list of node selector terms.
                              The terms are ORed.
                            items:
                              description: A null or empty node selector term matches
                                no objects. The requirements of them are ANDed. The
                                TopologySelectorTerm type implements a subset of the
                                NodeSelectorTerm.
                              properties:
                                matchExpressions:
                                  description: A list of node selector requirements
                                    by node's labels.
                                  items:
                                    description: A node selector requirement is a
                                      selector that contains values, a key, and an
                                      operator that relates the key and values.
                                    properties:
                                      key:
                                        description: The label key that the selector
                                          applies to.
                                        type: string
                                      operator:
                                        description: Represents a key's relationship
                                          to a set of values. Valid operators are
                                          In, NotIn, Exists, DoesNotExist. Gt, and
                                          Lt.
                                        type: string
                                      values:
                                        description: An array of string values. If
                                          the operator is In or NotIn, the values
                                          array must be non-empty. If the operator
                                          is Exists or DoesNotExist, the values array
                                          must be empty. If the operator is Gt or
                                          Lt, the values array must have a single
                                          element, which will be interpreted as an
                                          integer. This array is replaced during a
                                          strategic merge patch.
                                        items:
                                          type: string
                                        type: array
                                    required:
                                    - key
                                    - operator
                                    type: object
                                  type: array
                                matchFields:
                                  description: A list of node selector requirements
                                    by node's fields.
                                  items:
                                    description: A node selector requirement is a
                                      selector that contains values, a key, and an
                                      operator that relates the key and values.
                                    properties:
                                      key:
                                        description: The label key that the selector
                                          applies to.
                                        type: string
                                      operator:
                                        description: Represents a key's relationship
                                          to a set of values. Valid operators are
                                          In, NotIn, Exists, DoesNotExist. Gt, and
                                          Lt.
                                        type: string
                                      values:
                                        description: An array of string values. If
                                          the operator is In or NotIn, the values
                                          array must be non-empty. If the operator
                                          is Exists or DoesNotExist, the values array
                                          must be empty. If the operator is Gt or
                                          Lt, the values array must have a single
                                          element, which will be interpreted as an
                                          integer. This array is replaced during a
                                          strategic merge patch.
                                        items:
                                          type: string
                                        type: array
                                    required:
                                    - key
                                    - operator
                                    type: object
                                  type: array
                              type: object
                            type: array
                        required:
                        - nodeSelectorTerms
                        type: object
                    type: object
                  podAffinity:
                    description: Describes pod affinity scheduling rules (e.g. co-locate
                      this pod in the same node, zone, etc. as some other pod(s)).
                    properties:
                      preferredDuringSchedulingIgnoredDuringExecution:
                        description: The scheduler will prefer to schedule pods to
                          nodes that satisfy the affinity expressions specified by
                          this field, but it may choose a node that violates one or
                          more of the expressions. The node that is most preferred
                          is the one with the greatest sum of weights, i.e. for each
                          node that meets all of the scheduling requirements (resource
                          request, requiredDuringScheduling affinity expressions,
                          etc.), compute a sum by iterating through the elements of
                          this field and adding "weight" to the sum if the node has
                          pods which matches the corresponding podAffinityTerm; the
                          node(s) with the highest sum are the most preferred.
                        items:
                          description: The weights of all of the matched WeightedPodAffinityTerm
                            fields are added per-node to find the most preferred node(s)
                          properties:
                            podAffinityTerm:
                              description: Required. A pod affinity term, associated
                                with the corresponding weight.
                              properties:
                                labelSelector:
                                  description: A label query over a set of resources,
                                    in this case pods.
                                  properties:
                                    matchExpressions:
                                      description: matchExpressions is a list of label
                                        selector requirements. The requirements are
                                        ANDed.
                                      items:
                                        description: A label selector requirement
                                          is a selector that contains values, a key,
                                          and an operator that relates the key and
                                          values.
                                        properties:
                                          key:
                                            description: key is the label key that
                                              the selector applies to.
                                            type: string
                                          operator:
                                            description: operator represents a key's
                                              relationship to a set of values. Valid
                                              operators are In, NotIn, Exists and
                                              DoesNotExist.
                                            type: string
                                          values:
                                            description: values is an array of string
                                              values. If the operator is In or NotIn,
                                              the values array must be non-empty.
                                              If the operator is Exists or DoesNotExist,
                                              the values array must be empty. This
                                              array is replaced during a strategic
                                              merge patch.
                                            items:
                                              type: string
                                            type: array
                                        required:
                                        - key
                                        - operator
                                        type: object
                                      type: array
                                    matchLabels:
                                      additionalProperties:
                                        type: string
                                      description: matchLabels is a map of {key,value}
                                        pairs. A single {key,value} in the matchLabels
                                        map is equivalent to an element of matchExpressions,
                                        whose key field is "key", the operator is
                                        "In", and the values array contains only "value".
                                        The requirements are ANDed.
                                      type: object
                                  type: object
                                namespaceSelector:
                                  description: A label query over the set of namespaces
                                    that the term applies to. The term is applied
                                    to the union of the namespaces selected by this
                                    field and the ones listed in the namespaces field.
                                    null selector and null or empty namespaces list
                                    means "this pod's namespace". An empty selector
                                    ({}) matches all namespaces.
                                  properties:
                                    matchExpressions:
                                      description: matchExpressions is a list of label
                                        selector requirements. The requirements are
                                        ANDed.
                                      items:
                                        description: A label selector requirement
                                          is a selector that contains values, a key,
                                          and an operator that relates the key and
                                          values.
                                        properties:
                                          key:
                                            description: key is the label key that
                                              the selector applies to.
                                            type: string
                                          operator:
                                            description: operator represents a key's
                                              relationship to a set of values. Valid
                                              operators are In, NotIn, Exists and
                                              DoesNotExist.
                                            type: string
                                          values:
                                            description: values is an array of string
                                              values. If the operator is In or NotIn,
                                              the values array must be non-empty.
                                              If the operator is Exists or DoesNotExist,
                                              the values array must be empty. This
                                              array is replaced during a strategic
                                              merge patch.
                                            items:
                                              type: string
                                            type: array
                                        required:
                                        - key
                                        - operator
                                        type: object
                                      type: array
                                    matchLabels:
                                      additionalProperties:
                                        type: string
                                      description: matchLabels is a map of {key,value}
                                        pairs. A single {key,value} in the matchLabels
                                        map is equivalent to an element of matchExpressions,
                                        whose key field is "key", the operator is
                                        "In", and the values array contains only "value".
                                        The requirements are ANDed.
                                      type: object
                                  type: object
                                namespaces:
                                  description: namespaces specifies a static list
                                    of namespace names that the term applies to. The
                                    term is applied to the union of the namespaces
                                    listed in this field and the ones selected by
                                    namespaceSelector. null or empty namespaces list
                                    and null namespaceSelector means "this pod's namespace".
                                  items:
                                    type: string
                                  type: array
                                topologyKey:
                                  description: This pod should be co-located (affinity)
                                    or not co-located (anti-affinity) with the pods
                                    matching the labelSelector in the specified namespaces,
                                    where co-located is defined as running on a node
                                    whose value of the label with key topologyKey
                                    matches that of any node on which any of the selected
                                    pods is running. Empty topologyKey is not allowed.
                                  type: string
                              required:
                              - topologyKey
                              type: object
                            weight:
                              description: weight associated with matching the corresponding
                                podAffinityTerm, in the range 1-100.
                              format: int32
                              type: integer
                          required:
                          - podAffinityTerm
                          - weight
                          type: object
                        type: array
                      requiredDuringSchedulingIgnoredDuringExecution:
                        description: If the affinity requirements specified by this
                          field are not met at scheduling time, the pod will not be
                          scheduled onto the node. If the affinity requirements specified
                          by this field cease to be met at some point during pod execution
                          (e.g. due to a pod label update), the system may or may
                          not try to eventually evict the pod from its node. When
                          there are multiple elements, the lists of nodes corresponding
                          to each podAffinityTerm are intersected, i.e. all terms
                          must be satisfied.
                        items:
                          description: Defines a set of pods (namely those matching
                            the labelSelector relative to the given namespace(s))
                            that this pod should be co-located (affinity) or not co-located
                            (anti-affinity) with, where co-located is defined as running
                            on a node whose value of the label with key <topologyKey>
                            matches that of any node on which a pod of the set of
                            pods is running
                          properties:
                            labelSelector:
                              description: A label query over a set of resources,
                                in this case pods.
                              properties:
                                matchExpressions:
                                  description: matchExpressions is a list of label
                                    selector requirements. The requirements are ANDed.
                                  items:
                                    description: A label selector requirement is a
                                      selector that contains values, a key, and an
                                      operator that relates the key and values.
                                    properties:
                                      key:
                                        description: key is the label key that the
                                          selector applies to.
                                        type: string
                                      operator:
                                        description: operator represents a key's relationship
                                          to a set of values. Valid operators are
                                          In, NotIn, Exists and DoesNotExist.
                                        type: string
                                      values:
                                        description: values is an array of string
                                          values. If the operator is In or NotIn,
                                          the values array must be non-empty. If the
                                          operator is Exists or DoesNotExist, the
                                          values array must be empty. This array is
                                          replaced during a strategic merge patch.
                                        items:
                                          type: string
                                        type: array
                                    required:
                                    - key
                                    - operator
                                    type: object
                                  type: array
                                matchLabels:
                                  additionalProperties:
                                    type: string
                                  description: matchLabels is a map of {key,value}
                                    pairs. A single {key,value} in the matchLabels
                                    map is equivalent to an element of matchExpressions,
                                    whose key field is "key", the operator is "In",
                                    and the values array contains only "value". The
                                    requirements are ANDed.
                                  type: object
                              type: object
                            namespaceSelector:
                              description: A label query over the set of namespaces
                                that the term applies to. The term is applied to the
                                union of the namespaces selected by this field and
                                the ones listed in the namespaces field. null selector
                                and null or empty namespaces list means "this pod's
                                namespace". An empty selector ({}) matches all namespaces.
                              properties:
                                matchExpressions:
                                  description: matchExpressions is a list of label
                                    selector requirements. The requirements are ANDed.
                                  items:
                                    description: A label selector requirement is a
                                      selector that contains values, a key, and an
                                      operator that relates the key and values.
                                    properties:
                                      key:
                                        description: key is the label key that the
                                          selector applies to.
                                        type: string
                                      operator:
                                        description: operator represents a key's relationship
                                          to a set of values. Valid operators are
                                          In, NotIn, Exists and DoesNotExist.
                                        type: string
                                      values:
                                        description: values is an array of string
                                          values. If the operator is In or NotIn,
                                          the values array must be non-empty. If the
                                          operator is Exists or DoesNotExist, the
                                          values array must be empty. This array is
                                          replaced during a strategic merge patch.
                                        items:
                                          type: string
                                        type: array
                                    required:
                                    - key
                                    - operator
                                    type: object
                                  type: array
                                matchLabels:
                                  additionalProperties:
                                    type: string
                                  description: matchLabels is a map of {key,value}
                                    pairs. A single {key,value} in the matchLabels
                                    map is equivalent to an element of matchExpressions,
                                    whose key field is "key", the operator is "In",
                                    and the values array contains only "value". The
                                    requirements are ANDed.
                                  type: object
                              type: object
                            namespaces:
                              description: namespaces specifies a static list of namespace
                                names that the term applies to. The term is applied
                                to the union of the namespaces listed in this field
                                and the ones selected by namespaceSelector. null or
                                empty namespaces list and null namespaceSelector means
                                "this pod's namespace".
                              items:
                                type: string
                              type: array
                            topologyKey:
                              description: This pod should be co-located (affinity)
                                or not co-located (anti-affinity) with the pods matching
                                the labelSelector in the specified namespaces, where
                                co-located is defined as running on a node whose value
                                of the label with key topologyKey matches that of
                                any node on which any of the selected pods is running.
                                Empty topologyKey is not allowed.
                              type: string
                          required:
                          - topologyKey
                          type: object
                        type: array
                    type: object
                  podAntiAffinity:
                    description: Describes pod anti-affinity scheduling rules (e.g.
                      avoid putting this pod in the same node, zone, etc. as some
                      other pod(s)).
                    properties:
                      preferredDuringSchedulingIgnoredDuringExecution:
                        description: The scheduler will prefer to schedule pods to
                          nodes that satisfy the anti-affinity expressions specified
                          by this field, but it may choose a node that violates one
                          or more of the expressions. The node that is most preferred
                          is the one with the greatest sum of weights, i.e. for each
                          node that meets all of the scheduling requirements (resource
                          request, requiredDuringScheduling anti-affinity expressions,
                          etc.), compute a sum by iterating through the elements of
                          this field and adding "weight" to the sum if the node has
                          pods which matches the corresponding podAffinityTerm; the
                          node(s) with the highest sum are the most preferred.
                        items:
                          description: The weights of all of the matched WeightedPodAffinityTerm
                            fields are added per-node to find the most preferred node(s)
                          properties:
                            podAffinityTerm:
                              description: Required. A pod affinity term, associated
                                with the corresponding weight.
                              properties:
                                labelSelector:
                                  description: A label query over a set of resources,
                                    in this case pods.
                                  properties:
                                    matchExpressions:
                                      description: matchExpressions is a list of label
                                        selector requirements. The requirements are
                                        ANDed.
                                      items:
                                        description: A label selector requirement
                                          is a selector that contains values, a key,
                                          and an operator that relates the key and
                                          values.
                                        properties:
                                          key:
                                            description: key is the label key that
                                              the selector applies to.
                                            type: string
                                          operator:
                                            description: operator represents a key's
                                              relationship to a set of values. Valid
                                              operators are In, NotIn, Exists and
                                              DoesNotExist.
                                            type: string
                                          values:
                                            description: values is an array of string
                                              values. If the operator is In or NotIn,
                                              the values array must be non-empty.
                                              If the operator is Exists or DoesNotExist,
                                              the values array must be empty. This
                                              array is replaced during a strategic
                                              merge patch.
                                            items:
                                              type: string
                                            type: array
                                        required:
                                        - key
                                        - operator
                                        type: object
                                      type: array
                                    matchLabels:
                                      additionalProperties:
                                        type: string
                                      description: matchLabels is a map of {key,value}
                                        pairs. A single {key,value} in the matchLabels
                                        map is equivalent to an element of matchExpressions,
                                        whose key field is "key", the operator is
                                        "In", and the values array contains only "value".
                                        The requirements are ANDed.
                                      type: object
                                  type: object
                                namespaceSelector:
                                  description: A label query over the set of namespaces
                                    that the term applies to. The term is applied
                                    to the union of the namespaces selected by this
                                    field and the ones listed in the namespaces field.
                                    null selector and null or empty namespaces list
                                    means "this pod's namespace". An empty selector
                                    ({}) matches all namespaces.
                                  properties:
                                    matchExpressions:
                                      description: matchExpressions is a list of label
                                        selector requirements. The requirements are
                                        ANDed.
                                      items:
                                        description: A label selector requirement
                                          is a selector that contains values, a key,
                                          and an operator that relates the key and
                                          values.
                                        properties:
                                          key:
                                            description: key is the label key that
                                              the selector applies to.
                                            type: string
                                          operator:
                                            description: operator represents a key's
                                              relationship to a set of values. Valid
                                              operators are In, NotIn, Exists and
                                              DoesNotExist.
                                            type: string
                                          values:
                                            description: values is an array of string
                                              values. If the operator is In or NotIn,
                                              the values array must be non-empty.
                                              If the operator is Exists or DoesNotExist,
                                              the values array must be empty. This
                                              array is replaced during a strategic
                                              merge patch.
                                            items:
                                              type: string
                                            type: array
                                        required:
                                        - key
                                        - operator
                                        type: object
                                      type: array
                                    matchLabels:
                                      additionalProperties:
                                        type: string
                                      description: matchLabels is a map of {key,value}
                                        pairs. A single {key,value} in the matchLabels
                                        map is equivalent to an element of matchExpressions,
                                        whose key field is "key", the operator is
                                        "In", and the values array contains only "value".
                                        The requirements are ANDed.
                                      type: object
                                  type: object
                                namespaces:
                                  description: namespaces specifies a static list
                                    of namespace names that the term applies to. The
                                    term is applied to the union of the namespaces
                                    listed in this field and the ones selected by
                                    namespaceSelector. null or empty namespaces list
                                    and null namespaceSelector means "this pod's namespace".
                                  items:
                                    type: string
                                  type: array
                                topologyKey:
                                  description: This pod should be co-located (affinity)
                                    or not co-located (anti-affinity) with the pods
                                    matching the labelSelector in the specified namespaces,
                                    where co-located is defined as running on a node
                                    whose value of the label with key topologyKey
                                    matches that of any node on which any of the selected
                                    pods is running. Empty topologyKey is not allowed.
                                  type: string
                              required:
                              - topologyKey
                              type: object
                            weight:
                              description: weight associated with matching the corresponding
                                podAffinityTerm, in the range 1-100.
                              format: int32
                              type: integer
                          required:
                          - podAffinityTerm
                          - weight
                          type: object
                        type: array
                      requiredDuringSchedulingIgnoredDuringExecution:
                        description: If the anti-affinity requirements specified by
                          this field are not met at scheduling time, the pod will
                          not be scheduled onto the node. If the anti-affinity requirements
                          specified by this field cease to be met at some point during
                          pod execution (e.g. due to a pod label update), the system
                          may or may not try to eventually evict the pod from its
                          node. When there are multiple elements, the lists of nodes
                          corresponding to each podAffinityTerm are intersected, i.e.
                          all terms must be satisfied.
                        items:
                          description: Defines a set of pods (namely those matching
                            the labelSelector relative to the given namespace(s))
                            that this pod should be co-located (affinity) or not co-located
                            (anti-affinity) with, where co-located is defined as running
                            on a node whose value of the label with key <topologyKey>
                            matches that of any node on which a pod of the set of
                            pods is running
                          properties:
                            labelSelector:
                              description: A label query over a set of resources,
                                in this case pods.
                              properties:
                                matchExpressions:
                                  description: matchExpressions is a list of label
                                    selector requirements. The requirements are ANDed.
                                  items:
                                    description: A label selector requirement is a
                                      selector that contains values, a key, and an
                                      operator that relates the key and values.
                                    properties:
                                      key:
                                        description: key is the label key that the
                                          selector applies to.
                                        type: string
                                      operator:
                                        description: operator represents a key's relationship
                                          to a set of values. Valid operators are
                                          In, NotIn, Exists and DoesNotExist.
                                        type: string
                                      values:
                                        description: values is an array of string
                                          values. If the operator is In or NotIn,
                                          the values array must be non-empty. If the
                                          operator is Exists or DoesNotExist, the
                                          values array must be empty. This array is
                                          replaced during a strategic merge patch.
                                        items:
                                          type: string
                                        type: array
                                    required:
                                    - key
                                    - operator
                                    type: object
                                  type: array
                                matchLabels:
                                  additionalProperties:
                                    type: string
                                  description: matchLabels is a map of {key,value}
                                    pairs. A single {key,value} in the matchLabels
                                    map is equivalent to an element of matchExpressions,
                                    whose key field is "key", the operator is "In",
                                    and the values array contains only "value". The
                                    requirements are ANDed.
                                  type: object
                              type: object
                            namespaceSelector:
                              description: A label query over the set of namespaces
                                that the term applies to. The term is applied to the
                                union of the namespaces selected by this field and
                                the ones listed in the namespaces field. null selector
                                and null or empty namespaces list means "this pod's
                                namespace". An empty selector ({}) matches all namespaces.
                              properties:
                                matchExpressions:
                                  description: matchExpressions is a list of label
                                    selector requirements. The requirements are ANDed.
                                  items:
                                    description: A label selector requirement is a
                                      selector that contains values, a key, and an
                                      operator that relates the key and values.
                                    properties:
                                      key:
                                        description: key is the label key that the
                                          selector applies to.
                                        type: string
                                      operator:
                                        description: operator represents a key's relationship
                                          to a set of values. Valid operators are
                                          In, NotIn, Exists and DoesNotExist.
                                        type: string
                                      values:
                                        description: values is an array of string
                                          values. If the operator is In or NotIn,
                                          the values array must be non-empty. If the
                                          operator is Exists or DoesNotExist, the
                                          values array must be empty. This array is
                                          replaced during a strategic merge patch.
                                        items:
                                          type: string
                                        type: array
                                    required:
                                    - key
                                    - operator
                                    type: object
                                  type: array
                                matchLabels:
                                  additionalProperties:
                                    type: string
                                  description: matchLabels is a map of {key,value}
                                    pairs. A single {key,value} in the matchLabels
                                    map is equivalent to an element of matchExpressions,
                                    whose key field is "key", the operator is "In",
                                    and the values array contains only "value". The
                                    requirements are ANDed.
                                  type: object
                              type: object
                            namespaces:
                              description: namespaces specifies a static list of namespace
                                names that the term applies to. The term is applied
                                to the union of the namespaces listed in this field
                                and the ones selected by namespaceSelector. null or
                                empty namespaces list and null namespaceSelector means
                                "this pod's namespace".
                              items:
                                type: string
                              type: array
                            topologyKey:
                              description: This pod should be co-located (affinity)
                                or not co-located (anti-affinity) with the pods matching
                                the labelSelector in the specified namespaces, where
                                co-located is defined as running on a node whose value
                                of the label with key topologyKey matches that of
                                any node on which any of the selected pods is running.
                                Empty topologyKey is not allowed.
                              type: string
                          required:
                          - topologyKey
                          type: object
                        type: array
                    type: object
                type: object
              image:
                description: Image is the name of the RabbitMQ docker image to use
                  for RabbitMQ nodes in the RabbitmqCluster. Must be provided together
                  with ImagePullSecrets in order to use an image in a private registry.
                type: string
              imagePullSecrets:
                description: List of Secret resource containing access credentials
                  to the registry for the RabbitMQ image. Required if the docker registry
                  is private.
                items:
                  description: LocalObjectReference contains enough information to
                    let you locate the referenced object inside the same namespace.
                  properties:
                    name:
                      description: 'Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
                        TODO: Add other useful fields. apiVersion, kind, uid?'
                      type: string
                  type: object
                type: array
              override:
                properties:
                  service:
                    properties:
                      metadata:
                        properties:
                          annotations:
                            additionalProperties:
                              type: string
                            type: object
                          labels:
                            additionalProperties:
                              type: string
                            type: object
                        type: object
                      spec:
                        properties:
                          allocateLoadBalancerNodePorts:
                            type: boolean
                          clusterIP:
                            type: string
                          clusterIPs:
                            items:
                              type: string
                            type: array
                            x-kubernetes-list-type: atomic
                          externalIPs:
                            items:
                              type: string
                            type: array
                          externalName:
                            type: string
                          externalTrafficPolicy:
                            type: string
                          healthCheckNodePort:
                            format: int32
                            type: integer
                          internalTrafficPolicy:
                            type: string
                          ipFamilies:
                            items:
                              type: string
                            type: array
                            x-kubernetes-list-type: atomic
                          ipFamilyPolicy:
                            type: string
                          loadBalancerClass:
                            type: string
                          loadBalancerIP:
                            type: string
                          loadBalancerSourceRanges:
                            items:
                              type: string
                            type: array
                          ports:
                            items:
                              properties:
                                appProtocol:
                                  type: string
                                name:
                                  type: string
                                nodePort:
                                  format: int32
                                  type: integer
                                port:
                                  format: int32
                                  type: integer
                                protocol:
                                  default: TCP
                                  type: string
                                targetPort:
                                  anyOf:
                                  - type: integer
                                  - type: string
                                  x-kubernetes-int-or-string: true
                              required:
                              - port
                              type: object
                            type: array
                            x-kubernetes-list-map-keys:
                            - port
                            - protocol
                            x-kubernetes-list-type: map
                          publishNotReadyAddresses:
                            type: boolean
                          selector:
                            additionalProperties:
                              type: string
                            type: object
                            x-kubernetes-map-type: atomic
                          sessionAffinity:
                            type: string
                          sessionAffinityConfig:
                            properties:
                              clientIP:
                                properties:
                                  timeoutSeconds:
                                    format: int32
                                    type: integer
                                type: object
                            type: object
                          type:
                            type: string
                        type: object
                    type: object
                  statefulSet:
                    properties:
                      metadata:
                        properties:
                          annotations:
                            additionalProperties:
                              type: string
                            type: object
                          labels:
                            additionalProperties:
                              type: string
                            type: object
                        type: object
                      spec:
                        properties:
                          podManagementPolicy:
                            type: string
                          replicas:
                            format: int32
                            type: integer
                          selector:
                            properties:
                              matchExpressions:
                                items:
                                  properties:
                                    key:
                                      type: string
                                    operator:
                                      type: string
                                    values:
                                      items:
                                        type: string
                                      type: array
                                  required:
                                  - key
                                  - operator
                                  type: object
                                type: array
                              matchLabels:
                                additionalProperties:
                                  type: string
                                type: object
                            type: object
                          serviceName:
                            type: string
                          template:
                            properties:
                              metadata:
                                properties:
                                  annotations:
                                    additionalProperties:
                                      type: string
                                    type: object
                                  labels:
                                    additionalProperties:
                                      type: string
                                    type: object
                                  name:
                                    type: string
                                  namespace:
                                    type: string
                                type: object
                              spec:
                                properties:
                                  activeDeadlineSeconds:
                                    format: int64
                                    type: integer
                                  affinity:
                                    properties:
                                      nodeAffinity:
                                        properties:
                                          preferredDuringSchedulingIgnoredDuringExecution:
                                            items:
                                              properties:
                                                preference:
                                                  properties:
                                                    matchExpressions:
                                                      items:
                                                        properties:
                                                          key:
                                                            type: string
                                                          operator:
                                                            type: string
                                                          values:
                                                            items:
                                                              type: string
                                                            type: array
                                                        required:
                                                        - key
                                                        - operator
                                                        type: object
                                                      type: array
                                                    matchFields:
                                                      items:
                                                        properties:
                                                          key:
                                                            type: string
                                                          operator:
                                                            type: string
                                                          values:
                                                            items:
                                                              type: string
                                                            type: array
                                                        required:
                                                        - key
                                                        - operator
                                                        type: object
                                                      type: array
                                                  type: object
                                                weight:
                                                  format: int32
                                                  type: integer
                                              required:
                                              - preference
                                              - weight
                                              type: object
                                            type: array
                                          requiredDuringSchedulingIgnoredDuringExecution:
                                            properties:
                                              nodeSelectorTerms:
                                                items:
                                                  properties:
                                                    matchExpressions:
                                                      items:
                                                        properties:
                                                          key:
                                                            type: string
                                                          operator:
                                                            type: string
                                                          values:
                                                            items:
                                                              type: string
                                                            type: array
                                                        required:
                                                        - key
                                                        - operator
                                                        type: object
                                                      type: array
                                                    matchFields:
                                                      items:
                                                        properties:
                                                          key:
                                                            type: string
                                                          operator:
                                                            type: string
                                                          values:
                                                            items:
                                                              type: string
                                                            type: array
                                                        required:
                                                        - key
                                                        - operator
                                                        type: object
                                                      type: array
                                                  type: object
                                                type: array
                                            required:
                                            - nodeSelectorTerms
                                            type: object
                                        type: object
                                      podAffinity:
                                        properties:
                                          preferredDuringSchedulingIgnoredDuringExecution:
                                            items:
                                              properties:
                                                podAffinityTerm:
                                                  properties:
                                                    labelSelector:
                                                      properties:
                                                        matchExpressions:
                                                          items:
                                                            properties:
                                                              key:
                                                                type: string
                                                              operator:
                                                                type: string
                                                              values:
                                                                items:
                                                                  type: string
                                                                type: array
                                                            required:
                                                            - key
                                                            - operator
                                                            type: object
                                                          type: array
                                                        matchLabels:
                                                          additionalProperties:
                                                            type: string
                                                          type: object
                                                      type: object
                                                    namespaceSelector:
                                                      properties:
                                                        matchExpressions:
                                                          items:
                                                            properties:
                                                              key:
                                                                type: string
                                                              operator:
                                                                type: string
                                                              values:
                                                                items:
                                                                  type: string
                                                                type: array
                                                            required:
                                                            - key
                                                            - operator
                                                            type: object
                                                          type: array
                                                        matchLabels:
                                                          additionalProperties:
                                                            type: string
                                                          type: object
                                                      type: object
                                                    namespaces:
                                                      items:
                                                        type: string
                                                      type: array
                                                    topologyKey:
                                                      type: string
                                                  required:
                                                  - topologyKey
                                                  type: object
                                                weight:
                                                  format: int32
                                                  type: integer
                                              required:
                                              - podAffinityTerm
                                              - weight
                                              type: object
                                            type: array
                                          requiredDuringSchedulingIgnoredDuringExecution:
                                            items:
                                              properties:
                                                labelSelector:
                                                  properties:
                                                    matchExpressions:
                                                      items:
                                                        properties:
                                                          key:
                                                            type: string
                                                          operator:
                                                            type: string
                                                          values:
                                                            items:
                                                              type: string
                                                            type: array
                                                        required:
                                                        - key
                                                        - operator
                                                        type: object
                                                      type: array
                                                    matchLabels:
                                                      additionalProperties:
                                                        type: string
                                                      type: object
                                                  type: object
                                                namespaceSelector:
                                                  properties:
                                                    matchExpressions:
                                                      items:
                                                        properties:
                                                          key:
                                                            type: string
                                                          operator:
                                                            type: string
                                                          values:
                                                            items:
                                                              type: string
                                                            type: array
                                                        required:
                                                        - key
                                                        - operator
                                                        type: object
                                                      type: array
                                                    matchLabels:
                                                      additionalProperties:
                                                        type: string
                                                      type: object
                                                  type: object
                                                namespaces:
                                                  items:
                                                    type: string
                                                  type: array
                                                topologyKey:
                                                  type: string
                                              required:
                                              - topologyKey
                                              type: object
                                            type: array
                                        type: object
                                      podAntiAffinity:
                                        properties:
                                          preferredDuringSchedulingIgnoredDuringExecution:
                                            items:
                                              properties:
                                                podAffinityTerm:
                                                  properties:
                                                    labelSelector:
                                                      properties:
                                                        matchExpressions:
                                                          items:
                                                            properties:
                                                              key:
                                                                type: string
                                                              operator:
                                                                type: string
                                                              values:
                                                                items:
                                                                  type: string
                                                                type: array
                                                            required:
                                                            - key
                                                            - operator
                                                            type: object
                                                          type: array
                                                        matchLabels:
                                                          additionalProperties:
                                                            type: string
                                                          type: object
                                                      type: object
                                                    namespaceSelector:
                                                      properties:
                                                        matchExpressions:
                                                          items:
                                                            properties:
                                                              key:
                                                                type: string
                                                              operator:
                                                                type: string
                                                              values:
                                                                items:
                                                                  type: string
                                                                type: array
                                                            required:
                                                            - key
                                                            - operator
                                                            type: object
                                                          type: array
                                                        matchLabels:
                                                          additionalProperties:
                                                            type: string
                                                          type: object
                                                      type: object
                                                    namespaces:
                                                      items:
                                                        type: string
                                                      type: array
                                                    topologyKey:
                                                      type: string
                                                  required:
                                                  - topologyKey
                                                  type: object
                                                weight:
                                                  format: int32
                                                  type: integer
                                              required:
                                              - podAffinityTerm
                                              - weight
                                              type: object
                                            type: array
                                          requiredDuringSchedulingIgnoredDuringExecution:
                                            items:
                                              properties:
                                                labelSelector:
                                                  properties:
                                                    matchExpressions:
                                                      items:
                                                        properties:
                                                          key:
                                                            type: string
                                                          operator:
                                                            type: string
                                                          values:
                                                            items:
                                                              type: string
                                                            type: array
                                                        required:
                                                        - key
                                                        - operator
                                                        type: object
                                                      type: array
                                                    matchLabels:
                                                      additionalProperties:
                                                        type: string
                                                      type: object
                                                  type: object
                                                namespaceSelector:
                                                  properties:
                                                    matchExpressions:
                                                      items:
                                                        properties:
                                                          key:
                                                            type: string
                                                          operator:
                                                            type: string
                                                          values:
                                                            items:
                                                              type: string
                                                            type: array
                                                        required:
                                                        - key
                                                        - operator
                                                        type: object
                                                      type: array
                                                    matchLabels:
                                                      additionalProperties:
                                                        type: string
                                                      type: object
                                                  type: object
                                                namespaces:
                                                  items:
                                                    type: string
                                                  type: array
                                                topologyKey:
                                                  type: string
                                              required:
                                              - topologyKey
                                              type: object
                                            type: array
                                        type: object
                                    type: object
                                  automountServiceAccountToken:
                                    type: boolean
                                  containers:
                                    items:
                                      properties:
                                        args:
                                          items:
                                            type: string
                                          type: array
                                        command:
                                          items:
                                            type: string
                                          type: array
                                        env:
                                          items:
                                            properties:
                                              name:
                                                type: string
                                              value:
                                                type: string
                                              valueFrom:
                                                properties:
                                                  configMapKeyRef:
                                                    properties:
                                                      key:
                                                        type: string
                                                      name:
                                                        type: string
                                                      optional:
                                                        type: boolean
                                                    required:
                                                    - key
                                                    type: object
                                                  fieldRef:
                                                    properties:
                                                      apiVersion:
                                                        type: string
                                                      fieldPath:
                                                        type: string
                                                    required:
                                                    - fieldPath
                                                    type: object
                                                  resourceFieldRef:
                                                    properties:
                                                      containerName:
                                                        type: string
                                                      divisor:
                                                        anyOf:
                                                        - type: integer
                                                        - type: string
                                                        pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                        x-kubernetes-int-or-string: true
                                                      resource:
                                                        type: string
                                                    required:
                                                    - resource
                                                    type: object
                                                  secretKeyRef:
                                                    properties:
                                                      key:
                                                        type: string
                                                      name:
                                                        type: string
                                                      optional:
                                                        type: boolean
                                                    required:
                                                    - key
                                                    type: object
                                                type: object
                                            required:
                                            - name
                                            type: object
                                          type: array
                                        envFrom:
                                          items:
                                            properties:
                                              configMapRef:
                                                properties:
                                                  name:
                                                    type: string
                                                  optional:
                                                    type: boolean
                                                type: object
                                              prefix:
                                                type: string
                                              secretRef:
                                                properties:
                                                  name:
                                                    type: string
                                                  optional:
                                                    type: boolean
                                                type: object
                                            type: object
                                          type: array
                                        image:
                                          type: string
                                        imagePullPolicy:
                                          type: string
                                        lifecycle:
                                          properties:
                                            postStart:
                                              properties:
                                                exec:
                                                  properties:
                                                    command:
                                                      items:
                                                        type: string
                                                      type: array
                                                  type: object
                                                httpGet:
                                                  properties:
                                                    host:
                                                      type: string
                                                    httpHeaders:
                                                      items:
                                                        properties:
                                                          name:
                                                            type: string
                                                          value:
                                                            type: string
                                                        required:
                                                        - name
                                                        - value
                                                        type: object
                                                      type: array
                                                    path:
                                                      type: string
                                                    port:
                                                      anyOf:
                                                      - type: integer
                                                      - type: string
                                                      x-kubernetes-int-or-string: true
                                                    scheme:
                                                      type: string
                                                  required:
                                                  - port
                                                  type: object
                                                tcpSocket:
                                                  properties:
                                                    host:
                                                      type: string
                                                    port:
                                                      anyOf:
                                                      - type: integer
                                                      - type: string
                                                      x-kubernetes-int-or-string: true
                                                  required:
                                                  - port
                                                  type: object
                                              type: object
                                            preStop:
                                              properties:
                                                exec:
                                                  properties:
                                                    command:
                                                      items:
                                                        type: string
                                                      type: array
                                                  type: object
                                                httpGet:
                                                  properties:
                                                    host:
                                                      type: string
                                                    httpHeaders:
                                                      items:
                                                        properties:
                                                          name:
                                                            type: string
                                                          value:
                                                            type: string
                                                        required:
                                                        - name
                                                        - value
                                                        type: object
                                                      type: array
                                                    path:
                                                      type: string
                                                    port:
                                                      anyOf:
                                                      - type: integer
                                                      - type: string
                                                      x-kubernetes-int-or-string: true
                                                    scheme:
                                                      type: string
                                                  required:
                                                  - port
                                                  type: object
                                                tcpSocket:
                                                  properties:
                                                    host:
                                                      type: string
                                                    port:
                                                      anyOf:
                                                      - type: integer
                                                      - type: string
                                                      x-kubernetes-int-or-string: true
                                                  required:
                                                  - port
                                                  type: object
                                              type: object
                                          type: object
                                        livenessProbe:
                                          properties:
                                            exec:
                                              properties:
                                                command:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            failureThreshold:
                                              format: int32
                                              type: integer
                                            grpc:
                                              properties:
                                                port:
                                                  format: int32
                                                  type: integer
                                                service:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            httpGet:
                                              properties:
                                                host:
                                                  type: string
                                                httpHeaders:
                                                  items:
                                                    properties:
                                                      name:
                                                        type: string
                                                      value:
                                                        type: string
                                                    required:
                                                    - name
                                                    - value
                                                    type: object
                                                  type: array
                                                path:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                                scheme:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            initialDelaySeconds:
                                              format: int32
                                              type: integer
                                            periodSeconds:
                                              format: int32
                                              type: integer
                                            successThreshold:
                                              format: int32
                                              type: integer
                                            tcpSocket:
                                              properties:
                                                host:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                              required:
                                              - port
                                              type: object
                                            terminationGracePeriodSeconds:
                                              format: int64
                                              type: integer
                                            timeoutSeconds:
                                              format: int32
                                              type: integer
                                          type: object
                                        name:
                                          type: string
                                        ports:
                                          items:
                                            properties:
                                              containerPort:
                                                format: int32
                                                type: integer
                                              hostIP:
                                                type: string
                                              hostPort:
                                                format: int32
                                                type: integer
                                              name:
                                                type: string
                                              protocol:
                                                default: TCP
                                                type: string
                                            required:
                                            - containerPort
                                            type: object
                                          type: array
                                          x-kubernetes-list-map-keys:
                                          - containerPort
                                          - protocol
                                          x-kubernetes-list-type: map
                                        readinessProbe:
                                          properties:
                                            exec:
                                              properties:
                                                command:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            failureThreshold:
                                              format: int32
                                              type: integer
                                            grpc:
                                              properties:
                                                port:
                                                  format: int32
                                                  type: integer
                                                service:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            httpGet:
                                              properties:
                                                host:
                                                  type: string
                                                httpHeaders:
                                                  items:
                                                    properties:
                                                      name:
                                                        type: string
                                                      value:
                                                        type: string
                                                    required:
                                                    - name
                                                    - value
                                                    type: object
                                                  type: array
                                                path:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                                scheme:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            initialDelaySeconds:
                                              format: int32
                                              type: integer
                                            periodSeconds:
                                              format: int32
                                              type: integer
                                            successThreshold:
                                              format: int32
                                              type: integer
                                            tcpSocket:
                                              properties:
                                                host:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                              required:
                                              - port
                                              type: object
                                            terminationGracePeriodSeconds:
                                              format: int64
                                              type: integer
                                            timeoutSeconds:
                                              format: int32
                                              type: integer
                                          type: object
                                        resources:
                                          properties:
                                            limits:
                                              additionalProperties:
                                                anyOf:
                                                - type: integer
                                                - type: string
                                                pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                x-kubernetes-int-or-string: true
                                              type: object
                                            requests:
                                              additionalProperties:
                                                anyOf:
                                                - type: integer
                                                - type: string
                                                pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                x-kubernetes-int-or-string: true
                                              type: object
                                          type: object
                                        securityContext:
                                          properties:
                                            allowPrivilegeEscalation:
                                              type: boolean
                                            capabilities:
                                              properties:
                                                add:
                                                  items:
                                                    type: string
                                                  type: array
                                                drop:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            privileged:
                                              type: boolean
                                            procMount:
                                              type: string
                                            readOnlyRootFilesystem:
                                              type: boolean
                                            runAsGroup:
                                              format: int64
                                              type: integer
                                            runAsNonRoot:
                                              type: boolean
                                            runAsUser:
                                              format: int64
                                              type: integer
                                            seLinuxOptions:
                                              properties:
                                                level:
                                                  type: string
                                                role:
                                                  type: string
                                                type:
                                                  type: string
                                                user:
                                                  type: string
                                              type: object
                                            seccompProfile:
                                              properties:
                                                localhostProfile:
                                                  type: string
                                                type:
                                                  type: string
                                              required:
                                              - type
                                              type: object
                                            windowsOptions:
                                              properties:
                                                gmsaCredentialSpec:
                                                  type: string
                                                gmsaCredentialSpecName:
                                                  type: string
                                                hostProcess:
                                                  type: boolean
                                                runAsUserName:
                                                  type: string
                                              type: object
                                          type: object
                                        startupProbe:
                                          properties:
                                            exec:
                                              properties:
                                                command:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            failureThreshold:
                                              format: int32
                                              type: integer
                                            grpc:
                                              properties:
                                                port:
                                                  format: int32
                                                  type: integer
                                                service:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            httpGet:
                                              properties:
                                                host:
                                                  type: string
                                                httpHeaders:
                                                  items:
                                                    properties:
                                                      name:
                                                        type: string
                                                      value:
                                                        type: string
                                                    required:
                                                    - name
                                                    - value
                                                    type: object
                                                  type: array
                                                path:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                                scheme:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            initialDelaySeconds:
                                              format: int32
                                              type: integer
                                            periodSeconds:
                                              format: int32
                                              type: integer
                                            successThreshold:
                                              format: int32
                                              type: integer
                                            tcpSocket:
                                              properties:
                                                host:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                              required:
                                              - port
                                              type: object
                                            terminationGracePeriodSeconds:
                                              format: int64
                                              type: integer
                                            timeoutSeconds:
                                              format: int32
                                              type: integer
                                          type: object
                                        stdin:
                                          type: boolean
                                        stdinOnce:
                                          type: boolean
                                        terminationMessagePath:
                                          type: string
                                        terminationMessagePolicy:
                                          type: string
                                        tty:
                                          type: boolean
                                        volumeDevices:
                                          items:
                                            properties:
                                              devicePath:
                                                type: string
                                              name:
                                                type: string
                                            required:
                                            - devicePath
                                            - name
                                            type: object
                                          type: array
                                        volumeMounts:
                                          items:
                                            properties:
                                              mountPath:
                                                type: string
                                              mountPropagation:
                                                type: string
                                              name:
                                                type: string
                                              readOnly:
                                                type: boolean
                                              subPath:
                                                type: string
                                              subPathExpr:
                                                type: string
                                            required:
                                            - mountPath
                                            - name
                                            type: object
                                          type: array
                                        workingDir:
                                          type: string
                                      required:
                                      - name
                                      type: object
                                    type: array
                                  dnsConfig:
                                    properties:
                                      nameservers:
                                        items:
                                          type: string
                                        type: array
                                      options:
                                        items:
                                          properties:
                                            name:
                                              type: string
                                            value:
                                              type: string
                                          type: object
                                        type: array
                                      searches:
                                        items:
                                          type: string
                                        type: array
                                    type: object
                                  dnsPolicy:
                                    type: string
                                  enableServiceLinks:
                                    type: boolean
                                  ephemeralContainers:
                                    items:
                                      properties:
                                        args:
                                          items:
                                            type: string
                                          type: array
                                        command:
                                          items:
                                            type: string
                                          type: array
                                        env:
                                          items:
                                            properties:
                                              name:
                                                type: string
                                              value:
                                                type: string
                                              valueFrom:
                                                properties:
                                                  configMapKeyRef:
                                                    properties:
                                                      key:
                                                        type: string
                                                      name:
                                                        type: string
                                                      optional:
                                                        type: boolean
                                                    required:
                                                    - key
                                                    type: object
                                                  fieldRef:
                                                    properties:
                                                      apiVersion:
                                                        type: string
                                                      fieldPath:
                                                        type: string
                                                    required:
                                                    - fieldPath
                                                    type: object
                                                  resourceFieldRef:
                                                    properties:
                                                      containerName:
                                                        type: string
                                                      divisor:
                                                        anyOf:
                                                        - type: integer
                                                        - type: string
                                                        pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                        x-kubernetes-int-or-string: true
                                                      resource:
                                                        type: string
                                                    required:
                                                    - resource
                                                    type: object
                                                  secretKeyRef:
                                                    properties:
                                                      key:
                                                        type: string
                                                      name:
                                                        type: string
                                                      optional:
                                                        type: boolean
                                                    required:
                                                    - key
                                                    type: object
                                                type: object
                                            required:
                                            - name
                                            type: object
                                          type: array
                                        envFrom:
                                          items:
                                            properties:
                                              configMapRef:
                                                properties:
                                                  name:
                                                    type: string
                                                  optional:
                                                    type: boolean
                                                type: object
                                              prefix:
                                                type: string
                                              secretRef:
                                                properties:
                                                  name:
                                                    type: string
                                                  optional:
                                                    type: boolean
                                                type: object
                                            type: object
                                          type: array
                                        image:
                                          type: string
                                        imagePullPolicy:
                                          type: string
                                        lifecycle:
                                          properties:
                                            postStart:
                                              properties:
                                                exec:
                                                  properties:
                                                    command:
                                                      items:
                                                        type: string
                                                      type: array
                                                  type: object
                                                httpGet:
                                                  properties:
                                                    host:
                                                      type: string
                                                    httpHeaders:
                                                      items:
                                                        properties:
                                                          name:
                                                            type: string
                                                          value:
                                                            type: string
                                                        required:
                                                        - name
                                                        - value
                                                        type: object
                                                      type: array
                                                    path:
                                                      type: string
                                                    port:
                                                      anyOf:
                                                      - type: integer
                                                      - type: string
                                                      x-kubernetes-int-or-string: true
                                                    scheme:
                                                      type: string
                                                  required:
                                                  - port
                                                  type: object
                                                tcpSocket:
                                                  properties:
                                                    host:
                                                      type: string
                                                    port:
                                                      anyOf:
                                                      - type: integer
                                                      - type: string
                                                      x-kubernetes-int-or-string: true
                                                  required:
                                                  - port
                                                  type: object
                                              type: object
                                            preStop:
                                              properties:
                                                exec:
                                                  properties:
                                                    command:
                                                      items:
                                                        type: string
                                                      type: array
                                                  type: object
                                                httpGet:
                                                  properties:
                                                    host:
                                                      type: string
                                                    httpHeaders:
                                                      items:
                                                        properties:
                                                          name:
                                                            type: string
                                                          value:
                                                            type: string
                                                        required:
                                                        - name
                                                        - value
                                                        type: object
                                                      type: array
                                                    path:
                                                      type: string
                                                    port:
                                                      anyOf:
                                                      - type: integer
                                                      - type: string
                                                      x-kubernetes-int-or-string: true
                                                    scheme:
                                                      type: string
                                                  required:
                                                  - port
                                                  type: object
                                                tcpSocket:
                                                  properties:
                                                    host:
                                                      type: string
                                                    port:
                                                      anyOf:
                                                      - type: integer
                                                      - type: string
                                                      x-kubernetes-int-or-string: true
                                                  required:
                                                  - port
                                                  type: object
                                              type: object
                                          type: object
                                        livenessProbe:
                                          properties:
                                            exec:
                                              properties:
                                                command:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            failureThreshold:
                                              format: int32
                                              type: integer
                                            grpc:
                                              properties:
                                                port:
                                                  format: int32
                                                  type: integer
                                                service:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            httpGet:
                                              properties:
                                                host:
                                                  type: string
                                                httpHeaders:
                                                  items:
                                                    properties:
                                                      name:
                                                        type: string
                                                      value:
                                                        type: string
                                                    required:
                                                    - name
                                                    - value
                                                    type: object
                                                  type: array
                                                path:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                                scheme:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            initialDelaySeconds:
                                              format: int32
                                              type: integer
                                            periodSeconds:
                                              format: int32
                                              type: integer
                                            successThreshold:
                                              format: int32
                                              type: integer
                                            tcpSocket:
                                              properties:
                                                host:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                              required:
                                              - port
                                              type: object
                                            terminationGracePeriodSeconds:
                                              format: int64
                                              type: integer
                                            timeoutSeconds:
                                              format: int32
                                              type: integer
                                          type: object
                                        name:
                                          type: string
                                        ports:
                                          items:
                                            properties:
                                              containerPort:
                                                format: int32
                                                type: integer
                                              hostIP:
                                                type: string
                                              hostPort:
                                                format: int32
                                                type: integer
                                              name:
                                                type: string
                                              protocol:
                                                default: TCP
                                                type: string
                                            required:
                                            - containerPort
                                            type: object
                                          type: array
                                          x-kubernetes-list-map-keys:
                                          - containerPort
                                          - protocol
                                          x-kubernetes-list-type: map
                                        readinessProbe:
                                          properties:
                                            exec:
                                              properties:
                                                command:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            failureThreshold:
                                              format: int32
                                              type: integer
                                            grpc:
                                              properties:
                                                port:
                                                  format: int32
                                                  type: integer
                                                service:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            httpGet:
                                              properties:
                                                host:
                                                  type: string
                                                httpHeaders:
                                                  items:
                                                    properties:
                                                      name:
                                                        type: string
                                                      value:
                                                        type: string
                                                    required:
                                                    - name
                                                    - value
                                                    type: object
                                                  type: array
                                                path:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                                scheme:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            initialDelaySeconds:
                                              format: int32
                                              type: integer
                                            periodSeconds:
                                              format: int32
                                              type: integer
                                            successThreshold:
                                              format: int32
                                              type: integer
                                            tcpSocket:
                                              properties:
                                                host:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                              required:
                                              - port
                                              type: object
                                            terminationGracePeriodSeconds:
                                              format: int64
                                              type: integer
                                            timeoutSeconds:
                                              format: int32
                                              type: integer
                                          type: object
                                        resources:
                                          properties:
                                            limits:
                                              additionalProperties:
                                                anyOf:
                                                - type: integer
                                                - type: string
                                                pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                x-kubernetes-int-or-string: true
                                              type: object
                                            requests:
                                              additionalProperties:
                                                anyOf:
                                                - type: integer
                                                - type: string
                                                pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                x-kubernetes-int-or-string: true
                                              type: object
                                          type: object
                                        securityContext:
                                          properties:
                                            allowPrivilegeEscalation:
                                              type: boolean
                                            capabilities:
                                              properties:
                                                add:
                                                  items:
                                                    type: string
                                                  type: array
                                                drop:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            privileged:
                                              type: boolean
                                            procMount:
                                              type: string
                                            readOnlyRootFilesystem:
                                              type: boolean
                                            runAsGroup:
                                              format: int64
                                              type: integer
                                            runAsNonRoot:
                                              type: boolean
                                            runAsUser:
                                              format: int64
                                              type: integer
                                            seLinuxOptions:
                                              properties:
                                                level:
                                                  type: string
                                                role:
                                                  type: string
                                                type:
                                                  type: string
                                                user:
                                                  type: string
                                              type: object
                                            seccompProfile:
                                              properties:
                                                localhostProfile:
                                                  type: string
                                                type:
                                                  type: string
                                              required:
                                              - type
                                              type: object
                                            windowsOptions:
                                              properties:
                                                gmsaCredentialSpec:
                                                  type: string
                                                gmsaCredentialSpecName:
                                                  type: string
                                                hostProcess:
                                                  type: boolean
                                                runAsUserName:
                                                  type: string
                                              type: object
                                          type: object
                                        startupProbe:
                                          properties:
                                            exec:
                                              properties:
                                                command:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            failureThreshold:
                                              format: int32
                                              type: integer
                                            grpc:
                                              properties:
                                                port:
                                                  format: int32
                                                  type: integer
                                                service:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            httpGet:
                                              properties:
                                                host:
                                                  type: string
                                                httpHeaders:
                                                  items:
                                                    properties:
                                                      name:
                                                        type: string
                                                      value:
                                                        type: string
                                                    required:
                                                    - name
                                                    - value
                                                    type: object
                                                  type: array
                                                path:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                                scheme:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            initialDelaySeconds:
                                              format: int32
                                              type: integer
                                            periodSeconds:
                                              format: int32
                                              type: integer
                                            successThreshold:
                                              format: int32
                                              type: integer
                                            tcpSocket:
                                              properties:
                                                host:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                              required:
                                              - port
                                              type: object
                                            terminationGracePeriodSeconds:
                                              format: int64
                                              type: integer
                                            timeoutSeconds:
                                              format: int32
                                              type: integer
                                          type: object
                                        stdin:
                                          type: boolean
                                        stdinOnce:
                                          type: boolean
                                        targetContainerName:
                                          type: string
                                        terminationMessagePath:
                                          type: string
                                        terminationMessagePolicy:
                                          type: string
                                        tty:
                                          type: boolean
                                        volumeDevices:
                                          items:
                                            properties:
                                              devicePath:
                                                type: string
                                              name:
                                                type: string
                                            required:
                                            - devicePath
                                            - name
                                            type: object
                                          type: array
                                        volumeMounts:
                                          items:
                                            properties:
                                              mountPath:
                                                type: string
                                              mountPropagation:
                                                type: string
                                              name:
                                                type: string
                                              readOnly:
                                                type: boolean
                                              subPath:
                                                type: string
                                              subPathExpr:
                                                type: string
                                            required:
                                            - mountPath
                                            - name
                                            type: object
                                          type: array
                                        workingDir:
                                          type: string
                                      required:
                                      - name
                                      type: object
                                    type: array
                                  hostAliases:
                                    items:
                                      properties:
                                        hostnames:
                                          items:
                                            type: string
                                          type: array
                                        ip:
                                          type: string
                                      type: object
                                    type: array
                                  hostIPC:
                                    type: boolean
                                  hostNetwork:
                                    type: boolean
                                  hostPID:
                                    type: boolean
                                  hostname:
                                    type: string
                                  imagePullSecrets:
                                    items:
                                      properties:
                                        name:
                                          type: string
                                      type: object
                                    type: array
                                  initContainers:
                                    items:
                                      properties:
                                        args:
                                          items:
                                            type: string
                                          type: array
                                        command:
                                          items:
                                            type: string
                                          type: array
                                        env:
                                          items:
                                            properties:
                                              name:
                                                type: string
                                              value:
                                                type: string
                                              valueFrom:
                                                properties:
                                                  configMapKeyRef:
                                                    properties:
                                                      key:
                                                        type: string
                                                      name:
                                                        type: string
                                                      optional:
                                                        type: boolean
                                                    required:
                                                    - key
                                                    type: object
                                                  fieldRef:
                                                    properties:
                                                      apiVersion:
                                                        type: string
                                                      fieldPath:
                                                        type: string
                                                    required:
                                                    - fieldPath
                                                    type: object
                                                  resourceFieldRef:
                                                    properties:
                                                      containerName:
                                                        type: string
                                                      divisor:
                                                        anyOf:
                                                        - type: integer
                                                        - type: string
                                                        pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                        x-kubernetes-int-or-string: true
                                                      resource:
                                                        type: string
                                                    required:
                                                    - resource
                                                    type: object
                                                  secretKeyRef:
                                                    properties:
                                                      key:
                                                        type: string
                                                      name:
                                                        type: string
                                                      optional:
                                                        type: boolean
                                                    required:
                                                    - key
                                                    type: object
                                                type: object
                                            required:
                                            - name
                                            type: object
                                          type: array
                                        envFrom:
                                          items:
                                            properties:
                                              configMapRef:
                                                properties:
                                                  name:
                                                    type: string
                                                  optional:
                                                    type: boolean
                                                type: object
                                              prefix:
                                                type: string
                                              secretRef:
                                                properties:
                                                  name:
                                                    type: string
                                                  optional:
                                                    type: boolean
                                                type: object
                                            type: object
                                          type: array
                                        image:
                                          type: string
                                        imagePullPolicy:
                                          type: string
                                        lifecycle:
                                          properties:
                                            postStart:
                                              properties:
                                                exec:
                                                  properties:
                                                    command:
                                                      items:
                                                        type: string
                                                      type: array
                                                  type: object
                                                httpGet:
                                                  properties:
                                                    host:
                                                      type: string
                                                    httpHeaders:
                                                      items:
                                                        properties:
                                                          name:
                                                            type: string
                                                          value:
                                                            type: string
                                                        required:
                                                        - name
                                                        - value
                                                        type: object
                                                      type: array
                                                    path:
                                                      type: string
                                                    port:
                                                      anyOf:
                                                      - type: integer
                                                      - type: string
                                                      x-kubernetes-int-or-string: true
                                                    scheme:
                                                      type: string
                                                  required:
                                                  - port
                                                  type: object
                                                tcpSocket:
                                                  properties:
                                                    host:
                                                      type: string
                                                    port:
                                                      anyOf:
                                                      - type: integer
                                                      - type: string
                                                      x-kubernetes-int-or-string: true
                                                  required:
                                                  - port
                                                  type: object
                                              type: object
                                            preStop:
                                              properties:
                                                exec:
                                                  properties:
                                                    command:
                                                      items:
                                                        type: string
                                                      type: array
                                                  type: object
                                                httpGet:
                                                  properties:
                                                    host:
                                                      type: string
                                                    httpHeaders:
                                                      items:
                                                        properties:
                                                          name:
                                                            type: string
                                                          value:
                                                            type: string
                                                        required:
                                                        - name
                                                        - value
                                                        type: object
                                                      type: array
                                                    path:
                                                      type: string
                                                    port:
                                                      anyOf:
                                                      - type: integer
                                                      - type: string
                                                      x-kubernetes-int-or-string: true
                                                    scheme:
                                                      type: string
                                                  required:
                                                  - port
                                                  type: object
                                                tcpSocket:
                                                  properties:
                                                    host:
                                                      type: string
                                                    port:
                                                      anyOf:
                                                      - type: integer
                                                      - type: string
                                                      x-kubernetes-int-or-string: true
                                                  required:
                                                  - port
                                                  type: object
                                              type: object
                                          type: object
                                        livenessProbe:
                                          properties:
                                            exec:
                                              properties:
                                                command:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            failureThreshold:
                                              format: int32
                                              type: integer
                                            grpc:
                                              properties:
                                                port:
                                                  format: int32
                                                  type: integer
                                                service:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            httpGet:
                                              properties:
                                                host:
                                                  type: string
                                                httpHeaders:
                                                  items:
                                                    properties:
                                                      name:
                                                        type: string
                                                      value:
                                                        type: string
                                                    required:
                                                    - name
                                                    - value
                                                    type: object
                                                  type: array
                                                path:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                                scheme:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            initialDelaySeconds:
                                              format: int32
                                              type: integer
                                            periodSeconds:
                                              format: int32
                                              type: integer
                                            successThreshold:
                                              format: int32
                                              type: integer
                                            tcpSocket:
                                              properties:
                                                host:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                              required:
                                              - port
                                              type: object
                                            terminationGracePeriodSeconds:
                                              format: int64
                                              type: integer
                                            timeoutSeconds:
                                              format: int32
                                              type: integer
                                          type: object
                                        name:
                                          type: string
                                        ports:
                                          items:
                                            properties:
                                              containerPort:
                                                format: int32
                                                type: integer
                                              hostIP:
                                                type: string
                                              hostPort:
                                                format: int32
                                                type: integer
                                              name:
                                                type: string
                                              protocol:
                                                default: TCP
                                                type: string
                                            required:
                                            - containerPort
                                            type: object
                                          type: array
                                          x-kubernetes-list-map-keys:
                                          - containerPort
                                          - protocol
                                          x-kubernetes-list-type: map
                                        readinessProbe:
                                          properties:
                                            exec:
                                              properties:
                                                command:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            failureThreshold:
                                              format: int32
                                              type: integer
                                            grpc:
                                              properties:
                                                port:
                                                  format: int32
                                                  type: integer
                                                service:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            httpGet:
                                              properties:
                                                host:
                                                  type: string
                                                httpHeaders:
                                                  items:
                                                    properties:
                                                      name:
                                                        type: string
                                                      value:
                                                        type: string
                                                    required:
                                                    - name
                                                    - value
                                                    type: object
                                                  type: array
                                                path:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                                scheme:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            initialDelaySeconds:
                                              format: int32
                                              type: integer
                                            periodSeconds:
                                              format: int32
                                              type: integer
                                            successThreshold:
                                              format: int32
                                              type: integer
                                            tcpSocket:
                                              properties:
                                                host:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                              required:
                                              - port
                                              type: object
                                            terminationGracePeriodSeconds:
                                              format: int64
                                              type: integer
                                            timeoutSeconds:
                                              format: int32
                                              type: integer
                                          type: object
                                        resources:
                                          properties:
                                            limits:
                                              additionalProperties:
                                                anyOf:
                                                - type: integer
                                                - type: string
                                                pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                x-kubernetes-int-or-string: true
                                              type: object
                                            requests:
                                              additionalProperties:
                                                anyOf:
                                                - type: integer
                                                - type: string
                                                pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                x-kubernetes-int-or-string: true
                                              type: object
                                          type: object
                                        securityContext:
                                          properties:
                                            allowPrivilegeEscalation:
                                              type: boolean
                                            capabilities:
                                              properties:
                                                add:
                                                  items:
                                                    type: string
                                                  type: array
                                                drop:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            privileged:
                                              type: boolean
                                            procMount:
                                              type: string
                                            readOnlyRootFilesystem:
                                              type: boolean
                                            runAsGroup:
                                              format: int64
                                              type: integer
                                            runAsNonRoot:
                                              type: boolean
                                            runAsUser:
                                              format: int64
                                              type: integer
                                            seLinuxOptions:
                                              properties:
                                                level:
                                                  type: string
                                                role:
                                                  type: string
                                                type:
                                                  type: string
                                                user:
                                                  type: string
                                              type: object
                                            seccompProfile:
                                              properties:
                                                localhostProfile:
                                                  type: string
                                                type:
                                                  type: string
                                              required:
                                              - type
                                              type: object
                                            windowsOptions:
                                              properties:
                                                gmsaCredentialSpec:
                                                  type: string
                                                gmsaCredentialSpecName:
                                                  type: string
                                                hostProcess:
                                                  type: boolean
                                                runAsUserName:
                                                  type: string
                                              type: object
                                          type: object
                                        startupProbe:
                                          properties:
                                            exec:
                                              properties:
                                                command:
                                                  items:
                                                    type: string
                                                  type: array
                                              type: object
                                            failureThreshold:
                                              format: int32
                                              type: integer
                                            grpc:
                                              properties:
                                                port:
                                                  format: int32
                                                  type: integer
                                                service:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            httpGet:
                                              properties:
                                                host:
                                                  type: string
                                                httpHeaders:
                                                  items:
                                                    properties:
                                                      name:
                                                        type: string
                                                      value:
                                                        type: string
                                                    required:
                                                    - name
                                                    - value
                                                    type: object
                                                  type: array
                                                path:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                                scheme:
                                                  type: string
                                              required:
                                              - port
                                              type: object
                                            initialDelaySeconds:
                                              format: int32
                                              type: integer
                                            periodSeconds:
                                              format: int32
                                              type: integer
                                            successThreshold:
                                              format: int32
                                              type: integer
                                            tcpSocket:
                                              properties:
                                                host:
                                                  type: string
                                                port:
                                                  anyOf:
                                                  - type: integer
                                                  - type: string
                                                  x-kubernetes-int-or-string: true
                                              required:
                                              - port
                                              type: object
                                            terminationGracePeriodSeconds:
                                              format: int64
                                              type: integer
                                            timeoutSeconds:
                                              format: int32
                                              type: integer
                                          type: object
                                        stdin:
                                          type: boolean
                                        stdinOnce:
                                          type: boolean
                                        terminationMessagePath:
                                          type: string
                                        terminationMessagePolicy:
                                          type: string
                                        tty:
                                          type: boolean
                                        volumeDevices:
                                          items:
                                            properties:
                                              devicePath:
                                                type: string
                                              name:
                                                type: string
                                            required:
                                            - devicePath
                                            - name
                                            type: object
                                          type: array
                                        volumeMounts:
                                          items:
                                            properties:
                                              mountPath:
                                                type: string
                                              mountPropagation:
                                                type: string
                                              name:
                                                type: string
                                              readOnly:
                                                type: boolean
                                              subPath:
                                                type: string
                                              subPathExpr:
                                                type: string
                                            required:
                                            - mountPath
                                            - name
                                            type: object
                                          type: array
                                        workingDir:
                                          type: string
                                      required:
                                      - name
                                      type: object
                                    type: array
                                  nodeName:
                                    type: string
                                  nodeSelector:
                                    additionalProperties:
                                      type: string
                                    type: object
                                    x-kubernetes-map-type: atomic
                                  os:
                                    properties:
                                      name:
                                        type: string
                                    required:
                                    - name
                                    type: object
                                  overhead:
                                    additionalProperties:
                                      anyOf:
                                      - type: integer
                                      - type: string
                                      pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                      x-kubernetes-int-or-string: true
                                    type: object
                                  preemptionPolicy:
                                    type: string
                                  priority:
                                    format: int32
                                    type: integer
                                  priorityClassName:
                                    type: string
                                  readinessGates:
                                    items:
                                      properties:
                                        conditionType:
                                          type: string
                                      required:
                                      - conditionType
                                      type: object
                                    type: array
                                  restartPolicy:
                                    type: string
                                  runtimeClassName:
                                    type: string
                                  schedulerName:
                                    type: string
                                  securityContext:
                                    properties:
                                      fsGroup:
                                        format: int64
                                        type: integer
                                      fsGroupChangePolicy:
                                        type: string
                                      runAsGroup:
                                        format: int64
                                        type: integer
                                      runAsNonRoot:
                                        type: boolean
                                      runAsUser:
                                        format: int64
                                        type: integer
                                      seLinuxOptions:
                                        properties:
                                          level:
                                            type: string
                                          role:
                                            type: string
                                          type:
                                            type: string
                                          user:
                                            type: string
                                        type: object
                                      seccompProfile:
                                        properties:
                                          localhostProfile:
                                            type: string
                                          type:
                                            type: string
                                        required:
                                        - type
                                        type: object
                                      supplementalGroups:
                                        items:
                                          format: int64
                                          type: integer
                                        type: array
                                      sysctls:
                                        items:
                                          properties:
                                            name:
                                              type: string
                                            value:
                                              type: string
                                          required:
                                          - name
                                          - value
                                          type: object
                                        type: array
                                      windowsOptions:
                                        properties:
                                          gmsaCredentialSpec:
                                            type: string
                                          gmsaCredentialSpecName:
                                            type: string
                                          hostProcess:
                                            type: boolean
                                          runAsUserName:
                                            type: string
                                        type: object
                                    type: object
                                  serviceAccount:
                                    type: string
                                  serviceAccountName:
                                    type: string
                                  setHostnameAsFQDN:
                                    type: boolean
                                  shareProcessNamespace:
                                    type: boolean
                                  subdomain:
                                    type: string
                                  terminationGracePeriodSeconds:
                                    format: int64
                                    type: integer
                                  tolerations:
                                    items:
                                      properties:
                                        effect:
                                          type: string
                                        key:
                                          type: string
                                        operator:
                                          type: string
                                        tolerationSeconds:
                                          format: int64
                                          type: integer
                                        value:
                                          type: string
                                      type: object
                                    type: array
                                  topologySpreadConstraints:
                                    items:
                                      properties:
                                        labelSelector:
                                          properties:
                                            matchExpressions:
                                              items:
                                                properties:
                                                  key:
                                                    type: string
                                                  operator:
                                                    type: string
                                                  values:
                                                    items:
                                                      type: string
                                                    type: array
                                                required:
                                                - key
                                                - operator
                                                type: object
                                              type: array
                                            matchLabels:
                                              additionalProperties:
                                                type: string
                                              type: object
                                          type: object
                                        maxSkew:
                                          format: int32
                                          type: integer
                                        minDomains:
                                          format: int32
                                          type: integer
                                        topologyKey:
                                          type: string
                                        whenUnsatisfiable:
                                          type: string
                                      required:
                                      - maxSkew
                                      - topologyKey
                                      - whenUnsatisfiable
                                      type: object
                                    type: array
                                    x-kubernetes-list-map-keys:
                                    - topologyKey
                                    - whenUnsatisfiable
                                    x-kubernetes-list-type: map
                                  volumes:
                                    items:
                                      properties:
                                        awsElasticBlockStore:
                                          properties:
                                            fsType:
                                              type: string
                                            partition:
                                              format: int32
                                              type: integer
                                            readOnly:
                                              type: boolean
                                            volumeID:
                                              type: string
                                          required:
                                          - volumeID
                                          type: object
                                        azureDisk:
                                          properties:
                                            cachingMode:
                                              type: string
                                            diskName:
                                              type: string
                                            diskURI:
                                              type: string
                                            fsType:
                                              type: string
                                            kind:
                                              type: string
                                            readOnly:
                                              type: boolean
                                          required:
                                          - diskName
                                          - diskURI
                                          type: object
                                        azureFile:
                                          properties:
                                            readOnly:
                                              type: boolean
                                            secretName:
                                              type: string
                                            shareName:
                                              type: string
                                          required:
                                          - secretName
                                          - shareName
                                          type: object
                                        cephfs:
                                          properties:
                                            monitors:
                                              items:
                                                type: string
                                              type: array
                                            path:
                                              type: string
                                            readOnly:
                                              type: boolean
                                            secretFile:
                                              type: string
                                            secretRef:
                                              properties:
                                                name:
                                                  type: string
                                              type: object
                                            user:
                                              type: string
                                          required:
                                          - monitors
                                          type: object
                                        cinder:
                                          properties:
                                            fsType:
                                              type: string
                                            readOnly:
                                              type: boolean
                                            secretRef:
                                              properties:
                                                name:
                                                  type: string
                                              type: object
                                            volumeID:
                                              type: string
                                          required:
                                          - volumeID
                                          type: object
                                        configMap:
                                          properties:
                                            defaultMode:
                                              format: int32
                                              type: integer
                                            items:
                                              items:
                                                properties:
                                                  key:
                                                    type: string
                                                  mode:
                                                    format: int32
                                                    type: integer
                                                  path:
                                                    type: string
                                                required:
                                                - key
                                                - path
                                                type: object
                                              type: array
                                            name:
                                              type: string
                                            optional:
                                              type: boolean
                                          type: object
                                        csi:
                                          properties:
                                            driver:
                                              type: string
                                            fsType:
                                              type: string
                                            nodePublishSecretRef:
                                              properties:
                                                name:
                                                  type: string
                                              type: object
                                            readOnly:
                                              type: boolean
                                            volumeAttributes:
                                              additionalProperties:
                                                type: string
                                              type: object
                                          required:
                                          - driver
                                          type: object
                                        downwardAPI:
                                          properties:
                                            defaultMode:
                                              format: int32
                                              type: integer
                                            items:
                                              items:
                                                properties:
                                                  fieldRef:
                                                    properties:
                                                      apiVersion:
                                                        type: string
                                                      fieldPath:
                                                        type: string
                                                    required:
                                                    - fieldPath
                                                    type: object
                                                  mode:
                                                    format: int32
                                                    type: integer
                                                  path:
                                                    type: string
                                                  resourceFieldRef:
                                                    properties:
                                                      containerName:
                                                        type: string
                                                      divisor:
                                                        anyOf:
                                                        - type: integer
                                                        - type: string
                                                        pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                        x-kubernetes-int-or-string: true
                                                      resource:
                                                        type: string
                                                    required:
                                                    - resource
                                                    type: object
                                                required:
                                                - path
                                                type: object
                                              type: array
                                          type: object
                                        emptyDir:
                                          properties:
                                            medium:
                                              type: string
                                            sizeLimit:
                                              anyOf:
                                              - type: integer
                                              - type: string
                                              pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                              x-kubernetes-int-or-string: true
                                          type: object
                                        ephemeral:
                                          properties:
                                            volumeClaimTemplate:
                                              properties:
                                                metadata:
                                                  type: object
                                                spec:
                                                  properties:
                                                    accessModes:
                                                      items:
                                                        type: string
                                                      type: array
                                                    dataSource:
                                                      properties:
                                                        apiGroup:
                                                          type: string
                                                        kind:
                                                          type: string
                                                        name:
                                                          type: string
                                                      required:
                                                      - kind
                                                      - name
                                                      type: object
                                                    dataSourceRef:
                                                      properties:
                                                        apiGroup:
                                                          type: string
                                                        kind:
                                                          type: string
                                                        name:
                                                          type: string
                                                      required:
                                                      - kind
                                                      - name
                                                      type: object
                                                    resources:
                                                      properties:
                                                        limits:
                                                          additionalProperties:
                                                            anyOf:
                                                            - type: integer
                                                            - type: string
                                                            pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                            x-kubernetes-int-or-string: true
                                                          type: object
                                                        requests:
                                                          additionalProperties:
                                                            anyOf:
                                                            - type: integer
                                                            - type: string
                                                            pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                            x-kubernetes-int-or-string: true
                                                          type: object
                                                      type: object
                                                    selector:
                                                      properties:
                                                        matchExpressions:
                                                          items:
                                                            properties:
                                                              key:
                                                                type: string
                                                              operator:
                                                                type: string
                                                              values:
                                                                items:
                                                                  type: string
                                                                type: array
                                                            required:
                                                            - key
                                                            - operator
                                                            type: object
                                                          type: array
                                                        matchLabels:
                                                          additionalProperties:
                                                            type: string
                                                          type: object
                                                      type: object
                                                    storageClassName:
                                                      type: string
                                                    volumeMode:
                                                      type: string
                                                    volumeName:
                                                      type: string
                                                  type: object
                                              required:
                                              - spec
                                              type: object
                                          type: object
                                        fc:
                                          properties:
                                            fsType:
                                              type: string
                                            lun:
                                              format: int32
                                              type: integer
                                            readOnly:
                                              type: boolean
                                            targetWWNs:
                                              items:
                                                type: string
                                              type: array
                                            wwids:
                                              items:
                                                type: string
                                              type: array
                                          type: object
                                        flexVolume:
                                          properties:
                                            driver:
                                              type: string
                                            fsType:
                                              type: string
                                            options:
                                              additionalProperties:
                                                type: string
                                              type: object
                                            readOnly:
                                              type: boolean
                                            secretRef:
                                              properties:
                                                name:
                                                  type: string
                                              type: object
                                          required:
                                          - driver
                                          type: object
                                        flocker:
                                          properties:
                                            datasetName:
                                              type: string
                                            datasetUUID:
                                              type: string
                                          type: object
                                        gcePersistentDisk:
                                          properties:
                                            fsType:
                                              type: string
                                            partition:
                                              format: int32
                                              type: integer
                                            pdName:
                                              type: string
                                            readOnly:
                                              type: boolean
                                          required:
                                          - pdName
                                          type: object
                                        gitRepo:
                                          properties:
                                            directory:
                                              type: string
                                            repository:
                                              type: string
                                            revision:
                                              type: string
                                          required:
                                          - repository
                                          type: object
                                        glusterfs:
                                          properties:
                                            endpoints:
                                              type: string
                                            path:
                                              type: string
                                            readOnly:
                                              type: boolean
                                          required:
                                          - endpoints
                                          - path
                                          type: object
                                        hostPath:
                                          properties:
                                            path:
                                              type: string
                                            type:
                                              type: string
                                          required:
                                          - path
                                          type: object
                                        iscsi:
                                          properties:
                                            chapAuthDiscovery:
                                              type: boolean
                                            chapAuthSession:
                                              type: boolean
                                            fsType:
                                              type: string
                                            initiatorName:
                                              type: string
                                            iqn:
                                              type: string
                                            iscsiInterface:
                                              type: string
                                            lun:
                                              format: int32
                                              type: integer
                                            portals:
                                              items:
                                                type: string
                                              type: array
                                            readOnly:
                                              type: boolean
                                            secretRef:
                                              properties:
                                                name:
                                                  type: string
                                              type: object
                                            targetPortal:
                                              type: string
                                          required:
                                          - iqn
                                          - lun
                                          - targetPortal
                                          type: object
                                        name:
                                          type: string
                                        nfs:
                                          properties:
                                            path:
                                              type: string
                                            readOnly:
                                              type: boolean
                                            server:
                                              type: string
                                          required:
                                          - path
                                          - server
                                          type: object
                                        persistentVolumeClaim:
                                          properties:
                                            claimName:
                                              type: string
                                            readOnly:
                                              type: boolean
                                          required:
                                          - claimName
                                          type: object
                                        photonPersistentDisk:
                                          properties:
                                            fsType:
                                              type: string
                                            pdID:
                                              type: string
                                          required:
                                          - pdID
                                          type: object
                                        portworxVolume:
                                          properties:
                                            fsType:
                                              type: string
                                            readOnly:
                                              type: boolean
                                            volumeID:
                                              type: string
                                          required:
                                          - volumeID
                                          type: object
                                        projected:
                                          properties:
                                            defaultMode:
                                              format: int32
                                              type: integer
                                            sources:
                                              items:
                                                properties:
                                                  configMap:
                                                    properties:
                                                      items:
                                                        items:
                                                          properties:
                                                            key:
                                                              type: string
                                                            mode:
                                                              format: int32
                                                              type: integer
                                                            path:
                                                              type: string
                                                          required:
                                                          - key
                                                          - path
                                                          type: object
                                                        type: array
                                                      name:
                                                        type: string
                                                      optional:
                                                        type: boolean
                                                    type: object
                                                  downwardAPI:
                                                    properties:
                                                      items:
                                                        items:
                                                          properties:
                                                            fieldRef:
                                                              properties:
                                                                apiVersion:
                                                                  type: string
                                                                fieldPath:
                                                                  type: string
                                                              required:
                                                              - fieldPath
                                                              type: object
                                                            mode:
                                                              format: int32
                                                              type: integer
                                                            path:
                                                              type: string
                                                            resourceFieldRef:
                                                              properties:
                                                                containerName:
                                                                  type: string
                                                                divisor:
                                                                  anyOf:
                                                                  - type: integer
                                                                  - type: string
                                                                  pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                                                  x-kubernetes-int-or-string: true
                                                                resource:
                                                                  type: string
                                                              required:
                                                              - resource
                                                              type: object
                                                          required:
                                                          - path
                                                          type: object
                                                        type: array
                                                    type: object
                                                  secret:
                                                    properties:
                                                      items:
                                                        items:
                                                          properties:
                                                            key:
                                                              type: string
                                                            mode:
                                                              format: int32
                                                              type: integer
                                                            path:
                                                              type: string
                                                          required:
                                                          - key
                                                          - path
                                                          type: object
                                                        type: array
                                                      name:
                                                        type: string
                                                      optional:
                                                        type: boolean
                                                    type: object
                                                  serviceAccountToken:
                                                    properties:
                                                      audience:
                                                        type: string
                                                      expirationSeconds:
                                                        format: int64
                                                        type: integer
                                                      path:
                                                        type: string
                                                    required:
                                                    - path
                                                    type: object
                                                type: object
                                              type: array
                                          type: object
                                        quobyte:
                                          properties:
                                            group:
                                              type: string
                                            readOnly:
                                              type: boolean
                                            registry:
                                              type: string
                                            tenant:
                                              type: string
                                            user:
                                              type: string
                                            volume:
                                              type: string
                                          required:
                                          - registry
                                          - volume
                                          type: object
                                        rbd:
                                          properties:
                                            fsType:
                                              type: string
                                            image:
                                              type: string
                                            keyring:
                                              type: string
                                            monitors:
                                              items:
                                                type: string
                                              type: array
                                            pool:
                                              type: string
                                            readOnly:
                                              type: boolean
                                            secretRef:
                                              properties:
                                                name:
                                                  type: string
                                              type: object
                                            user:
                                              type: string
                                          required:
                                          - image
                                          - monitors
                                          type: object
                                        scaleIO:
                                          properties:
                                            fsType:
                                              type: string
                                            gateway:
                                              type: string
                                            protectionDomain:
                                              type: string
                                            readOnly:
                                              type: boolean
                                            secretRef:
                                              properties:
                                                name:
                                                  type: string
                                              type: object
                                            sslEnabled:
                                              type: boolean
                                            storageMode:
                                              type: string
                                            storagePool:
                                              type: string
                                            system:
                                              type: string
                                            volumeName:
                                              type: string
                                          required:
                                          - gateway
                                          - secretRef
                                          - system
                                          type: object
                                        secret:
                                          properties:
                                            defaultMode:
                                              format: int32
                                              type: integer
                                            items:
                                              items:
                                                properties:
                                                  key:
                                                    type: string
                                                  mode:
                                                    format: int32
                                                    type: integer
                                                  path:
                                                    type: string
                                                required:
                                                - key
                                                - path
                                                type: object
                                              type: array
                                            optional:
                                              type: boolean
                                            secretName:
                                              type: string
                                          type: object
                                        storageos:
                                          properties:
                                            fsType:
                                              type: string
                                            readOnly:
                                              type: boolean
                                            secretRef:
                                              properties:
                                                name:
                                                  type: string
                                              type: object
                                            volumeName:
                                              type: string
                                            volumeNamespace:
                                              type: string
                                          type: object
                                        vsphereVolume:
                                          properties:
                                            fsType:
                                              type: string
                                            storagePolicyID:
                                              type: string
                                            storagePolicyName:
                                              type: string
                                            volumePath:
                                              type: string
                                          required:
                                          - volumePath
                                          type: object
                                      required:
                                      - name
                                      type: object
                                    type: array
                                required:
                                - containers
                                type: object
                            type: object
                          updateStrategy:
                            properties:
                              rollingUpdate:
                                properties:
                                  maxUnavailable:
                                    anyOf:
                                    - type: integer
                                    - type: string
                                    x-kubernetes-int-or-string: true
                                  partition:
                                    format: int32
                                    type: integer
                                type: object
                              type:
                                type: string
                            type: object
                          volumeClaimTemplates:
                            items:
                              properties:
                                apiVersion:
                                  type: string
                                kind:
                                  type: string
                                metadata:
                                  properties:
                                    annotations:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    labels:
                                      additionalProperties:
                                        type: string
                                      type: object
                                    name:
                                      type: string
                                    namespace:
                                      type: string
                                  type: object
                                spec:
                                  properties:
                                    accessModes:
                                      items:
                                        type: string
                                      type: array
                                    dataSource:
                                      properties:
                                        apiGroup:
                                          type: string
                                        kind:
                                          type: string
                                        name:
                                          type: string
                                      required:
                                      - kind
                                      - name
                                      type: object
                                    dataSourceRef:
                                      properties:
                                        apiGroup:
                                          type: string
                                        kind:
                                          type: string
                                        name:
                                          type: string
                                      required:
                                      - kind
                                      - name
                                      type: object
                                    resources:
                                      properties:
                                        limits:
                                          additionalProperties:
                                            anyOf:
                                            - type: integer
                                            - type: string
                                            pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                            x-kubernetes-int-or-string: true
                                          type: object
                                        requests:
                                          additionalProperties:
                                            anyOf:
                                            - type: integer
                                            - type: string
                                            pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                                            x-kubernetes-int-or-string: true
                                          type: object
                                      type: object
                                    selector:
                                      properties:
                                        matchExpressions:
                                          items:
                                            properties:
                                              key:
                                                type: string
                                              operator:
                                                type: string
                                              values:
                                                items:
                                                  type: string
                                                type: array
                                            required:
                                            - key
                                            - operator
                                            type: object
                                          type: array
                                        matchLabels:
                                          additionalProperties:
                                            type: string
                                          type: object
                                      type: object
                                    storageClassName:
                                      type: string
                                    volumeMode:
                                      type: string
                                    volumeName:
                                      type: string
                                  type: object
                              type: object
                            type: array
                        type: object
                    type: object
                type: object
              persistence:
                default:
                  storage: 10Gi
                description: The desired persistent storage configuration for each
                  Pod in the cluster.
                properties:
                  storage:
                    anyOf:
                    - type: integer
                    - type: string
                    default: 10Gi
                    description: The requested size of the persistent volume attached
                      to each Pod in the RabbitmqCluster. The format of this field
                      matches that defined by kubernetes/apimachinery. See https://pkg.go.dev/k8s.io/apimachinery/pkg/api/resource#Quantity
                      for more info on the format of this field.
                    pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                    x-kubernetes-int-or-string: true
                  storageClassName:
                    description: The name of the StorageClass to claim a PersistentVolume
                      from.
                    type: string
                type: object
              rabbitmq:
                description: Configuration options for RabbitMQ Pods created in the
                  cluster.
                properties:
                  additionalConfig:
                    description: Modify to add to the rabbitmq.conf file in addition
                      to default configurations set by the operator. Modifying this
                      property on an existing RabbitmqCluster will trigger a StatefulSet
                      rolling restart and will cause rabbitmq downtime. For more information
                      on this config, see https://www.rabbitmq.com/configure.html#config-file
                    maxLength: 2000
                    type: string
                  additionalPlugins:
                    description: 'List of plugins to enable in addition to essential
                      plugins: rabbitmq_management, rabbitmq_prometheus, and rabbitmq_peer_discovery_k8s.'
                    items:
                      description: A Plugin to enable on the RabbitmqCluster.
                      maxLength: 100
                      pattern: ^\w+$
                      type: string
                    maxItems: 100
                    type: array
                  advancedConfig:
                    description: Specify any rabbitmq advanced.config configurations
                      to apply to the cluster. For more information on advanced config,
                      see https://www.rabbitmq.com/configure.html#advanced-config-file
                    maxLength: 100000
                    type: string
                  envConfig:
                    description: Modify to add to the rabbitmq-env.conf file. Modifying
                      this property on an existing RabbitmqCluster will trigger a
                      StatefulSet rolling restart and will cause rabbitmq downtime.
                      For more information on env config, see https://www.rabbitmq.com/man/rabbitmq-env.conf.5.html
                    maxLength: 100000
                    type: string
                type: object
              replicas:
                default: 1
                description: Replicas is the number of nodes in the RabbitMQ cluster.
                  Each node is deployed as a Replica in a StatefulSet. Only 1, 3,
                  5 replicas clusters are tested. This value should be an odd number
                  to ensure the resultant cluster can establish exactly one quorum
                  of nodes in the event of a fragmenting network partition.
                format: int32
                minimum: 0
                type: integer
              resources:
                default:
                  limits:
                    cpu: 2000m
                    memory: 2Gi
                  requests:
                    cpu: 1000m
                    memory: 2Gi
                description: The desired compute resource requirements of Pods in
                  the cluster.
                properties:
                  limits:
                    additionalProperties:
                      anyOf:
                      - type: integer
                      - type: string
                      pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                      x-kubernetes-int-or-string: true
                    description: 'Limits describes the maximum amount of compute resources
                      allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/'
                    type: object
                  requests:
                    additionalProperties:
                      anyOf:
                      - type: integer
                      - type: string
                      pattern: ^(\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))(([KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]*)?)|(\.[0-9]+))))?$
                      x-kubernetes-int-or-string: true
                    description: 'Requests describes the minimum amount of compute
                      resources required. If Requests is omitted for a container,
                      it defaults to Limits if that is explicitly specified, otherwise
                      to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/'
                    type: object
                type: object
              secretBackend:
                description: Secret backend configuration for the RabbitmqCluster.
                  Enables to fetch default user credentials and certificates from
                  K8s external secret stores.
                properties:
                  vault:
                    description: VaultSpec will add Vault annotations (see https://www.vaultproject.io/docs/platform/k8s/injector/annotations)
                      to RabbitMQ Pods. It requires a Vault Agent Sidecar Injector
                      (https://www.vaultproject.io/docs/platform/k8s/injector) to
                      be installed in the K8s cluster. The injector is a K8s Mutation
                      Webhook Controller that alters RabbitMQ Pod specifications (based
                      on the added Vault annotations) to include Vault Agent containers
                      that render Vault secrets to the volume.
                    properties:
                      annotations:
                        additionalProperties:
                          type: string
                        description: Vault annotations that override the Vault annotations
                          set by the cluster-operator. For a list of valid Vault annotations,
                          see https://www.vaultproject.io/docs/platform/k8s/injector/annotations
                        type: object
                      defaultUserPath:
                        description: Path in Vault to access a KV (Key-Value) secret
                          with the fields username and password for the default user.
                          For example "secret/data/rabbitmq/config".
                        type: string
                      defaultUserUpdaterImage:
                        description: Sidecar container that updates the default user's
                          password in RabbitMQ when it changes in Vault. Additionally,
                          it updates /var/lib/rabbitmq/.rabbitmqadmin.conf (used by
                          rabbitmqadmin CLI). Set to empty string to disable the sidecar
                          container.
                        type: string
                      role:
                        description: Role in Vault. If vault.defaultUserPath is set,
                          this role must have capability to read the pre-created default
                          user credential in Vault. If vault.tls is set, this role
                          must have capability to create and update certificates in
                          the Vault PKI engine for the domains "<namespace>" and "<namespace>.svc".
                        type: string
                      tls:
                        properties:
                          altNames:
                            description: 'Specifies the requested Subject Alternative
                              Names (SANs), in a comma-delimited list. These will
                              be appended to the SANs added by the cluster-operator.
                              The cluster-operator will add SANs: "<RabbitmqCluster
                              name>-server-<index>.<RabbitmqCluster name>-nodes.<namespace>"
                              for each pod, e.g. "myrabbit-server-0.myrabbit-nodes.default".'
                            type: string
                          commonName:
                            description: Specifies the requested certificate Common
                              Name (CN). Defaults to <serviceName>.<namespace>.svc
                              if not provided.
                            type: string
                          ipSans:
                            description: Specifies the requested IP Subject Alternative
                              Names, in a comma-delimited list.
                            type: string
                          pkiIssuerPath:
                            description: Path in Vault PKI engine. For example "pki/issue/hashicorp-com".
                              required
                            type: string
                        type: object
                    type: object
                type: object
              service:
                default:
                  type: ClusterIP
                description: The desired state of the Kubernetes Service to create
                  for the cluster.
                properties:
                  annotations:
                    additionalProperties:
                      type: string
                    description: Annotations to add to the Service.
                    type: object
                  type:
                    default: ClusterIP
                    description: 'Type of Service to create for the cluster. Must
                      be one of: ClusterIP, LoadBalancer, NodePort. For more info
                      see https://pkg.go.dev/k8s.io/api/core/v1#ServiceType'
                    enum:
                    - ClusterIP
                    - LoadBalancer
                    - NodePort
                    type: string
                type: object
              skipPostDeploySteps:
                description: If unset, or set to false, the cluster will run `rabbitmq-queues
                  rebalance all` whenever the cluster is updated. Set to true to prevent
                  the operator rebalancing queue leaders after a cluster update. Has
                  no effect if the cluster only consists of one node. For more information,
                  see https://www.rabbitmq.com/rabbitmq-queues.8.html#rebalance
                type: boolean
              terminationGracePeriodSeconds:
                default: 604800
                description: 'TerminationGracePeriodSeconds is the timeout that each
                  rabbitmqcluster pod will have to terminate gracefully. It defaults
                  to 604800 seconds ( a week long) to ensure that the container preStop
                  lifecycle hook can finish running. For more information, see: https://github.com/rabbitmq/cluster-operator/blob/main/docs/design/20200520-graceful-pod-termination.md'
                format: int64
                minimum: 0
                type: integer
              tls:
                description: TLS-related configuration for the RabbitMQ cluster.
                properties:
                  caSecretName:
                    description: Name of a Secret in the same Namespace as the RabbitmqCluster,
                      containing the Certificate Authority's public certificate for
                      TLS. The Secret must store this as ca.crt. This Secret can be
                      created by running `kubectl create secret generic ca-secret
                      --from-file=ca.crt=path/to/ca.cert` Used for mTLS, and TLS for
                      rabbitmq_web_stomp and rabbitmq_web_mqtt.
                    type: string
                  disableNonTLSListeners:
                    description: 'When set to true, the RabbitmqCluster disables non-TLS
                      listeners for RabbitMQ, management plugin and for any enabled
                      plugins in the following list: stomp, mqtt, web_stomp, web_mqtt.
                      Only TLS-enabled clients will be able to connect.'
                    type: boolean
                  secretName:
                    description: Name of a Secret in the same Namespace as the RabbitmqCluster,
                      containing the server's private key & public certificate for
                      TLS. The Secret must store these as tls.key and tls.crt, respectively.
                      This Secret can be created by running `kubectl create secret
                      tls tls-secret --cert=path/to/tls.cert --key=path/to/tls.key`
                    type: string
                type: object
              tolerations:
                description: Tolerations is the list of Toleration resources attached
                  to each Pod in the RabbitmqCluster.
                items:
                  description: The pod this Toleration is attached to tolerates any
                    taint that matches the triple <key,value,effect> using the matching
                    operator <operator>.
                  properties:
                    effect:
                      description: Effect indicates the taint effect to match. Empty
                        means match all taint effects. When specified, allowed values
                        are NoSchedule, PreferNoSchedule and NoExecute.
                      type: string
                    key:
                      description: Key is the taint key that the toleration applies
                        to. Empty means match all taint keys. If the key is empty,
                        operator must be Exists; this combination means to match all
                        values and all keys.
                      type: string
                    operator:
                      description: Operator represents a key's relationship to the
                        value. Valid operators are Exists and Equal. Defaults to Equal.
                        Exists is equivalent to wildcard for value, so that a pod
                        can tolerate all taints of a particular category.
                      type: string
                    tolerationSeconds:
                      description: TolerationSeconds represents the period of time
                        the toleration (which must be of effect NoExecute, otherwise
                        this field is ignored) tolerates the taint. By default, it
                        is not set, which means tolerate the taint forever (do not
                        evict). Zero and negative values will be treated as 0 (evict
                        immediately) by the system.
                      format: int64
                      type: integer
                    value:
                      description: Value is the taint value the toleration matches
                        to. If the operator is Exists, the value should be empty,
                        otherwise just a regular string.
                      type: string
                  type: object
                type: array
            type: object
          status:
            description: Status presents the observed state of RabbitmqCluster
            properties:
              binding:
                description: 'Binding exposes a secret containing the binding information
                  for this RabbitmqCluster. It implements the service binding Provisioned
                  Service duck type. See: https://github.com/servicebinding/spec#provisioned-service'
                properties:
                  name:
                    description: 'Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
                      TODO: Add other useful fields. apiVersion, kind, uid?'
                    type: string
                type: object
              conditions:
                description: Set of Conditions describing the current state of the
                  RabbitmqCluster
                items:
                  properties:
                    lastTransitionTime:
                      description: The last time this Condition type changed.
                      format: date-time
                      type: string
                    message:
                      description: Full text reason for current status of the condition.
                      type: string
                    reason:
                      description: One word, camel-case reason for current status
                        of the condition.
                      type: string
                    status:
                      description: True, False, or Unknown
                      type: string
                    type:
                      description: Type indicates the scope of RabbitmqCluster status
                        addressed by the condition.
                      type: string
                  required:
                  - status
                  - type
                  type: object
                type: array
              defaultUser:
                description: Identifying information on internal resources
                properties:
                  secretReference:
                    description: Reference to the Kubernetes Secret containing the
                      credentials of the default user.
                    properties:
                      keys:
                        additionalProperties:
                          type: string
                        description: Key-value pairs in the Secret corresponding to
                          `username`, `password`, `host`, and `port`
                        type: object
                      name:
                        description: Name of the Secret containing the default user
                          credentials
                        type: string
                      namespace:
                        description: Namespace of the Secret containing the default
                          user credentials
                        type: string
                    required:
                    - keys
                    - name
                    - namespace
                    type: object
                  serviceReference:
                    description: Reference to the Kubernetes Service serving the cluster.
                    properties:
                      name:
                        description: Name of the Service serving the cluster
                        type: string
                      namespace:
                        description: Namespace of the Service serving the cluster
                        type: string
                    required:
                    - name
                    - namespace
                    type: object
                type: object
              observedGeneration:
                description: observedGeneration is the most recent successful generation
                  observed for this RabbitmqCluster. It corresponds to the RabbitmqCluster's
                  generation, which is updated on mutation by the API Server.
                format: int64
                type: integer
            required:
            - conditions
            type: object
        type: object
    served: true
    storage: true
    subresources:
      status: {}
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: rabbitmq-cluster-operator
  namespace: rabbitmq-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  labels:
    app.kubernetes.io/component: rabbitmq-operator
    app.kubernetes.io/name: rabbitmq-cluster-operator
    app.kubernetes.io/part-of: rabbitmq
  name: rabbitmq-cluster-leader-election-role
  namespace: rabbitmq-system
rules:
- apiGroups:
  - coordination.k8s.io
  resources:
  - leases
  verbs:
  - get
  - list
  - watch
  - create
  - update
  - patch
  - delete
- apiGroups:
  - ""
  resources:
  - events
  verbs:
  - create
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  labels:
    app.kubernetes.io/component: rabbitmq-operator
    app.kubernetes.io/name: rabbitmq-cluster-operator
    app.kubernetes.io/part-of: rabbitmq
  name: rabbitmq-cluster-operator-role
rules:
- apiGroups:
  - ""
  resources:
  - configmaps
  verbs:
  - create
  - get
  - list
  - update
  - watch
- apiGroups:
  - ""
  resources:
  - endpoints
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - ""
  resources:
  - events
  verbs:
  - create
  - get
  - patch
- apiGroups:
  - ""
  resources:
  - persistentvolumeclaims
  verbs:
  - create
  - get
  - list
  - update
  - watch
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - get
  - list
  - update
  - watch
- apiGroups:
  - ""
  resources:
  - pods/exec
  verbs:
  - create
- apiGroups:
  - ""
  resources:
  - secrets
  verbs:
  - create
  - get
  - list
  - update
  - watch
- apiGroups:
  - ""
  resources:
  - serviceaccounts
  verbs:
  - create
  - get
  - list
  - update
  - watch
- apiGroups:
  - ""
  resources:
  - services
  verbs:
  - create
  - get
  - list
  - update
  - watch
- apiGroups:
  - apps
  resources:
  - statefulsets
  verbs:
  - create
  - delete
  - get
  - list
  - update
  - watch
- apiGroups:
  - rabbitmq.com
  resources:
  - rabbitmqclusters
  verbs:
  - create
  - get
  - list
  - update
  - watch
- apiGroups:
  - rabbitmq.com
  resources:
  - rabbitmqclusters/finalizers
  verbs:
  - update
- apiGroups:
  - rabbitmq.com
  resources:
  - rabbitmqclusters/status
  verbs:
  - get
  - update
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - rolebindings
  verbs:
  - create
  - get
  - list
  - update
  - watch
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - roles
  verbs:
  - create
  - get
  - list
  - update
  - watch
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  labels:
    app.kubernetes.io/component: rabbitmq-operator
    app.kubernetes.io/name: rabbitmq-cluster-operator
    app.kubernetes.io/part-of: rabbitmq
  name: rabbitmq-cluster-leader-election-rolebinding
  namespace: rabbitmq-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: rabbitmq-cluster-leader-election-role
subjects:
- kind: ServiceAccount
  name: rabbitmq-cluster-operator
  namespace: rabbitmq-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  labels:
    app.kubernetes.io/component: rabbitmq-operator
    app.kubernetes.io/name: rabbitmq-cluster-operator
    app.kubernetes.io/part-of: rabbitmq
  name: rabbitmq-cluster-operator-rolebinding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: rabbitmq-cluster-operator-role
subjects:
- kind: ServiceAccount
  name: rabbitmq-cluster-operator
  namespace: rabbitmq-system
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app.kubernetes.io/component: rabbitmq-operator
    app.kubernetes.io/name: rabbitmq-cluster-operator
    app.kubernetes.io/part-of: rabbitmq
  name: rabbitmq-cluster-operator
  namespace: rabbitmq-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: rabbitmq-cluster-operator
  template:
    metadata:
      labels:
        app.kubernetes.io/component: rabbitmq-operator
        app.kubernetes.io/name: rabbitmq-cluster-operator
        app.kubernetes.io/part-of: rabbitmq
    spec:
      containers:
      - command:
        - /manager
        env:
        - name: OPERATOR_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
        image: rabbitmqoperator/cluster-operator:1.14.0
        name: operator
        ports:
        - containerPort: 9782
          name: metrics
          protocol: TCP
        resources:
          limits:
            cpu: 200m
            memory: 500Mi
          requests:
            cpu: 200m
            memory: 500Mi
      serviceAccountName: rabbitmq-cluster-operator
      terminationGracePeriodSeconds: 10
---
apiVersion: rabbitmq.com/v1beta1
kind: RabbitmqCluster
metadata:
  name: weko-rabbitmq
  namespace: weko3ra
spec:
  image: rabbitmq:3.10.7
  persistence:
    storage: 50Gi
    storageClassName: nfs-client
  rabbitmq:
    additionalConfig: |
      consumer_timeout = 10800000
  replicas: 1
  resources:
    limits:
      cpu: 500m
      memory: 2000Mi
    requests:
      cpu: 300m
      memory: 1500Mi
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.org/server-snippets: |
      allow 136.187.176.0/23; #NII
      allow 36.13.31.125/32; #NII
      allow 126.204.173.71/32; #NII
      allow 39.110.207.95/32; #ARI
      allow 39.110.216.121/32; #ARI
      allow 196.216.191.17/32; #WACREN
      deny all;
    nginx.org/server-tokens: "False"
  name: rabbitmq
  namespace: weko3ra
spec:
  ingressClassName: nginx-internal
  rules:
  - host: rabbitmq-af.ir.rcos.nii.ac.jp
    http:
      paths:
      - backend:
          service:
            name: weko-rabbitmq
            port:
              number: 15672
        path: /
        pathType: Prefix

```

2. deploy rabbitmq.

```
$ kubectl apply -f deploy.yaml
namespace/rabbitmq-system created
namespace/weko3ra created
customresourcedefinition.apiextensions.k8s.io/rabbitmqclusters.rabbitmq.com created
serviceaccount/rabbitmq-cluster-operator created
role.rbac.authorization.k8s.io/rabbitmq-cluster-leader-election-role created
clusterrole.rbac.authorization.k8s.io/rabbitmq-cluster-operator-role created
rolebinding.rbac.authorization.k8s.io/rabbitmq-cluster-leader-election-rolebinding created
clusterrolebinding.rbac.authorization.k8s.io/rabbitmq-cluster-operator-rolebinding created
deployment.apps/rabbitmq-cluster-operator created
rabbitmqcluster.rabbitmq.com/weko-rabbitmq created
ingress.networking.k8s.io/rabbitmq created

```

3. check deployment result

```
$ kubectl get all -n weko3ra
NAME                         READY   STATUS    RESTARTS   AGE
pod/weko-rabbitmq-server-0   1/1     Running   0          37s

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                        AGE
service/weko-rabbitmq         ClusterIP   10.233.36.212   <none>        15672/TCP,15692/TCP,5672/TCP   39s
service/weko-rabbitmq-nodes   ClusterIP   None            <none>        4369/TCP,25672/TCP             39s

NAME                                    READY   AGE
statefulset.apps/weko-rabbitmq-server   1/1     39s

NAME                                         ALLREPLICASREADY   RECONCILESUCCESS   AGE
rabbitmqcluster.rabbitmq.com/weko-rabbitmq   True               True               43s

```

## Redis

1. create yaml file for redis.

```
$ vi deploy.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: weko3re
---
apiVersion: v1
data:
  redis.conf: |
    databases 40000
    maxclients 150000
    maxmemory 100gb
    dir /redis-storage
    save 3600 1
    save 300 100
    save 60 10000
    client-output-buffer-limit slave 0 0 0
    loglevel notice
  sentinel.conf: |
    sentinel monitor mymaster MASTER_ADDR 6379 2
    sentinel down-after-milliseconds mymaster 1000
    sentinel notification-script mymaster /data/conf/notify-sentinel.sh
    maxclients 150000
    loglevel notice
kind: ConfigMap
metadata:
  name: redis-configmap
  namespace: weko3re
---
apiVersion: v1
data:
  EXIT_UNHEALTHY: "1"
  INTERVAL_FOR_INIT_SENTINEL: "2"
  INTERVAL_FOR_RESET_SLAVE: "40"
  MASTER_NAME: mymaster
  NUM_OF_REDIS_REPLICAS: "1"
  PING_TIMEOUT: "0.3"
  REDIS_PORT: "6379"
  REDIS_SERVICE: weko-redis-service.weko3re.svc.cluster.local
  SCRIPT_DIR: /data/conf
  SENTINEL_PORT: "26379"
  SENTINEL_QUORUM: "2"
  SENTINEL_SERVICE: weko-sentinel-service.weko3re.svc.cluster.local
  SPLITBRAIN_THRESHOLD_OF_COUNT_CONNECTED_SENTINELS: "1"
  SPLITBRAIN_THRESHOLD_OF_COUNT_CONNECTED_SLAVES: "1"
  WAIT_TIME_FOR_UP_REDIS: "10"
kind: ConfigMap
metadata:
  name: redis-env-configmap
  namespace: weko3re
---
apiVersion: v1
kind: Service
metadata:
  name: weko-redis-service
  namespace: weko3re
spec:
  clusterIP: None
  ports:
  - port: 6379
    targetPort: 6379
  selector:
    app: redis
---
apiVersion: v1
kind: Service
metadata:
  name: weko-sentinel-service
  namespace: weko3re
spec:
  clusterIP: None
  ports:
  - port: 26379
    targetPort: 26379
  selector:
    app: sentinel
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: weko-sentinel
  namespace: weko3re
spec:
  replicas: 1
  selector:
    matchLabels:
      app: sentinel
  template:
    metadata:
      labels:
        app: sentinel
    spec:
      containers:
      - args:
        - cp -r -L /redis-config/* ./conf && ./conf/setup-sentinel.sh
        command:
        - bash
        - -c
        envFrom:
        - configMapRef:
            name: redis-env-configmap
        image: mhayashi55/weko-sentinel:latest
        imagePullPolicy: Always
        name: sentinel
        ports:
        - containerPort: 26379
        readinessProbe:
          exec:
            command:
            - ./conf/healthy-sentinel.sh
          failureThreshold: 3
          initialDelaySeconds: 0
          periodSeconds: 1
          successThreshold: 1
        resources:
          limits:
            cpu: 100m
            memory: 400Mi
          requests:
            cpu: 50m
            memory: 300Mi
        volumeMounts:
        - mountPath: /redis-config
          name: config
      initContainers:
      - command:
        - bash 
        - -c 
        - until [ $(dig $REDIS_SERVICE +short | wc -l) = $(($NUM_OF_REDIS_REPLICAS+1)) ]; do echo waiting for redis; sleep $INTERVAL_FOR_INIT_SENTINEL;done
        envFrom:
        - configMapRef:
            name: redis-env-configmap
        image: mhayashi55/weko-sentinel:latest
        name: init-sentinel
      restartPolicy: Always
      volumes:
      - configMap:
          name: redis-configmap
        name: config
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: weko-redis
  namespace: weko3re
spec:
  replicas: 2
  selector:
    matchLabels:
      app: redis
  serviceName: weko-redis-service
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - args:
        - cp -r -L /redis-config/* ./conf && ./conf/setup-redis.sh
        command:
        - bash
        - -c
        envFrom:
        - configMapRef:
            name: redis-env-configmap
        image: mhayashi55/weko-redis:latest
        imagePullPolicy: Always
        name: redis
        ports:
        - containerPort: 6379
        readinessProbe:
          exec:
            command:
            - ./conf/healthy-redis.sh
          failureThreshold: 3
          initialDelaySeconds: 0
          periodSeconds: 1
          successThreshold: 1
        resources:
          limits:
            cpu: 1500m
            memory: 7Gi
          requests:
            cpu: 1000m
            memory: 6Gi
        volumeMounts:
        - mountPath: /redis-config
          name: config
        - mountPath: /redis-storage
          name: weko-redis-storage
      initContainers:
      - command:
        - bash
        - -c
        - sleep $WAIT_TIME_FOR_UP_REDIS
        envFrom:
        - configMapRef:
            name: redis-env-configmap
        image: mhayashi55/weko-redis:latest
        name: init-redis
      restartPolicy: Always
      volumes:
      - configMap:
          name: redis-configmap
        name: config
  volumeClaimTemplates:
  - metadata:
      name: weko-redis-storage
    spec:
      accessModes:
      - ReadWriteOnce
      storageClassName: nfs-client
      resources:
        requests:
          storage: 50G

```

2. deploy redis

```
$ kubectl apply -f deploy.yaml
namespace/weko3re created
configmap/redis-configmap created
configmap/redis-env-configmap created
service/weko-redis-service created
service/weko-sentinel-service created
deployment.apps/weko-sentinel created
statefulset.apps/weko-redis created

```

3. check deployment result

```
$ kubectl get all -n weko3re
NAME                                 READY   STATUS    RESTARTS   AGE
pod/weko-redis-0                     1/1     Running   0          21h
pod/weko-redis-1                     1/1     Running   0          20h
pod/weko-sentinel-6c9df8b68d-j6tpf   1/1     Running   0          21h

NAME                            TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)     AGE
service/weko-redis-service      ClusterIP   None         <none>        6379/TCP    21h
service/weko-sentinel-service   ClusterIP   None         <none>        26379/TCP   21h

NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/weko-sentinel   1/1     1            1           21h

NAME                                       DESIRED   CURRENT   READY   AGE
replicaset.apps/weko-sentinel-6c9df8b68d   1         1         1       21h

NAME                          READY   AGE
statefulset.apps/weko-redis   2/2     21h

```

## Persistant Volume

1. check mount point of NFS Server

```
$ showmount -e <NFS Server IP Address>
Export list for <NFS Server IP Address>:
/var/wiwdata   10.50.50.177,10.50.50.176,10.50.50.175,10.50.50.174
/var/weko3data 10.50.50.177,10.50.50.176,10.50.50.175,10.50.50.174

```

2. access node server that is connected NFS server.

```
ssh user@10.50.50.177 -i ~/.ssh/id_rsa
```

3. mount directory and make directories for WEKO3

```
sudo mount -t nfs <NFS Server IP Address>:/var/weko3data /mnt/weko3data/
sudo mkdir -p /mnt/weko3data/fs-nginx/weko.example.org
sudo mkdir -p /mnt/weko3data/fs-shibboleth/weko.example.org
sudo mkdir -p /mnt/weko3data/fs-config/weko.example.org
sudo mkdir -p /mnt/weko3data/fs-data/weko.example.org

```

# WEKO3

## build image

```
$ docker login
Log in with your Docker ID or email address to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com/ to create one.
You can log in with your password or a Personal Access Token (PAT). Using a limited-scope PAT grants better security and is required for organizations using SSO. Learn more at https://docs.docker.com/go/access-tokens/

Username: mhayashi55
Password: 
WARNING! Your password will be stored unencrypted in /home/mhaya/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

```
docker tag weko-web:latest mhayashi55/weko3-web:latest
docker tag weko-nginx:latest mhayashi55/weko3-nginx:latest
```

##

1. create yaml file for creating namespace.

```
$ kubectl apply -f namespace.yaml
namespace/weko3 created

```

## deploy weko.example.org

1. make a persistent volume 

```
$ vi volume-pv.yaml
---
apiVersion: v1
kind: PersistentVolume
metadata:
  namespace: weko3
  name: repository-ren-ng-nginx-pv
  labels:
    volume: repository-ren-ng-nginx-nfs
  annotations:
    volume.beta.kubernetes.io/storage-class: "nfs"
spec:
  capacity:
    storage: 50Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  nfs:
    server: 10.50.50.180
    path: /var/weko3data/fs-nginx/repository.ren.ng
---
apiVersion: v1
kind: PersistentVolume
metadata:
  namespace: weko3
  name: repository-ren-ng-shib-pv
  labels:
    volume: repository-ren-ng-shib-nfs
  annotations:
    volume.beta.kubernetes.io/storage-class: "nfs"
spec:
  capacity:
    storage: 50Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  nfs:
    server: 10.50.50.180
    path: /var/weko3data/fs-shibboleth/repository.ren.ng
---
#apiVersion: v1
#kind: PersistentVolume
#metadata:
#  namespace: weko3
#  name: repository-ren-ng-static-pv
#  labels:
#    volume: repository-ren-ng-static-nfs
#  annotations:
#    volume.beta.kubernetes.io/storage-class: "nfs"
#spec:
#  capacity:
#    storage: 50Gi
#  accessModes:
#    - ReadWriteOnce
#  persistentVolumeReclaimPolicy: Retain
#  nfs:
#    server: 10.50.50.180
#    path: /var/weko3data/fs-jcbackup/beta2/repository.ren.ng/volumes/static
#---
apiVersion: v1
kind: PersistentVolume
metadata:
  namespace: weko3
  name: repository-ren-ng-config-pv
  labels:
    volume: repository-ren-ng-config-nfs
  annotations:
    volume.beta.kubernetes.io/storage-class: "nfs"
spec:
  capacity:
    storage: 50Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  nfs:
    server: 10.50.50.180
    path: /var/weko3data/fs-config/repository.ren.ng
---
apiVersion: v1
kind: PersistentVolume
metadata:
  namespace: weko3
  name: repository-ren-ng-data-pv
  labels:
    volume: repository-ren-ng-data-nfs
  annotations:
    volume.beta.kubernetes.io/storage-class: "nfs"
spec:
  capacity:
    storage: 50Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  nfs:
    server: 10.50.50.180
    path: /var/weko3data/fs-data/repository.ren.ng

```

```
$ kubectl apply -f volume-pv.yaml
Warning: metadata.annotations[volume.beta.kubernetes.io/storage-class]: deprecated since v1.8; use "storageClassName" attribute instead
persistentvolume/research-ren-ng-nginx-pv created
persistentvolume/research-ren-ng-shib-pv created
persistentvolume/research-ren-ng-config-pv created
persistentvolume/research-ren-ng-data-pv created

```

2. make a persistent volume claim

```
$ cat volume-pvc.yaml
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  namespace: weko3
  name: repository-ren-ng-nginx-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi
  storageClassName: "nfs"
  selector:
    matchLabels:
      volume: repository-ren-ng-nginx-nfs
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  namespace: weko3
  name: repository-ren-ng-shib-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi
  storageClassName: "nfs"
  selector:
    matchLabels:
      volume: repository-ren-ng-shib-nfs
---
#apiVersion: v1
#kind: PersistentVolumeClaim
#metadata:
#  namespace: weko3
#  name: repository-ren-ng-static-pvc
#spec:
#  accessModes:
#    - ReadWriteOnce
#  resources:
#    requests:
#      storage: 50Gi
#  storageClassName: "nfs"
#  selector:
#    matchLabels:
#      volume: repository-ren-ng-static-nfs
#---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  namespace: weko3
  name: repository-ren-ng-config-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi
  storageClassName: "nfs"
  selector:
    matchLabels:
      volume: repository-ren-ng-config-nfs
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  namespace: weko3
  name: repository-ren-ng-data-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi
  storageClassName: "nfs"
  selector:
    matchLabels:
      volume: repository-ren-ng-data-nfs

```

```
$ kubectl apply -f volume-pvc.yaml
persistentvolumeclaim/research-ren-ng-nginx-pvc created
persistentvolumeclaim/research-ren-ng-shib-pvc created
persistentvolumeclaim/research-ren-ng-config-pvc created
persistentvolumeclaim/research-ren-ng-data-pvc created

```

3. make a secret

```
$ cat secret.yaml
apiVersion: v1
kind: Secret
metadata:
  namespace: weko3
  name: repository-ren-ng-secret
type: Opaque
stringData:
  INVENIO_RABBITMQ_USER: invenio
  INVENIO_RABBITMQ_PASS: uspass123
  INVENIO_POSTGRESQL_DBUSER: invenio
  INVENIO_POSTGRESQL_DBPASS: dbpass123
  INVENIO_USER_EMAIL: wekosoftware@nii.ac.jp
  INVENIO_USER_PASS: uspass123
  GOOGLE_TRACKING_ID_SYSTEM: None
  WEKO_RECORDS_UI_SECRET_KEY: FMCjj7kG
  SECRET_KEY: repository.ren.ng-NcVV6mVZ
  WTF_CSRF_SECRET_KEY: repository.ren.ng-BX8vwrcs
  S3_ACCCESS_KEY_ID: # change me
  S3_SECRECT_ACCESS_KEY: # change me
  S3_ENDPOINT_URL: # change me

```

```
$ kubectl apply -f secret.yaml
secret/research-ren-ng-secret created

```

4. make a configmap


```
$ cat configmap.yaml
kind: ConfigMap
apiVersion: v1
metadata:
  namespace: weko3
  name: weko-example-org-configmap
data:
  FLASK_DEBUG: "0"
  INVENIO_ELASTICSEARCH_HOST: elasticsearch.weko3es
  INVENIO_POSTGRESQL_HOST: pgpool.weko3pg
  INVENIO_RABBITMQ_HOST: weko-rabbitmq.weko3ra
  INVENIO_RABBITMQ_VHOST: weko-example-org
  INVENIO_REDIS_HOST: 127.0.0.1
  INVENIO_FILES_LOCATION_NAME: local
  INVENIO_FILES_LOCATION_URI: /var/tmp
  INVENIO_POSTGRESQL_DBNAME: research_ren_africa
  INVENIO_POSTGRESQL_DBUSER: invenio
  INVENIO_POSTGRESQL_DBPASS: ZGJwYXNzMTIz
  INVENIO_DB_POOL_CLASS: NullPool
  INVENIO_ROLE_COMMUNITY: Community Administrator
  INVENIO_ROLE_CONTRIBUTOR: Contributor
  INVENIO_ROLE_REPOSITORY: Repository Administrator
  INVENIO_ROLE_SYSTEM: System Administrator
  INVENIO_WEB_HOST: 127.0.0.1
  INVENIO_WEB_HOST_NAME: research.ren.africa
  INVENIO_WEB_INSTANCE: invenio
  INVENIO_WEB_VENV: invenio
  INVENIO_WEB_PROTOCOL: https
  INVENIO_WORKER_HOST: 127.0.0.1
  SHIB_IDP_LOGIN_ENABLED: "True"
  SHIB_IDP_LOGIN_URL: https://research.ren.africa/secure/login.php
  PATH: /home/invenio/.virtualenvs/invenio/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
  SEARCH_INDEX_PREFIX: research_ren_africa
  VIRTUALENVWRAPPER_PYTHON: /home/invenio/.virtualenvs/invenio/bin/python
  TMPDIR: /home/invenio/.virtualenvs/invenio/var/instance/data/tmp
  WEKO_HANDLE_ALLOW_REGISTER_CRNI: "False"
  IDENTIFIER_GRANT_SUFFIX_METHOD: "0"
  CACHE_REDIS_DB: "12004"
  ACCOUNTS_SESSION_REDIS_DB_NO: "22004"
  CELERY_RESULT_BACKEND_DB_NO: "32004"
  WEKO_AGGREGATE_EVENT_HOUR: "0"
  WEKO_AGGREGATE_EVENT_MINUTE: "6"

```


```
$ kubectl apply -f configmap.yaml
configmap/research-ren-ng-configmap created

```

5. deploy containers

```
$ cat deploy-web.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: weko3
  name: repository-ren-ng-web
spec:
  replicas: 1
  selector:
    matchLabels:
      app: repository-ren-ng-nginx
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: repository-ren-ng-nginx
    spec:
      hostAliases:
      - ip: "127.0.0.1"
        hostnames:
        - repository.ren.ng
      initContainers:
      - name: init
        image: mhayashi55/weko-init:latest
        command: [ "/bin/bash" ]
        args: [ "-c", "jinja2 /conf/instance.cfg > /conf/invenio.cfg" ]
        envFrom:
        - configMapRef:
            name: repository-ren-ng-configmap
        - secretRef:
            name: repository-ren-ng-secret
        volumeMounts:
        - mountPath: /conf
          name: repository-ren-ng-config-volume
      containers:
      - name: nginx
        image: mhayashi55/weko3-nginx:latest
        imagePullPolicy: Always
        resources:
          limits:
            memory: "300Mi"
          requests:
            memory: "250Mi"
        ports:
        - containerPort: 80
        - containerPort: 443
        volumeMounts:
        - name: vol-secret
          mountPath: /etc/app/secrets
        - mountPath: /etc/nginx
          name: repository-ren-ng-nginx-volume
        - mountPath: /etc/shibboleth
          name: repository-ren-ng-shib-volume
        - mountPath: /home/invenio/.virtualenvs/invenio/var/instance/static
          name: repository-ren-ng-static-volume
        - mountPath: /home/invenio/.virtualenvs/invenio/var/instance/data
          name: repository-ren-ng-data-volume
        # readinessProbe:
        #   httpGet:
        #     path: /ping
        #     port: 443
        #     scheme: HTTPS
        #   timeoutSeconds: 3
      - name: web
        image: mhayashi55/weko3-web:latest
        imagePullPolicy: Always
        resources:
          limits:
            memory: "2000Mi"
          requests:
            memory: "700Mi"
        command: [ "/bin/bash" ]
        args: ["-c", "if [ -z `ls -A /home/invenio/.virtualenvs/invenio/var/instance/static/.` ];then mv /home/invenio/.virtualenvs/invenio/var/instance/static.org/* /home/invenio/.virtualenvs/invenio/var/instance/static/.;fi && uwsgi --ini /home/invenio/.virtualenvs/invenio/var/instance/conf/uwsgi.ini"]
        envFrom:
        - configMapRef:
            name: repository-ren-ng-configmap
        - secretRef:
            name: repository-ren-ng-secret
        ports:
        - containerPort: 5000
        volumeMounts:
        - mountPath: /home/invenio/.virtualenvs/invenio/var/instance/static
          name: repository-ren-ng-static-volume
        - mountPath: /home/invenio/.virtualenvs/invenio/var/instance/data
          name: repository-ren-ng-data-volume
        - mountPath: /home/invenio/.virtualenvs/invenio/var/instance/conf
          name: repository-ren-ng-config-volume
      - name: worker
        image: mhayashi55/weko3-web:latest
        imagePullPolicy: Always
        resources:
          limits:
            memory: "2000Mi"
          requests:
            memory: "400Mi"
        command: [ "/bin/bash" ]
        args: ["-c", "rm -f /home/invenio/celeryd.pid && celery worker --pidfile /home/invenio/celeryd.pid --schedule=/home/invenio/celerybeat-schedule -c 2 -A invenio_app.celery --loglevel=INFO -B"]
        envFrom:
        - configMapRef:
            name: repository-ren-ng-configmap
        - secretRef:
            name: repository-ren-ng-secret
        volumeMounts:
        - mountPath: /home/invenio/.virtualenvs/invenio/var/instance/static
          name: repository-ren-ng-static-volume
        - mountPath: /home/invenio/.virtualenvs/invenio/var/instance/data
          name: repository-ren-ng-data-volume
        - mountPath: /home/invenio/.virtualenvs/invenio/var/instance/conf
          name: repository-ren-ng-config-volume
      restartPolicy: Always
      securityContext:
        fsGroup: 1000
      volumes:
        - name: vol-secret
          secret:
            secretName: repository-ren-ng-tls
        - name: repository-ren-ng-nginx-volume
          persistentVolumeClaim:
            claimName: repository-ren-ng-nginx-pvc
        - name: repository-ren-ng-shib-volume
          persistentVolumeClaim:
            claimName: repository-ren-ng-shib-pvc
        - name: repository-ren-ng-static-volume
        - name: repository-ren-ng-data-volume
          persistentVolumeClaim:
            claimName: repository-ren-ng-data-pvc
        - name: repository-ren-ng-config-volume
          persistentVolumeClaim:
            claimName: repository-ren-ng-config-pvc

status: {}

```

```
$ kubectl apply -f deploy-web.yaml
deployment.apps/research-ren-ng-web created

```

6. deploy ingress

```
$ cat ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  namespace: weko3
  name: repository-ren-ng-ingress
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
    nginx.ingress.kubernetes.io/proxy-buffering: "off"
    nginx.ingress.kubernetes.io/proxy-cookie-path: "/ /"
    nginx.ingress.kubernetes.io/proxy-set-headers: "configmap/repository-ren-ng-nginx-headers"
spec:
  tls:
  - hosts:
    - repository.ren.ng
    secretName: repository-ren-ng-tls
  ingressClassName: nginx
  rules:
  - host: repository.ren.ng
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: repository-ren-ng-nginx
            port:
              number: 443

```

## make config file 

1. copy shibboleth file to nfs directory

```
sudo cp -rp shibboleth_template/* /mnt/weko3data/fs-shibboleth/weko.example.org/
sudo sed -i "s/__WEKO3_VHOST__/weko.example.org/g" /mnt/weko3data/fs-shibboleth/weko.example.org/shibboleth2.xml

```

2. copy nginx file to nfs directory

```
sudo cp -rp nginx_template/* /mnt/weko3data/fs-nginx/weko.example.org/.
sudo cp nginx_template/.htdigest /mnt/weko3data/fs-nginx/weko.example.org/.
sudo sed -i "s/__WEKO3_VHOST__/weko.example.org/g" /mnt/weko3data/fs-nginx/weko.example.org/co
nf.d/weko.conf

```

3. config WEKO3 config to nfs directory

```
sudo cp -rp config_template/* /mnt/weko3data/fs-config/weko.example.org/.
sudo chown -R 1000:1000 /mnt/weko3data/fs-config/weko.example.org

```

4. prepare data directory

```
sudo cp -rp data_template/* /mnt/weko3data/fs-data/weko.example.org/.
sudo chown -R 1000:1000 /mnt/weko3data/fs-data/weko.example.org
sudo mkdir /mnt/weko3data/fs-data/weko.example.org/tmp
sudo chmod og+rwx /mnt/weko3data/fs-data/weko.example.org/tmp

```

## configure rabbitmq

1. login container

```
$ kubectl exec -n weko3ra weko-rabbitmq-server-0 -- rabbitmqctl add_user invenio uspass12
3
Defaulted container "rabbitmq" out of: rabbitmq, setup-container (init)
Adding user "invenio" ...
Done. Don't forget to grant the user permissions to some virtual hosts! See 'rabbitmqctl help set_permissions' to learn more.

```

2. add virtual host

```
$ kubectl exec -n weko3ra weko-rabbitmq-server-0 -- rabbitmqctl add_vhost research-ren-ng/
Defaulted container "rabbitmq" out of: rabbitmq, setup-container (init)
Adding vhost "research-ren-ng/" ...
$ kubectl exec -n weko3ra weko-rabbitmq-server-0 -- rabbitmqctl set_permissions -p research-ren-ng/ invenio ".*" ".*" ".*"
Defaulted container "rabbitmq" out of: rabbitmq, setup-container (init)
Setting permissions for user "invenio" in vhost "research-ren-ng/" ...

```

## check

### PostgreSQL connection

1. connect postgreSQL in web container

```
$ kubectl exec -n weko3 -it research-ren-ng-web-746bd4d95c-762qb -c web -- bash
(invenio) invenio@research-ren-ng-web-746bd4d95c-762qb:/code$ python
Python 3.6.15 (default, Dec 21 2021, 12:28:02)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import psycopg2
>>> conn = psycopg2.connect(database="template1",host="weko-postgresql.weko3pg",user="invenio",password="dbpass123")
>>> cursor = conn.cursor()
>>> cursor.execute("SELECT * FROM pg_stat_statements LIMIT 1")
>>> print(cursor.fetchone())
(10, 13398, None, '<insufficient privilege>', 2, 0.029199000000000003, 0.013517, 0.015682, 0.014599500000000001, 0.0010825000000000014, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0)
>>>

```

### redis connection

1. connect redis service

```
$ kubectl exec -n weko3 -it research-ren-ng-web-746bd4d95c-762qb -c web -- bash
(invenio) invenio@research-ren-ng-web-746bd4d95c-762qb:/code$ python
Python 3.6.15 (default, Dec 21 2021, 12:28:02)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import redis
>>> redis = redis.Redis(host='weko-redis-service.weko3re',port=6379,db=0)
>>> redis.keys()
[]
>>>

```

2. connect sentinel service

```
$ kubectl exec -n weko3re -it weko-redis-0 -- bash
Defaulted container "redis" out of: redis, init-redis (init)
root@weko-redis-0:/data# redis-cli -h weko-sentinel-service.weko3re -p 26379
weko-sentinel-service.weko3re:26379> info sentinel
# Sentinel
sentinel_masters:1
sentinel_tilt:0
sentinel_running_scripts:0
sentinel_scripts_queue_length:0
sentinel_simulate_failure_flags:0
master0:name=mymaster,status=ok,address=10.233.86.234:6379,slaves=1,sentinels=1
weko-sentinel-service.weko3re:26379>

```

3. find master in python

```
$ kubectl exec -n weko3 -it research-ren-ng-web-746bd4d95c-762qb -c web -- bash
(invenio) invenio@research-ren-ng-web-746bd4d95c-762qb:/code$ python
Python 3.6.15 (default, Dec 21 2021, 12:28:02)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from redis.sentinel import Sentinel
>>> sentinel = Sentinel([('weko-sentinel-service.weko3re',26379)],stream_timeout=0.1)
>>> sentinel.discover_master('mymaster')
('10.233.86.234', 6379)
>>>

```

## initialize Application

```
WEB_POD=repository-aggregator-ren-ng-web-7f8b66b598-2bwr2
PSQL_MASTER=weko-postgresql-0
DB=repository_aggregator_togorer_tg
date; kubectl exec -n weko3 $WEB_POD -c web -- bash -x ./scripts/populate-instance.sh; date
kubectl cp -n weko3 -c web $WEB_POD:scripts/demo/item_type4.sql /tmp/item_type4.sql
kubectl cp -n weko3pg /tmp/item_type4.sql $PSQL_MASTER:/tmp/ -c postgres
kubectl exec -n weko3pg $PSQL_MASTER -c postgres -- psql -U invenio $DB -f /tmp/item_type4.sql
kubectl exec -n weko3 $WEB_POD -c web -- invenio workflow init action_status,Action,Flow
kubectl exec -n weko3 $WEB_POD -c web -- invenio shell scripts/demo/register_oai_schema.py overwrite_all
kubectl exec -n weko3 $WEB_POD -c web -- invenio shell tools/update/addjpcoar_v1_mapping.py
kubectl exec -n weko3pg $PSQL_MASTER -c postgres -- psql -U invenio $DB -c "select setval('pidstore_recid_recid_seq', 2000000);"
kubectl exec -n weko3 $WEB_POD -c web -- invenio shell scripts/demo/register_properties.py only_specified
kubectl exec -n weko3 $WEB_POD -c web -- invenio shell scripts/demo/renew_all_item_types.py only_specified ALL
```

# HAProxy setting

```
$ cat /etc/haproxy/haproxy.cfg
global
        log /dev/log    local0
        log /dev/log    local1 notice
        chroot /var/lib/haproxy
        stats socket /run/haproxy/admin.sock mode 660 level admin
        stats timeout 30s
        user haproxy
        group haproxy
        daemon

        # Default SSL material locations
        ca-base /etc/ssl/certs
        crt-base /etc/ssl/private

        # See: https://ssl-config.mozilla.org/#server=haproxy&server-version=2.0.3&config=intermediate
        ssl-default-bind-ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384
        ssl-default-bind-ciphersuites TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256
        ssl-default-bind-options ssl-min-ver TLSv1.2 no-tls-tickets

defaults
        log     global
        mode    http
        option  httplog
        option  dontlognull
        timeout connect 5000
        timeout client  50000
        timeout server  50000
        errorfile 400 /etc/haproxy/errors/400.http
        errorfile 403 /etc/haproxy/errors/403.http
        errorfile 408 /etc/haproxy/errors/408.http
        errorfile 500 /etc/haproxy/errors/500.http
        errorfile 502 /etc/haproxy/errors/502.http
        errorfile 503 /etc/haproxy/errors/503.http
        errorfile 504 /etc/haproxy/errors/504.http

frontend k8s-apiserver-frontend
bind 196.216.189.178:6443
mode tcp
option log-health-checks
timeout client 3h
timeout server 3h
use_backend k8s-apiserver-backend

backend k8s-apiserver-backend
mode tcp
server node-k8s-1  node-k8s-1.cluster.local:6443 check check-ssl verify none inter 10
server node-k8s-2  node-k8s-2.cluster.local:6443 check check-ssl verify none inter 10
server node-k8s-3  node-k8s-3.cluster.local:6443 check check-ssl verify none inter 10
balance roundrobin

frontend multiple_http_domains
    bind *:80
    mode http
    option httplog
    acl is_repository_aggregator_ren_ng hdr_dom(host) -i repository-aggregator.ren.ng
    acl is_repository_ren_ng hdr_dom(host) -i repository.ren.ng
    acl is_wiw hdr_dom(host) -i notebooks-staging.wacren.net
    use_backend ingress-http-repository-aggregator-ren-ng if is_repository_aggregator_ren_ng
    use_backend ingress-http-repository-ren-ng if is_repository_ren_ng
    use_backend ingress-wiw-http if is_wiw
    default_backend ingress-http

backend ingress-http-repository-aggregator-ren-ng
    mode http
    server node-k8s-4a   node-k8s-4.cluster.local:30355 check
    server node-k8s-5a   node-k8s-5.cluster.local:30355 check
    server node-k8s-6a   node-k8s-6.cluster.local:30355 check
    server node-k8s-7a   node-k8s-7.cluster.local:30355 check
    balance roundrobin

backend ingress-http-repository-ren-ng
    mode http
    server node-k8s-4a   node-k8s-4.cluster.local:31485 check
    server node-k8s-5a   node-k8s-5.cluster.local:31485 check
    server node-k8s-6a   node-k8s-6.cluster.local:31485 check
    server node-k8s-7a   node-k8s-7.cluster.local:31485 check
    balance roundrobin

backend ingress-http
    mode http
    server node-k8s-4   node-k8s-4.cluster.local:30000  check
    server node-k8s-5   node-k8s-5.cluster.local:30000  check
    server node-k8s-6   node-k8s-6.cluster.local:30000  check
    server node-k8s-7   node-k8s-7.cluster.local:30000  check
    balance roundrobin

backend ingress-wiw-http
    mode http
    server node-k8s-4   node-k8s-4.cluster.local:31701  check
    server node-k8s-5   node-k8s-5.cluster.local:31701  check
    server node-k8s-6   node-k8s-6.cluster.local:31701  check
    server node-k8s-7   node-k8s-7.cluster.local:31701  check
    balance roundrobin

frontend multiple_https_domains
    bind *:443
    mode tcp
    option tcplog
    tcp-request inspect-delay 5s
    tcp-request content accept if { req.ssl_hello_type 1 }
    use_backend ingress-https-repository-aggregator-ren-ng if  { req_ssl_sni -i repository-aggregator.ren.ng }
    use_backend ingress-https-repository-ren-ng if  { req_ssl_sni -i repository.ren.ng }
    default_backend ingress-https

backend ingress-https-repository-aggregator-ren-ng
    mode tcp
    server node-k8s-4   node-k8s-4.cluster.local:31557  check  check-ssl verify none
    server node-k8s-5   node-k8s-5.cluster.local:31557  check  check-ssl verify none
    server node-k8s-6   node-k8s-6.cluster.local:31557  check  check-ssl verify none
    server node-k8s-7   node-k8s-7.cluster.local:31557  check  check-ssl verify none
    balance roundrobin

backend ingress-https-repository-ren-ng
    mode tcp
    server node-k8s-4   node-k8s-4.cluster.local:31585  check  check-ssl verify none
    server node-k8s-5   node-k8s-5.cluster.local:31585  check  check-ssl verify none
    server node-k8s-6   node-k8s-6.cluster.local:31585  check  check-ssl verify none
    server node-k8s-7   node-k8s-7.cluster.local:31585  check  check-ssl verify none
    balance roundrobin

backend ingress-https
    mode tcp
    server node-k8s-4   node-k8s-4.cluster.local:30000  check  check-ssl verify none
    server node-k8s-5   node-k8s-5.cluster.local:30000  check  check-ssl verify none
    server node-k8s-6   node-k8s-6.cluster.local:30000  check  check-ssl verify none
    server node-k8s-7   node-k8s-7.cluster.local:30000  check  check-ssl verify none
    balance roundrobin


#frontend wiw-https
#    bind *:443
#    mode tcp
#    option httplog
#    default_backend ingress-wiw-https

#backend ingress-wiw-https
    #mode tcp
    #server node-k8s-4   node-k8s-4.cluster.local:30851  check
    #server node-k8s-5   node-k8s-5.cluster.local:30851  check
    #server node-k8s-6   node-k8s-6.cluster.local:30851  check
    #server node-k8s-7   node-k8s-7.cluster.local:30851  check
    #balance roundrobin
```


# Shibboleth setting

```
$ cat shibboleth2.xml
<SPConfig xmlns="urn:mace:shibboleth:3.0:native:sp:config"
    xmlns:conf="urn:mace:shibboleth:3.0:native:sp:config"
    clockSkew="180">

    <OutOfProcess tranLogFormat="%u|%s|%IDP|%i|%ac|%t|%attr|%n|%b|%E|%S|%SS|%L|%UA|%a" />
 <UnixListener address="/tmp/shibd.sock"/>

    <!--
    By default, in-memory StorageService, ReplayCache, ArtifactMap, and SessionCache
    are used. See example-shibboleth2.xml for samples of explicitly configuring them.
    -->
    <RequestMapper type="XML">
    <RequestMap>
        <Host name="weko.example.org"
                authType="shibboleth"
                requireSession="true"
                redirectToSSL="443">
            <Path name="/secure" />
            <!-- other Path, PathRegex or Query elements here -->
        </Host>
        <!-- other Host or HostRegex elements here -->
    </RequestMap>
    </RequestMapper>

    <!-- The ApplicationDefaults element is where most of Shibboleth's SAML bits are defined. -->
    <ApplicationDefaults entityID="https://weko.example.org/shibboleth-sp"
        REMOTE_USER="eppn persistent-id targeted-id"
        cipherSuites="DEFAULT:!EXP:!LOW:!aNULL:!eNULL:!DES:!IDEA:!SEED:!RC4:!3DES:!kRSA:!SSLv2:!SSLv3:!TLSv1:!TLSv1.1">

        <!--
        Controls session lifetimes, address checks, cookie handling, and the protocol handlers.
        Each Application has an effectively unique handlerURL, which defaults to "/Shibboleth.sso"
        and should be a relative path, with the SP computing the full value based on the virtual
        host. Using handlerSSL="true" will force the protocol to be https. You should also set
        cookieProps to "https" for SSL-only sites. Note that while we default checkAddress to
        "false", this makes an assertion stolen in transit easier for attackers to misuse.
        -->
        <Sessions lifetime="28800" timeout="3600" relayState="ss:mem"
                  checkAddress="false" handlerSSL="false" cookieProps="http">

            <!--
            Configures SSO for a default IdP. To properly allow for >1 IdP, remove
            entityID property and adjust discoveryURL to point to discovery service.
            You can also override entityID on /Login query string, or in RequestMap/htaccess.
            -->
        <SSO entityID="https://wacren.wacren.eduid.africa/saml2/idp/metadata.php">
              SAML2
            </SSO>

            <!-- SAML and local-only logout. -->
            <Logout>SAML2 Local</Logout>

            <!-- Administrative logout. -->
            <LogoutInitiator type="Admin" Location="/Logout/Admin" acl="127.0.0.1 ::1" />

            <!-- Extension service that generates "approximate" metadata based on SP configuration. -->
            <Handler type="MetadataGenerator" Location="/Metadata" signing="false"/>

            <!-- Status reporting service. -->
            <Handler type="Status" Location="/Status" acl="127.0.0.1 ::1"/>

            <!-- Session diagnostic service. -->
            <Handler type="Session" Location="/Session" showAttributeValues="false"/>

            <!-- JSON feed of discovery information. -->
            <Handler type="DiscoveryFeed" Location="/DiscoFeed"/>
        </Sessions>

        <!--
        Allows overriding of error template information/filenames. You can
        also add your own attributes with values that can be plugged into the
        templates, e.g., helpLocation below.
        -->
        <Errors supportContact="root@localhost"
            helpLocation="/about.html"
            styleSheet="/shibboleth-sp/main.css"/>

        <!-- Example of locally maintained metadata. -->

        <MetadataProvider type="XML" validate="false" file="idp-metadata.xml"/>
        <MetadataProvider type="XML" validate="true"
                url="https://wacren.wacren.eduid.africa/saml2/idp/metadata.php">
        </MetadataProvider>

        <!-- Example of remotely supplied batch of signed metadata. -->
        <!--
        <MetadataProvider type="XML" validate="true"
                url="http://federation.org/federation-metadata.xml"
              backingFilePath="federation-metadata.xml" maxRefreshDelay="7200">
            <MetadataFilter type="RequireValidUntil" maxValidityInterval="2419200"/>
            <MetadataFilter type="Signature" certificate="fedsigner.pem" verifyBackup="false"/>
            <DiscoveryFilter type="Blacklist" matcher="EntityAttributes" trimTags="true"
              attributeName="http://macedir.org/entity-category"
              attributeNameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri"
              attributeValue="http://refeds.org/category/hide-from-discovery" />
        </MetadataProvider>
        -->

        <!-- Example of remotely supplied "on-demand" signed metadata. -->
        <!--
        <MetadataProvider type="MDQ" validate="true" cacheDirectory="mdq"
                baseUrl="http://mdq.federation.org" ignoreTransport="true">
            <MetadataFilter type="RequireValidUntil" maxValidityInterval="2419200"/>
            <MetadataFilter type="Signature" certificate="mdqsigner.pem" />
        </MetadataProvider>
        -->

        <!-- Map to extract attributes from SAML assertions. -->
        <AttributeExtractor type="XML" validate="true" reloadChanges="false" path="attribute-map.xml"/>

        <!-- Default filtering policy for recognized attributes, lets other data pass. -->
        <AttributeFilter type="XML" validate="true" path="attribute-policy.xml"/>

        <!-- Simple file-based resolvers for separate signing/encryption keys. -->
        <!--
        <CredentialResolver type="File" use="signing"
            key="shibboleth-common.key" certificate="shibboleth-common.cer"/>
        <CredentialResolver type="File" use="encryption"
            key="shibboleth-common.key" certificate="shibboleth-common.cer"/>
        -->
        <CredentialResolver type="File" key="server.key" certificate="server.crt"/>
    </ApplicationDefaults>

    <!-- Policies that determine how to process and authenticate runtime messages. -->
    <SecurityPolicyProvider type="XML" validate="true" path="security-policy.xml"/>

    <!-- Low-level configuration about protocols and bindings available for use. -->
    <ProtocolProvider type="XML" validate="true" reloadChanges="false" path="protocols.xml"/>

</SPConfig>

```

# install certificate

```
$ kubectl get all -n cert-manage
r
NAME                                           READY   STATUS    RESTARTS        AGE
pod/cert-manager-84489bc478-rj5z2              1/1     Running   573 (26d ago)   28d
pod/cert-manager-cainjector-7477d56b47-n8jmp   1/1     Running   498 (26d ago)   28d
pod/cert-manager-webhook-6d5cb854fc-fjxdn      1/1     Running   692 (26d ago)   28d

NAME                           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
service/cert-manager           ClusterIP   10.233.60.211   <none>        9402/TCP   113d
service/cert-manager-webhook   ClusterIP   10.233.58.129   <none>        443/TCP    113d

NAME                                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/cert-manager              1/1     1            1           113d
deployment.apps/cert-manager-cainjector   1/1     1            1           113d
deployment.apps/cert-manager-webhook      1/1     1            1           113d

NAME                                                 DESIRED   CURRENT   READY   AGE
replicaset.apps/cert-manager-84489bc478              1         1         1       113d
replicaset.apps/cert-manager-cainjector-7477d56b47   1         1         1       113d
replicaset.apps/cert-manager-webhook-6d5cb854fc      1         1         1       113d



$ kubectl get ClusterIssuer
NAME                  READY   AGE
letsencrypt-prod      True    113d
letsencrypt-staging   True    113d




```


```
$ kubectl -n weko3 rollout restart deployment repository-ren-ng-web
deployment.apps/repository-ren-ng-web restarted
```


```
kubectl exec -n weko3 repository-ren-ng-web-84d4c7dbbc-vm2xc -c web -- invenio shell scripts/demo/register_oai_schema.py overwrite_all
kubectl exec -n weko3 repository-ren-ng-web-84d4c7dbbc-vm2xc -c web -- invenio shell scripts/demo/register_properties.py only_specified
kubectl exec -n weko3 repository-ren-ng-web-84d4c7dbbc-vm2xc -c web -- invenio shell scripts/demo/renew_all_item_types.py only_specified ALL
```

```
kubectl exec -n weko3 repository-aggregator-ren-ng-web-7f8b66b598-2bwr2  -c web -- invenio shell scripts/demo/register_oai_schema.py overwrite_all
kubectl exec -n weko3 repository-aggregator-ren-ng-web-7f8b66b598-2bwr2  -c web -- invenio shell scripts/demo/register_properties.py only_specified
kubectl exec -n weko3 repository-aggregator-ren-ng-web-7f8b66b598-2bwr2  -c web -- invenio shell scripts/demo/renew_all_item_types.py only_specified ALL
```


```
$ kubectl exec -n weko3pg -it weko-postgresql-0 -- psql -U
 invenio template1
```



# Appendex
