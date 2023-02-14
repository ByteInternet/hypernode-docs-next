---
myst:
  html_meta:
    description: 'As a result of how MySQL stores data, a ibdata1 file can grow very
      large and removing it can cause data loss/corruption. Learn how to free disk
      space. '
    title: How to free disk space from MySQL ibdata1? | Hypernode
redirect_from:
  - /en/hypernode/mysql/how-to-free-disk-space-from-mysql-ibdata1/
  - /knowledgebase/free-diskspace-ibdata1/
---

<!-- source: https://support.hypernode.com/en/hypernode/mysql/how-to-free-disk-space-from-mysql-ibdata1/ -->

# How to Free Disk Space From MySQL ibdata1

MySQL uses several files for journaling transactions, among these files there is the `ibdata1` file.

Due to the way MySQL stores its data, this file can grow very large and unfortunately cannot simply be removed without risking corruption and/or data loss.

## How to Find the Root Cause

The most likely cause is one or more queries that take a very long time to complete. These queries run transactions which stay open as long as the query itself. While that transaction is running, all changes compared to the original table are kept inside the `ibdata1` file.

The MySQL slow logs can be found under `/var/log/mysql/mysql-slow.log`.

Alternatively, a summary report can be created using the `pt-query-digest utility`:

`pt-query-digest /var/log/mysql/mysql-slow.log`

**Dutch** speaking customers also have the option to monitor the long running queries in the “MySQL slow queries” section on their [Service Panel](https://auth.byte.nl/). You can sort them by query time to see the longest queries at the top.

## How to Reclaim the Disk Space

Before reclaiming the disk space it's important that the long running queries have been resolved/stopped!

The only safe way to free up the disk space taken by `ibdata1` is a procedure only Hypernode support can perform, as this procedure requires root privileges. **Furthermore this procedure can only be performed on MySQL 5.6 and 5.7 at the moment.**

This procedure includes:

- dumping/backing up all databases
- stopping MySQL
- removing the MySQL data directory
- recreating the empty skeleton databases
- restarting MySQL
- re-importing the databases from the backup

As mentioned [in this Stack Exchange article](http://dba.stackexchange.com/questions/24942/how-do-i-shrink-the-innodb-file-ibdata1-without-dumping-all-databases) there sadly is no other solution than the aforementioned procedure.

**If you're encountering this problem on a Hypernode, please contact support@hypernode.com so we can help you reclaim your disk space!**
