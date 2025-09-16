---
myst:
  html_meta:
    description: This article explains how to configure Valkey on your Magento 2 shop on Hypernode and how to work with redis-cli or valkey-cli.
    title: How to configure Valkey for Magento 2? | Hypernode
redirect_from:
  - /ecommerce-applications/magento-2/how-to-configure-valkey-for-magento-2/
---

# How to Enable Valkey for Magento 2

Valkey is a Redis-compatible in-memory store. On Hypernode, **Valkey-8** is available on Debian Bookworm single-node setups. It is not supported on Debian Buster or on Hypernode Clusters. **Redis remains supported.**

> If you previously used Redis, **no action needed** after enabling it ( **see example below** ), existing Magento settings continue to work with Valkey.
>
## Paths

- Logs: `/var/log/valkey/`
- App-scoped directory on Hypernode: `/data/web/valkey/`

---

Valkey is Redis-compatible, so your existing Magento `redis` configuration flags work unchanged.

> **Enable Valkey on supported nodes**
>
> ```console
> $ hypernode-systemctl settings valkey_enabled True
> ```

Take a look at the `livelog` command to check the progress on the update job.

## Redis Tools or Valkey Tools?

> `redis-cli`and `redis-tools` is symlinked to `valkey-cli` and `valkey-tools` when Valkey is enabled. You can use **either**. Examples below show `redis-cli` with an `or valkey-cli` alternative.


# First Time Setup - Redis Not Previously Configured

## Configure Valkey Cache for Magento 2

There are two ways to configure the cache. You can run a command that updates `env.php`, or you can edit it yourself.

## Configure Valkey Cache for Magento 2 Through the Commandline

Use the following command to enable backend caching:

```console
$ cd /data/web/magento2
$ bin/magento setup:config:set     --cache-backend=redis     --cache-backend-redis-server=redismaster     --cache-backend-redis-db=1
```

Now flush your cache:

```console
$ rm -rf /data/web/magento2/var/cache/*
$ redis-cli flushall
# or
$ valkey-cli flushall
```

## Configure Valkey Full Page Caching for Magento 2

Enable page caching:

```console
$ cd /data/web/magento2
$ bin/magento setup:config:set     --page-cache=redis     --page-cache-redis-server=redismaster     --page-cache-redis-db=2
```

And flush your cache:

```console
$ rm -rf /data/web/magento2/var/cache/*
$ redis-cli flushall
# or
$ valkey-cli flushall
```

## Flush Your Caches

To flush your Magento cache, clear the Valkey database you configured:

```console
$ redis-cli -n 1 flushdb
# or
$ valkey-cli -n 1 flushdb
```

Or alternatively use `n98-magerun2` or the Magento cli tool:

```console
## Flush using n98-magerun2
$ n98-magerun2 cache:flush
## Flush using magento cli
$ cd /data/web/magento2 && bin/magento cache:flush
```

To flush all sessions, caches etc (flush the full instance), use the following command:

```console
$ redis-cli flushall
# or
$ valkey-cli flushall
```

## Changing the Compression Library

It is possible to use the compression library 'Snappy' on Hypernode.

In order to use the compression library Snappy for your Valkey cache you can run the following commands:

```console
$ bin/magento setup:config:set --cache-backend-redis-compression-lib=snappy
$ # If you use Magento's builtin page cache
$ bin/magento setup:config:set --page-cache-redis-compression-lib=snappy
```

## Configure Magento 2 to Use Valkey as the Session Store

You can use Valkey for storing sessions too.

### Configure Magento 2 to Store Sessions in Valkey

Run the following command:

```console
$ cd /data/web/magento2
$ bin/magento setup:config:set     --session-save=redis     --session-save-redis-host=redismaster     --session-save-redis-db=3
```

Now flush your cache:

```console
$ redis-cli flushall
# or
$ valkey-cli flushall
```

### Enable Second Valkey Instance for Sessions

Enable the second instance for sessions:

```console
$ hypernode-systemctl settings redis_persistent_instance True
```

After enabling the second instance change the session port to `6378` and the database to `0`:

```console
$ cd /data/web/magento2
$ bin/magento setup:config:set     --session-save-redis-port=6378     --session-save-redis-db=0
```

Furthermore you can add the following line to your crontab to take periodic background snapshots:

```
* * * * * redis-cli -p 6378 bgsave
# or
* * * * * valkey-cli -p 6378 bgsave
```

### Test Whether Your Sessions Are Stored in Valkey

To verify whether your configuration is working properly, first clear your filesystem session store:

```console
$ rm /data/web/public/var/sessions/*
```

Now open the site in your browser and hit `F5` a few times or log in to the admin panel. Then check the configured database:

```console
$ redis-cli -n 0 keys '*'
# or
$ valkey-cli -n 0 keys '*'
```
