---
myst:
  html_meta:
    description: This article explains how you set up a staging environment on Hypernode
      for a Magento 1 shop. Follow the steps mentioned in this article.
    title: How to set up a staging environment for Magento 1? | Hypernode
redirect_from:
  - /en/ecommerce/magento-1/how-to-set-up-a-staging-environment-for-magento-1/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-set-up-a-staging-environment-for-magento-1/ -->

# How to Set Up a Staging Environment for Magento 1

A staging environment is very useful, for things such as:

- Let a customer (shop-owner) click around a proposed change
- Quickly make a copy of a production shop to analyse a bug that didn't show up during development
- Automated testing by external tools

This article explains how you set one up on Hypernode for a Magento 1 shop.

Keep in mind:

- Your staging environment **shares resources** (disk, CPU, memory) with your production site. If you want to do things such as automated load tests, it is recommended to order a [development plan](../../hypernode-platform/tools/how-to-use-hypernode-development-plans.md) instead, so your production site will not be affected.
- We don't recommend creating hardlinks from your production media folder to your staging media folder as our backup mechanism does not cope well with hardlinks.

## How Does it Work

A second document root (/data/web/staging) is provided and supports all defined vhosts (notably: every SSL vhost). It is reachable on port 8888 and 8880 (http) and 8443 (https).

For Nginx configuration (in /data/web/nginx/\*), the following rules apply:

- http.\* files are included only once in HTTP context
- server.\* files are included in every vhost
- public.\* files are ONLY included in the production vhosts
- staging.\* files are ONLY included in the staging vhosts

This has two distinct advantages. First, there's no need to change DNS, so its very easy to send your customer a link and it just works. Second, SSL certificates will work the same without warning.

Remember that you will need to update the base_url for every storefront (with the new port number). You would have to update the config anyway, as you will likely require a separate database for MySQL and Redis. See below for a simple command.

## How to Make a Copy of a Live Site

Setup your staging environment by following the steps.

It is strongly recommended to use separate databases for your staging environment, so using the staging environment will not interfere with the production data.

### Step One: Copy Your Files to the Staging Directory

```nginx
rsync -va --delete --delete-excluded \
--exclude /var/report/ \
--exclude /var/session/ \
--exclude /var/log/ \
--exclude \*.sql \
--exclude \*.zip \
/data/web/public/ /data/web/staging/

```

### Step two: Create a staging database

```nginx
mysql -e 'create database if not exists staging'

```

### Step Three: Dump the Production Database and Import Into the Staging Database

```nginx
magerun --root-dir=/data/web/public db:dump --strip="@stripped" --stdout | mysql staging

```

### Step Four: Edit Your local.xml and fpc.xml to Use MySQL and Redis Databases Separate From the Production Databases.

```nginx
editor /data/web/staging/app/etc/local.xml
editor /data/web/staging/app/etc/fpc.xml

```

Now at least change your MySQL database to staging and your Redis databases for cache and FPC to another one that is not in use by the production (for example: 3 and 4).

### Step Five: Change the Base URL's of Your Staging Environment

**Warning! Changing the base URL's before changing your MySQL database to your staging database will have impact on your production site.**

```nginx
cd /data/web/staging
export SHOPHOST="mynode.hypernode.io"
magerun --root-dir=/data/web/staging config:set web/unsecure/base_url http://$SHOPHOST:8888/
magerun --root-dir=/data/web/staging config:set web/secure/base_url https://$SHOPHOST:8443/
magerun --root-dir=/data/web/staging cache:flush

```

If you have many storefronts, that all should be changed it's easier to use [our script](https://gist.github.com/hn-support/faf03c5898f5553b7fd9f4059709aef4)to change the base URL's of your staging environment.

To use this script:

```nginx
wget https://gist.githubusercontent.com/hn-support/faf03c5898f5553b7fd9f4059709aef4/raw/0374d20b7a18cf4d81c9cd713910696dd0710674/change_magento1_staging_baseurls.py
python change_magento1_staging_baseurls.py

```

