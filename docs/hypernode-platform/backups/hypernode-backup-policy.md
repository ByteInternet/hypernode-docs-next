---
myst:
  html_meta:
    description: A complete overview of Hypernode's backup policy, showing the scheme,
      methods, locations, and frequency backups, and additional services.
    title: Hypernode Backup Policy | Backups
redirect_from:
  - /en/hypernode/backups/hypernode-backup-policy/
---

<!-- source: https://support.hypernode.com/en/hypernode/backups/hypernode-backup-policy/ -->

# Hypernode Backup Policy

Hypernode recognizes that the backup of data is critical to the viability and operations of any organization. This documents outlines the measures we take to create safe, secure, and usable backups for our customers to use.

# Cloud Hosting Backup

On Amazon Web Services (AWS) and Combell OpenStack we use snapshots to create backups. When things go slightly wrong (ie. a product is accidentally deleted), you can go back in time to restore the appropriate database table, files or directories from the snapshot. Snapshots are easy to use, creating them take up less time and there’s no need to upgrade your Hypernode if you don’t have enough disk space.

A snapshot is a saved state of the `/data` device at a given moment in time. We can use this to create a static copy of that given state in time and transform this to a virtual device which we can attach to your Hypernode. Once attached, this device is mounted under `/data/backup` and you can easily restore your files by copying them from this file system.

## Frequency and Retention Times

Snapshots are made every day and saved for 7 days. We also save 1 backup per week for 3 weeks. This means you will have 4 weeks worth of backups.

Snapshots are rotated daily after the creation of a new backup. This implies that the backups that are older than 4 weeks will be automatically removed.

If you have an SLA Standard for your Hypernode, additional snapshots are available. For details see the SLA Standard section below.

## Restoring Data

To access the backup snapshots to restore data, you will first need to get the backup attached to your Hypernode. You can do so using the `hypernode-systemctl attach_backup` command.
As the backup snapshot contains a second MySQL instance running, attaching a snapshot has a minor impact on your resources. For this reason, the backup snapshot while be automatically detached within 24 hours. Please contact Support if you want the snapshot detached earlier.

To restore database and file backups from a snapshot, see [this article](how-to-restore-your-hypernode-from-a-snapshot.md).
**Please note:** Restoring a snapshot/backup is never completely without risk, Hypernode is not liable for data loss or other discrepancies.

You can always attach the most recent snapshot to your Hypernode for free. Depending on your SLA, attaching older snapshots might come at a fee. For details see the SLA Standard section below.

### Requesting Older Snapshots

If you need a less recent snapshot (older than one day) and you don't have SLA Standard, you need to contact Support. Please note we charge a fee for this:

|                                              |                 |                  |
| -------------------------------------------- | --------------- | ---------------- |
|                                              | **SLA Basic**   | **SLA Standard** |
| Most recent Hypernode Backup (AWS/Openstack) | Free            | Free             |
| Most recent Hypernode Backup (DigitalOcean)  | Free            | Free             |
| Older Hypernode Backups                      | € 25,- (ex VAT) | Free             |

## SLA Standard

If you have SLA Standard, you get extra snapshots on top of our basic backup policy. This means we create a total of four snapshots per day for your Hypernode. These extra backups will be saved for 24 hours. Apart from that we'll have a daily snapshot available for the first 7 days. **As a result you always have a snapshot available which is at most six hours old.**

With SLA Standard, you will be able to use the following commands:

- `hypernode-systemctl attach_backup`
  Use this command to attach the most recent snapshot to your Hypernode. This is also available to users with SLA Basic.
- `hypernode-systemctl create_backup`
  Use this command to create a snapshot on the spot. Then use the `attach_backup` command to attach the snapshot you just created to the Hypernode. These instant snapshots are saved for two days.
- `hypernode-systemctl list_backups`
  List all available snapshots. This way you have access to all snapshots.
- `hypernode-systemctl attach_backup [ID NUMBER]`
  If you don’t specify an ID number, the most recent snapshot will be attached to your Hypernode.

SLA Standard users can also create instant snapshots via the Control Panel

1. Log in to the Control Panel and select the Hypernode you want to backup by clicking Go.
1. Click Backups in the sidebar to go to the backup page.
1. If you have SLA Standard, you can either select a pre-made backup from the list by clicking Attach Backup. Or you can click Instant Backup to create a snapshot. It will then appear in the list and you can attach it to your Hypernode by clicking the Attach Backup button.

# Offsite backups

All Hypernodes, both Dedicated and Cluster hosted, as well as Cloud hosted, make use of off-site backups. Offsite backups allow (partial) restoration of the production environment when it experiences accidental dataloss, or hardware issues. Offsite backups are easy to use, but creation and restoration times are affected by size of the data, amount of modifications to the data, and (available) network bandwidth. It also requires a small amount of diskspace to speed up operations.

Offsite backups are incremental backups of the `/data` device. Due to the technology used, this backup is not from a singular moment in time, and as such can be considered a "Fuzzy backup". We also make a `mysqldump` backup of the database, using transactional technology to ensure a proper database backup.

## Frequency and Retention Times

Offsite backups are created once a day. Daily backups are retained for a minimum of 28 days, and, due to the use of Incremental backups, a maximum of 42 days.

Offsite database backups are made every day and saved for 7 days. We also save 1 backup per week for 3 weeks. This means you will have 4 weeks worth of backups.

## Restoring Data

To access the offsite backup, you will need assistance of our Support Engineers, see [this article](how-to-restore-your-hypernode-from-external-backups.md).
If you are unable to restore this backup yourself, our support engineers are available to restore data from your offsite backup for you. This means that we restore the appropriate database, files or directories from the backup. This service costs €125,-. Contact Support for more information about this.
**Please note:** Restoring a backup is never completely without risk, Hypernode is not liable for data loss or other discrepancies.

# Additional Information

## Using Hard-Links for Backup Retention

Our backup mechanism is not very good in managing hard-links. They will not be ignored in the backup, but at restore time, every hardlink is restored as a real file, causing the restore to take up much more disk space.

This can result in lots of extra files when downloading a restore, effectively taking up much more space needed for the same data after a restore.

We recommend to avoid hard-links in your content at all times.

## Creating offline backups

Due to security reasons we don't have easy options to just click and download your files/database to your local machine from your Control Panel. If you still want to download the files/database to your local machine for your peace of mind you'd have to do this manually. You can find instructions in our [documentation](../../best-practices/backups/how-to-create-a-backup-and-download-it-to-your-local-machine.md).
