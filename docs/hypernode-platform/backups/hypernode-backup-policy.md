---
myst:
  html_meta:
    description: Easily restore files, directories, and database tables with Hypernode's
      daily snapshots. Depending on your SLA, you get additional backup options.
    title: Hypernode Backup Policy | Secure and Automated
redirect_from:
  - /en/hypernode/backups/hypernode-backup-policy/
---

<!-- source: https://support.hypernode.com/en/hypernode/backups/hypernode-backup-policy/ -->

# Hypernode Backup Policy

On Amazon (AWS) and Combell OpenStack we use snapshots to create backups. When things go slightly wrong (ie. a product is accidentally deleted), you can go back in time to restore the appropriate database table, files or directories from the snapshot. Snapshots are easy to use, take up less time and there’s no need to upgrade your Hypernode if you don’t have enough disk space.

## Retention Times

Snapshots are made every day and saved for 7 days. We also save 1 backup per week for 3 weeks. This means you will have 4 weeks worth of backups.

Snapshots are rotated daily after the creation of a new backup. This implies that the backups that are older than 4 weeks will be automatically removed. To save storage costs, we do not keep additional backups older than 4 weeks, so please do not wait too long before requesting a backup.

## The Most Recent Snapshot of Your Hypernode

A snapshot is a saved state of the `/data` device at a given moment in time. We can use this to create a static copy of that given state in time and transform this to a virtual device which we can attach to your Hypernode. Once attached, this device is mounted under `/data/backup` and you can easily restore your files by copying them from this file system. To restore database and file backups, see [this article](how-to-restore-your-hypernode-from-a-snapshot.md).

**Everyone can always attach the most recent snapshot to your Hypernode for free**. You can do so by using the following command to attach the latest available snapshot to your node:

`hypernode-systemctl attach_backup`

The backup snapshot is automagically detached/unmounted, before the new snapshots are made. There is a second MySQL instance running so you’ll lose some resources while it is attached. Please contact Support if you want the snapshot detached earlier, to save on resources.

## Requesting Older Snapshots

If you need a less recent snapshot (older than one day) and you don't have SLA Standard, you need to contact Support. Please note we charge a fee for this:

|                                              |                 |                  |
| -------------------------------------------- | --------------- | ---------------- |
|                                              | **SLA Basic**   | **SLA Standard** |
| Most recent Hypernode Backup (AWS/Openstack) | Free            | Free             |
| Most recent Hypernode Backup (DigitalOcean)  | Free            | Free             |
| Older Hypernode Backups                      | € 25,- (ex VAT) | Free             |

## SLA Standard

If you have SLA Standard, you get extra snapshots on top of our basic backup policy. This means we create four snapshots per day for your Hypernode. These backups will be saved for 24 hours. Apart from that we'll have a daily snapshot available for the first 7 days.**As a result you always have a snapshot available which is at most six hours old.**

Please be aware that multiple and instant snapshots are not available for Hypernodes hosted on DigitalOcean.

With SLA Standard, you will be able to use the following commands:

- `hypernode-systemctl attach_backup`
  Use this command to attach the most recent snapshot to your Hypernode. This is also available to users with SLA Basic.
- `hypernode-systemctl create_backup`
  Use this command to create a snapshot on the spot. Then use the `attach_backup` command to attach the snapshot you just created to the Hypernode. These instant snapshots are saved for two days.
- `hypernode-systemctl list_backups`
  List all available snapshots. This way you have access to all snapshots.
- `hypernode-systemctl attach_backup [ID NUMBER]`
  If you don’t specify an ID number, the most recent snapshot will be attached to your Hypernode.

SLA Standard users can also create instant snapshots via the Control Panel (for customers with access to my.hypernode.com)

1. Log in to the Control Panel and select the Hypernode you want to backup by clicking Go.
1. Click Backups in the sidebar to go to the backup page.
1. If you have SLA Standard, you can either select a pre-made backup from the list by clicking Attach Backup. Or you can click Instant Backup to create a snapshot. It will then appear in the list and you can attach it to your Hypernode by clicking the Attach Backup button.

## Restoring Your Hypernode From a Snapshot

You can restore your Hypernode from a snapshot yourself by using [this article](how-to-restore-your-hypernode-from-a-snapshot.md) from our support documentation.

Besides attaching the snapshot, which requires you to restore your data yourself, we can also restore your Hypernode from a snapshot for you. This means that we restore the appropriate database, files or directories from the backup. This service costs €125,-. Contact Support for more information about this.

**Please note:** Restoring a snapshot/backup is never completely without risk, Hypernode is not liable for data loss or other discrepancies.

## Create Your Own Backup and Download it to Your Local Machine

Due to security reasons we don't have easy options to just click and download your files/database to your local machine from your Control Panel. If you still want to download the files/database to your local machine for your peace of mind you'd have to do this manually. You can find instructions in our [documentation](../../best-practices/backups/how-to-create-a-backup-and-download-it-to-your-local-machine.md).

## Using Hard-Links for Backup Retention

Our backup mechanism is not very good in managing hard-links. They will not be ignored in the backup, but at restore time, every hardlink is restored as a real file, causing the restore to take up much more disk space.

This can result in lots of extra files when downloading a restore, effectively taking up much more space needed for the same data after a restore.

We recommend to avoid hard-links in your content at all times.

## Additional Information

We make use of two backup mechanisms: One for the Hypernodes running on Amazon (AWS) and Combell OpenStack, and another mechanism for backups on DigitalOcean.

Read more about restoring backups on Hypernode in [our restore backups article](how-to-restore-your-hypernode-from-a-snapshot.md).

### Backups on DigitalOcean

At DigitalOcean (and also Combell as extra security) we currently create backups using [Duply](http://duply.net/) and [Duplicity](http://duplicity.nongnu.org/) and push those to an S3 storage bucket at Amazon (AWS).
