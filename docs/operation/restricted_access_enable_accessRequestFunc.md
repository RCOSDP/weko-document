## 利用申請機能の有効化手順（運用担当者向け）

利用申請機能の有効化手順をまとめる。
本手順は、**利用申請機能の先行利用申請があった機関（以降、対象機関）に対して実施する手順である**。
本手順は、対象機関の状態を事前に確認する「事前準備」と、
実際に利用申請機能を有効化する「利用申請機能の有効化」の2段階ある。

### 1. 事前準備

事前準備は、対象機関に対して、実際に利用申請機能を有効化する「利用申請機能の有効化」の想定通りの環境となっているかを
事前に確認することを目的としている。

#### 1-1. 各ツールの取得
 
必要なファイルをコンテナ内で取得する。

``` sh
# sh変数の定義
$ REPO=xxx.repo.nii.ac.jp              # 切り替え対象とする機関名
$ WORK_DIR=WEKO3_OPE-xxxx              # ワークディレクトリを指定
$ BRANCH=fix/issue60615  # 使用するブランチはNII担当者に確認

$ WEB_POD=$(kubectl get po -n weko3 | grep ^$(echo ${REPO} | tr ._ -)-web | awk '{ print $1;}')
$ GITHUB_PATH=https://raw.githubusercontent.com/RCOSDP/weko/refs/heads/${BRANCH}

# 確認
$ declare -p REPO WORK_DIR BRANCH WEB_POD GITHUB_PATH

# コンテナ内で必要ファイルを取得
$ kubectl exec -n weko3 ${WEB_POD} -c web -- bash -c "
    curl -o scripts/demo/resticted_access.sql ${GITHUB_PATH}/scripts/demo/resticted_access.sql &&
    curl -o tools/switch_restricted_access/disable/get_target_table_hash.sql ${GITHUB_PATH}/tools/switch_restricted_access/disable/get_target_table_hash.sql &&
    curl -o tools/switch_restricted_access/disable/verify_table.json ${GITHUB_PATH}/tools/switch_restricted_access/disable/verify_table.json &&
    curl -o tools/switch_restricted_access/enable/get_target_table_hash.sql ${GITHUB_PATH}/tools/switch_restricted_access/enable/get_target_table_hash.sql &&
    curl -o tools/switch_restricted_access/enable/verify_table.json ${GITHUB_PATH}/tools/switch_restricted_access/enable/verify_table.json &&
    curl -o tools/restricted_upadate.sh ${GITHUB_PATH}/tools/restricted_upadate.sh &&
    curl -o tools/update_restricted_access_property.py ${GITHUB_PATH}/tools/update_restricted_access_property.py &&
    curl -o tools/verify_restricted_records.py ${GITHUB_PATH}/tools/verify_restricted_records.py &&
    curl -o tools/verify_restricted_update.sh ${GITHUB_PATH}/tools/verify_restricted_update.sh"
```

#### 1-2. 現在のDB状態の確認

1. 以下のコマンドを実行する。

```sh
$ LOG_DIR=/usr/local/share/operation/${WORK_DIR}
$ mkdir -p ${LOG_DIR}
$ kubectl exec -n weko3 ${WEB_POD} -c web -- invenio shell tools/verify_restricted_records.py enable &> ${LOG_DIR}/verify_restricted_records_${REPO//[.-]/_}.log
# ログの確認
cat ${LOG_DIR}/verify_restricted_records_${REPO//[.-]/_}.log | python3 -c 'import sys,re,ast; s=sys.stdin.read(); expected={"all":["mail_template_genres","mail_templates"],"some":[],"no":["item_type_name","item_type","item_type_mapping","item_type_property","index","workflow_flow_define","workflow_flow_action","workflow_workflow","workflow_userrole","admin_settings"]}; patterns={"all":r"Tables with all records correct:\s*(\[[^\]]*\])","some":r"Tables with some records correct:\s*(\[[^\]]*\])","no":r"Tables with no records correct:\s*(\[[^\]]*\])"}; matches={k:re.search(p,s) for k,p in patterns.items()}; actual={k:ast.literal_eval(m.group(1)) for k,m in matches.items() if m}; errors=[k+": result not found" for k,m in matches.items() if not m]; errors += [k+": expected="+str(sorted(expected[k]))+", actual="+str(sorted(actual[k])) for k in expected if k in actual and set(actual[k]) != set(expected[k])]; print("OK: 検証結果は期待値と一致しています" if not errors else "ERROR:\n"+"\n".join(errors)); sys.exit(0 if not errors else 1)'
```

