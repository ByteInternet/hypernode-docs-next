---
myst:
  html_meta:
    description: This article explains how you can set up a staging environment on
      Hypernode for a Shopware 6 shop. Learn everything you need to know!
    title: How to use a staging environment with Shopware 6?
redirect_from:
  - /en/ecommerce/shopware/how-to-use-a-basic-staging-environment-with-shopware-6/
---

<!-- source: https://support.hypernode.com/en/ecommerce/shopware/how-to-use-a-basic-staging-environment-with-shopware-6/ -->

# How to Use a Basic Staging Environment With Shopware 6

A staging environment is very useful, for things such as:

- Let a customer (shop-owner) try out a proposed change
- To quickly make a copy of a production shop to analyse a bug that didn't show up during development
- Automated testing by external tools

This article explains how you can set up a staging environment on Hypernode for a Shopware shop.

Keep in mind:

- Your staging environment **shares resources** (disk, CPU, mem) with your production site. If you want to do things such as automated load tests, it is recommended to order a [development plan](../../hypernode-platform/tools/how-to-use-hypernode-development-plans.md) instead, so your production site will not be affected.
- We don't recommend creating hard links from your production media folder to your staging media folder as our back up mechanism does not cope well with hard links.

## How To Make a Copy of a Live Site

Set up your staging environment by following the steps. It is strongly recommended to use separate databases for your staging environment, so using the staging environment will not interfere with the production data.

### Step One: Create a New Vhost for the Staging Environment

First create a new vhost for the staging environment, in this example I'd like to use a subdomain for my staging environment: `staging.example.hypernode.io`

```bash
hypernode-manage-vhosts staging.example.hypernode.io --type shopware6 --https --force-https
```

### Step Two: Set the Webroot

Now there is a new vhost, you need to set the webroot to the folder you'd like to use for your staging environment. You can do this by editing the **webroot** on the first line in the following 2 files: `/data/web/nginx/staging.example.hypernode.io/public.shopware6.conf`
`/data/web/nginx/staging.example.hypernode.io/staging.webroot.conf`

### Step Three: Copy Your Shopware Files to the Staging Directory

```bash
rsync -va --delete --delete-excluded \
          --exclude /var/cache/ \
          /data/web/shopware/ /data/web/shopware_staging/
```

### Step Four: Create a Staging Database

```bash
mysql -e 'create database if not exists staging'
```

### Step Five: Connect Your File System to the Database

```bash
editor /data/web/shopware_staging/.env
```

Make sure to change the `DATABASE_URL` value to your staging database. Change the databasename after the "**/**" into your staging databasename: "**staging**"

### Step Six: Dump the Production Database and Import Into the Staging Database

```bash
mysqldump $databasename | mysql staging
```

### Step Seven: Change the SHOP_URL in /data/web/staging/.env

```bash
editor /data/web/shopware_staging/.env
```

Make sure you edit the value of APP_URL to your Hypernode-URL: APP_URL="<http://APPNAME.hypernode.io:8888/>"

### Step Eight: Change the URL in the `sales_channel_domain` Table for Your Staging Database

Now to use the staging environment, we need to change the base URLs to use the ports for the staging environment. This way your site is accessible through the same URLs as the production shop but will be using different ports. We change the HTTP port to 8888 and the HTTPS port to 8443. Please note to check which ID is relevant for your URL with the `select * from sales_channel_domain;` query.

```console
$ mysql
> use staging;
> select * from sales_channel_domain;
> update sales_channel_domain set url = 'https://staging.APPNAME.hypernode.io' where url = 'https://EXAMPLE.com';
```

### Step Nine: Flush the Cache

After caching the URL the cache needs to be flushed before the change is processed

```bash
cd /data/web/shopware_staging
php bin/console cache:clear
```

### Step Ten: Set the Symlink

The final step is to create the symlink.

```bash
rm -rf /data/web/staging
ln -s /data/web/shopware_staging/public/ /data/web/staging
```