### Step Six: Change All References in Your Staging Directory Pointing at `/data/web/public` to `/data/web/staging`

Isolate your staging environment from your production environment by removing all references to `/data/web/public`:

- Find symlinks: `find /data/web/staging -type l -exec ls -lsa {} \;`
- Grep for `/data/web/public` in your staging directory: `grep -R '/data/web/public' /data/web/staging`
- If you use Git submodules keep in mind that you should change the hardcoded paths and symlinks from `/data/web/public` to `/data/web/staging` to avoid collisions between the staging and the production environment.
- Fix symlinks in your .modman dir that are still pointing to `/data/web/public`
- Change all custom links and references that are in your staging installation pointing to the production installation.

You can update symlinks using the `ln` tool with the `-f` (force) feature flag:

```nginx
ln -sf /data/web/staging/some_file /data/web/staging/some_other_file

```

That's all! Now you should be able to reach your staging environment on <http://mynode.hypernode.io:8888>

### How to Limit Access to a Staging Environment

If you want to restrict access, you can do so by editing /data/web/nginx/staging.access. There are two options.

- Restrict by IP, use this code:

```nginx
allow your.ip.add.ress;
deny all;

```

- Restrict by password (called HTTP basic authentication).

```nginx
auth_basic "Restricted area";
  auth_basic_user_file /data/web/htpasswd-staging;

```

And run this command to add a Hypernode/Hypernode user for the staging environment:

```nginx
htpasswd -bc /data/web/htpasswd-staging hypernode hypernode

```

Read more [here](../../hypernode-platform/nginx/how-to-protect-your-magento-store-with-a-password-in-nginx.md) about using HTTP basic authentication on Hypernode.

## Nginx Configuration

To make config adjustments that are only active in the staging environment, use Nginx config files starting with staging. (For example staging.rewrites instead of server.rewrites)

all configuration files for Nginx in /data/web/nginx starting with "staging." will only be included in the staging server block.

*Files starting with "public." will be included in the public environment only.
Files starting with "server." will be included in both the public and the staging environment.*

## Troubleshooting

### Do You Have Enough Disk Space?

If you don't import log and report tables, it will save you a lot. Use [**this script**](https://gist.github.com/hn-support/be909515580cd08bd23a45dc561c3b78#file-check-enough-space-sh%5B/embed%5D) to check whether you have enough space to make a copy of your live site.

To use this script, save it in your home directory on the Hypernode and execute with `bash scriptname.`

### Find and Remove Hardlinks

In an earlier version of this article we explained how to link your media folder of your staging site with the media folder of the production site using hardlinks.
As we later found out, our backup mechanism could not cope with hardlinks and restores the linked files as individual files, causing the restored backup to be a lot larger than the original.

We do not recommend to use hardlinks anymore.

To detect earlier created hardlinks, use find:

```nginx
find /data/web/ -type f -links +1

```

### External module crashes on different base_url?

The updated base_url will possibly conflict with external modules that use the base_url (with the new port) as license key. Usually, you can fix this by updating the module or asking the vendor to add your staging base_url to the license check.

Status of some common module vendors:

- Xtento: ignores ports since 3 years so not a problem
- GoMage: is a problem, but you can have your staging URL added to the license for free (send them a mail)
- Aitoc: not a problem since 2013. Customers can get a free license key update on request.

### Product feeds pushed for staging environment

If you use extensions that push a product feed to merchant indexing sites like Bol, Google and Marktplaats or Ebay, turn off these feeds for your staging environment to be sure your staging product feeds are not being pushed to any merchant index site.

## Cleanup and Refresh

If you created a staging before on the same machine, you might want to do a resync of the content and the database or remove all staging components

### Cleanup

To cleanup or uninstall your Magento installation use the following magerun command:

```nginx
magerun --root-dir=/data/web/staging uninstall --installationFolder=/data/web/staging --force

```

This will remove your Magento installation and drops the database as well.

### Refresh

To refresh your installation, run all steps again.
This will resync your files and dumps the production database into the staging.
