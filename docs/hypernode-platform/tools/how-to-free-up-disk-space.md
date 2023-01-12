---
myst:
  html_meta:
    description: Is your disk full? Before upgrading to a bigger plan you can use
      these suggestions to free up disk space on your Hypernode.
    title: How to free up disk space on your Hypernode?
redirect_from:
  - /en/hypernode/tools/how-to-free-up-disk-space/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-free-up-disk-space/ -->

# How to Free up Disk Space

Is your disk full? Before upgrading to a bigger plan you can use these suggestions to free up disk space on your Hypernode.

## Find the Bottleneck: Is It the Amount of Bytes or the Amount of Files?

To display the percentile usage of files that can be created: `df -i /data`

To display the percentage of used space in gigabytes: `df -h /data`

To display the disk usage report sorted in descending order: `ncdu /data`

## Do You Have Too Many Files? Did You Run out of Inodes?

In most situations, there was an explosion of session-files. Check in /data/web/public/var/session whether this is the case. You could consider to store your sessions in MySQL or Redis. If the amount of sessions is not the problem (ie less than 100K), then use this command to find the folder with the most files:

```bash
find /data -xdev -printf '%h\n' | sort | uniq -c | sort -k 1 -n
```

If you have identified a folder with lots (millions) of files, this is a handy command to, for example delete all session files older than 2 days:

```bash
cd /data/web/public/var/session
find . -type f -mtime +2 -ls -delete
```

## Is Disk Space the Bottleneck?

Try to see where you can clear up the most space. The following command (using SSH) will show you the top 10 largest directories:

```bash
du -h /data/web /data/mysql | sort -h | tail -10
```

## Have You Tried Optimizing Your Images Yet?

This can save you up to 30% in disk space without any downsides. Additionally, your site will become a lot faster for your visitors. Use the Hypernode Image Optimizer to [optimize your Magento images](../../best-practices/performance/how-to-optimize-your-images.md) within 5 minutes.

## Another Quick Fix Would Be to Clear the Magento Cache.

This can be done through the Magento back-end (“clear cache”). You can also do this with SSH by issuing the following command:

For Magento 1:

```bash
magerun cache:flush
```

For Magento 2:

```bash
magerun2 cache:flush
```

## Perhaps You Have Collected a Bunch of Logs and Reports.

You can remove these with the following command:

```bash
find ~/public/var/reports -type f -delete
find ~/public/var/log -type f -delete
```

## Do You Suffer From the MySQL ibdata Bug?

When running specific extremely long queries (several hours), MySQL disk usage may grow but is freed. This is known behaviour of MySQL and can only be resolved manually. Check whether you are affected:

```console
$ ls -lah /data/mysql/ibdata1
-rw-rw---- 1 mysql mysql 29G Jun 28 12:48 /data/mysql/ibdata1
```

If the size is more than 2 GB, see our instructions on [how to resolve growing ibdata1](../mysql/how-to-free-disk-space-from-mysql-ibdata1.md).

## Find out If You Cleaned up Adequate Space

You can check your disk usage with:

```bash
df -h /data
df -i /data
```

## Deleted Files, but df -h Doesn’t Show Any Difference in Disk Usage?

In case you have deleted some supersized log files or other ambiguous and huge files, but this doesn’t result in more available disk space when checking it with the aforementioned commands, then some process is still using these files. You can easily check this with:

```bash
lsof +L1
```

This will show you a list of processes that are still using the original file and preventing the disk space to be reclaimed as being available. Just copy the process id (PID) and kill the process using:

```bash
kill <PID>
```

## /data.image Is Taking up All My Disk Space

To ensure you always have the promised amount of disk space at your disposal and to prevent your shop from filling up the entire Hypernode which can cause migration problems or in extreme cases storage issues that can affect the operating system, we use an image file that is mounted on `/data`.

This image file is created the first time the node is booted and contains the exact maximum amount of disk space available for your Hypernode plan.

This way we can give guarantees about the available disk space for your shop without the need to re-partition the server, as this is a time consuming process that delays the delivery of your ordered Hypernode too much.

This `/data.image` file is stored in the root of the server and is safe for you to ignore. It contains all the files and database storage used for your shop and has a fixed size.

When cleaning up your Hypernode to save disk space, always check the `/data` partition, not the root (/) partition.

The root partition is used by the operating system and is not added to the disk space statistics.
