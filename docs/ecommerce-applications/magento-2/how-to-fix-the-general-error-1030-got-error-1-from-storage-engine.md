---
myst:
  html_meta:
    description: You can simply follow the instructions in this article to make sure
      that all the categories and products will be visible again on the frontend of
      your webshop.
    title: How to fix the general error 1030 in Magento 2? | Hypernode
redirect_from:
  - /en/ecommerce/magento-2/how-to-fix-the-general-error-1030-got-error-1-from-storage-engine/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-fix-the-general-error-1030-got-error-1-from-storage-engine/ -->

# How to Fix the "General error: 1030 Got error 1 from storage engine"

## What Is the Issue

In some very rare occassions an up- or downgrade results in some of your categories and/or product not showing on the frontend of your webshop. When this happens you will usually come across an error like the one below in `/data/web/magento2/var/report/1234567890`:

```console
app@83f0vz-jesper-magweb-cmbl:/data/web/magento2/var/report$ cat 191158599534
{"0":"SQLSTATE[HY000]: General error: 1030 Got error 1 from storage engine, query was: SELECT `main_table`.*, count(main_table.value) AS `count` FROM (SELECT `main_table`.`category_id` AS `value` FROM `catalog_category_product_index_store1` AS `main_table`\n INNER JOIN `search_tmp_5fbf5581f1df68_75800387` AS `entities` ON main_table.product_id  = entities.entity_id\n INNER JOIN `catalog_category_entity` A
```

## How to Fix the Issue

Luckily the fix is quite an easy one. You can simply follow the instructions below to make sure that all the categories and products will be visible again on the frontend of your webshop:

1. First make a backup of your current database by running the command `mysqldump [databasename] > /data/web/databasename_backup_YYYYMMDD.sql`. This step is to make sure that you will still have all your data in case you make a mistake in the next steps.
1. Check what database is being used by your Magento installation. You can find this in the `env.php` of your Magento installation.
1. Log in to the MySQL commandline with the command: `mysql` and open the database used by Magento with the command: `use databasename;`
1. Now it is time for the *scary* part. First show all the tables within the database with the command: `show tables;`. Now look for all the tables similar to **catalog_category_product_index_store1** and their **replica**. Once you have a list of all these tables (e.g. store1, store1_replica, store2, store2_replica, etc.) you need to drop these tables with the command: `drop table catalog_category_product_index_store1;` and `drop table catalog_category_product_index_store1_replica;`. You need to run this command for all the different **catalog_category_product_index_store**+**number**tables.
1. Once you have dropped all these tables all that is left to do is to run a reindex using the command `bin/magento indexer:reindex` from within your Magento2 root directory (on Hypernode this is usually `/data/web/magento2)`.
