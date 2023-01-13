---
myst:
  html_meta:
    description: This article will explain how to configure Redis on your Magento
      2 shop on Hypernode and how to work with redis-cli.
    title: How to configure Redis for Magento 2? | Hypernode
redirect_from:
  - /en/ecommerce/magento-2/how-to-configure-redis-for-magento-2/
  - /knowledgebase/configure-sessions-redis-magento2/
  - /knowledgebase/configure-redis-magento2/
  - /knowledgebase/setup-php-redis-admin-manage-redis-caches/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-configure-redis-for-magento-2/ -->

# How to Configure Redis for Magento 2

Redis is a caching method which can increase the speed of the backend and frontend of your shop. On Hypernode every customer has access to Redis cache, starting from 64 MB, depending on the plan. This article will explain how to configure Redis on your Magento 2 shop on Hypernode and how to work with redis-cli.

Want to know how to configure Redis in Magento 1? Have a look at [this article](../../ecommerce-applications/magento-1/how-to-configure-redis-for-magento-1.md)!

## Configure Redis Cache for Magento 2

There are two ways to configure Redis Cache for Magento 2. You can either run a command which automatically updates the `env.php` with the correct details or you can manually change the `env.php` file.

## Configure Redis Cache for Magento 2 Through the Commandline

Use the following command to enable Redis backend caching:

```console
$ cd /data/web/magento2
$ bin/magento setup:config:set \
    --cache-backend=redis \
    --cache-backend-redis-server=redismaster \
    --cache-backend-redis-db=1
```

Now flush your cache:

```console
$ rm -rf /data/web/magento2/var/cache/*
$ redis-cli flushall
```

## Configure Redis Full Page Caching for Magento 2

To enable page caching Redis, extend your /data/web/magento2/app/etc/env.php with the following snippet. You should paste this in between the cache keys, so leave the cache tag in this snippet out of it.

```console
$ cd /data/web/magento2
$ bin/magento setup:config:set \
    --page-cache=redis \
    --page-cache-redis-server=redismaster \
    --page-cache-redis-db=2
```

And flush your cache:

```console
$ rm -rf /data/web/magento2/var/cache/*
$ redis-cli flushall
```

## Flush Your Caches

To flush your Magento cache, clear the Redis database corresponding to your configured Redis database:

```console
$ redis-cli -n 1 flushdb
```

Or alternatively use `n98-magerun2` or the Magento cli tool:

```console
## Flush using n98-magerun2
$ n98-magerun2 cache:flush
## Flush using magento cli
$ cd /data/web/magento2 && bin/magento cache:flush
```

To flush all sessions, caches etc (flush the full Redis instance), use the following command:

```console
$ redis-cli flushall
```

## Changing the Compression Library

It is possible to use the compression library 'Snappy' on Hypernode. More information about Snappy can be found in the changelog: [Release-4224](https://changelog.hypernode.com/changelog/release-4224/).

In order to use the compression library Snappy for your Redis cache you can run the following commands:

```console
$ bin/magento setup:config:set --cache-backend-redis-compression-lib=snappy
$ # If you use Magento's builtin page cache with Redis
$ bin/magento setup:config:set --page-cache-redis-compression-lib=snappy
```

## Configure Magento 2 to Use Redis as the Session Store

You can use Redis for storing sessions too!

Hypernodes bigger than a Grow plan, often have enough memory to store the session data in Redis. This way sessions are stored in-memory, making the shop faster and use less IO than when using MySQL or files as session store.

### Configure Magento 2 to Store Sessions in Redis

As Magento 2 is fully supporting Redis, there is no need to install additional extensions to configure Redis. All you need to do is extend your `app/etc/env.php` and flush your cache.

To enable session storage in Redis, run the following command:

```console
$ cd /data/web/magento2
$ bin/magento setup:config:set \
    --session-save=redis \
    --session-save-redis-host=redismaster \
    --session-save-redis-db=3
```

Now flush your cache:

```console
$ rm -rf /data/web/magento2/var/cache/*
$ redis-cli flushall
```

### Enable Second Redis Instance for Sessions

We have made is possible to enable a second Redis instance more tailored for saving session data (more information can be found in our [changelog](https://changelog.hypernode.com/changelog/experimental-changes-redis-sessions-aws-performance/)).

To enable the second Redis instance for sessions you run the command: `hypernode-systemctl settings redis_persistent_instance --value True`

After enabling the second Redis instance you need to change the configured Redis session port value to `6378` instead of the default `6379` and the database to `0`, since we're using a separate Redis instance now:

```console
$ cd /data/web/magento2
$ bin/magento setup:config:set \
    --session-save-redis-port=6378 \
    --session-save-redis-db=0
```

Furthermore you need to add the following line to your crontab:

```
* * * * * redis-cli -p 6378 bgsave
```

### Test Whether Your Sessions Are Stored in Redis

To verify whether your configuration is working properly, first clear your session store:

```console
$ rm /data/web/public/var/sessions/*
```

Now open the site in your browser and hit `F5` a few times or log in to the admin panel. If all is well, no additional sessions files should be written to `/data/web/var/sessions`, but instead to the Redis database:

To verify whether your configuration is working properly, first clear your session store:

```console
$ redis-cli -n 2 keys '*'
```

## Troubleshooting

A quick note, when you run into the configured max memory limit make sure that the necessary Redis keys are set to volatile (ensure an expire). Otherwise the complete allocated configured memory will fill up and Redis will 'crash'.

When your Redis instance memory is full, and a new write comes in, Redis evicts keys to make room for the write based on your instance's maxmemory policy. This is called the eviction policy.

In some cases we see that when Redis reaches the configured limit and tries to expire keys to make room, the eviction policy gets stuck in a loop. This means keys won’t be expired and Redis reaches its limit.

A temporary solution is to flush the Redis cache, you can do this by using the `flushall` command:

```console
$ redis-cli flushall
```

This will flush out all available Redis databases. Please keep in mind that this is only a temporary solution. The underlying cause is in the code of your application and needs to be permanently resolved.

A more extended how-to about configuring Redis caches can be found on the [Magento help pages](http://devdocs.magento.com/guides/v2.0/config-guide/redis/redis-pg-cache.html).

## Bots

As you know, the sessions of your webshop can also be stored in Redis. If you use Redis caching and store the sessions in Redis as well, you'll have to share the available Redis memory. This shouldn't be a problem on a regular basis, however we've seen scenarios wherein a shop stores its sessions in Redis and had some aggressive bots/crawlers visiting the shop. This resulted in a much larger amount of sessions to be stored in Redis than usual which is causing the Redis memory to fill up in no time, and crashes Redis.

You can check the bot traffic on your shop at any time on MageReport. If you want to get a more detailed insight in the bot traffic you can use the command `pnl --yesterday --php --bots --fields ua | sort | uniq -c | sort -n`to get an overview of the top 10 bots that visited your webshop yesterday. For more information about abuse bot check our [article](../../best-practices/performance/how-to-fix-performance-issues-caused-by-bots-and-crawlers.md).
