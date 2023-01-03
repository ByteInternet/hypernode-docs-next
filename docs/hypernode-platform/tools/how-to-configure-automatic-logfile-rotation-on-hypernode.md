---
redirect_from:
- /en/support/solutions/articles/48001185227-how-to-configure-automatic-logfile-rotation-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001185227-how-to-configure-automatic-logfile-rotation-on-hypernode/ -->

# How to configure automatic logfile rotation on Hypernode

We have a hypernode-auto-logrotate command as part of our hypernode- system utilities. This is a command line tool that automatically rotates log files, which helps avoid disk space issues and decreases time the required to restore back-ups.

## Log rotation

A hypernode contains files that applications write their logs to. For example, Magento writes to `/data/web/magento2/var/log/debug.log`. These log files can get quite large (we’ve seen examples of over 30GB), so for example when doing a backup, you end up transferring obscenely large files over the internet.

You can avoid this problem by rotating the log files. This means that when a log file `/data/web/example.log` gets too big, you compress it, move it to `/data/web/example.log.1.gz`, and give the application an empty log file to write to. The `hypernode-auto-logrotate` command automates this process.

## Example Usage

For a log file `~/example.log`, the tool can be used as follows:

```console
app@levkd4-example-magweb-cmbl:~$ hypernode-auto-logrotate example.log
Adding logrotate cron job
Adding logrotate config entry for "/data/web/example.log"
```

This will cause the log file to be rotated on a daily basis, at around midnight. If the file is over 50MB, the next day the old logs will have been moved to `~/example.log.1.gz`.

```console
app@levkd4-example-magweb-cmbl:~$ ls example.log*
example.log example.log.1.gz
```

The tool also has a `--detect` option, with which it will search for log files and rotate them:

```console
app@levkd4-example-magweb-cmbl:~$ hypernode-auto-logrotate --detect
Searching for logfiles...
Logfile found: /data/web/example.log
Logfile found: /data/web/magento2/var/log/system.log
Logfile found: /data/web/magento2/var/log/connector.log
Logfile found: /data/web/magento2/var/log/debug.log
Logfile found: /data/web/magento2-sample-data/dev/tools/exclude.log
Logfile "/data/web/example.log" is already being rotated
Adding logrotate config entry for "/data/web/magento2/var/log/system.log"
Adding logrotate config entry for "/data/web/magento2/var/log/connector.log"
Adding logrotate config entry for "/data/web/magento2/var/log/debug.log"
Adding logrotate config entry for "/data/web/magento2-sample-data/dev/tools/exclude.log"
```

The default threshold of the hypernode-auto-logrote is 500 MB meaning the tool will only detect logs larger than 500 MB. You can also lower the threshold by adding the option `--threshold 200MB` (or any other amount) so it will search for logs bigger than 200 MB for example.

The tool has a `--dry-run` option which will print what the tool will do without actually doing it. For more detailed output, run it with the `--verbose` option.

## Configuration

The `hypernode-auto-logrotate` command comes with a sensible out-of-the-box configuration. Among other things, this means that it will rotate log files daily, only when they exceed 50MB, and that it will keep four files in rotation (meaning you end up with `example.log.1.gz` up to `example.log.4.gz`). These configurations are stored in `/data/web/hypernode_logrotate.conf`, and can be customized per log by editing this file. For example, the entry added for `example.log` reads

```
/data/web/example.log {
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

The [logrotate main page](https://linux.die.net/man/8/logrotate) contains instructions on how to customize this
