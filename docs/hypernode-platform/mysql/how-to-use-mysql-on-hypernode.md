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

This article explains how to use MySQL on Hypernode, from finding your credentials, whitelisting your IP address to using PHPMyAdmin.

## Finding Your Credentials

Your MySQL credentials are stored in the homedir of application user.

You find them in the file `.my.cnf` located in `/data/web`.

```nginx
cat ~/.my.cnf
```

```nginx
[client]
user = app
password = JlogA1Sws6XMHmAj7QlP9vpfjlprtpE5
host = mysqlmaster.example.hypernode.io
```

## What You Should Know

- There is no predefined database, so you should create your own.
- The `app`user is the local superuser. This means you can (among other things):
  - Can create your own databases;
  - Create users;
  - Define views and triggers.
- If you want to use a GUI to work on your database we recommend using a local GUI ([HeidiSQL](../../best-practices/database/how-to-use-heidisql-on-hypernode.md)) instead of an online GUI ([PHPMyAdmin](../mysql/how-to-use-phpmyadmin.md)).

## Whitelisting Your IP Address

Port 3306 is fire-walled on all Hypernodes to prevent hackers and bruteforces from connecting to your MySQL instance. That's why if you want to externally connect to MySQL on the Hypernode, you’ll need to add a whitelisting entry first.

### Whitelist via the hypernode-systemctl CLI Tool

First check which IP addresses have been whitelisted already, if any.

```nginx
hypernode-systemctl whitelist get
```

### Adding to Whitelist

To add more values to your whitelists you can run the following. Please note that descriptions are optional:

```nginx
hypernode-systemctl whitelist add database 1.2.3.4 --description "my description"
```

### Removing From Whitelist

To remove values from your whitelists you can run the following:

```nginx
hypernode-systemctl whitelist remove database 1.2.3.4
```

### Whitelist via Your Service Panel

Only our Service Panel users have the option to whitelist an IP via the Service Panel.

1. Log on to your [Service Panel](https://auth.byte.nl).
1. Select your Hypernode.
1. Go to `Instellingen` > `Externe database toegang`.
1. Add the IP addresses to the firewall whitelist.

## How to Connect to MySQL

### Use the Command Line Shell on the Production Node

Because we’ve provided a `~/.my.cnf`, you’re all set to go.

Just type `mysql` and you’re in.

```nginx
mysql
```

### Use the Command Line Shell From a Remote Host

Use your credentials to connect like so:

```nginx
mysql --host=mysqlmaster.example.hypernode.io --user=app --password=mypassword
```

### Using HeidiSQL/PHPMyAdmin to Connect to MySQL

Read the following articles on how to use both HeidiSQL and PHPMyAdmin for Hypernode:

- Using HeidiSQL
- Using PHPMyAdmin

### Using an SSH Tunnel to Circumvent Firewalls

If you are blocked by a firewall, you can tunnel the remote MySQL service to your local computer (Mac or Linux).

Use this command:

```nginx
ssh -NL 3306:mysqlmaster:3306 app@example.hypernode.io
```

Voila, now your Hypernode database is reachable through localhost port 3306!

## Creating a MySQL Back-Up

### Using Magerun

Use the following command using SSH:

```nginx
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

To upgrade your MySQL version you can use[the hypernode-systemctl tool](../tools/how-to-use-the-hypernode-systemctl-cli-tool.md#mysql) through the command line.

```nginx
hypernode-systemctl settings mysql_version --value 5.7
```

### How to Create a New Database

To create a new database, we’ll login using the MySQL client and drop the database using the command line.

```nginx
>DATABASE="new_database"
mysql -e "CREATE DATABASE IF NOT EXISTS $DATABASE"
```

Voila! If the database was not already present, you just created a new database.

### How to Remove an Old Database

Removing (aka drop) a database is as easy as creating a database, but some caution is required:

To prevent incorrect deletion of database that are still in use, ensure yourself:

- The database is not used anymore by checking it’s content.
- The database is not defined in your application configuration anymore.
  (IE: Check the `local.xml` and/or your `wp-config.php).`
- You created a backup to ensure yourself you are able to restore the database if necessary.

When you are 100% sure it is safe to delete the database, issue the following command:

```nginx
DATABASE="old_database"
mysql -e "DROP DATABASE $DATABASE"
```

And **POOF!** Now your database is gone.

### How to Truncate a Database Table

To truncate a database table, use the same caution as with dropping a database.
If you truncate a database table, all records are removed but the table structure is saved for further use. This is a hard reset of your database table: It wipes out any record the table contains.

After you ensured yourself it is safe to delete all records of the table, use the following command:

```nginx
DATABASE="magento"
TABLE="core_url_rewrite"
mysql "$DATABASE" -e "TRUNCATE TABLE $TABLE"
```

### Changing Your MySQL 5.6 Password

Login to your MySQL server via the following command:

```nginx
mysql
```

This will get you into the MySQL prompt. Select the database which holds user accounts, here it’s called mysql;

```nginx
use mysql;
```

Now change the password for a given user account using this command:

```nginx
update user set password=PASSWORD('newpassword') where user='username';
```

Let’s assume here that your username is ‘trial’ and your new password is ‘hypernode’. Your actual command would look like this:

```nginx
update user set password=PASSWORD('hypernode') where user='trial';
```

Now your password is changed in the database, but they haven’t filtered into memory yet. Change that by typing:

```nginx
flush privileges;
```

Your password has been updated. There’s no need to restart the MySQL demon. Exit the MySQL with

```nginx
exit;
```

## How to Upgrade Your MySQL Version

### Upgrading to MySQL 5.7

**Please note that once you have upgraded the MySQL version on your Hypernode, you won't be able to downgrade it.**

You can upgrade the MySQL version on your Hypernode from 5.6 to 5.7 with the following command:

```nginx
hypernode-systemctl settings mysql_version 5.7
```

You can then check with `livelog` when the process has finished and your MySQL version has been upgraded.

### Changing Your MySQL 5.7 Password

Login to your MySQL server via the following command

```nginx
mysql
```

This will get you into the MySQL prompt. Select the database which holds user accounts, here it’s called mysql;

```nginx
use mysql;
```

Now change the password for a given user account using this command, in this case the `app` user:

```nginx
update user set authentication_string=password('newpassword') where user='app';
```

Now your password is changed in the database, but they haven’t filtered into memory yet. Change that by typing:

```nginx
flush privileges;
```

Your password has been updated. There’s no need to restart the MySQL demon. Exit the MySQL with

```nginx
exit;
```

Remember to update your `~/.my.cnf` with your new password so you could easily login your MySQL-CLI without entering the password each time.

### Upgrading to MySQL 8.0

**Please note that once you have upgraded the MySQL version on your Hypernode, you won't be able to downgrade it.**

Before you can upgrade to MySQL 8.0 you first need to upgrade the MySQL version to 5.7 and wait for this process to finish. Once You can upgrade the MySQL version on your Hypernode from 5.7 to 8.0 with the following command:

```nginx
hypernode-systemctl settings mysql_version 8.0
```

You can then check with `livelog` when the process has finished and your MySQL version has been upgraded.
