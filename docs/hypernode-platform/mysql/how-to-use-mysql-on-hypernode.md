---
myst:
  html_meta:
    description: This article explains how to use MySQL on Hypernode, from finding
      your credentials, whitelisting your IP address to using PHPMyAdmin.
    title: How to use MySQL on Hypernode?
redirect_from:
  - /en/hypernode/mysql/how-to-use-mysql-on-hypernode/
  - /knowledgebase/using-mysql-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/hypernode/mysql/how-to-use-mysql-on-hypernode/ -->

# How to Use Mysql on Hypernode

This article explains how to use MySQL on Hypernode, from finding your credentials, allowlisting your IP address, to using PHPMyAdmin.

## Finding Your Credentials

Your MySQL credentials are stored in the homedir of application user.

You find them in the file `.my.cnf` located in `/data/web`.

```bash
cat ~/.my.cnf
```

```ini
[client]
user = app
password = JlogA1Sws6XMHmAj7QlP9vpfjlprtpE5
host = mysqlmaster.example.hypernode.io
```

## What You Should Know

- There is no predefined database, so you should create your own.
- The `app` user is the local superuser. This means you can (among other things):
  - Create your own databases;
  - Create users and manage passwords;
  - Define views and triggers.
- If you want to use a GUI to work on your database we recommend using a local GUI (Such as [HeidiSQL](../../best-practices/database/how-to-use-heidisql-on-hypernode.md) on Windows) instead of an online GUI ([PHPMyAdmin](../mysql/how-to-use-phpmyadmin.md)).

## Whitelisting Your IP Address

Port 3306 is firewalled on all Hypernodes to prevent hackers and bruteforces from connecting to your MySQL instance. That's why if you want to externally connect to MySQL on the Hypernode, you’ll need to add the remote IP address to the allowlist first.

### Allow an IP via the hypernode-systemctl CLI tool

First check which IP addresses have been whitelisted already, if any.

```console
hypernode-systemctl whitelist get
```

### Adding to the Allowlist

To add more values to your allowlist you can run the following. Please note that descriptions are optional:

```console
hypernode-systemctl whitelist add database 203.0.113.4 --description "my description"
```

### Removing From the Allowlist

To remove IP addresses from your allowlists you can run the following:

```console
hypernode-systemctl whitelist remove database 203.0.113.4
```

### Manage the Allowlist via the Control Panel

It's also possible to whitelist an IP address via the Control Panel

