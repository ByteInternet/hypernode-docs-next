---
myst:
  html_meta:
    description: To restore your Hypernode from the external backup, please follow
      the instructions mentioned in this article.
    title: How to restore your Hypernode from the external backup? | Backups
---

# How to Restore Your Hypernode From the External Backup

```{tip}
It's often much faster to restore your Hypernode from a snapshot. If you are using a Hypernode **Falcon** or **Eagle** product, we highly recommend you use [Snapshot Backups](./how-to-restore-your-hypernode-from-a-snapshot) instead.
```

**Some hands-on experience is required! If you have never used the command line, please contact **[**one of our partners**](https://www.hypernode.com/partners/)** to get some assistance.**

Your Hypernode is backed up daily to an external server. This page explains how you can use that backup to restore specific files or database content.

# Accessing Backups

Please contact our support department if you want to access an external backup. We will prepare the data onto the server so you can restore the data yourself. Be sure to indicate if you need a backup of a file, database or both, and from before what date and time you require the backup to be.

# Restore from a Prepared Backup

## Restore from a Prepared Database Backup

When we prepare a database backup, you’ll find a database dump compressed with gzip.

The name of this backup has the format `database_name_date_timezone.sql.gz`

To restore this backup you can use either magerun or use the MySQL client utility:

Using magerun:

First unzip the back-up file:

```bash
gunzip database_name_01-01-2018.sql.gz
```

For Magento 1:

```bash
magerun db:import --root-dir=~/public database_name_01-01-2018.sql
```

For Magento 2:

```bash
magerun2 db:import --root-dir=~/magento2 database_name_01-01-2018.sql
```

Using MySQL client:

```bash
zcat database_name_01-01-2018.sql.gz | mysql database_name
```

And then wait until the database is fully imported.

*This might take a while for large databases, so get yourself some coffee in the meantime.*

### Restore from a Prepared File Backup

When you request a file backup, we create a directory in your homedir in which we restore from a certain point in time.

To restore this backup, remove the old file or directory and copy the file(s) and/or directories in place in your `/data/web/public` directory.

IE: if you need to restore the var directory, use the command:

```bash
rm -rvf /data/web/public/var/ && mv restore/var /data/web/public/
```

If you need some visual assistance, you can use mc ([midnight commander](http://linuxcommand.org/lc3_adv_mc.php)).
