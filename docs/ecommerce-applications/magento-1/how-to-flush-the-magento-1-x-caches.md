---
myst:
  html_meta:
    description: There are multiple ways to flush your caches in Magento 1.x. Learn
      how to flush your cache via the Magento backend or the Commandline.
    title: How to flush Magento 1 caches? | Hypernode
redirect_from:
  - /en/ecommerce/magento-1/how-to-flush-the-magento-1-x-caches/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-flush-the-magento-1-x-caches/ -->

# How to Flush the Magento 1.x Caches

There are multiple ways to flush your caches in Magento 1.x

## Flush the Magento Cache via the Backend

The easiest way to flush your Magento cache is via the backend. After changing something via the backend you'll usualy need to flush one or more of the built-in caches. Follow the instructions below to flush individual caches

- Login to the Magento backend
- Go to `System` > `Cache Management`
- Click the checkbox of any cache that has been marked `Invalidated` or use one of the selection options above the list to select a group of caches
- Set the `Actions` dropdown to `Refresh` and click the `Submit` button

You can also flush all the caches at once by using either the `Flush Magento Cache` or `Flush Cache Storage` at the top of the page. On Hypernode it is safe to use either of these buttons since the `var/cache` folder that is used by Magento is not shared with any other applications.

## Flush the Magento Cache via the Commandline

Another way to flush the Magento caches is via the commandline using Magerun. You can use Magerun to flush specific caches or all caches at once.

With Magerun you can very easily retrieve a list of all caches and their respective status with the following command:

```bash
magerun cache:list
```

This will give you an overview similar to the one below:

```bash
+--------------------------------+---------+
| code                           | status  |
+--------------------------------+---------+
| config                         | enabled |
| layout                         | enabled |
| block_html                     | enabled |
| translate                      | enabled |
| collections                    | enabled |
| eav                            | enabled |
| config_api                     | enabled |
| config_api2                    | enabled |
| full_page                      | enabled |
+--------------------------------+---------+
```

To flush all of the aforementioned caches at once, simply use the command:

```bash
magerun cache:flush
```

To flush one single cache, for example `full_page` use the command:

```bash
magerun cache:flush full_page
```
