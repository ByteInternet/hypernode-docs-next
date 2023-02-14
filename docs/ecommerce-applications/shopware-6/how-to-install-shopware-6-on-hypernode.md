---
myst:
  html_meta:
    description: Shopware 6 requires a Hypernode Professional S hosting plan or larger.
      We explain how you can setup the latest version of Shopware 5 on Hypernode.
    title: 'How to install Shopware 6 on Hypernode? '
redirect_from:
  - /en/ecommerce/shopware/how-to-install-shopware-6-on-hypernode/
  - /knowledgebase/how-to-install-shopware-6-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/ecommerce/shopware/how-to-install-shopware-6-on-hypernode/ -->

# How to Install Shopware 6 on Hypernode

This article will explain how you can setup the latest version of Shopware 6 on Hypernode as easy as possible. Shopware 6 cannot be installed on the old Grow plans.

## Upgrade Your PHP Version

Shopware 6 need at least PHP version 7.4 to be able to run. So the first thing to do is upgrade your PHP version to 7.4 with the following command:

```bash
hypernode-systemctl settings php_version 7.4
```

## Change the MySQL Version to 5.7

Shopware 6 needs MySQL 5.7 to be able to run. You can change the MySQL version by running the following command:

```bash
hypernode-systemctl settings mysql_version 5.7
```

## Install Node.js v10.16

```bash
hypernode-systemctl settings nodejs_version 10
```

## Two Ways to Install Shopware 6

There are two ways to install Shopware 6: either by using the pre-install or doing it manually. See below for the two options. *Please note: you only have to use one of the two options to install Shopware 6.*

### Download and Install Shopware 6 Using the Pre-install

On Hypernode we offer an easy way to install Shopware 6 using one of our pre-install images. Use the following command to install Shopware 6.

```bash
hypernode-systemctl preinstall shopware_6
```

### Download and Install the Latest Version of Shopware 6

Download the latest Shopware 6 version to the public folder from the [Shopware website](https://www.shopware.com/en/download/#shopware-6) by right clicking on "Download for free" click on "Copy Link Address" and paste the link after the `wget` command below.

```bash
mkdir shopware
cd shopware
wget https://releases.shopware.com/sw6/install_6.0.0_ea2_1571125323.zip

# Unzip the downloaded .zip file
unzip install_6.0.0_ea2_1571125323.zip

# Enable secure document root
cd ~
rm -rf /data/web/public
ln -s /data/web/shopware/public/ /data/web/public
```

## Install Shopware 6

Now open your browser and browse to [https://APPNAME.hypernode.io/recovery/update/index.php](https://APPNAME.hypernode.io/recovery/install/index.php). At this point you can follow the guide through your browser. Make sure to fill in the right details at the **Configure database**:

- Database server: localhost
- Database user: app
- Database password: run `cat ~/.my.cnf` in your terminal and copy that password.
- Database name: Select your database
- Select "new database", and pick a name you like
- Fill in the **Basic shop set-up** how you see fit.

**Done!** You’ve now successfully installed Shopware 6.

**Demo data**
If you’d like you could install demo data as well. To do this you’ll need to login the backend: [http://APPNAME.hypernode.io/admin/](http://APPNAME.hypernode.io/backend/) with the credentials you entered during the step: Basic shop set-up at the installation. At your first login you’ll see the “First Run Wizard”, make sure to install the Demo data at the “Demo data” menu.
