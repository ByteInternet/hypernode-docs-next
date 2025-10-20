---
myst:
  html_meta:
    description: 'In this article we will explain how to use Valkey on Hypernode. '
    title: How to use Valkey? | Hypernode
redirect_from:
  - /en/hypernode/tools/how-to-use-valkey-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-use-valkey-on-hypernode/ -->

# How to use Valkey on your Hypernode

This article explains how to use Valkey on our Hypernode platform.

## What is Valkey?

Valkey is a Redis-compatible in-memory store. On Hypernode, **Valkey-8** is available on Debian Bookworm single-node setups.
Since Valkey is a drop-in replacement for Redis, it can be used in the same applications as Redis.

## Changing from Redis to Valkey

Your Hypernode is configured with Redis by default.
Changing from Redis to Valkey is pretty easy on Hypernode. You can use the `hypernode-systemctl` command-line tool to change from Redis to Valkey.

```console
app@levka6-appname-magweb-cmbl:~$ hypernode-systemctl settings valkey_enabled true
Operation was successful and is being processed. Please allow a few minutes for the settings to be applied. Run 'livelog' to see the progress.
```

It may take a few minutes for the changes to be applied. You can monitor the progress by running `hypernode-log`.
Once the process is complete, Valkey will be enabled and Redis will be disabled on your Hypernode.

## Using Valkey tools

Redis comes by default with a bunch of useful tools pre-installed on Hypernode, like `redis-cli` and `redis-benchmark`.
Once you have switched to Valkey, you can use the `valkey-cli` and `valkey-benchmark` tools instead.
However, to make it even more easy, we made sure that the `redis-cli` and `redis-benchmark` commands are symlinked to their Valkey counterparts when Valkey is enabled.
In this way you can keep using the same commands you are used to.

## How to configure Valkey in Magento 2

The configuration for Valkey is the same as for Redis.
You can follow our [Magento 2 Redis configuration guide](../../ecommerce-applications/magento-2/how-to-configure-redis-for-magento-2.md) to configure Valkey for Magento 2.
