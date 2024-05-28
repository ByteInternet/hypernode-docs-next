---
myst:
  html_meta:
    description: This article will explain how to install Laravel on your Hypernode.
      Laravel is a PHP framework that is used to build web applications.
    title: How to install Laravel on Hypernode
---

# How to install Laravel on Hypernode

This article will explain how to install Laravel on your Hypernode. Laravel is a PHP framework that is used to build web applications.

## Upgrade your PHP version

Laravel only has a few system requirements. One of which, is that PHP needs to be at least 8.1. Run the following command to upgrade to PHP 8.1:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-systemctl settings php_version 8.2
```

## Installing Laravel

To install Laravel, there are two options:

1. Using our preinstall command-line tool
1. Installing Laravel manually

### Install Laravel using the preinstall

On Hypernode we offer an easy way to install Laravel using one of our preinstall presets. Use the following command to install Laravel:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-systemctl preinstall laravel
```

To follow the progress of the preinstall, run the program `livelog`.

### Installing Laravel manually

Manual installation is also possible, which also doesn't take much time.

First you need to create a database for the Laravel application and create some directories:

```console
app@abcdef-example-magweb-cmbl:~$ echo create database laravel | mysql
```

Then you can install Laravel using Composer:

```console
app@abcdef-example-magweb-cmbl:~$ composer create-project laravel/laravel /data/web/laravel
```

Before we can run the application, we need to adjust some configurations. Open the `.env` file in the root of the Laravel application and run the following commands:

```console
app@abcdef-example-magweb-cmbl:~$ export MYSQL_PASSWORD=$(grep password /data/web/.my.cnf | awk '{print $3}')
app@abcdef-example-magweb-cmbl:~$ sed -i "s/DB_HOST=.*/DB_HOST=mysqlmaster/g" /data/web/laravel/.env
app@abcdef-example-magweb-cmbl:~$ sed -i "s/DB_DATABASE=.*/DB_DATABASE=laravel/g" /data/web/laravel/.env
app@abcdef-example-magweb-cmbl:~$ sed -i "s/DB_USERNAME=.*/DB_USERNAME=app/g" /data/web/laravel/.env
app@abcdef-example-magweb-cmbl:~$ sed -i "s/DB_PASSWORD=.*/DB_PASSWORD=$MYSQL_PASSWORD/g" /data/web/laravel/.env
app@abcdef-example-magweb-cmbl:~$ sed -i "s/REDIS_HOST=.*/REDIS_HOST=redismaster/g" /data/web/laravel/.env
app@abcdef-example-magweb-cmbl:~$ sed -i "s/MAIL_MAILER=.*/MAIL_MAILER=sendmail/g" /data/web/laravel/.env
app@abcdef-example-magweb-cmbl:~$ sed -i "s#APP_URL=.*#APP_URL=https://example.hypernode.io#g" /data/web/laravel/.env
```

With these commands we set the database credentials, the Redis host, the mailer backend and the application URL.

Now we can install the application:

```console
app@abcdef-example-magweb-cmbl:~$ cd /data/web/laravel
app@abcdef-example-magweb-cmbl:~$ php artisan migrate
```

## Setting up the NGINX vhost

Finally, we need to set up the NGINX vhost.

We need to configure the vhost to point to the `public` directory of the Laravel application and to have the `generic-php` vhost type.
We also generate a new SSL certificate for the domain using the `--https` flag.

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-manage-vhosts example.hypernode.io --webroot /data/web/laravel/public --type generic-php --https
...
INFO: Managing configs for example.hypernode.io
INFO: Writing HTTP config for example.hypernode.io
INFO: Writing HTTPS config for example.hypernode.io
```

## Your journey begins

There you go! You have installed a Laravel application on your Hypernode. Your journey starts here.
If you have any questions along the way, feel free to contact our support team. We're happy to help!
