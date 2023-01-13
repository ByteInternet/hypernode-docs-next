---
myst:
  html_meta:
    description: Hypernode offers a staging environment so it can be used as a sandbox
      for your Akeneo 4 or 5 PIM project. Learn more in this article!
    title: How to use a basic staging environment with Akeneo 4 and 5?
redirect_from:
  - /en/support/solutions/articles/48001183489-how-to-use-a-basic-staging-environment-with-akeneo-4-and-5/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001183489-how-to-use-a-basic-staging-environment-with-akeneo-4-and-5/ -->

# How To Use A Basic Staging Environment with Akeneo 4 and 5

Hypernode offers a staging environment so it can be used as a sandbox for your Akeneo PIM project. Please keep in mind that your staging environment for Akeneo shares resources (disk, CPU, memory) with your production environment. It’s also possible to order a [development plan](../../hypernode-platform/tools/how-to-use-hypernode-development-plans.md) instead, so your production environment will not be affected.

## Create a vhost

Create a vhost for your staging environment.

```bash
hypernode-manage-vhosts staging.example.hypernode.io --force-https --https --type akeneo4
```

## Split the Nnginx Configuration for Production and Staging

Edit the `~/nginx/staging.example.hypernode.io/server.akeneo4.conf` and change to:

```nginx
root /data/web/akeneo_staging;
include /etc/nginx/handlers.conf;

location * {
    try_files $request_filename $uri;
}

location / {
    if (!-f $request_filename) {
        rewrite ^(.*)$ /index.php/ break;
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
ln -s ~/akeneo-staging/akeneo/pim-community-standard/public akeneo_staging
```

## Duplicate the akeneo_pim database to staging_akeneo_pim

```bash
mysql -e 'CREATE DATABASE staging_akeneo_pim;'
mysqldump akeneo_pim | mysql staging_akeneo_pim
```

## Change the Parameters for the Staging Akeneo

Edit `~/akeneo-staging/akeneo/pim-community-standard/.env` and change the following:

- change database_name from akeneo_pim to staging_akeneo_pim
- update the Elasticsearch index names by adding a staging prefix for example: akeneo_pim_product_and_product_model > staging_akeneo_pim_product_and_product_model

*Don’t forget configs like the temp upload directory, please update accordingly.*

## Reindex Elasticsearch

```bash
bin/console akeneo:elasticsearch:reset-indexes
bin/console pim:product:index --all
bin/console pim:product-model:index --all
```

## Configure a Cronjob for Staging

```bash
* * * * * flock -n ~/.daemon-staging.lock -c 'php /data/web/akeneo-staging/akeneo/pim-community-standard/bin/console akeneo:batch:job-queue-consumer-daemon --env=prod'
```

**Tada! The staging is now up and running on `https://staging.example.hypernode.io`**