OK: 検証結果は期待値と一致しています と出力されれば、成功である。
ERROR：　が出力された場合は、失敗である。

2. ログファイルをNII担当者に送付する。

NII担当者はログファイルを確認し、利用申請機能の有効化を実施する機関を決定する。
ログファイルが想定外であった場合は、データマイグレーション検討が必要なため、対象機関から一旦外す。

### 2. 利用申請機能の有効化

利用申請機能の有効化は、対象機関に対して、実際に利用申請機能を有効化する。

#### 2-1. 準備

1. sh変数の設定

※ shの切り替えやセッション切れなどがあった場合は再設定すること。

```sh
$ REPO=xxxx.repo.nii.ac.jp             # 機関リポジトリ名
$ WORK_DIR=WEKO3_OPE-xxxxx             # ワークディレクトリ
$ BRANCH=fix/issue60615                # githubのブランチ(NII担当者に確認)

$ GITHUB_PATH=https://raw.githubusercontent.com/RCOSDP/weko/refs/heads/${BRANCH}
$ DEPLOYMENT=$(kubectl get deployment -n weko3 | grep ^$(echo ${REPO} | tr ._ -)-web | awk '{ print $1;}')
$ DB=$(echo ${REPO} | tr .- _)
$ PG_MASTER=$(kubectl get po -n weko3pg -l spilo-role=master --no-headers | awk '{ print $1; }')

# 確認
$ declare -p REPO WORK_DIR BRANCH GITHUB_PATH DEPLOYMENT DB PG_MASTER
```
    
1. repositories.txtの作成

切り替え対象機関のみのrepositories.txtを作成する。

#### 2-2. サービスの停止

1. メンテナンス画面用Ingressの準備

```sh
$ cd /usr/local/weko-k8s/scripts

# 前回作成したメンテナンスページ表示用のマニフェストファイルが存在しないことを確認
$ ls /tmp/maintenance_ingress_manifests.yaml

# ingressのマニフェストファイルの作成
$ ./make_maintenance_manifests.sh <作成したrepositories.txt> /tmp/maintenance_ingress_manifests.yaml
```

1. メンテナンス画面の表示

```sh
$ cd /usr/local/weko-k8s/deploy/maintenance

# 日付などを編集する
$ vi configmap.yaml

# configmapをデプロイ
$ kubectl apply -f configmap.yaml

# メンテナンス画面用PODのデプロイ
$ kubectl apply -f deploy-maintainance.yaml

# メンテナンス画面への切り替え
$ kubectl apply -f /tmp/maintenance_ingress_manifests.yaml
```

対象機関のリポジトリにブラウザでアクセスし、メンテナンス画面に切り替わっていることを確認する。

1. WEB PODの削除

```sh
$ kubectl delete deployment -n weko3 ${DEPLOYMENT}
```

#### 2-3. バックアップ

1. instance.cfgのバックアップを取得する。

```sh
$ sudo cp /fs-config/${REPO}/instance.cfg /fs-config/${REPO}/instance.cfg_$(date +%Y%m%d)
```

1. DBのバックアップを取得する。

```sh
# バックアップディレクトリの作成
$ sudo mkdir -p /fs-pgbackup/${WORK_DIR}

# バックアップ実行
$ kubectl exec -n weko3pg ${PG_MASTER} -c postgres -- pg_dump -d ${DB} -U invenio -t 'item_type_name' -t 'item_type' -t 'item_type_mapping' -t 'item_type_property' -t 'accounts_role' -t 'index' -t 'workflow_flow_define' -t 'workflow_flow_action' -t 'workflow_workflow' -t 'workflow_userrole' -t 'mail_template_genres' -t 'mail_templates' -t 'admin_settings' -t 'item_type_edit_history' -t 'jsonld_mappings' -t 'rocrate_mapping' -t 'access_actionsroles' -t 'accounts_userrole' -t 'communities_community' -t 'shibboleth_userrole' -t 'workflow_flow_action_role' -t 'harvest_settings' -t 'journal' -t 'resync_indexes' -t 'workflow_activity' -t 'sword_clients' -t 'mail_template_users' -t 'author_affiliation_community_relations' -t 'author_community_relations' -t 'author_prefix_community_relations' -t 'communities_community_record' -t 'communities_featured_community' -t 'user_activity_logs' -t 'resync_logs' -t 'workflow_activity_action' -f /var/lib/postgresql/backup/${WORK_DIR}/disable_dump.sql --clean
```

