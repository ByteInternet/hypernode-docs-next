---
myst:
  html_meta:
    description: 'With Composer, you can easily install, update or remove dependencies.
      Read here how to use Composer 2 on our Hypernode platform. '
    title: How to use Componsor 2 on Hypernode?
redirect_from:
  - /en/support/solutions/articles/48001184546-how-to-use-composer-2-on-your-hypernode/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001184546-how-to-use-composer-2-on-your-hypernode/ -->

# How to use Composer 2 on your Hypernode

This article explains how to use Composer 2 on our Hypernode platform.

## Change the Default Version to Composer 2

From January 2022, Composer 2 is the default Composer version on our Hypernode platform. We've also made setting the system Composer version to 1 or 2 configurable. All existing nodes (booted before January 2022) will keep composer 1 as their `/usr/local/bin/composer` unless otherwise configured.

To switch between Composer versions you can use the hypernode-api or the hypernode-systemctl command-line tool:

```console
app@levka6-appname-magweb-cmbl:~$ ls -lah /usr/local/bin/composer
lrwxrwxrwx 1 root root 9 Jan  5 16:08 /usr/local/bin/composer -> composer1
app@levka6-appname-magweb-cmbl:~$ ls -lah /usr/local/bin/composer*
lrwxrwxrwx 1 root root    9 Jan  5 16:08 /usr/local/bin/composer -> composer1
-rwxr-xr-x 1 root root 2.0M Jan  5 16:09 /usr/local/bin/composer1
-rwxr-xr-x 1 root root 2.3M Jan  5 16:09 /usr/local/bin/composer2
app@levka6-appname-magweb-cmbl:~$ hypernode-systemctl settings composer_version 2.x
Operation was successful and is being processed. Please allow a few minutes for the settings to be applied. Run 'livelog' to see the progress.
app@levka6-appname-magweb-cmbl:~$ hypernode-log | head -n 2  # wait for update_node to finish
ACTION                          START                 END                   STATE     TASKS  RUNNING
update_node                     2022-01-06T15:50:12Z  2022-01-06T15:50:13Z  running   2/4   php_update_node_to_update_flow
app@levka6-appname-magweb-cmbl:~$ ls -lah /usr/local/bin/composer*
lrwxrwxrwx 1 root root    9 Jan  5 16:08 /usr/local/bin/composer -> composer2
-rwxr-xr-x 1 root root 2.0M Jan  5 16:09 /usr/local/bin/composer1
-rwxr-xr-x 1 root root 2.3M Jan  5 16:09 /usr/local/bin/composer2
```

And to switch back to Composer 1:

```console
app@levka6-appname-magweb-cmbl:~$ hypernode-systemctl settings composer_version 1.x
Operation was successful and is being processed. Please allow a few minutes for the settings to be applied. Run 'livelog' to see the progress.
```

## Use Composer 2 in a Separate Path

Hypernodes contain both `/usr/local/bin/composer1`and `/usr/local/bin/composer2`. The first one self-updates with the `--1` flag to the latest Composer 1 version and the latter self-updates to the most recent Composer 2 version. Depending on which Composer version is configured, `/usr/local/composer` is a symlink to either one of those paths.

The reason for this is backwards compatibility because Magento only started [including support for Composer 2 in Magento 2.4.2](https://devdocs.magento.com/guides/v2.4/comp-mgr/cli/cli-upgrade.html).

Of course you could install any version of composer you want manually by running:

```console
$ wget https://getcomposer.org/composer-stable.phar -O composer
$ chmod +x composer
$ ./composer --version
Composer version 2.2.18 2022-08-20 11:33:38
```

But to have all the relevant development tools available out of the box we have also added `composer2` in a separate path:

```console
$ which composer
/usr/local/bin/composer1
$ which composer2
/usr/local/bin/composer2
$ composer --version
Composer version 1.10.21 2021-04-01 09:16:34
$ composer2 --version
Composer version 2.2.18 2022-08-20 11:33:38
```

So if you want to use Composer 2 you only need to run `composer2` instead of `composer`.
