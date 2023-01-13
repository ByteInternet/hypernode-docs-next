---
myst:
  html_meta:
    description: To restore your Hypernode from a snapshot, instant or an older backup,
      please follow the instructions mentioned in this article.
    title: How to restore your Hypernode from a snapshot? | Backups
redirect_from:
  - /en/hypernode/backups/how-to-restore-your-hypernode-from-a-backup/
  - /knowledgebase/restore-hypernode-backup/
---

<!-- source: https://support.hypernode.com/en/hypernode/backups/how-to-restore-your-hypernode-from-a-backup/ -->

# How to Restore Your Hypernode From a Snapshot

**Some hands-on experience is required! If you have never used the command line, please contact**[**one of our partners**](https://www.hypernode.com/partners/)**to get some assistance.**

To restore your Hypernode from a backup use the steps below.

## Restore Using Snapshots

On Amazon (AWS) and Combell OpenStack we use snapshots to create backups. A snapshot is a saved state of the `/data` device at a given moment in time. We can use this to create a static copy of that given state in time and transform this to a virtual device which we can attach to your Hypernode. Once attached, this device is mounted under `/data/backup` and you can easily restore your files by copying them from this file system.

By using the following command you attach the latest available snapshot to your node:

`hypernode-systemctl attach_backup`

The backup snapshot is automagically detached/unmounted, before the backups are made. There is a second MySQL instance running so you’ll lose some resources while it is attached. Please contact Support if you want the snapshot detached earlier, to save on resources.

### Instant and Older Backups

**Do you need access to backups older than one day or do you want the ability to create instant backups? These functionalities are part of the SLA Standard add-on, which is available for all Hypernodes. Please see [this article for more information about the difference between SLA Basic and SLA Standard](../../hypernode-platform/backups/hypernode-backup-policy.md#sla-standard).**

### Restore a Database From Snapshots

#### Create a Database Dump

To create a database dump from the backup instance, connect to port 3307 with the mysqldump utility and create a dump. Replace *`DATABASE_NAME`* with the name of YOUR database in the commands below:

```nginx
mysqldump DATABASE_NAME -P 3307 | gzip > /data/web/DATABASE_NAME.sql.gz
```

When the export is created, a backup file can be found in `/data/web` named after the database, with the `.sql.gz` extension.

#### Dump the Data From the Backup MySQL Instance Into the Production Database

To restore the backup and immediately import it in the production database use the following command, again, replace *magento2* with the name of your database.

```nginx
mysqldump DATABASE_NAME -P 3307 | mysql DATABASE_NAME
```

While attaching a snapshot to your Hypernode does not require any resources, creating a database dump does require CPU, so please keep this in mind when doing so.

### Restore a File Backup From a Snapshot

To restore your files, copy the files from `/data/backup/current` to your `public/` or `magento2/` directory.

\*\*Assuming the environment has the default Magento root directory setup you can restore the file backup with the following commands. If you have an alternative setup, you should change the Magento root directory in the commands below:

**Magento 1**

```nginx
mv /data/web/public /data/web/public_backup ##Rename the magento root directory so you still have a backup of the files
cp -R /data/backup/current/web/public /data/web/ ##Copy the files from the backup to the new public directory
```

**Magento 2**

```nginx
mv /data/web/magento2 /data/web/magento2_backup ##Rename the magento root directory so you still have a backup of the files
cp -R /data/backup/current/web/magento2 /data/web/ ##Copy the files from the backup to the new public directory
```

## Restore on DigitalOcean

### Restore a Database Backup on DigitalOcean

When we restore a database backup, you’ll find a database dump compressed with gzip.

The name of this backup has the format `database_name_date_timezone.sql.gz`

To restore this backup you can use either magerun or use the MySQL client utility:

Using magerun:

First unzip the back-up file:

```nginx
gunzip database_name_01-01-2018.sql.gz
```

For Magento 1:

```nginx
magerun db:import --root-dir=~/public database_name_01-01-2018.sql
```

For Magento 2:

```nginx
magerun2 db:import --root-dir=~/magento2 database_name_01-01-2018.sql
```

Using MySQL client:

```nginx
zcat database_name_01-01-2018.sql.gz | mysql database_name
```

And then wait until the database is fully imported.

*This might take a while for large databases, so get yourself some coffee in the meantime.*

### Restore a File Backup on DigitalOcean

When you request a file backup on a Hypernode at DigitalOcean, we create a directory in your homedir in which we restore from a certain point in time.

To restore this backup, remove the old file or directory and copy the file(s) and/or directories in place in your `/data/web/public` directory.

IE: if you need to restore the var directory, use the command:

```nginx
rm -rvf /data/web/public/var/ && mv restore/var /data/web/public/
```

If you need some visual assistance, you can use mc ([midnight commander](http://linuxcommand.org/lc3_adv_mc.php)).