#### 2-4. スクリプトの実行準備

1. 対象機関のWEB PODを起動

```sh
# 対象機関のWEB PODのデプロイ
$ kubectl apply -f /usr/local/share/deploy_logs/weko-manifests/${REPO}/manifests/deploy-web.yaml

# 起動確認(PODのStatusが3/3)になるまで待つ
$ kubectl get po -n weko3 | grep ${DEPLOYMENT}

# ログの確認
$ WEB_POD=$(kubectl get po -n weko3 | grep ^${DEPLOYMENT} | awk '{ print $1;}')
$ kubectl logs -n weko3 ${WEB_POD} -c web
```

1. コンテナ内に必要ファイルを取得

1. コンテナ内に必要ファイルを取得

``` sh
$ kubectl exec -n weko3 ${WEB_POD} -c web -- bash -c "
    curl -o scripts/demo/resticted_access.sql ${GITHUB_PATH}/scripts/demo/resticted_access.sql &&
    curl -o tools/switch_restricted_access/disable/get_target_table_hash.sql ${GITHUB_PATH}/tools/switch_restricted_access/disable/get_target_table_hash.sql &&
    curl -o tools/switch_restricted_access/disable/verify_table.json ${GITHUB_PATH}/tools/switch_restricted_access/disable/verify_table.json &&
    curl -o tools/switch_restricted_access/enable/get_target_table_hash.sql ${GITHUB_PATH}/tools/switch_restricted_access/enable/get_target_table_hash.sql &&
    curl -o tools/switch_restricted_access/enable/verify_table.json ${GITHUB_PATH}/tools/switch_restricted_access/enable/verify_table.json &&
    curl -o tools/restricted_upadate.sh ${GITHUB_PATH}/tools/restricted_upadate.sh &&
    curl -o tools/update_restricted_access_property.py ${GITHUB_PATH}/tools/update_restricted_access_property.py &&
    curl -o tools/verify_restricted_records.py ${GITHUB_PATH}/tools/verify_restricted_records.py &&
    curl -o tools/verify_restricted_update.sh ${GITHUB_PATH}/tools/verify_restricted_update.sh"
```

#### 2-5. 有効化スクリプトの実行

1. wekoブランチの切り替え

```sh
$ cd /usr/local/weko
$ git status    # 現在のブランチを確認
$ git stash     # ローカルブランチに変更がある場合は一旦stashする
$ git pull      # 最新の変更を取り込み
$ git checkout ${BRANCH}
```

1. 有効化スクリプトの実行。

```sh
# ログディレクトリの作成
$ LOG_DIR=/usr/local/share/operation/${WORK_DIR}
$ mkdir -p ${LOG_DIR}
$ cd /usr/local/weko/

# スクリプトの実行
$ ./tools/restricted_upadate.sh ${REPO} &> ${LOG_DIR}/restricted_update_${REPO//[.-]/_}.log
```

1. 確認

```sh
$ grep -i -e error -e fail ${LOG_DIR}/restricted_update_${REPO//[.-]/_}.log
```

