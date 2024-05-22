---
myst:
  html_meta:
    description: How to enhance your WordPress/WooCommerce site's performance using Redis. Discover the benefits of Redis, recommended plugins, and step-by-step installation instructions.
    title: How to Use Redis with WooCommerce and WordPress on Hypernode
redirect_from:
  - /en/ecommerce/woocommerce/how-to-use-redis-with-woocommerce-and-wordpress-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/ecommerce/woocommerce/how-to-use-redis-with-woocommerce-and-wordpress-on-hypernode/ -->

# How to Use Redis with WooCommerce and WordPress on Hypernode

Remote Dictionary Server (Redis) is an in-memory, persistent, key-value database known as a data structure server. Unlike similar servers, Redis can store and manipulate high-level data types such as lists, maps, sets, and sorted sets.

By storing important data in its memory, Redis ensures fast data retrieval, significantly boosting performance and reducing response times.

## Which Plugins Can We Use for Redis in WordPress/WooCommerce?

There are several plugins available for Redis. The two most commonly used are [Redis Object Cache](https://wordpress.org/plugins/redis-cache/) and [W3 Total Cache](https://wordpress.org/plugins/w3-total-cache/).

Due to the complexity of the cache module in "W3 Total Cache" and the possibility that you may already be using other cache plugins, we recommend the "Redis Object Cache" plugin.

## How to Install Redis Object Cache
Redis is already active on the server on port 6379.

Next, install the Redis Object Cache plugin via the WordPress Dashboard or using Composer. For detailed installation instructions, please refer to the standard installation procedure for WordPress plugins.

After installing and activating the plugin, navigate to `WordPress` -> `Settings` -> `Redis` or `Network Admin` -> `Settings` -> `Redis on Multisite networks`. Enable the cache and check if the plugin can connect automatically.