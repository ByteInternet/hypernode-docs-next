---
myst:
  html_meta:
    description: Hypernode offers a staging environment so it can be used as a sandbox
      for your Akeneo 3 PIM project. Learn more in this article!
    title: How to use a basic staging environment with Akeneo 3?
redirect_from:
  - /en/ecommerce/akeneo/how-to-use-a-basic-staging-environment-with-akeneo/
---

<!-- source: https://support.hypernode.com/en/ecommerce/akeneo/how-to-use-a-basic-staging-environment-with-akeneo/ -->

# How To Use A Basic Staging Environment with Akeneo 3

Hypernode offers a staging environment so it can be used as a sandbox for your Akeneo PIM project. Please keep in mind that your staging environment for Akeneo shares resources (disk, CPU, memory) with your production environment. It’s also possible to order a [development plan](../../hypernode-platform/tools/how-to-use-hypernode-development-plans.md) instead, so your production environment will not be affected. Once again a big thank you to our partner [Experius](https://www.experius.nl/) for contributing to this article!

## Update managed_vhosts

Update the current managed_vhost with staging port.

```bash
hypernode-manage-vhosts  akeneo.example.hypernode.io --port-http-staging 8888 --port-https-staging 8443 --force-https --https
```

## Split the Nnginx Configuration for Production and Staging

First run the following commands to differentiate between te Production and Staging environment within Nginx.

```bash
cd ~/nginx/demo.akeneo.experius.io
cp server.akeneo.conf staging.akeneo.conf
mv server.akeneo.conf public.akeneo.conf
```

Next, edit the `staging.akeneo.conf` and change to:

```nginx
root /data/web/akeneo_staging;
include /etc/nginx/handlers.conf;

index app.php;
set $fastcgi_root /data/web/akeneo_staging;
location * {
    try_files $request_filename $uri;
}

location / {
  # If the requested page is a file that doesn't exist, serve
  # app.php instead, and let it be executed using phpfpm.
  if (!-f $request_filename){
      rewrite ^(.*)$ /app.php/ break;
      echo_exec @phpfpm;
  }
}

location ~ \.php$ {
    echo_exec @phpfpm;
}
```

## Setup the Web Symlink for the Staging Environment

```bash
cd ~
mkdir akeneo-staging
cp -R akeneo akeneo-staging
ln -s /data/web/akeneo-staging/akeneo/pim-community-standard/web akeneo_staging
```

## Duplicate the akeneo_pim database to staging_akeneo_pim

```bash
mysql -e 'CREATE DATABASE staging_akeneo_pim;'
mysqldump akeneo_pim | mysql staging_akeneo_pim
```

## Change the Parameters for the Staging Akeneo

Edit `~/akeneo-staging/akeneo/pim-community-standard/app/config/parameters.yml` and change the following:

- change database_name from akeneo_pim to staging_akeneo_pim
- update the Elasticsearch index names by adding a staging prefix for example: akeneo_pim_product > staging_akeneo_pim_product

*Don’t forget configs like the temp upload directory, please update accordingly.*

## Reindex Elasticsearch

```bash
bin/console akeneo:elasticsearch:reset-indexes
bin/console pim:product:index --all
bin/console pim:product-model:index --all
```

## Configure a Cronjob for Staging

```bash
* * * * * flock -n ~/.daemon-staging.lock -c 'php /data/web/akeneo-staging/pim-community-standard/bin/console akeneo:batch:job-queue-consumer-daemon --env=prod'
```

**Tada! The staging is now up and running on `https://akeneo.example.hypernode.io:8443`**
