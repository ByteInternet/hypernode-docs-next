---
myst:
  html_meta:
    description: Install Akeneo 6 on a separate Hypernode instance or on the same
      Hypernode as your Magento or Shopware installation. Learn more!
    title: How to install Akeneo 6 on Hypernode?
redirect_from:
  - /en/support/solutions/articles/48001220118-how-to-install-akeneo-6-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001220118-how-to-install-akeneo-6-on-hypernode/ -->

# How to Install Akeneo 6 on Hypernode

Akeneo 6 preferably requires a Hypernode Pelican L, Falcon M, Eagle M hosting plan or larger. You can either choose to install it on a seperate Hypernode instance or on the same Hypernode as your Magento or Shopware installation. If you choose the latter you have to make sure that you have enough resources (disk space, memory and CPU) left. Furthermore you need to make sure that you are already using **MySQL 8.0, PHP 8.0 and Elasticsearch 7.x**, so it won’t affect your shop negatively. Installing Akeneo version 6.x may take up to 15 minutes.

## Managed Vhosts

Hypernode uses [Hypernode Managed Vhosts](../../hypernode-platform/nginx/hypernode-managed-vhosts.md). Ensure you have a vhost for your Akeneo domain.

## Create a Managed_vhost for a (Sub)Domain

If your Magento or Shopware installation already points to `example.hypernode.io`, you can create a managed_vhost for your Akeneo installation on a subdomain, for example `akeneo.example.hypernode.io`. The command below will also install Let’s Encrypt and force your domain to use HTTPS.

```bash
hypernode-manage-vhosts akeneo.example.hypernode.io --type generic-php --https --force-https --webroot /data/web/akeneo/public
```

The file `server.akeneo.conf` will be created and the nginx configuration will look like this:

```nginx
root /data/web/akeneo/public;

include /etc/nginx/handlers.conf;
include /etc/nginx/phpmyadmin.conf;

index index.php index.html;

location / {
    try_files $uri /index.php$is_args$args;
}

location ~ \.php$ {
    echo_exec @phpfpm;
}
```

## Upgrade to MySQL 8.0

**Important: After an update to MySQL 5.7 or 8.0, it’s not possible to switch back to MySQL 5.6.**

It's important to follow these steps in order since you *cannot* upgrade straight from **MySQL 5.6** to **MySQL 8.0**.

First you’ll have to upgrade MySQL 5.6 to 5.7 by running the commando:

```bash
hypernode-systemctl settings mysql_version 5.7
```

After that upgrade from MySQL 5.7 to MySQL 8.0

```bash
hypernode-systemctl settings mysql_version 8.0
```

## Upgrade Your PHP Version to 8.0

Before installing Akeneo, make sure your [PHP version](../../hypernode-platform/php/supported-php-versions-and-how-to-change-them-on-hypernode.md#changing-the-php-version-you-use-on-hypernode) is changed to `PHP 8.0`.

```bash
hypernode-systemctl settings php_version 8.0
```

## Enable PHP-APCU

```bash
hypernode-systemctl settings php_apcu_enabled True
```

## Configure and Enable Elasticsearch v7.x

```bash
hypernode-systemctl settings elasticsearch_version 7.x
```

```bash
hypernode-systemctl settings elasticsearch_enabled True
```

## Download and Install Akeneo 6 Using the Pre-install

Soon available.

## Download and Install Akeneo 6 Manually Using the Command Line

If you don't want to use the pre-install image, than follow the steps below to manually download and install Akeneo in `/data/web/akeneo`

## Configuring Node.js v16

```bash
hypernode-systemctl settings nodejs_version 16
```

After Node.js has been installed you can check if it’s correctly set by running `node -v`. This should output v16.x.x.

### Install the Latest Version of Yarn

```bash
echo 'prefix=${HOME}/.npm' > ~/.npmrc
npm install -g yarn
mkdir -p ~/.local/bin
ln -s ~/.npm/bin/yarn ~/.local/bin/yarn
ln -s ~/.npm/bin/yarnpkg ~/.local/bin/yarnpkg
source ~/.profile
```

### Download Akeneo 6

```bash
composer create-project akeneo/pim-community-standard:"^6.0" akeneo
```

### Create a Database

```bash
mysql -e "create database akeneo_pim;"
```

### Configure Your .env File

Edit the values of your MySQL user, password, host and Elasticsearch host in `/data/web/akeneo/.env`

```bash
sed -i "s/APP_DATABASE_PASSWORD=akeneo_pim/APP_DATABASE_PASSWORD=$(cat ~/.my.cnf | grep password | awk '{print$NF}')/" /data/web/akeneo/.env
sed -i "s/APP_DATABASE_USER=akeneo_pim/APP_DATABASE_USER=$(cat ~/.my.cnf | grep user | awk '{print$NF}')/" /data/web/akeneo/.env
sed -i "s/APP_DATABASE_HOST=mysql/APP_DATABASE_HOST=mysqlmaster/" /data/web/akeneo/.env
sed -i "s/APP_INDEX_HOSTS=elasticsearch:9200/APP_INDEX_HOSTS=localhost:9200/" /data/web/akeneo/.env

cp /data/web/akeneo/.env /data/web/akeneo/.env.local
```

### Launch Akeneo 6

```bash
NO_DOCKER=true make prod
```

### Create a Symlink

```bash
ln -s /data/web/akeneo/public /data/web/akeneo_public
```

### Create an Administrator User

Fill in the form with a Username, Password, First name, Last name, Email and local code.

```bash
bin/console pim:user:create
```

## Setting up the job queue daemon

On Hypernode we have two options to set up the job queue daemon for Akeneo. This can be done via Supervisor or the Cron.

### Option 1. Configure Supervisor

#### Enable Supervisor

Before we start using Supervisor we first need to enable it on the Hypernode.

```bash
hypernode-systemctl settings supervisor_enabled True
```

#### Create a configuration file for Supervisor

Create a file in the configuration directory of supervisor: ~/supervisor/akeneodaemon.conf

```ini
[program:akeneo_queue_daemon]
directory=/data/web/akeneo
command=php bin/console messenger:consume ui_job import_export_job data_maintenance_job --env=prod
autostart=false
autorestart=true
stderr_logfile=/data/web/akeneo_daemon.err.log
stdout_logfile=/data/web/akeneo_daemon.out.log
user=app
```

#### Bring the changes into effect

```bash
supervisorctl reread
supervisorctl update
```

#### Launch the daemon

```bash
supervisorctl start akeneo_queue_daemon
```

### Option 2. Configure Your Akeneo Crons

Configure your crons by adding these scripts to your crontab file as recommended by Akeneo:

```bash
30 1 * * * php /data/web/akeneo/bin/console pim:versioning:refresh
30 2 * * * php /data/web/akeneo/bin/console pim:versioning:purge –more-than-days 90
1 * * * * php /data/web/akeneo/bin/console akeneo:connectivity-audit:update-data
20 0 1 * * php /data/web/akeneo/bin/console akeneo:batch:purge-job-execution
0 1 * * * php /data/web/akeneo/bin/console pim:asset:send-expiration-notification
30 4 * * * php /data/web/akeneo/bin/console pim:volume:aggregate
* * * * * php /data/web/akeneo/bin/console akeneo:batch:job-queue-consumer-daemon
```
