---
myst:
  html_meta:
    description: This article explains how you can set up a staging environment on
      Hypernode for a Shopware 5 shop. Learn everything you need to know!
    title: How to use a staging environment with Shopware 5?
redirect_from:
  - /en/ecommerce/shopware/how-to-use-a-basic-staging-environment-with-shopware/
---

<!-- source: https://support.hypernode.com/en/ecommerce/shopware/how-to-use-a-basic-staging-environment-with-shopware/ -->

# How to Use a Basic Staging Environment With Shopware

A staging environment is very useful, for things such as:

- Let a customer (shop-owner) try out a proposed change
- To quickly make a copy of a production shop to analyse a bug that didn't show up during development
- Automated testing by external tools

This article explains how you can set up a staging environment on Hypernode for a Shopware shop.

Keep in mind:

- Your staging environment **shares resources** (disk, CPU, mem) with your production site. If you want to do things such as automated load tests, it is recommended to order a [development plan](../../hypernode-platform/tools/how-to-use-hypernode-development-plans.md) instead, so your production site will not be affected.
- We don't recommend creating hard links from your production media folder to your staging media folder as our back up mechanism does not cope well with hard links.

## How to Make a Copy of a Live Site

Set up your staging environment by following the steps.

It is strongly recommended to use separate databases for your staging environment, so using the staging environment will not interfere with the production data.

### Step one: Copy your Shopware files to the staging directory

```nginx
rsync -va --delete --delete-excluded \
--exclude /var/cache/ \
/data/web/public/ /data/web/staging/
```

### Step two: Create a staging database

```nginx
mysql -e 'create database if not exists staging'
```

### Step three: Connect your file system to the database

```nginx
editor /data/web/staging/.env
```

Make sure to change the 'DB_DATABASE' value to your staging database: DB_DATABASE="staging"

### Step four: Dump the production database and import into the staging database

```nginx
mysqldump shopware | mysql staging
```

### Step five: Redirect domains to your staging environment

To redirect requests to the staging environment, you need the following snippet. Create a `/data/web/nginx/http.staging_redir_mapping` file containing:

```nginx
map $http_host $staging_site {
hostnames;
dehault 0;
example.com 1;
}
```

Next, create a snippet to redirect all sites mapped as staging_site to the staging environment.

To do this, create a /data/web/nginx/server.staging_redir file containing:

```nginx
if ($staging_site = 1) {
return 301 http://$http_host:8888$request_uri;
}
```

Now all traffic for domains that are mapped as staging_domain, will be redirected to the same URL but on port 8888.

### Step six: Change the SHOP_URL in /data/web/staging/.env

`editor /data/web/staging/.env`

Make sure you edit the value of SHOP_URL to your Hypernode-URL: SHOP_URL=`http://APPNAME.hypernode.io:8888/`

### Step seven: Change the URL in the 's_core_shop' table for your staging database

Now to use the staging environment, we need to change the base URLs to use the ports for the staging environment. This way your site is accessible through the same URLs as the production shop but will be using different ports. We change the HTTP port to 8888 and the HTTPS port to 8443.

Please note to check which ID is relevant for your URL with the `select * from s_core_shops;`

```nginx
mysql
> use staging
> select * from s_core_shops;
> update s_core_shops set host = 'APPNAME.hypernode.io:8888' where id = 1;
```
