---
myst:
  html_meta:
    description: Learn how to install the latest version of Shopware 6 on Hypernode
      with Composer, or how to set up Shopware 6.0.
    title: How to install Shopware 6 on Hypernode?
redirect_from:
  - /en/ecommerce/shopware/how-to-install-shopware-6-on-hypernode/
  - /knowledgebase/how-to-install-shopware-6-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/ecommerce/shopware/how-to-install-shopware-6-on-hypernode/ -->

# How to Install Shopware 6 on Hypernode

This article explains how you can set up Shopware 6 on Hypernode as easily as possible. It covers two situations:

- [Install the latest version of Shopware 6](#install-the-latest-version-of-shopware-6). Use this for new shops.
- [Install Shopware 6.0](#install-shopware-60). Use this only if you specifically need this older version.

## Install the Latest Version of Shopware 6

The latest versions of Shopware 6 are installed with Composer. The steps below are based on Shopware 6.7.

### Check the Requirements

Shopware 6.7 has the following requirements:

| Software | Required version                      | Recommended on Hypernode |
| -------- | ------------------------------------- | ------------------------ |
| PHP      | 8.2 or higher                         | 8.4                      |
| MySQL    | 8.0.22 or higher                      | 8.4                      |
| Node.js  | 20 or higher                          | 24                       |
| Composer | 2.2 or higher                         | 2.x                      |
| Redis    | 7.0 or higher (optional, for caching) | Redis 7                  |

For the full list of requirements, see the [Shopware system requirements](https://developer.shopware.com/docs/guides/hosting/).

### Upgrade Your PHP Version

Change the PHP version to PHP 8.4 with the following command:

```bash
hypernode-systemctl settings php_version 8.4
```

### Upgrade Your MySQL Version

Shopware 6.7 needs at least MySQL 8.0. You can check your current MySQL version with `mysql --version`. Upgrade to MySQL 8.4 with the following command:

```bash
hypernode-systemctl settings mysql_version --value 8.4
```

```{important}
You can only upgrade to MySQL 8.4 from MySQL 8.0, and you cannot downgrade your MySQL version afterwards. See [How to Use MySQL on Hypernode](../../hypernode-platform/mysql/how-to-use-mysql-on-hypernode.md) for the full upgrade path.
```

### Upgrade Your Node.js and Composer Versions

Shopware uses Node.js to build the administration and storefront. Change the Node.js version to 24 and make sure you use Composer 2:

```bash
hypernode-systemctl settings nodejs_version 24
hypernode-systemctl settings composer_version 2.x
```

Use `livelog` to check when the changes are applied.

### Create the Shopware Project

Create a new Shopware project in `/data/web/shopware` with Composer:

```bash
cd /data/web
composer create-project shopware/production shopware
```

This installs the latest stable version of Shopware 6. If you need a specific version, add it to the package name, for example `shopware/production:6.7.15.1`.

### Configure the Database Connection

Shopware reads its configuration from the `.env.local` file in the project folder. Look up the password of the `app` MySQL user:

```bash
cat ~/.my.cnf
```

Then create the `.env.local` file:

```bash
cd /data/web/shopware
cat > .env.local <<'EOF'
APP_ENV=prod
APP_URL=https://APPNAME.hypernode.io
DATABASE_URL=mysql://app:PASSWORD@mysqlmaster:3306/shopware
EOF
```

Replace `APPNAME` with the name of your Hypernode and `PASSWORD` with the password from `~/.my.cnf`. If the password contains special characters, such as `@`, `/` or `#`, [URL-encode](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding) these characters.

### Install Shopware

Run the Shopware installer. The `--create-database` option creates the `shopware` database for you:

```bash
cd /data/web/shopware
bin/console system:install --basic-setup --create-database
```

This creates the database tables, a default sales channel, and an admin user.

### Enable the Secure Document Root

The web root of Shopware is the `public` folder of the project. Point the Hypernode document root to this folder:

```bash
rm -rf /data/web/public
ln -s /data/web/shopware/public/ /data/web/public
```

Your shop is now available at `https://APPNAME.hypernode.io`.

### Log In to the Administration

Open `https://APPNAME.hypernode.io/admin` in your browser and log in with the default credentials:

- Username: `admin`
- Password: `shopware`

```{warning}
Change the password of the admin user directly after your first login.
```

**Done!** You've now successfully installed the latest version of Shopware 6.

For better performance, configure [Redis](./how-to-configure-redis-for-shopware-6.md) and [Varnish](./how-to-configure-varnish-for-shopware-6.md) for your shop.

## Install Shopware 6.0

The steps below explain how to install Shopware 6.0.

### Upgrade Your PHP Version

Shopware 6.0 needs at least PHP version 7.4 to be able to run. So the first thing to do is upgrade your PHP version to 7.4 with the following command:

```bash
hypernode-systemctl settings php_version 7.4
```

### Change the MySQL Version to 5.7

Shopware 6.0 needs MySQL 5.7 to be able to run. You can change the MySQL version by running the following command:

```bash
hypernode-systemctl settings mysql_version 5.7
```

### Install Node.js v10.16

```bash
hypernode-systemctl settings nodejs_version 10
```

### Two Ways to Install Shopware 6.0

There are two ways to install Shopware 6.0: either by using the pre-install or doing it manually. See below for the two options. *Please note: you only have to use one of the two options to install Shopware 6.0.*

#### Download and Install Shopware 6 Using the Pre-install

On Hypernode we offer an easy way to install Shopware 6 using one of our pre-install images. Use the following command to install Shopware 6.

```bash
hypernode-systemctl preinstall shopware_6
```

#### Download and Install Shopware 6.0 Manually

Download Shopware 6.0 to the public folder from the [Shopware website](https://www.shopware.com/en/download/#shopware-6) by right clicking on "Download for free" click on "Copy Link Address" and paste the link after the `wget` command below.

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

### Run the Shopware 6.0 Installer

Now open your browser and browse to `https://APPNAME.hypernode.io/recovery/update/index.php`. At this point you can follow the guide through your browser. Make sure to fill in the right details at the **Configure database**:

- Database server: localhost
- Database user: app
- Database password: run `cat ~/.my.cnf` in your terminal and copy that password.
- Database name: Select your database
- Select "new database", and pick a name you like
- Fill in the **Basic shop set-up** how you see fit.

**Done!** You’ve now successfully installed Shopware 6.0.

**Demo data**
If you’d like you could install demo data as well. To do this you’ll need to login the backend: `https://APPNAME.hypernode.io/admin/` with the credentials you entered during the step: Basic shop set-up at the installation. At your first login you’ll see the “First Run Wizard”, make sure to install the Demo data at the “Demo data” menu.
