---
myst:
  html_meta:
    description: 'In this article we will explain how to configure a large MySQL thread_stack
      in detail. '
    title: How to configure a large MySQL thread stack? | Hypernode
redirect_from:
  - /en/hypernode/mysql/how-to-configure-a-large-mysql-thread-stack/
---

<!-- source: https://support.hypernode.com/en/hypernode/mysql/how-to-configure-a-large-mysql-thread-stack/ -->

# How to Configure a Large MySQL thread_stack

While on Hypernode you have full admin privileges on your entire MySQL database, it is not possible to change root-owned MySQL related config files. This means that you can configure any runtime setting, but settings that go in the `mysqld.conf` and need to be defined at start-up time or settings that you don’t want to re-apply every time MySQL is restarted sometimes can’t be set by the unprivileged `app` user.

To facilitate some type of flexibility regarding these settings anyway we have a set of MySQL related opt-in settings that can be set using the [hypernode-api](https://community.hypernode.io/#/Documentation/hypernode-api/settings/README) or using the `hypernode-systemctl` command-line tool (which implements this API).

## Enabling a Larger thread_stack

On a Hypernode you can enable the larger `thread_stack` by running this command:

```nginx
$ hypernode-systemctl settings mysql_enable_large_thread_stack --value True
```

You can then check the progress of your change by running:

```nginx
hypernode-log  # or 'livelog' for an auto-updating variant of that command
```

Once the setting has been activated you will see the configuration file change on disk:

```nginx
# Before
$ cat /etc/mysql/conf.d/mysql-master.cnf | grep thread
thread_cache_size       = 256
innodb_read_io_threads          = 8
innodb_write_io_threads         = 8

# After
$ cat /etc/mysql/conf.d/mysql-master.cnf | grep thread
thread_cache_size       = 256
thread_stack                    = 512K
innodb_read_io_threads          = 8
innodb_write_io_threads         = 8
```

You might need to restart MySQL to load the new configuration:

```nginx
$ hypernode-servicectl restart mysql
```

To check the size of your active `thread_stack` you can run this MySQL query:

```nginx
# Before
$ mysql -e "SHOW GLOBAL VARIABLES LIKE 'thread_stack';"
+---------------+--------+
| Variable_name | Value  |
+---------------+--------+
| thread_stack  | 196608 |
+---------------+--------+

# After
$ mysql -e "SHOW GLOBAL VARIABLES LIKE 'thread_stack';"
+---------------+--------+
| Variable_name | Value  |
+---------------+--------+
| thread_stack  | 524288 |
+---------------+--------+
```

## Hypernode Docker

Note that if you want to change this setting in a [hypernode-docker](https://github.com/byteinternet/hypernode-docker) instead of on your production Hypernode you will not be able to use the `hypernode-systemctl` command-line tool, as that tool talks to the `hypernode-api` which for obvious reasons is not connected to your local Docker environment. If you would like to change this setting in your local Docker as well, you can simply edit `/etc/mysql/conf.d/mysql-master.cnf` as the `root` user and add the `thread_stack` line and [restart the services](https://github.com/byteinternet/hypernode-docker#restarting-services).

## Shopware

We’ve noticed that for some larger Shopware installations the default `thread_stack` size can become an issue. If you have the memory to spare changing the MySQL thread_stack from the default `192K` to `512K` might be a good solution (or at least quick fix to identify your problem).

In Shopware the [search index & keywords tables](https://developers.shopware.com/developers-guide/shopware-5-performance-for-devs/) have been seen to require a larger `thread_stack` in some configurations. We’ve seen issues where queries on these aggregate tables started to cause issues in shops with north of 40K SKU’s during a search reindexation.

If you encounter these types of errors:

```nginx
SQLSTATE[HY000]: General error: 1436 Thread stack overrun: 180608 bytes used of a 196608 byte stack, and 16000 bytes needed. Use 'mysqld --thread_stack=#' to specify a bigger stack.
```

It might be a good idea to enable this feature and see if this setting addresses your issue.