1. Log on to the [Control Panel](https://my.hypernode.com).
1. Select your Hypernode.
1. Select `Allowlist` from the menu.
1. Add the IP addresses to the database allowlist.

## How to Connect to MySQL

### Use the Command Line Shell on the Production Node

Because we’ve provided a `~/.my.cnf`, you’re all set to go.

Just type `mysql` and you’re in.

```console
mysql
```

### Use the Command Line Shell From a Remote Host

Use your credentials to connect like so:

```console
mysql --host=mysqlmaster.example.hypernode.io --user=app --password=mypassword
```

Please note you will need to add the remote host's IP address to the allowlist first, as described above.

### Using HeidiSQL/PHPMyAdmin to Connect to MySQL

Read the following articles on how to use both HeidiSQL and PHPMyAdmin for Hypernode:

- Using [HeidiSQL](../../best-practices/database/how-to-use-heidisql-on-hypernode.md
- Using [PHPMyAdmin](../mysql/how-to-use-phpmyadmin.md)

### Using an SSH Tunnel to Circumvent Firewalls

If you are blocked by a firewall, you can create a temporary tunnel between the remote MySQL service and your local computer.

Use this command:

```console
ssh -NL 3306:mysqlmaster:3306 app@example.hypernode.io
```

Voila, now your Hypernode database is reachable through localhost port 3306!

## Creating a MySQL Back-Up

### Using Magerun

Use the following command using SSH:

```console
magerun db:dump -n -c gz -s @stripped
```

This will create a compressed SQL file suitable for importing using either Magerun or MySQLclient. The dump will exclude any logfiles or temporary import tables.

### Using HeidiSQL

You should consider using Magerun (see above), but you could use HeidiSQL to create a database dump.

1. Start HeidiSQL.
1. Connect to your node.
1. Use `Tools` > `Export database as SQL`.
1. In the left pane, choose the Magento database.
1. Choose a filename to export to.
1. Choose appropriate options, notably `data`.
1. Press Export.

### Using phpMyAdmin

1. Go To domain.hypernode.io/phpmyadmin
1. Click on “Databases” and select the database.
1. Click on “Export”.
1. Click on “Go” and the export/backup will be available.

## Using MySQL

### How to Upgrade the MySQL Version

Hypernode offers several version of MySQL to be able to meet te requirements of several Magento, Shopware and Akeneo versions. For example, if you want to install Magento 2.4, you'd have to run MySQL 5.7 or 8.0.

To upgrade your MySQL version you can use [the hypernode-systemctl tool](../tools/how-to-use-the-hypernode-systemctl-cli-tool.md#mysql) through the command line.

```console
hypernode-systemctl settings mysql_version --value 5.7
```

### How to Create a New Database

To create a new database, we’ll login using the MySQL client and create the database using the command line.

```bash
DATABASE="new_database"
mysql -e "CREATE DATABASE IF NOT EXISTS $DATABASE"
```

Voila! If the database was not already present, you just created a new database.

### How to Remove an Old Database

Removing (aka drop) a database is as easy as creating a database, but some caution is required:

To prevent incorrect deletion of database that are still in use, ensure yourself:

- The database is not used anymore by checking it’s content.
- The database is not defined in your application configuration anymore.
  (IE: Check the `local.xml`, `env.php`, and/or your `wp-config.php).
- You created a backup to ensure yourself you are able to restore the database if necessary.

When you are 100% sure it is safe to delete the database, issue the following command:

```bash
DATABASE="old_database"
mysql -e "DROP DATABASE $DATABASE"
```

And **POOF!** Now your database is gone.

### How to Truncate a Database Table

To truncate a database table, use the same caution as with dropping a database.
If you truncate a database table, all records are removed but the table structure is saved for further use. This is a hard reset of your database table: It wipes out any record the table contains.

After you ensured yourself it is safe to delete all records of the table, use the following command:

```bash
DATABASE="magento"
TABLE="core_url_rewrite"
mysql "$DATABASE" -e "TRUNCATE TABLE $TABLE"
```

## Changing Your Password

How you change the database password depends on what version of MySQL you are running on your Hypernode.

### Changing Your Password on MySQL 5.6

Login to your MySQL server via the following command:

```console
mysql
```

This will get you into the MySQL prompt. In this example we change the password for the `app` user to `p4ssw0rd`

```mysql
SET PASSWORD FOR 'app'@'%' = PASSWORD("p4ssw0rd");
```

Your password has been updated. There’s no need to restart the MySQL demon. Exit the MySQL with

```mysql
exit;
```

### Changing Your Password on MySQL 5.7

Login to your MySQL server via the following command

```console
mysql
```

This will get you into the MySQL prompt. In this example we change the password for the `app` user to `p4ssw0rd`

```mysql
ALTER USER `app` IDENTIFIED BY 'p4ssw0rd';
```

Your password has been updated. There’s no need to restart the MySQL demon. Exit the MySQL with

```mysql
exit;
```

Remember to update your `~/.my.cnf` with your new password so you could easily login your MySQL-CLI without entering the password each time.

### Changing Your Password on MySQL 8.0

Login to your MySQL server via the following command

```console
mysql
```

This will get you into the MySQL prompt. In this example we change the password for the `app` user to `p4ssw0rd`

```mysql
ALTER USER `app` IDENTIFIED BY 'p4ssw0rd';
```

Your password has been updated. There’s no need to restart the MySQL demon. Exit the MySQL with

```mysql
exit;
```

Remember to update your `~/.my.cnf` with your new password so you could easily login your MySQL-CLI without entering the password each time.

## How to Upgrade Your MySQL Version

### Upgrading to MySQL 5.7

**Please note that once you have upgraded the MySQL version on your Hypernode, you won't be able to downgrade it.**

You can upgrade the MySQL version on your Hypernode from 5.6 to 5.7 with the following command:

```console
hypernode-systemctl settings mysql_version 5.7
```

You can then check with `livelog` when the process has finished and your MySQL version has been upgraded.

### Upgrading to MySQL 8.0

**Please note that once you have upgraded the MySQL version on your Hypernode, you won't be able to downgrade it.**

Before you can upgrade to MySQL 8.0 you first need to upgrade the MySQL version to 5.7 and wait for this process to finish. Once that is done, you can upgrade the MySQL version on your Hypernode from 5.7 to 8.0 with the following command:

```console
hypernode-systemctl settings mysql_version 8.0
```

You can then check with `livelog` when the process has finished and your MySQL version has been upgraded.
