---
myst:
  html_meta:
    description: This article explains how you set up a staging environment on Hypernode
      for a Magento 2 shop. Follow the steps mentioned in this article.
    title: How to set up a staging environment for Magento 2? | Hypernode
redirect_from:
  - /en/ecommerce/magento-2/how-to-set-up-a-basic-staging-environment-for-magento-2/
  - /knowledgebase/using-a-basic-staging-environment-magento2/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-set-up-a-basic-staging-environment-for-magento-2/ -->

# How to Set Up a Basic Staging Environment for Magento 2

This article is an extension to the [article for Magento 1](../magento-1/how-to-set-up-a-staging-environment-for-magento-1.md). For information about the capabilities of the staging environment, please read it first.

Your staging environment **shares resources**(disk, CPU, memory) with your production site. If you want to do things such as automated load tests, it is recommended to order a [development plan](../../hypernode-platform/tools/how-to-use-hypernode-development-plans.md) instead, so your production site will not be affected.

## How to Make a Copy of a Live Site

Setup your staging environment by following the steps.

It is strongly recommended to use separate databases for your staging environment, so using the staging environment will not interfere with the production data.

### Step One: Copy Your Magento2 Directory to a Staging Content Directory

```nginx
rsync -va --delete --delete-excluded \
--exclude /var/report/ \
--exclude /var/session/ \
--exclude /var/log/ \
--exclude \*.sql \
--exclude \*.zip \
/data/web/magento2/ /data/web/magento2_staging/

```

### Step Two: Recreate Symlinks for the Staging Public Directory

```nginx
cd ~
rm -rf /data/web/staging && ln -s /data/web/magento2_staging/pub /data/web/staging
```

### Step Three: Create a Staging Database

```nginx
mysql -e 'create database if not exists staging'

```

### Step Four: Edit Your di.xml and env.php to Use MySQL and Redis Databases Separate From the Production Databases

```nginx
sensible-editor /data/web/magento2_staging/app/etc/env.php

```

Now at least change your MySQL database to staging and your Redis databases for cache and FPC to another one that is not in use by the production. (for example: 3 and 4)

### Step Five: Dump the Production Database Into the Staging Database

```nginx
magerun2 --root-dir=/data/web/magento2 db:dump --strip="@stripped" --stdout | mysql staging

```

### Step Six: Change the Base URL's of Your Staging Environment

**Warning! Changing the base URL's before changing your MySQL database to your staging database will have impact on your production site.**

Now to use the staging environment, we need to change the base URL's to use the ports for the staging environment. This way your site is accessible through the same URL's as the production shop but will be using different ports. We change the HTTP port to 8888 and the HTTPS port to 8443.

`**`Please note the we often see conflicts when the unsecure and the secure Base-URLs are not the same. So either set both Base-URLs to HTTP -> 8888 or both URLs to HTTPS -> 8443. For example:

```nginx
| id | code    | unsecure_baseurl                       | secure_baseurl                         |
+----+---------+----------------------------------------+----------------------------------------+
| 1  | default | http://www.example.com:8888/      | http://www.example.com:8888/

```

OR:

```nginx
| 1 | default | https://www.example.com:8443/ | https://www.example.com:8443/

```

Use the following command to change the ports of your staging shop, but use your own domains. You can do this for a single storefront or for all of them.
This way, if your live shop is `[https://www.example.com/](https://www.example.com/%60)`, your staging environment will be accessible on `[https://www.example.com:8443/](https://www.example.com:8443/%60)`

#### Change the Base URL's for a Single Storefront Using Magerun

```nginx
cd /data/web/staging
export SHOPHOST="mynode.hypernode.io"
magerun2 --root-dir=/data/web/magento2_staging config:store:set web/unsecure/base_url http://$SHOPHOST:8888/
magerun2 --root-dir=/data/web/magento2_staging config:store:set web/secure/base_url https://$SHOPHOST:8443/
magerun2 --root-dir=/data/web/magento2_staging cache:flush

```

#### Change the Base URL's for All Storefronts Using a Script

If you have many storefronts, that all should be changed it's easier to use [our script](https://gist.github.com/hn-support/d7a6fdd89bd78ebd7a03982605743616) to change the base URL's of your staging environment.

To use this script:

```nginx
wget https://gist.githubusercontent.com/hn-support/d7a6fdd89bd78ebd7a03982605743616/raw/77837096d4a325b3f863609cd8282531faf0fe4a/change_magento2_staging_baseurls.py
python change_magento2_staging_baseurls.py

```

