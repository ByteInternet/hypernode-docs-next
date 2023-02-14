---
myst:
  html_meta:
    description: This article will explain how you can setup the latest version of
      WooCommerce on Hypernode as easy as possible.
    title: How to install WooCommerce on Hypernode?
redirect_from:
  - /en/support/solutions/articles/48001213397-how-to-install-woocommerce-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001213397-how-to-install-woocommerce-on-hypernode/ -->

# How to install WooCommerce on Hypernode

This article will explain how you can setup the latest version of WooCommerce on Hypernode as easy as possible.

## Upgrade your PHP version

WooCommerce supports a [wide range of PHP versions](https://woocommerce.com/document/server-requirements/), but for this article we'll choose the highest possible version. Run the following command to upgrade to PHP 8.1:

```console
$ hypernode-systemctl settings php_version 8.1
```

## Upgrade your MySQL version

To make sure you're on MySQL 8.0, run the following command:

```console
hypernode-systemctl settings mysql_version 8.0
```

## Setting your NGINX vhost type

To be able to host WooCommerce on Hypernode you need to set your vhost type to 'wordpress':

```console
$ hypernode-manage-vhosts mynode.hypernode.io --type wordpress
INFO: Managing configs for mynode.hypernode.io
INFO: Writing HTTP config for mynode.hypernode.io
INFO: Writing HTTPS config for mynode.hypernode.io
```

## Installing WooCommerce

To install WooCommerce, there are two options:

1. Using our preinstall command-line tool
1. Installing WooCommerce manually

### Download and install WooCommerce using the preinstall

On Hypernode we offer an easy way to install WooCommerce using one of our pre-install presets. Use the following command to install WooCommerce:

```console
$ hypernode-systemctl preinstall woocommerce
```

To follow the progress of the preinstall, run the program livelog.

### Installing WooCommerce manually

First you need to create a database for the WooCommerce application and create some directories:

```console
$ echo create database woocommerce | mysql
$ mkdir -p /data/web/wordpress
$ # Backup public directory. If the directory is empty or wasn't being used, feel free to remove it instead.
$ test -d /data/web/public && mv /data/web/public /data/web/public.bak
$ ln -s /data/web/wordpress /data/web/public
```

Now we can start downloading, configuring and installing the base for WooCommerce onto the Hypernode.

```console
$ ~/wordpress
$ wp core download
$ #  Please check your mysql password at ~/.my.cnf for the next step
$ wp core config --dbhost='localhost' --dbuser='app' --dbpass='your_mysql_password' --dbprefix='wp_'
$ wp core install --admin_user='mynode_admin' --admin_password='insecure_wp_password' --admin_email='owner@example.com' --url='https://mynode.hypernode.io' --title='My WooCommerce Shop'
```

At this point, you should be able to access your application at '<https://mynode.hypernode.io>', but you'll note that it's just a WordPress site. To change that into a WooCommerce site, run the following commands:

```console
$ # Optional: before installing the WooCommerce plugin, we set the email from address so we can make sure that our mails arrive.
$ wp option set woocommerce_email_from_address 'noreply@mynode.hypernode.io'
$ wp plugin install redis-cache nginx-helper woocommerce wordfence --activate
$ wp theme install storefront --activate
$ wp redis enable
```

Now when you reload your site, you'll see that some things have changed and that there's a 'Shop' link in the menu. WooCommerce is now up and running! Below are some recommended settings you can do:

```console
$ # Use SEO friendly URL rewrites
$ wp rewrite structure '/%postname%/'
$ # Run the WordPress cron from the system and not during web page requests (2 steps)
$ wp config set DISABLE_WP_CRON true
$ # Open your crontab editor with `crontab -e` and add the following line:
$ */2 * * * * chronic php /data/web/wordpress/wp-cron.php
```