エラーが出力された場合にはNII担当者に連絡し、確認の上[切り戻し手順（有効）](#切り戻し手順有効)を実施する。


#### 2-6. 利用有効化の確認・反映

1. 確認スクリプトの実行

```sh
# 確認スクリプトの実行
$ kubectl exec -n weko3 ${WEB_POD} -c web -- invenio shell tools/verify_restricted_records.py enable &> ${LOG_DIR}/verify_restricted_records_${REPO//[.-]/_}.log.log

# 実行結果を確認する
cat ${LOG_DIR}/verify_restricted_records_${REPO//[.-]/_}.log.log | python3 -c 'import sys,re,ast; s=sys.stdin.read(); expected={"all":["item_type_name","item_type","item_type_mapping","item_type_property","index","workflow_flow_define","workflow_flow_action","workflow_workflow","workflow_userrole","mail_template_genres","mail_templates","admin_settings"],"some":[],"no":[]}; patterns={"all":r"Tables with all records correct:\s*(\[[^\]]*\])","some":r"Tables with some records correct:\s*(\[[^\]]*\])","no":r"Tables with no records correct:\s*(\[[^\]]*\])"}; matches={k:re.search(p,s) for k,p in patterns.items()}; actual={k:ast.literal_eval(m.group(1)) for k,m in matches.items() if m}; errors=[k+": result not found" for k,m in matches.items() if not m]; errors += [k+": expected="+str(sorted(expected[k]))+", actual="+str(sorted(actual[k])) for k in expected if k in actual and set(actual[k]) != set(expected[k])]; print("OK: 検証結果は期待値と一致しています" if not errors else "ERROR:\n"+"\n".join(errors)); sys.exit(0 if not errors else 1)'
```

「OK: 検証結果は期待値と一致しています」と出力された場合は成功である。

以下のように「ERROR:」が出力された場合、NII担当者へ報告し、[切り戻し手順（有効）](#切り戻し手順有効)を実施する。エラーの出力内容は環境により異なる可能性がある。 

```
ERROR:
all: expected=['admin_settings', 'index', 'item_type', 'item_type_mapping', 'item_type_name', 'item_type_property', 'mail_template_genres', 'mail_templates', 'workflow_flow_action', 'workflow_flow_define', 'workflow_userrole', 'workflow_workflow'], actual=['mail_template_genres', 'mail_templates']
no: expected=[], actual=['admin_settings', 'index', 'item_type', 'item_type_mapping', 'item_type_name', 'item_type_property', 'workflow_flow_action', 'workflow_flow_define', 'workflow_userrole', 'workflow_workflow']
```

1. 設定値を環境に反映させ、サービスを開始する。

```sh
# instance.cfgの設定を反映するためPODをリスタート
$ kubectl rollout restart -n weko3 deployment/${DEPLOYMENT}

# 起動確認(Statusが3/3になるまで待つ)
$ kubectl get po -n weko3 | grep ${DEPLOYMENT}

# エラーがないかログを確認する
WEB_POD=$(kubectl get po -n weko3 | grep ^$(echo ${DEPLOYMENT} | tr ._ -)-web | awk '{ print $1;}')
$ kubectl logs -n weko3 ${WEB_POD} -c web | less

# 問題なければサービスを再開する
$ kubectl apply -f /usr/local/share/deploy_logs/weko-manifests/${rEPO}$/manifests/ingress.yaml
```

ブラウザで対象機関にアクセスし、問題ないか確認する。

1. アナウンス

NII担当者に作業完了報告を実施する。

#### 2-7. 事後作業

1. メンテナンスPODを削除する

```sh
$ cd /usr/local/weko-k8s/deploy/maintenance

# メンテナンス画面のPODの削除
$ kubectl delete -f deploy-maintainance.yaml
```

### 3. 有効化の切り戻し手順

#### 3-1. 設定値の切り戻し

1. instance.cfgのバックアップを書き戻す。

```sh
$ sudo cp /fs-config/${REPO}/instance.cfg_<バックアップ日付> /fs-config/${REPO}/instance.cfg
    ```

#### 3-2. WEB PODの停止

※ メンテナンス画面が表示されている前提

1. WEB PODが起動している場合は停止する。

```sh
$ kubectl delete deployment -n weko3 ${DEPLOYMENT}
```

#### 3-3. DBの切り戻し

1. バックアップからレストアする。

```sh
$ kubectl exec -n weko3pg ${PG_MASTER} -c postgres -- psql -d ${DB} -U invenio -f /var/lib/postgresql/backup/${WORK_DIR}/disable_dump.sql
```

#### 3-4. WEB PODデプロイ

1. WEB PODのデプロイ

```sh
# 対象機関のWEB PODのデプロイ
$ kubectl apply -f /usr/local/share/deploy_logs/weko-manifests/${REPO}/manifests/deploy-web.yaml

# 起動確認(PODのStatusが3/3)になるまで待つ
$ kubectl get po -n weko3 | grep ${DEPLOYMENT}

# ログの確認
$ WEB_POD=$(kubectl get po -n weko3 | grep ^${DEPLOYMENT} | awk '{ print $1;}')
kubectl logs -n weko3 ${WEB_POD} -c web
```

1. サービスを開始する。

```sh
# 問題なければサービスを再開する
$ kubectl apply -f /usr/local/share/deploy_logs/weko-manifests/${REPO}/manifests/ingress.yaml
```

ブラウザで対象機関にアクセスし、問題ないか確認する。

1. アナウンス

NII担当者に作業完了報告を実施する。

#### 3-5. 事後作業
1. メンテナンスPODを削除する

```sh
$ cd /usr/local/weko-k8s/deploy/maintenance

# メンテナンス画面のPODの削除
$ kubectl delete -f deploy-maintainance.yaml
    ```

