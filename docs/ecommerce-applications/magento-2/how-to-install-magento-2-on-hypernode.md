---
myst:
  html_meta:
    description: Learn how to install Magento 2 on Hypernode. It requires preferably
      a Falcon M hosting plan or bigger and will take only 5-10 minutes.
    title: How to install Magento 2 on Hypernode?
redirect_from:
  - /en/ecommerce/magento-2/how-to-install-magento-2-on-hypernode/
  - /knowledgebase/installing-magento-on-hypernode/
  - /knowledgebase/installing-magento-2-on-hypernode
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-install-magento-2-on-hypernode/ -->

# How to Install Magento 2 on Hypernode

Magento 2 requires preferably a Falcon M hosting plan or bigger. Want to [install Magento 1](../magento-1/how-to-install-magento-1-on-hypernode.md) instead?

Installing Magento 2 will take only 5-10 minutes (add 15 minutes if you want the sample data).

## Upgrade Your PHP Version

**Before installing Magento,**[**change your PHP version**](../../hypernode-platform/php/supported-php-versions-and-how-to-change-them-on-hypernode.md#changing-the-php-version-you-use-on-hypernode)**to php7.1 or higher**

Some vendor libraries are not compatible with older PHP version anymore, causing errors during the installation.

That's why you must first change your PHP version to PHP7.1 before starting the Magento 2 installation.

## Remove Existing Magento 1 Installation (If Any)

This is obviously only required if you have a previous Magento 1 installation. Log in to your Hypernode and run this command

```
magerun --root-dir=/data/web/public uninstall --installationFolder=/data/web/public --force
```

This will delete the default database (such as `shop_preinstalled_magento`), and recursively delete the `/data/web/public directory`. Any instances of Magento installed in other directories will not be touched.

## Remove Existing Magento 2 Installation (If Any)

This is obviously only required if you have a previous Magento 2 installation. Use this command to clean up any previous Magento 2 installation:

```
rm -rf /data/web/public /data/web/magento2-sample-data
```

Drop any previous M2 preinstall db:

```
mysql
show databases;
drop database appname_preinstalled_magento;
```

## Activate Magento 2 Mode

Hypernode will activate all kinds of Magento 2 cleverness when you activate M2 mode. This happens if you create a file called `/data/web/nginx/magento2.flag`:

```
touch ~/nginx/magento2.flag
```

## `NEW`: Install our Pre-installed Magento 2 version with ONE command

Using the command `hypernode-systemctl preinstall [preinstall_type]`, the installation is automatically installed. The current supported preinstall_types are `magento_1`, `magento_2`, `shopware_5`, `shopware_6`, `akeneo3.2` and `akeneo4.0`. By adding `--sample-data` as an argument we install the version with sample data . Take a look at the `livelog` command to check the progress on the update job.

Please be aware that this does not set the general Hypernode settings (php, mysql) to the proper values. This still needs to happen manually. In addition, for Magento make sure the /data/web/public folder is empty.

First make sure the current Composer version is set to **2.x**

```
# Check composer version
composer -V
Composer version 1.10.26 2022-04-13 16:39:56

# Update composer version to 2.x
hypernode-systemctl settings composer_version 2.x
```

Now you can start the preinstall of Magento 2

```console
# Start the preinstall
app@appname.hypernode.io:~$ hypernode-systemctl preinstall magento_2 --sample-data
Preinstall magento2 with sample data job posted, see hypernode-log (or livelog) for job progress.

# Check the preinstall status
app@appname.hypernode.io:~$ livelog # or hypernode-log

# Check out your new installation
app@appname.hypernode.io:~$ ls /data/web # See the magento2 directory and the contents of public
```

## Install Magento 2 Using the Command Line

### Download and Unzip the Latest Release to /data/web/magento2

```
mkdir ~/magento2
cd ~/magento2
wget -qO- https://magento.mirror.hypernode.com/releases/magento2-latest.tar.gz | tar xfz -
```

### Create a Database (In This Example, We Named the Database ‘magento2’, but You Can Name It However You Like)

```
echo "create database magento2" | mysql
```

### Enable the Magento 2 Management Tool

```
chmod 755 bin/magento
```

### Almost Done! Look up Your Database Credentials

```
cat ~/.my.cnf
```

### Fill in the User, Hostname and Password in the Following Command and You Are Ready to Install Magento 2

```
bin/magento setup:install --db-host=[HOSTNAME] --db-name=[DATABASE] --db-user=app --db-password=[DATABASE_PASSWORD] \
--admin-firstname=[YOURFIRSTNAME] --admin-lastname=[YOURSURNAME] --admin-user=[ADMINNAME] \
--admin-password=[ADMINPASSWORD] --admin-email=[YOUR@EMAIL.COM] --base-url=[http://YOUR.HYPERNODE.IO] \
--language=en_US --timezone=Europe/Berlin --currency=EUR --use-rewrites=1
```

### Enable Secure Document Root

```
rm --dir /data/web/public
ln -s /data/web/magento2/pub /data/web/public
```

### Build Static Assets

```
cd ~/magento2
bin/magento setup:static-content:deploy
```

Alternatively you can deploy only the static content for a single theme:

```
bin/magento setup:static-content:deploy --theme=Magento/luma en_US
```

Or for a single language:

```
bin/magento setup:static-content:deploy --language=en_US
```

*A secure, random Magento admin URL will be created for you and printed. Bookmark it for future access.*

Congratulations, Magento 2 is installed on your Hypernode!

### Want to Install Sample Data Too?

Login at the [Magento Marketplace](https://marketplace.magento.com/customer/account/) with your account. Go to the top right => My Profile => Under Marketplace => Access Keys. Create a new access key. Copy your public key (username) and private key (password).

```
cd ~/magento2
composer update
```

Enter your public and private key when asked for user and password.

When asked to save to a location, the default is fine.

```
ln -fs ~/.composer/auth.json var/composer_home/
```

This is required due to a bug: <https://github.com/magento/magento2/issues/2523>

```
bin/magento sampledata:deploy
```

This action will take about 10-15 minutes:

```
bin/magento setup:upgrade
```

## Configure Your Magento 2 Cron

After installing Magento, you can install the Magento crons by by running:

```
bin/magento cron:install
```

## Troubleshooting

- I’m getting the error:
  `PHP Parse error: syntax error, unexpected '.' in /data/web/magento2/vendor/magento/framework/ObjectManager/Factory/AbstractFactory.php on line 93`
  This is caused by the php version. Upgrade from php5 to php7 as not all vendor libraries are php5 compatible anymore.

>

- Web Setup Wizard is not visible:
  Check/Recreate the symlinks on your Hypernode:

```
mv /data/web/public /data/web/public_OLD
mkdir /data/web/public
ln -fs /data/web/magento2/pub/* /data/web/public
ln -fs /data/web/magento2/setup/ /data/web/public/
cd ~/magento2/
magerun2 cache:flush
```

- I’m getting `out-of-memory` errors:
  If you are running on a Start plan: Upgrade to a bigger hypernode with more memory available.
  If this happens while you are running a setup:static-content:deploy: Try deploying static content per language or per theme rather then all at once.
