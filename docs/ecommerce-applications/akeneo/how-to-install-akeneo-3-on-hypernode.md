---
myst:
  html_meta:
    description: Install Akeneo 3 on a separate Hypernode instance or on the same
      Hypernode as your Magento or Shopware installation. Learn more!
    title: How to install Akeneo 3 on Hypernode?
redirect_from:
  - /en/ecommerce/akeneo/how-to-install-akeneo-3-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/ecommerce/akeneo/how-to-install-akeneo-3-on-hypernode/ -->

# How to Install Akeneo 3 on Hypernode

Akeneo 3 preferably requires a Hypernode Pelican L, Falcon M, Eagle M hosting plan or larger. You can either choose to install it on a seperate Hypernode instance or on the same Hypernode as your Magento or Shopware installation. If you choose the latter you have to make sure that you have enough resources (disk space, memory and CPU) left. Furthermore you need to make sure that you are already using **MySQL 5.7, PHP 7.2 and Elasticsearch 6.x**, so it won’t affect your shop negatively. Installing Akeneo version 3.x may take up to 15 minutes.

## Enable managed_vhosts

All new Hypernodes (from April 2020) will automatically be booted with [Hypernode Managed Vhosts](../../hypernode-platform/nginx/hypernode-managed-vhosts.md). If you already have an older Hypernode, then you need to enable Hypernode Managed Vhosts by running the following command:

```bash
hypernode-systemctl settings managed_vhosts_enabled True
```

## Create a Managed_vhost for a (Sub)Domain

If your Magento or Shopware installation already points to `example.hypernode.io`, you can create a managed_vhost for your Akeneo installation on a subdomain, for example `akeneo.example.hypernode.io`. The command below will also install Let’s Encrypt and force your domain to use HTTPS.

```bash
hypernode-manage-vhosts akeneo.example.hypernode.io --type akeneo --https --force-https
```

## Upgrade to MySQL 5.7

**Important: After an update to MySQL 5.7 or 8.0, it’s not possible to switch back to MySQL 5.6.**

```bash
hypernode-systemctl settings mysql_version 5.7
```

## Upgrade Your PHP Version to 7.2

