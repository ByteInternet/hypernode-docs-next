---
myst:
  html_meta:
    description: You can set MySQL variables for Magento by editing the initStatements.
      This way the variables won’t get lost after a MySQL restart or an upgrade.
    title: How to set MySQL variables globally for Magento 2 | Hypernode
redirect_from:
  - /en/support/solutions/articles/48001208261-how-to-set-mysql-variables-globally-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001208261-how-to-set-mysql-variables-globally-on-hypernode/ -->

# How to set MySQL variables globally on Hypernode

You can set MySQL variables for Magento in `~/magento2/app/etc/env.php` by editing the initStatements. This way the variables won’t get lost after a MySQL restart or an upgrade. Below you can find some examples on how to configure this in your env.php file.

Example configuration on how to change the innodb_lock_wait_timeout:

```nginx
'initStatements' => 'SET NAMES utf8; SET GLOBAL innodb_lock_wait_timeout = 200;',
```

Example configuration on how to change the SQL_mode:

```nginx
'initStatements' => 'SET NAMES utf8; SET GLOBAL sql_mode = "STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION";'
```

Example configuration on how to add multiple variables like changing the innodb_lock_wait_timeout and max_allowed_packet:

```nginx
'initStatements' => 'SET NAMES utf8; SET GLOBAL innodb_lock_wait_timeout = 200;SET GLOBAL max_allowed_packet=1048576;',
```
