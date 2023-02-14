---
myst:
  html_meta:
    description: Learn how to create and download a backup of your Hypernode application
      and database to your local machine. This can be done with SSH access.
    title: Create and Download a Backup to Your Local Machine
redirect_from:
  - /en/support/solutions/articles/48001208755-how-to-create-a-backup-and-download-it-to-your-local-machine/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001208755-how-to-create-a-backup-and-download-it-to-your-local-machine/ -->

# How to Create a Backup and Download it to Your Local Machine

This article will explain how you can create you own backup and download it your PC. Do note that you'll need to have **SSH** access to your Hypernode to be able to create the backup. In this tutorial we assume you're already logged into your Hypernode with SSH.

*Please note that the following procedure is not supported by Hypernode. We simply list this option as we have had a number of customers who have requested this for a variety of reasons. If you run into any issues following the below steps we are unfortunately not able to help you with this.*

*That said, we can upon your request and for a small fee (€ 75 EUR) arrange for a complete copy of your website (and/or database) to be made available for download. If you would like to make use of this option please send us an e-mail at [support@hypernode.com](http://support@hypernode.com) with the subject ‘Requesting backup for download’ with a description of what you need and we will take care of this within 12 (working) hours. The costs will then be added to your next invoice.*

## Create the Backup

A backup of your shop exists of two parts. A backup of the files of your application, and a backup of the database from the shop. Once you have both, we can zip both files nicely into one single .zip file. To keep it consistent we create e new directory in which we will place the backup(s). So the first step is to create that directory:

- `mkdir /data/web/backup_hypernode`

### Create File Backup

The most efficient way to create a file backup will be to zip your files. Before you run this command you need to make sure what the location is of the root directory of your application. For example, if you have Magento 2, the default location would often be **/data/web/magento2**. To create a .zip file of this directory follow run this command. (replace \*\[date\]\*with the date of the backup, just for your own clarification):

- `zip -ry /data/web/backup_hypernode/file_backup_[date].zip /data/web/magento2`

If your application is in another folder you need to replace "/data/web/magento2" with the path of your application folder.

### Create Database Backup

In this step you'll create a dump of your database, and zip that dump into a .zip file. To do this you need to know the name of the database.

- `mysqldump database > /data/web/backup_hypernode/database_[date].sql`
- `zip -ry /data/web/backup_hypernode/database_backup_[date].zip /data/web/backup_hypernode/database_[date].sql`

### Zip Both Backups into a Single .zip File

Now we have a backup for both the files and the database, you can zip both backups into one file.

- `zip /data/web/backup_hypernode/full_backup_[date].zip /data/web/backup_hypernode/file_backup_[date].zip /data/web/backup_hypernode/database_backup_[date].zip`

## Download the Backup to Your Local Machine

Now that you've created the backup(s) in **/data/web/backup_hypernode**, you can download the desired backup. There are several options for downloading your backup. In this section we're gonna explain two options. You can choose which ever one would be most convenient for you.

### Download via FTP

Follow these steps to download your backup via FTP:

- First of all create a [FTP-user](../../hypernode-platform/ftp/how-to-configure-ftp-sftp-on-hypernode.md)(If you already have a FTP-user make sure it's able to access the backup directory)
  - set the **home-dir** to `/data/web/backup_hypernode`
  - Set your IP on the FTP whitelist
  - Login with your FTP-user on for example FileZilla

### Download via SSH

With SSH you can use **scp** to copy the .zip file of the backup to your local machine. Do note that you'll need to know your local path to download the .zip file to. Run this commando in your local terminal, NOT in the Hypernode environment.

- `scp app@APPNAME.hypernode.io:/data/web/backup_hypernode/full_backup_[date].zip /path/to/local/directory`

Once you ran this command the .zip file of the backup should be in the directory you indicated in your command.