Before installing Akeneo, make sure your [PHP version](../../hypernode-platform/php/supported-php-versions-and-how-to-change-them-on-hypernode.md#changing-the-php-version-you-use-on-hypernode) is changed to `PHP 7.2`.

```bash
hypernode-systemctl settings php_version 7.2
```

## Enable PHP-APCU

```bash
hypernode-systemctl settings php_apcu_enabled True
```

## Configure and Enable Elasticsearch v6.x

```bash
hypernode-systemctl settings elasticsearch_version 6.x
```

```bash
hypernode-systemctl settings elasticsearch_enabled True
```

## Two ways to install Akeneo 3: Pre-install or the Command Line

### Download and Install Akeneo 3 Using the Pre-install

On Hypernode we offer an easy way to install Akeneo 3 using one of our pre-install images. Use the following command to install Akeneo 3.

```bash
hypernode-systemctl preinstall akeneo_3_2
```

### Install Akeneo 3 Using the Command Line

#### Install Node.js v10.16

```bash
cd /tmp
wget https://nodejs.org/dist/v10.16.0/node-v10.16.0-linux-x64.tar.xz
tar xvfJ node-v10.16.0-linux-x64.tar.xz
mv node-v10.16.0-linux-x64 ~/.node
rm node-v10.16.0-linux-x64.tar.xz
mkdir -p ~/.local/bin
for f in ~/.node/bin/*; do ln -s $f ~/.local/bin/`basename $f`; done
source ~/.profile
```

After Node.js has been installed you can check if it’s correctly set by running `node -v`. This should output v10.16.0.

#### Install the Latest Version of Yarn

```bash
cd /tmp
wget https://yarnpkg.com/latest.tar.gz
tar zvxf latest.tar.gz
mv yarn-v* ~/.yarn
rm latest.tar.gz
ln -s ~/.yarn/bin/yarn ~/.local/bin/yarn
ln -s ~/.yarn/bin/yarnpkg ~/.local/bin/yarnpkg
source ~/.profile
```

#### Download and Install Akeneo 3 Using the Command Line

Follow the instructions below to download and unzip the latest stable release to /data/web/akeneo.

#### Download Akeneo with Sample Data

If you want to start with preconfigured demo data also known as ‘icecat’.

```bash
wget https://download.akeneo.com/pim-community-standard-v3.2-latest-icecat.tar.gz -O akeneo.tar.gz
```

#### Download Akeneo without Sample Data

If you want to start a fresh blank catalog also known as ‘minimal’.

```bash
wget https://download.akeneo.com/pim-community-standard-v3.2-latest.tar.gz -O akeneo.tar.gz
```

#### Unpack Akeneo

After you’ve downloaded Akeneo unpack it.

```bash
mkdir ~/akeneo
tar zvxf akeneo.tar.gz -C ~/akeneo/
```

#### Setting up Akeneo

First change the MySQL username and password in `~/akeneo/pim-community-standard/app/config/parameters.yml` to your own [credentials](../../hypernode-platform/mysql/how-to-use-mysql-on-hypernode.md#finding-your-credentials).

```bash
mysql -e "create database akeneo_pim;"
cd ~/akeneo/pim-community-standard
php -d memory_limit=3G ../composer.phar install --optimize-autoloader --prefer-dist
yarn install
php bin/console cache:clear --no-warmup --env=prod
php bin/console pim:installer:assets --symlink --clean --env=prod
bin/console pim:install --force --symlink --clean --env=prod
yarn run webpack
```

#### Create an Administrator User

Fill in the form with a Username, Password, First name, Last name, Email and local code.

```bash
bin/console pim:user:create
```

#### Finish the Installation

```bash
bin/console pim:completeness:calculate --env=prod
bin/console pim:versioning:refresh --env=prod
bin/console pim:volume:aggregate --env=prod
ln -s /data/web/akeneo/pim-community-standard/web /data/web/akeneo_public
```

#### Restart PHP-FPM

```bash
hypernode-servicectl restart php7.2-fpm
```

**Tada! Your Akeneo-installation is now available on `akeneo.example.hypernode.io`!**

## Configure Your Akeneo Cron

After installing Akeneo, configure your cron by adding these scripts to your crontab file:

```bash
*/15 * * * * php /data/web/akeneo/pim-community-standard/bin/console pim:completeness:calculate --env=prod > /data/web/akeneo/pim-community-standard/app/logs/calculate_completeness.log 2>&1
*/15 * * * * php /data/web/akeneo/pim-community-standard/bin/console pim:versioning:refresh --env=prod > /data/web/akeneo/pim-community-standard/app/logs/refresh_versioning.log 2>&1
*/15 * * * * php /data/web/akeneo/pim-community-standard/bin/console pim:volume:aggregate --env=prod > /data/web/akeneo/pim-community-standard/app/logs/volume_aggregate.log 2>&1
20 0 1 * * php /data/web/akeneo/pim-community-standard/bin/console akeneo:batch:purge-job-execution –env=prod > /data/web/akeneo/pim-community-standard/var/logs/purge_job_execution.log 2>&1
* * * * * flock -n ~/.daemon.lock -c 'php /data/web/akeneo/pim-community-standard/bin/console akeneo:batch:job-queue-consumer-daemon --env=prod'
```

## Troubleshooting

### Error when installing Akeneo: No alive nodes found in your cluster

Make sure ElasticSearch is enabled.

### When creating a user in Akeneo: Property “user_default_locale” expects a valid locale code. The locale does not exist, “en_US” given.

Akeneo wasn’t installed properly, probably because elasticsearch wasn’t enabled in the first place.

### request.CRITICAL: Uncaught PHP Exception “index_not_found_exception”,”reason”:”no such index”

There may be mismatches in the Elastic index. Reset the Elasticsearch indexes:

```bash
cd /data/web/akeneo/pim-community-standard
php bin/console akeneo:elasticsearch:reset-indexes --env=prod
php bin/console pim:product:index --all --env=prod
php bin/console pim:product-model:index --all --env=prod
```
