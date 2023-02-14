---
myst:
  html_meta:
    description: 'The hypernode-auto-logrotate is a command line tool that automatically
      rotates log files. Learn how to configure Automatic Logfile Rotation. '
    title: How to configure automatic logfile rotation? | Hypernode
redirect_from:
  - /en/hypernode/tools/how-to-configure-automatic-logfile-rotation/
  - /en/support/solutions/articles/48001185227-how-to-configure-automatic-logfile-rotation-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-configure-automatic-logfile-rotation/ -->

# How to Configure Automatic Logfile Rotation

We have a `hypernode-auto-logrotate` command as part of our `hypernode-` system utilities. This is a command line tool that automatically rotates log files, which helps avoid disk space issues and decreases time the required to restore back-ups.

## Log Rotation

A Hypernode contains files that applications write their logs to. For example, Magento writes to `/data/web/magento2/var/log/debug.log`. These log files can get quite large (we’ve seen examples of over 30GB), so for example when doing a backup, you end up transferring obscenely large files over the internet.

You can avoid this problem by rotating the log files. This means that when a log file `/data/web/example.log` gets too big, you compress it, move it to `/data/web/example.log.1.gz`, and give the application an empty log file to write to. The `hypernode-auto-logrotate` command automates this process.

## Example Usage

For log files `~/magento2/var/log/system.log` and `~/magento2/var/log/debug.log`, the tool can be used as follows:

```console
app@levkd4-example-magweb-cmbl:~$ hypernode-auto-logrotate /data/web/magento2/var/log/system.log /data/web/magento2/var/log/debug.log
Adding logrotate cron job
Adding logrotate config entry for "/data/web/magento2/var/log/system.log"
Adding logrotate config entry for "/data/web/magento2/var/log/debug.log"
```

This will cause the log file to be rotated on a daily basis, at around midnight. If the file is over 50MB, the next day the old logs will have been moved to `~/magento2/var/log/system.log.1.gz`.

```console
app@levkd4-example-magweb-cmbl:~/magento2/var/log$ ls system.log*
system.log system.log.1.gz
```

The tool also has a `--detect` option, with which it will search for log files bigger than 500 MB and rotate them:

```console
app@levkd4-example-magweb-cmbl:~$ hypernode-auto-logrotate --detect
Searching for logfiles...
Logfile found: /data/web/magento2/var/log/system.log
Logfile found: /data/web/magento2/var/log/connector.log
Logfile found: /data/web/magento2/var/log/debug.log
Logfile found: /data/web/magento2-sample-data/dev/tools/exclude.log
Adding logrotate config entry for "/data/web/magento2/var/log/system.log"
Adding logrotate config entry for "/data/web/magento2/var/log/connector.log"
Adding logrotate config entry for "/data/web/magento2/var/log/debug.log"
Adding logrotate config entry for "/data/web/magento2-sample-data/dev/tools/exclude.log"
```

The tool has a `--dry-run` option which will print what the tool will do without actually doing it. For more detailed output, run it with the `--verbose` option.

## Configuration

The `hypernode-auto-logrotate` command comes with a sensible out-of-the-box configuration. Among other things, this means that it will rotate log files daily, only when they exceed 50MB, and that it will keep four files in rotation (meaning you end up with `system.log.1.gz` up to `system.log.4.gz`). These configurations are stored in `/data/web/hypernode_logrotate.conf`, and can be customized per log by editing this file. For example, the entry added for `system.log` reads

```
/data/web/magento2/var/log/system.log {
    rotate 4
    daily
    compress
    # do not raise an error if the logfile does not exist
    missingok
    # file size at which rotation is triggered
    size 50M
    # copy the file and truncate the original, in case
    # another process cannot be told to close the logfile
    copytruncate
}
```

The [logrotate main page](https://linux.die.net/man/8/logrotate)contains instructions on how to customize this.

## Keeping the configuration up to date

*****This cronjob configuration is deployed by default on new Hypernodes. If you don't want this configuration, feel free to comment or delete the configuration from your crontab.*****

To make sure you keep your logrotate config keeps up to date with newer log files, it is advised to run `hypernode-auto-logrotate-detect --detect` every night. Open your cronjob configuration with `crontab -e` and add the following configuration.

```
# Add logfiles to logrotate configuration
0 4 * * * /usr/bin/chronic /usr/bin/hypernode-auto-logrotate --detect
```
