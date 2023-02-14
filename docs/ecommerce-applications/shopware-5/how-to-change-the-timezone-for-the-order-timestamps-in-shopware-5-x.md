---
myst:
  html_meta:
    description: The solution is quite simpel. There is a free plugin for Shopware
      5 which allows you to correct the timestamps of the orders.
    title: Change the timezone for order timestamps in Shopware 5
redirect_from:
  - /en/support/solutions/articles/48001166328-how-to-change-the-timezone-for-the-order-timestamps-in-shopware-5-x/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001166328-how-to-change-the-timezone-for-the-order-timestamps-in-shopware-5-x/ -->

# How to Change the Timezone for the Order Timestamps in Shopware 5.x

As you probably know, the world is divided in a bunch of time zones. Because Hypernode is hosted in the cloud, the system timezone is set to UTC. This is because we cannot always know in what timezone the server will be hosted, but we want to deliver a consistent system timezone for our customers.

Because the system timezone, and therefore the MySQL timezone as well, is set to UTC. The order timestamps might not match with the timezone that applies to your shop. So you will probably want to change the MySQL timezone for the correct order timestamps.

The solution is quite simpel. There is a free [**plugin for Shopware 5**](https://store.shopware.com/en/bauer34122590788f/order-timestamp-correction-mysql-server-with-utc.html) which allows you to correct the timestamps of the orders.
