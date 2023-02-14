---
myst:
  html_meta:
    description: Sometimes when debugging complex performance issues, it can be useful
      to log all database queries to a log file. Learn how to do this in Magento 1.
    title: How to enable MySQL query logging for Magento 1? | Hypernode
redirect_from:
  - /en/ecommerce/magento-1/how-to-enable-mysql-query-logging-for-magento-1-x/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-enable-mysql-query-logging-for-magento-1-x/ -->

# How to Enable MySQL Query Logging for Magento 1.x

Sometimes when debugging complex performance issues, it can be useful to log all database queries to a log file.

Superusers are used to do this changing the query logging settings of the MySQL server.

As enabling this requires root permissions, this functionality is not available to Hypernode users.

Luckily Magento provides it's own mechanism to log all queries in a log file.

## Enabling Query Debug Logging in Magento

To turn on Magento's own query logging mechanism, edit `/data/web/public/lib/Varien/Db/Adapter/Pdo/Mysql.php:`

Now look for the line containing `$_debug` and change `false` to `true`:

```nginx
protected $_debug = true;
```

Sometimes you need to flush your cache before the first queries are logged.

## Log Destination

By default, Magento logs to the `/data/web/public/var/debug/pdo_mysql.log`

**Warning: Turning query logging on is very resource intensive and causes the show to slow down considerably! Don't forget to change `$_debug` to `false` when you are done debugging your issue.**