#### Change the Base URLS' for All Your Storefronts Via MySQL

Another easy way to change the base URLs of all your stores is by running the [following database queries:](https://gist.github.com/experius-nl/8e5cfd21bbb407dfdaa79021ee1f3da1)

A big thank you to our partner [Experius](https://www.experius.nl/) for providing these.

#### Manually Change the Base URL's of Your Storefronts

If you want to set the base URL's manually, check [our documentation](../magento-1/how-to-change-the-base-url-in-magento-1-x.md) on changing your base URL's for Magento 1. Do you have a Magento 2 shop, please check [this article](how-to-change-your-magento-2-base-urls.md) on changing base URL's.

### Step Seven: Change All References in Your Staging Directory

**If your media directory is stored in `/data/web/staging`, make sure first not to overwrite this folder with a symlink**

Keep in mind:

- Re-deploy your static files (clean out pub/static, and [deploy your static files](how-to-install-magento-2-on-hypernode.md#build-static-assets)
- Find symlinks: `find /data/web/magento2_staging -type l -exec ls -lsa {} \;`
- Grep for `/data/web/public` in your staging directory: `grep -R '/data/web/public' /data/web/staging`
- Grep for `/data/web/magento2` in your staging directory: `grep -R '/data/web/magento2' /data/web/{staging,magento2_staging}`
- If you use Git submodules keep in mind that you should change the hardcoded paths and symlinks from `/data/web/public` to `/data/web/staging` to avoid collisions between the staging and the production environment.
- Fix symlinks in your .modman dir that are still pointing to `/data/web/public`
- Regenerate your sitemap as it may still contain links to your live site.
- Change all custom links and references that are in your staging installation pointing to the production install.

Now you should be able to reach your Magento 2 staging environment on <http://mynode.hypernode.io:8888>

For additional configuration and troubleshooting refer to the [Magento 1 staging environment article](../magento-1/how-to-set-up-a-staging-environment-for-magento-1.md)

## Staging Environment and Varnish

Do note that when Varnish is active on the live environment and you are using the same Base-URL for the staging environment you can't use Varnish on the staging environment. This might result in mixed content from the Varnish live environment on the Varnish staging environment.

For example. Your live Base-URL `https://www.example.com` and your staging environment has `https://www.example.com:8443/`. So both environments use the same domain which causes the varnish cache to get mixed up.

If you want to use Varnish for the staging URL make sure to use an unique domain so both domains have their own cache. To do this you can either use the Hypernode domain, or create a subdomain for yourself. For example:

live: [https://www.example.com/](https://example.com/)

staging: <https://APPNAME.hypernode.io:8443/>

or: [https://staging.example.com:8443/](https://staging.example.com/%3C.code%3E)

In the example above the domain for the staging environment is always different than the one from the live environment and therefor the Varnish cache won't get mixed up.

## Hypernode Manage Vhosts

Another solution is creating a unique vhost for your staging environment. This will allow you to use the normal ports so you don't have to use port `8443`.
For example, you can create a vhost `staging.example.com`. Afterwards you can always choose to enable or disable varnish for this vhost.

```console
$ hypernode-manage-vhosts staging.example.com --varnish
$ hypernode-manage-vhosts --list
+---------------------------------+------------+----------------+-------+-------------+---------+--------------+
|            servername           |    type    | default_server | https | force_https | varnish |  ssl_config  |
+---------------------------------+------------+----------------+-------+-------------+---------+--------------+
|       staging.example.com       |  magento2  |     False      | False |    False    |   True  | intermediate |
+---------------------------------+------------+----------------+-------+-------------+---------+--------------+
```

To be able to reach the new staging environment you need to change the webroot of the vhost to whatever folder you like. In this case let's create a folder called **/data/web/example_staging/**. You can change the webroot in the nginx-folder that has been created by creating the vhost, in this case: **/data/web/nginx/staging.example.com/public.magento2.conf**. The webroot is set in the first uncommented line of the file:

```nginx
root /data/web/public;
```

So now we want to set this to: `root /data/web/example_staging;` and save the file. Now you can set the Magento installation in this location and you're set.

## Cleanup and Refresh

If you created a staging environment before on the same machine, you might want to do a resync of the content and the database or remove all staging components

### Cleanup

```bash
magerun2 --root-dir=/data/web/magento2_staging uninstall --installationFolder=/data/web/magento2_staging --force
```

This will remove your Magento installation and drops the database as well.

To refresh your installation, run all steps again.
This will resync your files and dumps the production database into the staging.
All steps are the same, making it easy to recreate your environment
