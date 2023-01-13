---
myst:
  html_meta:
    description: There are multiple ways to flush your caches in Magento 2.x. Learn
      how to flush your cache via the Magento backend or the Commandline.
    title: How to flush Magento 2 caches? | Hypernode
redirect_from:
  - /en/ecommerce/magento-2/how-to-flush-the-magento-2-x-caches/
  - /knowledgebase/magento-cache-management/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-flush-the-magento-2-x-caches/ -->

# How to Flush the Magento 2.x Caches

There are multiple ways to flush your caches in Magento 2.x

## Flush the Magento Cache via the Backend

The easiest way to flush your Magento cache is via the backend. After changing something via the backend you'll usualy need to flush one or more of the built-in caches. Follow the instructions below to flush individual caches

- Login to the Magento backend
- Go to `System` > `Tools` > `Cache Management`
- Click the checkbox of any caches that you wish to flush
- Set the `Action` dropdown to `Refresh` and click the `Submit` button

You can also flush all the caches at once by using either the `Flush Magento Cache` or `Flush Cache Storage` at the top of the page. On Hypernode it is safe to use either of these buttons since the `var/cache` folder that is used by Magento is not shared with any other applications.

## Flush the Magento Cache via the Commandline

### Use Magerun to Flush the Cache

**When using Magerun for Magento 2.x you need to make sure that you run it in the folder where you installed Magento 2.x.**

Another way to flush the Magento caches is via the commandline using Magerun. You can use Magerun to flush specific caches or all caches at once.

With Magerun you can very easily retrieve a list of all caches and their respective status with the following command:

```bash
magerun2 cache:list
```

This will give you an overview similar to the one below:

```bash
  Magento Cache Types

+------------------------+--------------------------------+---------+
| Name                   | Type                           | Enabled |
+------------------------+--------------------------------+---------+
| config                 | Configuration                  | 1       |
| layout                 | Layouts                        | 1       |
| block_html             | Blocks HTML output             | 1       |
| collections            | Collections Data               | 1       |
| reflection             | Reflection Data                | 1       |
| db_ddl                 | Database DDL operations        | 1       |
| eav                    | EAV types and attributes       | 1       |
| customer_notification  | Customer Notification          | 1       |
| full_page              | Page Cache                     | 1       |
| config_integration     | Integrations Configuration     | 1       |
| config_integration_api | Integrations API Configuration | 1       |
| translate              | Translations                   | 1       |
| config_webservice      | Web Services Configuration     | 1       |
+------------------------+--------------------------------+---------+
```

To flush all of the aforementioned caches at once, simply use the command:

```bash
magerun2 cache:flush
```

To flush one single cache, for example `full_page` use the command:

```bash
magerun2 cache:flush full_page
```

### Use the Magento Commandline to Flush the Cache

Magento 2.x offers a third option for flushing the Magento caches using the commandline tool. This tool can be called upon from the Magento root-directory and works in a similar way to Magerun, but with slightly different commands

To flush all of the aforementioned caches at once, simply use the command:

```bash
php bin/magento cache:flush
```

To flush one single cache, for example `full_page` use the command:

```bash
php bin/magento cache:flush full_page
```
