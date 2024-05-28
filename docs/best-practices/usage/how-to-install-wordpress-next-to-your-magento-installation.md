---
myst:
  html_meta:
    description: This article explains in detail how to install WordPress next to
      your Magento application on Hypernode. Please be aware of the security implications.
    title: How to install WordPress next to your Magento installation?
redirect_from:
  - /en/best-practices/usage/how-to-install-wordpress-next-to-your-magento-installation/
---

<!-- source: https://support.hypernode.com/en/best-practices/usage/how-to-install-wordpress-next-to-your-magento-installation/ -->

# How to Install WordPress Next to Your Magento Installation

**Warning:** Installing WordPress on your Hypernode has some serious security implications: Although Magento is quite secure, many vulnerability issues are discovered in WordPress extensions. We recommend running your WordPress blog on a different server than your webshop as a security leak in WordPress causes attackers to have full access to your webshop!

**Due to high demand we decided to document how to install WordPress on Hypernode. This is at your own risk!**

## Create a Database

First create a database for WordPress:

```bash
mysql -Be 'create database if not exists wordpress'
```

## Installing WordPress

To install WordPress on Hypernode, we’ll use the `/data/web/public/blog` directory.

### Create a Directory

```bash
mkdir -p ~/public/blog
```

### Download WordPress to the blog/ Directory

```bash
cd /data/web/public/blog/
wp core download --force
```

### Unpack WordPress and Create a wp-config.php

```bash
wp core config --dbhost=mysqlmaster --dbname=wordpress --dbuser=app --dbpass=<your mysql password>
```

### Install WordPress and Load the Database Schema

```bash
wp core install --title="blog" --admin_user="your-admin-user" --admin_password="your-admin-password" --admin_email="you@example.com" --url=appname.hypernode.io/blog/
```

Activate All Plugins, Sync the Database Schema and Flush the Cache

```bash
wp plugin activate --all
wp core update-db
wp cache flush
```

*Now your Wordpress is fully installed.*

## Configuring WordPress to Work in a Subdirectory

To configure WordPress to work in a subdirectory, add the following snippet to the top of your `wp-config.php`:

```php
$host = 'http://' . $_SERVER['HTTP_HOST'] . '/blog/';
define('WP_HOME', $host);
define('WP_SITEURL', $host);
define('AUTOMATIC_UPDATER_DISABLED', false);
define('WP_AUTO_UPDATE_CORE', true);
```

## Configuring Nginx to Serve WordPress in a Subdirectory

Now all we need to do is configuring Nginx to serve a WordPress site in a subdirectory.

Create a `/data/web/nginx/server.wordpress` with the following content:

```nginx
location /blog {
    root /data/web/public;
    index index.php;
    try_files $uri $uri/ /blog/index.php;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }

    location ~* /(?:uploads|files)/.*\.php$ {
        deny all;
    }
}
```

## Visit Your WordPress Site

After installing and configuring Nginx, you can visit your WordPress at `/blog/`

## Multisite

It is possible to set up a multisite environment in WordPress. To do this, refer to the [original WordPress documentation about creating multisites](https://codex.wordpress.org/Create_A_Network)and the article [about configuring WordPress on Nginx](https://wordpress.org/support/article/nginx/).

*Please note that it won’t work in all cases due to the fact that certain Nginx configurations cannot be changed. At the moment we are still looking into a solution that will work for everyone.*
