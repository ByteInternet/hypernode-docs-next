---
myst:
  html_meta:
    description: This article will explain how to configure Redis on your Magento
      1 shop on Hypernode and how to work with redis-cli. Learn all you need to know
      in this article!
    title: How to configure Redis for Magento 1? | Hypernode
redirect_from:
  - /en/ecommerce/magento-1/how-to-configure-redis-for-magento-1/
  - /knowledgebase/configure-sessions-redis-magento1/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-configure-redis-for-magento-1/ -->

# How to Configure Redis for Magento 1

Redis is a caching method which can increase the speed of the backend and frontend of your shop. On Hypernode every customer has access to Redis cache, starting from 64 MB, depending on the plan. This article will explain how to configure Redis on your Magento 1 shop on Hypernode and how to work with redis-cli.

**NB: When you used the [hypernode-importer](../../hypernode-platform/tools/how-to-migrate-your-shop-to-hypernode.md#how-to-migrate-your-shop-to-hypernode) and you were already using Redis you don't have to follow this tutorial.**

Want to know how to configure Redis in Magento 2? Have a look at [this article](../../ecommerce-applications/magento-2/how-to-configure-redis-for-magento-2.md)!

## Setup Redis by Changing your local.xml File

**NB: When you're using a Magento version newer than 1.8.x, you can use the built-in Redis module and simply copy and paste the below snippet. If you're still using an older version than 1.8.x than you need to first [download the Redis Extension.](#download-the-redis-extension-from-collin-mollenhour-from-github-for-magento-versions-older-than-18x)**

Open your local.xml file and paste the next lines of code after the tag:

```nginx
   <cache>
       <backend>Cm_Cache_Backend_Redis</backend>
       <backend_options>
          <server>redismaster</server>
          <port>6379</port>
          <persistent></persistent>
          <database>0</database>
          <password></password>
          <force_standalone>0</force_standalone>
          <connect_retries>1</connect_retries>
          <read_timeout>10</read_timeout>
          <automatic_cleaning_factor>0</automatic_cleaning_factor>
          <compress_data>1</compress_data>
          <compress_tags>1</compress_tags>
          <compress_threshold>20480</compress_threshold>
          <compression_lib>gzip</compression_lib>
       </backend_options>
  </cache>
```

Flush your cache after making these adjustments:

```nginx
n98-magerun cache:flush

```

## Download the Redis Extension From Collin Mollenhour from Github for Magento Versions Older than 1.8.x

**NB: If you're using a Magento version later than 1.8.x, you can use the built-in Redis module as described above.**

Follow these steps to change your caching backend to Redis:

- Go to your public folder: `/data/web/public`
- Use the following commands to install the Redis module on your shop:
- `modman init`
- modman clone git://github.com/colinmollenhour/Cm_Cache_Backend_Redis.git
- Redis is now installed on your shop.

## Use the redis-cli Command

On Hypernode you can use the redis-cli command to get more information out of the Redis server. All the available commands can be found on the [Command](http://redis.io/commands) page of the Redis website. Below are some examples:

- Flush all keys in all databases:

```nginx
n98-magerun cache:flush

```

- Flush all keys in database 0 or database 1 respectively:

```nginx
redis-cli flushall
```

- Flush all keys in database 0 or database 1 respectively:

```nginx
redis-cli -n 0 flushdb
redis-cli -n 1 flushdb
```

- Check how much Redis Cache you're currently using

```nginx
redis-cli info | grep used_memory_human
```

- List all stored keys

```nginx
redis-cli --scan
```

## Choosing the Right Database

If you use both a staging environment and a production site, pick the databases carefully. Using the same Redis databases for both production and development can cause unexpected behaviour on both sites.

Example:

| Environment | DB type       | Redis Database |
| ----------- | ------------- | -------------- |
| production  | Magento Cache | 0              |
| production  | Magento FPC   | 1              |
| production  | Sessions      | 2              |
| staging     | Magento Cache | 3              |
| staging     | Magento FPC   | 4              |
| staging     | Sessions      | 5              |

## Changing the Compression Library

It is possible to use the compression library 'Snappy' on Hypernode. More information about Snappy can be found in the changelog: [Release-4224](https://changelog.hypernode.com/changelog/release-4224/).

In order to use the compression library Snappy for your Redis cache you need to change `gzip` to `snappy`in your local.xml.

## Configure Magento 1 to Use Redis as the Session Storage

You can use Redis for storing sessions too!

Hypernode plans bigger than Magento Grow, often have enough memory to store the session data in Redis.
This way sessions are stored in-memory, making the shop faster and use less IO than when using MySQL or files as session store.

### Install `Cm_RedisSession`

First install the Redis sessions plugin from Gordon Lesti to enable session storage in Redis:

```
modman clone https://github.com/colinmollenhour/Cm_RedisSession
```

### Configure Magento 1 to Store Your Sessions in Redis

To save your sessions for Magento add/change the following settings in your local.xml:

```
<session_save>db</session_save>
	<redis_session>
		<host>redismaster</host>
        <port>6379</port>
        <password></password>
        <timeout>2.5</timeout>
        <persistent></persistent>
        <db>2</db>
        <compression_threshold>2048</compression_threshold>
        <compression_lib>gzip</compression_lib>
        <log_level>1</log_level>
        <max_concurrency>6</max_concurrency>
        <break_after_frontend>5</break_after_frontend>
        <fail_after>10</fail_after>
        <break_after_adminhtml>30</break_after_adminhtml>
        <first_lifetime>600</first_lifetime>
        <bot_first_lifetime>60</bot_first_lifetime>
        <bot_lifetime>7200</bot_lifetime>
        <disable_locking>0</disable_locking>
        <min_lifetime>60</min_lifetime>
		<max_lifetime>2592000</max_lifetime>
   	</redis_session></code></pre>
```

Now flush your cache:

```
rm -rf /data/web/public/var/cache/* redis-cli flushall
```

### Enable Second Redis Instance for Sessions

We have made is possible to enable a second Redis instance more tailored for saving session data (more informatie can be found in our [changelog](https://changelog.hypernode.com/changelog/experimental-changes-redis-sessions-aws-performance/))

To enable the second Redis instance for sessions you run the command: `hypernode-systemctl settings redis_persistent_instance --value True`

After enabling the second Redis instance you need to update the `/data/web/public/app/etc/local.xml` file and change the port value to `6378` instead of the default `6379`. Furthermore you need to add the following line to your crontab:

`* * * * * redis-cli -p 6378 bgsave`

### Test Whether Your Sessions Are Stored in Redis

To verify whether your configuration is working properly, first clear your session store:

```
rm /data/web/public/var/session/*
```

Now open the site in your browser and hit `F5` a few times or log in to the admin panel.

If all is well, no additional sessions files should be written to `/data/web/var/sessions`, but instead to the Redis database:

```
redis-cli -n 2 keys \*
```

## Troubleshooting

A quick note, when you run into the configured max memory limit make sure that the necessary Redis keys are set to volatile (ensure an expire). Otherwise the complete allocated configured memory will fill up and Redis will 'crash'.

When your Redis instance memory is full, and a new write comes in, Redis evicts keys to make room for the write based on your instance’s maxmemory policy. This is called the eviction policy.

In some cases we see that when Redis reaches the configured limit and tries to expire keys to make room, the eviction policy gets stuck in a loop. This means keys won’t be expired and Redis reaches it limit.

A temporary solution is to flush the Redis cache, you can do this by using the flushall command:

```nginx
 redis-cli flushall
```

This will flush out all available Redis databases. Please keep in mind that this is only a temporary solution. The underlying cause is in the code of your application and needs to be permanently resolved.

## Bots

As you know, the sessions of your webshop can also be stored in Redis. If you use Redis caching and store the sessions in Redis as well, you’ll have to share the available Redis memory. This shouldn’t be a problem on a regular basis, however we’ve seen scenarios wherein a shop stores its sessions in Redis and had some aggressive bots/crawlers visiting the shop. This resulted in a much larger amount of sessions to be stored in Redis than usual which is causing the Redis memory to fill up in no time, and crashes Redis.

You can check the bot traffic on your shop at any time on MageReport. If you want to get a more detailed insight in the bot traffic you can use the command `pnl --yesterday --php --bots --fields ua | sort | uniq -c | sort -n` to get an overview of the top 10 bots that visited your webshop yesterday. For more information about abuse bot check our [article](../../best-practices/performance/how-to-fix-performance-issues-caused-by-bots-and-crawlers.md).
