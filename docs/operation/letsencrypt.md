# Let's Encrypt

## multi domain 証明書

### 更新

```
docker-compose run --rm certbot certonly --webroot -w /var/www/html -d <FQDN1> -d <FQDN2> --email <Mail address> --agree-tos -n --expand
```

```
$ docker-compose run --rm certbot certonly --webroot -w /var/www/html -d <FQDN1> -d <FQDN2> --email <Mail address> --agree-tos -n --expand
WARNING: The ELASTICSEARCH_S3_ACCESS_KEY variable is not set. Defaulting to a blank string.
WARNING: The ELASTICSEARCH_S3_SECRET_KEY variable is not set. Defaulting to a blank string.
WARNING: The ELASTICSEARCH_S3_ENDPOINT variable is not set. Defaulting to a blank string.
WARNING: The ELASTICSEARCH_S3_BUCKET variable is not set. Defaulting to a blank string.
Creating weko_certbot_run ... done
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator webroot, Installer None
Cert is due for renewal, auto-renewing...
Renewing an existing certificate for <FQDN1> and <FQDN2>
Performing the following challenges:
http-01 challenge for <FQDN1>
http-01 challenge for <FQDN2>
Using the webroot path /var/www/html for all unmatched domains.
Waiting for verification...
Cleaning up challenges

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/<FQDN1>/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/<FQDN1>/privkey.pem
   Your certificate will expire on 2025-05-12. To obtain a new or
   tweaked version of this certificate in the future, simply run
   certbot again. To non-interactively renew *all* of your
   certificates, run "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le
```

```
docker-compose restart nginx
```

```
$ docker-compose restart nginx
Restarting weko_nginx_1 ... done
```