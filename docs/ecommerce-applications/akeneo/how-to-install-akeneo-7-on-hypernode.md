---
myst:
  html_meta:
    description: Install Akeneo 7 on a separate Hypernode instance or on the same
      Hypernode as your Magento or Shopware installation. Learn more!
    title: How to install Akeneo 7 on Hypernode?
redirect_from:
  - /en/support/solutions/articles/48001220118-how-to-install-akeneo-7-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001220118-how-to-install-akeneo-7-on-hypernode/ -->

# How to Install Akeneo 7 on Hypernode

Akeneo 7 preferably requires a Hypernode Pelican L, Falcon M, Eagle M hosting plan or larger. You can either choose to install it on a seperate Hypernode instance or on the same Hypernode as your Magento or Shopware installation. If you choose the latter you have to make sure that you have enough resources (disk space, memory and CPU) left. Furthermore you need to make sure that you are already using **MySQL 8.0, PHP 8.1 and OpenSearch 2.x**, so it won’t affect your shop negatively. Installing Akeneo version 7.x may take up to 15 minutes.\
**Important note: Akeneo 7.x requires MySQL 8.0.30, which is only available on Debian Bookworm.**

## Create a Vhost for a (Sub)Domain

Ensure you have a vhost for your Akeneo domain.

If your Magento or Shopware installation already points to `example.hypernode.io`, you can create a vhost for your Akeneo installation on a subdomain, for example `akeneo.example.hypernode.io`. The command below will also install Let’s Encrypt and force your domain to use HTTPS.

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

## Upgrade Your PHP Version to 8.1

Before installing Akeneo, make sure your [PHP version](../../hypernode-platform/php/supported-php-versions-and-how-to-change-them-on-hypernode.md#changing-the-php-version-you-use-on-hypernode) is changed to `PHP 8.1`.

```bash
hypernode-systemctl settings php_version 8.1
```

## Enable PHP-APCU

```bash
hypernode-systemctl settings php_apcu_enabled True
```

## Configure and Enable OpenSearch v2.6

```bash
hypernode-systemctl settings opensearch_version 2.6
hypernode-systemctl settings opensearch_enabled True
```

## Download and Install Akeneo 7 Using the Pre-install

On Hypernode we offer an easy way to install Akeneo 7 using one of our pre-install images. Use the following command to install Akeneo 7.

```bash
hypernode-systemctl preinstall akeneo_7_0
```

## Download and Install Akeneo 7 Manually Using the Command Line

If you don't want to use the pre-install image, than follow the steps below to manually download and install Akeneo in `/data/web/akeneo`

## Configuring Node.js v18

```bash
hypernode-systemctl settings nodejs_version 18
```

After Node.js has been installed you can check if it’s correctly set by running `node -v`. This should output v18.x.x.

### Install the Latest Version of Yarn

```bash
echo 'prefix=${HOME}/.npm' > ~/.npmrc
npm install -g yarn
mkdir -p ~/.local/bin
ln -s ~/.npm/bin/yarn ~/.local/bin/yarn
ln -s ~/.npm/bin/yarnpkg ~/.local/bin/yarnpkg
source ~/.profile
```

### Download Akeneo 7

```bash
composer create-project akeneo/pim-community-standard:"^7.0" akeneo
```

### Create a Database

```bash
mysql -e "create database akeneo_pim;"
```

### Configure Your .env File

Edit the values of your MySQL user, password, host and OpenSearch host in `/data/web/akeneo/.env`

```bash
sed -i "s/APP_DATABASE_PASSWORD=akeneo_pim/APP_DATABASE_PASSWORD=$(cat ~/.my.cnf | grep password | awk '{print$NF}')/" /data/web/akeneo/.env
sed -i "s/APP_DATABASE_USER=akeneo_pim/APP_DATABASE_USER=$(cat ~/.my.cnf | grep user | awk '{print$NF}')/" /data/web/akeneo/.env
sed -i "s/APP_DATABASE_HOST=mysql/APP_DATABASE_HOST=mysqlmaster/" /data/web/akeneo/.env
sed -i "s/APP_INDEX_HOSTS=localhost:9200/" /data/web/akeneo/.env

cp /data/web/akeneo/.env /data/web/akeneo/.env.local
```

### Launch Akeneo 7

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
30 2 * * * php /data/web/akeneo/bin/console pim:versioning:purge –more-than-days 90 --no-interaction --force
1 * * * * php /data/web/akeneo/bin/console akeneo:connectivity-audit:update-data
20 0 1 * * php /data/web/akeneo/bin/console akeneo:batch:purge-job-execution
30 4 * * * php /data/web/akeneo/bin/console pim:volume:aggregate
10 * * * * php /data/web/akeneo/bin/console akeneo:connectivity-connection:purge-error
30 3 * * * php /data/web/akeneo/bin/console akeneo:connectivity-audit:purge-error-count
15 0 * * * php /data/web/akeneo/bin/console pim:data-quality-insights:schedule-periodic-tasks
10 * * * * php /data/web/akeneo/bin/console pim:data-quality-insights:prepare-evaluations
30 * * * * php /data/web/akeneo/bin/console pim:data-quality-insights:evaluations
5 * * * * php /data/web/akeneo/bin/console akeneo:connectivity-connection:purge-events-api-logs
4 21 * * 0 php /data/web/akeneo/bin/console akeneo:connectivity-connection:openid-keys:create --no-interaction
30 0 * * * php /data/web/akeneo/bin/console pim:data-quality-insights:clean-completeness-evaluation-results --no-interaction
*/10 * * * * php /data/web/akeneo/bin/console pim:job-automation:push-scheduled-jobs-to-queue
0 */2 * * * php /data/web/akeneo/bin/console akeneo:messenger:doctrine:purge-messages messenger_messages default
```
