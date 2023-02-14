---
myst:
  html_meta:
    description: Shopware 5 requires a Hypernode Professional S hosting plan or larger.
      We explain how you can setup the latest version of Shopware 5 on Hypernode.
    title: 'How to install Shopware 5 on Hypernode? '
redirect_from:
  - /en/ecommerce/shopware/how-to-install-shopware-5-on-hypernode/
  - /knowledgebase/how-to-install-shopware-5-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/ecommerce/shopware/how-to-install-shopware-5-on-hypernode/ -->

# How to Install Shopware 5 on Hypernode

Shopware 5 requires a Hypernode Professional S hosting plan or larger. This article will explain how you can setup the latest version of Shopware 5 on Hypernode as easy as possible.

- **TABLE OF CONTENTS**
  - [Upgrade Your PHP Version](#upgrade-your-php-version)
  - [Add the Shopware Nginx Config File](#add-the-shopware-nginx-config-file)
  - [Two Ways to Install Shopware 5](#two-ways-to-install-shopware-5)
    - [Download and Install Shopware 5 Using the Pre-install](#download-and-install-shopware-5-using-the-pre-install)
    - [Download and Install the Latest version of Shopware 5](#download-and-install-the-latest-version-of-shopware-5)
  - [Install Shopware 5](#install-shopware-5)

## Upgrade Your PHP Version

The latest version of Shopware 5 need at least PHP version 7.2 to be able to run. So the first thing to do is upgrade your PHP version to 7.2 with the following command:

```nginx
hypernode-systemctl settings php_version 7.2
```

## Add the Shopware Nginx Config File

To be able to host Shopware on Hypernode you need to add an nginx config file so the server knows where to find the Shopware installation. You can add the `server.shopware` config file according to our [documentation](how-to-host-shopware-on-hypernode.md#configuring-hypernode-for-shopware).

## Two Ways to Install Shopware 5

There are two ways to install Shopware 5: either by using the pre-install or doing it manually. See below for the two options. *Please note: you only have to use one of the two options to install Shopware 5.*

### Download and Install Shopware 5 Using the Pre-install

On Hypernode we offer an easy way to install Shopware 5 using one of our pre-install images. Use the following command to install Shopware 5.

```nginx
hypernode-systemctl preinstall shopware_5
```

### Download and Install the Latest version of Shopware 5

Download the latest Shopware 5 version to the public folder from the [Shopware website](https://www.shopware.com/en/download/#shopware-5) by right clicking on "Download for free" click on "Copy Link Address" and paste the link after the `wget` command below.

```nginx
cd ~/public/
wget https://releases.shopware.com/install_5.6.2_6cadc5c14bad4ea8839395461ea42dbc359e9666.zip
Unzip the downloaded .zip file
unzip install_5.6.2_6cadc5c14bad4ea8839395461ea42dbc359e9666.zip

```

## Install Shopware 5

Before you proceed with the installation you need to create a database for Shopware. In this example we name it "shopware", of course you can name it however you seem fit.

```nginx
echo "create database shopware" | mysql
```

Now open your browser and browse to `https://APPNAME.hypernode.io/recovery/install/index.php`.

At this point you can follow the guide through your browser. Make sure to fill in the right details at the **Configure database:**

- Database server: localhost
- Database user: app
- Database password: run `cat ~/.my.cnf` in your terminal and copy that password.
- Database name: Select your database

Now fill in the **Basic shop set-up** however you see fit.

**Done!** You've now successfully installed Shopware 5.

**Demo data**

If you'd like you could install demo data as well. To do this you'll need to login the backend: `http://APPNAME.hypernode.io/backend/` with the credentials you entered during the step: `Basic shop set-up` at the installation. At your first login you'll see the "First Run Wizard". Make sure to install the Demo data at the "Demo data" menu.

## Install the Shopware 5 cron

To install the default cronjob for Shopware 5 run crontab -e and add the following line:

```nginx
*/10 * * * * php /data/web/public/bin/console sw:cron:run
```
