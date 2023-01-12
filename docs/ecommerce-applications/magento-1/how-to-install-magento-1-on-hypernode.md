---
myst:
  html_meta:
    description: Although Magento 1 has been End of Life since June 30 2020, it is
      still possible to host your Magento 1 store at Hypernode by using OpenMage.
    title: How to install Magento 1 on Hypernode?
redirect_from:
  - /en/ecommerce/magento-1/how-to-install-magento-1-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-install-magento-1-on-hypernode/ -->

# How to Install Magento 1 on Hypernode

Although Magento 1 has been End of Life since June 30 2020, it is still possible to host your Magento 1 store at Hypernode by using OpenMage. OpenMage is a free of charge fork of Magento 1, and allows store owners to continue the use of Magento 1 as a stable and secure eCommerce platform for the next years to come.

OpenMage can be installed by using their [documentation](https://www.openmage.org/magento-lts/install.html). Don't implement OpenMage on production nodes without testing OpenMage first on a [Development plan](../../hypernode-platform/tools/how-to-use-hypernode-development-plans.md).

Would you rather install the officially supported Magento 2? Installing Magento 2 on Hypernode can be done by following the steps in the article: [Installing Magento 2 on Hypernode](../../ecommerce-applications/magento-2/how-to-install-magento-2-on-hypernode.md)

## Cleaning up existing installed software

Before you can install Magento, you first need to ensure you've removed any and all applications installed in /data/web/magento2, or /data/web/public. More information on how to do so can be found in [our documentation about deleting your Magento installation](../../ecommerce-applications/magento-1/how-to-remove-your-magento-1-x-installation.md).

## Install our Pre-installed Magento 1 version with ONE command

Using the command `hypernode-systemctl preinstall`, you can automatically install a supported application. The current supported applications are `magento_1`, `magento_2`, `shopware_5`, `shopware_6`, `akeneo3.2` and `akeneo4.0`. By adding `--sample-data` as an argument we install the version with sample data . Take a look at the `livelog` command to check the progress on the update job.

Please be aware that this does not set the general Hypernode settings (php, mysql) to the supported values. This still needs to happen manually. In addition, for Magento 1, make sure the `/data/web/public` folder is empty.

```bash
# Start the preinstall
app@example.hypernode.io:~$ hypernode-systemctl preinstall magento1 --sample-data
Preinstall magento1 with sample data job posted, see hypernode-log (or livelog) for job progress.

# Check the preinstall progress
app@example.hypernode.io:~$ livelog

# Check out your new installation
app@example.hypernode.io:~$ ls -l /data/web/public
```

## Installing Magento 1 manually

### Activate Magento 1 Mode

By default, your Hypernode is configured to use Magento 2. If you wish to instead use Magento 1, disable the [Magento 2 Mode](../../ecommerce-applications/magento-2/how-to-install-magento-2-on-hypernode.md#activate-magento-2-mode).

This disables the configuration that is only needed for Magento 2. To do this, run the following command

```bash
 rm ~/nginx/magento2.flag
```

You will also need to [configure your vhost](../../hypernode-platform/nginx/hypernode-managed-vhosts.md) to use the magento 1 configuration.

```bash
hypernode-manage-vhosts --type=magento1 example.hypernode.io
```

If you are already testing on another vhost, you will need to change it's type too.

### Create a New Database

The first step should be to create a database. You connect to your database with the following command:

```bash
 mysql
```

Create a database by using the next command:

```mysql
CREATE DATABASE <database_name>;
```

After this you exit the MySQL client and write down your database name so you can use it with the installer later. You will also need your database settings. You can see these with the following command:

```bash
cat ~/.my.cnf
```

This will show you the username, password, and host used on your Hypernode. Together with the database you created above you now have all the information needed to install Magento 1

### Installing Magento 1 using magerun

- To install the latest Magento you’ll have to go to your **public** directory: cd /data/web/public
  Use the following command to install Magento through `magerun`:

```bash
magerun install
```

- Choose which version you wish to install. The first option \[1\] is the most recent version of Magento. You may also choose to install the openmage LTS version. Press “Enter”.
- Insert the installation folder. This should be /data/web/public, and press ENTER. magerun will now download the files of the installation.
- Enter your database credentials:
  - database host
  - database username
  - database password
  - database name
  - database port
  - table prefix (optional)
- Press “y” or “n” depending on whether you want to install sample data.
  If you told the script you’d like to have some sample data, better grab a cup of coffee or tea as this might take a while...
- You’re asked to fill in some information to finish the installation.
  You have to submit the following information:
  - session save
  - admin frontname
  - default currency code
  - locale code
  - timezone
  - admin username
  - admin password
  - admin’s firstname
  - admin’s lastname
  - admin’s email
  - base url
- After this, the script will install Magento for you.
- When the installation is finished, [flush your caches](../../ecommerce-applications/magento-1/how-to-flush-the-magento-1-x-caches.md).
- When you’re asked if you want to write the base-url to your .htaccess file, press “n” and the script will reindex all data in your shop.
- The installation is complete.

You’re presented with all the checks the script did to ensure Magento was successfully installed on your Hypernode.

Your shop will now be visible through your Hypernode URL.

### Configure Redis as Cache Backend

Follow the steps mentioned in the article [Configure Redis](../../ecommerce-applications/magento-1/how-to-configure-redis-for-magento-1.md) to configure Redis as your cache backend.

### Optional: Change Your Base URL

If you wish to change your Base URL, please follow our documentation on changing the [Base URL in Magento 1](../../ecommerce-applications/magento-1/how-to-change-the-base-url-in-magento-1-x.md).

### Optional: Configure Lesti::FPC

If you’d like to use Lesti::FPC on Hypernode, please follow the steps mentioned in article [How to Configure Lesti::FPC](../../hypernode-platform/tools/how-to-configure-lesti-fpc.md).
