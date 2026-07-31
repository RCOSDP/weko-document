
```
$ docker compose -f docker-compose2.yml run --rm certbot certonly --manual --preferred-challenges dns-01 -d ams-dev.ir.rcos.nii.ac.jp
[+] Building 0.0s (0/0)                                                                                                                                            
[+] Building 0.0s (0/0)                                                                                                                                            
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Renewing an existing certificate for ams-dev.ir.rcos.nii.ac.jp

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please deploy a DNS TXT record under the name:

_acme-challenge.ams-dev.ir.rcos.nii.ac.jp.

with the following value:

EDmWvzp4fJLMcsTl8HBKUy8LW6W9NtVFgb0bKUAkV50

Before continuing, verify the TXT record has been deployed. Depending on the DNS
provider, this may take some time, from a few seconds to multiple minutes. You can
check if it has finished deploying with aid of online tools, such as the Google
Admin Toolbox: https://toolbox.googleapps.com/apps/dig/#TXT/_acme-challenge.ams-dev.ir.rcos.nii.ac.jp.
Look for one or more bolded line(s) below the line ';ANSWER'. It should show the
value(s) you've just added.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Press Enter to Continue
```

```
$ dig -t txt _acme-challenge.ams-dev.ir.rcos.nii.ac.jp

; <<>> DiG 9.11.36-RedHat-9.11.36-8.el8 <<>> -t txt _acme-challenge.ams-dev.ir.rcos.nii.ac.jp
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 64775
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1424
; COOKIE: 101b72322de4279c01000000696d7329026b090af6a542a8 (good)
;; QUESTION SECTION:
;_acme-challenge.ams-dev.ir.rcos.nii.ac.jp. IN TXT

;; ANSWER SECTION:
_acme-challenge.ams-dev.ir.rcos.nii.ac.jp. 60 IN TXT "EDmWvzp4fJLMcsTl8HBKUy8LW6W9NtVFgb0bKUAkV50"

;; Query time: 10 msec
;; SERVER: 136.187.17.3#53(136.187.17.3)
;; WHEN: Mon Jan 19 08:56:25 JST 2026
;; MSG SIZE  rcvd: 154
```

```

Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/ams-dev.ir.rcos.nii.ac.jp/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/ams-dev.ir.rcos.nii.ac.jp/privkey.pem
This certificate expires on 2026-04-18.
These files will be updated when the certificate renews.

NEXT STEPS:
- This certificate will not be renewed automatically. Autorenewal of --manual certificates requires the use of an authentication hook script (--manual-auth-hook) but one was not provided. To renew this certificate, repeat this same certbot command before the certificate's expiry date.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
If you like Certbot, please consider supporting our work by:
 * Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
 * Donating to EFF:                    https://eff.org/donate-le
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

```
