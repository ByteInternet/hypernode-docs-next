---
myst:
  html_meta:
    description: How to enhance your WordPress/WooCommerce site's performance using
      Redis. Discover the benefits of Redis, recommended plugins, and step-by-step
      installation instructions.
    title: How to Use Redis with WooCommerce and WordPress on Hypernode
---

# How to Use Redis with WooCommerce and WordPress on Hypernode

Remote Dictionary Server (Redis) is an in-memory, persistent, key-value database known as a data structure server. Unlike similar servers, Redis can store and manipulate high-level data types such as lists, maps, sets, and sorted sets.

Because Redis stores data in memory, it can return frequently requested data very quickly. This can improve the performance of WordPress and WooCommerce by reducing database load and speeding up response times.

## Which Plugins Can We Use for Redis in WordPress/WooCommerce?

There are several plugins available for Redis. The two most commonly used are [Redis Object Cache](https://wordpress.org/plugins/redis-cache/) and [W3 Total Cache](https://wordpress.org/plugins/w3-total-cache/).

Due to the complexity of the cache module in "W3 Total Cache" and the possibility that you may already be using other cache plugins, we recommend the "Redis Object Cache" plugin.

## How to set a TTL on Redis keys

BBy default, most Redis plugins for WordPress do not set a TTL (time to live) on keys stored in Redis. This means cached keys may remain in memory indefinitely, which can eventually fill up Redis memory and lead to performance issues or downtime.

To set a TTL for all keys stored in Redis, add the following lines to your wp-config.php file:

```console
define('WP_REDIS_PREFIX', 'example');
define('WP_REDIS_MAXTTL', '900');
define('WP_REDIS_SELECTIVE_FLUSH', true);
```

```{important}
Be sure to change the example prefix to a unique name for your application so Redis keys do not get mixed up when Redis is used by multiple applications on the same Hypernode.
```

### Explanation of the wp-config.php options

- **WP_REDIS_PREFIX** adds a clear prefix to your Redis keys. This helps prevent key collisions, especially when multiple applications use Redis.
- **WP_REDIS_MAXTTL** sets a maximum lifetime for cached items, in this example 900 seconds.
- **WP_REDIS_SELECTIVE_FLUSH**\* ensures that only keys related to this WordPress installation are flushed, instead of clearing the entire Redis database.

## How to Install Redis Object Cache

Redis is already available on Hypernode and listens on port 6379.

Install the Redis Object Cache plugin through the WordPress Dashboard or with Composer. For general plugin installation steps, see the standard WordPress plugin installation documentation.

After installing and activating the plugin, go to Settings -> Redis or Network Admin -> Settings -> Redis on Multisite networks

Enable object caching and verify that the plugin connects to Redis automatically.

If the plugin does not connect automatically, check whether Redis is reachable on 127.0.0.1:6379 and confirm that your WordPress configuration does not override the default connection settings.
