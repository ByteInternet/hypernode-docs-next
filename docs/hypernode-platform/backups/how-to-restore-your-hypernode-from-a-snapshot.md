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

# How to Restore Your Hypernode From a Snapshot

```{important}
	Snapshots are only available for the Hypernode **Falcon** and **Eagle** products. For Pelican and Jackal products, please use the [External Backups](./how-to-restore-your-hypernode-from-external-backups).
```

**Some hands-on experience is required! If you have never used the command line, please contact **[**one of our partners**](https://www.hypernode.com/partners/)** to get some assistance.**

## What are Snapshot Backups?

To protect against accidental data loss, your Hypernode uses snapshot technology to create backups. A snapshot is a saved state of the `/data` device at a given moment in time. Since the `/data` drive contains both the files and database, a snapshot provides you easy access to both.
Thanks to cloud technology, this snapshot can be converted into a virtual device which we can attach to your Hypernode. Once attached, this backup becomes available under `/data/backup/current` and you can easily access the data stored in the backup.

## Attaching a Snapshot Backup

By using the following command you attach the most recent snapshot to your node:

```bash
hypernode-systemctl attach_backup
```

The backup snapshot is automagically detached 24 hours after you attached it. We do this as the backup also contains a second MySQL instance running so you’ll lose some resources while it is attached. Please contact Support if you want the snapshot detached earlier, to save on resources.
Of course you can simply reattach the backup again if you still need access to the data.

### Older Backups

The `attach_backup` command will default to using the most recently created snapshot. If you wish to attach an older snapshot, you will need to provide the specific Backup ID of the snapshot you wish to access. You can list the available backups, and the associated dates, using the following command:

```bash
hypernode-systemctl list_backups
```

This will show you a list of all the available backups, when they were created and how long they'll still be available.

If you have an [SLA Standard](../../hypernode-platform/backups/hypernode-backup-policy.md#sla-standard) you can attach this backup directly by providing the Backup ID to the `hypernode-systemctl attach_backups` command, as shown in the example below:

```session
app@xiobly-example-magweb-cmbl:~$ hypernode-systemctl list_backups
Backup ID                             Type      Created at                 Expires at
fbe78356-1d19-42ad-9fe2-f9e433ec8021  periodic  2023-02-22T16:17:40+01:00  2023-03-22T16:17:40+01:00
4e073707-b6ec-4762-8c24-ea3fe6b7bfc8  periodic  2023-03-01T21:16:32+01:00  2023-03-29T22:16:32+02:00
f6b68279-2ab4-4844-8afb-3efc36764311  periodic  2023-03-08T22:08:42+01:00  2023-04-05T23:08:42+02:00
d8eba410-dd7d-4d5d-a963-6667c27c7f75  periodic  2023-03-15T11:09:12+01:00  2023-04-12T12:09:12+02:00
f696166b-db65-480c-9702-d897e7535e47  periodic  2023-03-17T05:09:19+01:00  2023-03-24T05:09:19+01:00
81776877-0754-4323-bedb-892472c73086  periodic  2023-03-17T23:09:37+01:00  2023-03-24T23:09:37+01:00
696dcf49-a888-4e4f-8772-c660357f0d6e  periodic  2023-03-18T17:12:37+01:00  2023-03-25T17:12:37+01:00
45c33da8-097b-4ef1-b619-d70f4b8e5abc  periodic  2023-03-19T11:09:00+01:00  2023-03-26T12:09:00+02:00
1436d2f6-9ef2-4c53-a770-6aca1a986b4b  periodic  2023-03-21T05:08:34+01:00  2023-04-18T06:08:34+02:00
5f8d364f-3c8b-4c5f-8321-e6a6a1dc593c  periodic  2023-03-21T17:12:36+01:00  2023-03-22T17:12:36+01:00
1c231a08-503e-413c-867b-0a40998a8b3f  periodic  2023-03-21T23:10:16+01:00  2023-03-29T00:10:16+02:00
2df233ba-fd4d-494b-8212-8ef968809cd3  periodic  2023-03-22T05:08:38+01:00  2023-03-23T05:08:38+01:00
08d6b5ee-a970-4dbe-ab5e-692bac37f176  periodic  2023-03-22T11:09:25+01:00  2023-03-23T11:09:25+01:00
app@xiobly-example-magweb-cmbl:~$ hypernode-systemctl attach_backup 696dcf49-a888-4e4f-8772-c660357f0d6e
Attach backup job posted, see hypernode-log (or livelog) for job progress. The backup will appear in /data/backup/ once attached
```

If you have an SLA Basic and need to access an older snapshot, you can request it be attached via the Control Panel, using the steps bellow:

1. Log in to the Control Panel and select the Hypernode whos snapshot you want to attach.
1. Click Backups in the sidebar to go to the backup page.
1. Fill in and submit the form.

Our support team will now manually attach the backup to your Hypernode, and inform you when it has become available. Please note that [a fee may apply](./hypernode-backup-policy.md#requesting-older-snapshots) for customers with an SLA Basic.

```{important}
Our support team is only available during business hours (Amsterdam/Netherlands time). If you need an older snapshot to be attached manually outside of business hours, please file an [Hypernode Emergency Support Request](../../about-hypernode/support/emergency-support-outside-office-hours.md)
```

## Restore a Database From a Snapshot

To ease accessing the data from a database snapshot, a second MySQL instance will become available after attaching a snapshot. This service runs on port 3307, instead of 3306. You can connect to this backup instance using your regular MySQL tools.

### Create a Database Dump

To create a database dump from the backup instance, connect to port 3307 with the mysqldump utility and create a dump. In the example below we create an export of the `example_preinstall` database, and save a compressed version of this dump.

```bash
mysqldump -P 3307 example_preinstall | gzip > /data/web/backup.sql.gz
```

While attaching a snapshot to your Hypernode does not require any resources, creating a database dump does require CPU, so please keep this in mind when doing so.

### Directly Importing a Snapshot to your Production Database

It's possible to create a dump of the database snapshot and import this into the production database straight away. Please note this will overwrite all data in your production database, so exercise caution before running these commands. Consider making a backup of your production database first, or importing the data to a secondary database and changing your configuration to use that database instead. We also advise to set your site to maintenance mode and disabling crons while importing, to prevent corruption or crashes.

In the example below we import the `example_preinstall` database from the backup instance into the production database with the same name. If you wish to import the backup into a different database, simply change the second `example_preinstall` in the example command. Please note that you will have to [create this database](../../hypernode-platform/mysql/how-to-use-mysql-on-hypernode.md#how-to-create-a-new-database) yourself before you can import to it.

```bash
mysqldump -P 3307 example_preinstall | mysql example_preinstall
```

## Restore a File Backup From a Snapshot

After a snapshot has been attached it will become available in `/data/backup/current/web`. This folder will contain an exact copy of your homedir, including your application, nginx configuration, deployment files, and more.

To restore these files, simply copy them from `/data/backup/current` to your `public/` or `magento2/` directory.

Assuming the environment has the default Magento root directory setup you can restore the file backup with the following commands. If you have an alternative setup, you should change the Magento root directory in the commands below:

**Magento 1**

```bash
mv /data/web/public /data/web/public_backup         # Rename the magento root directory so you still have a backup of the files
cp -R /data/backup/current/web/public /data/web/    # Copy the files from the backup to the new public directory
```

**Magento 2**

```bash
mv /data/web/magento2 /data/web/magento2_backup     # Rename the magento root directory so you still have a backup of the files
cp -R /data/backup/current/web/magento2 /data/web/  # Copy the files from the backup to the new public directory
```
