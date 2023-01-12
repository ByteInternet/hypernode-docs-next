---
myst:
  html_meta:
    description: 'In this article we will explain how to configure Lesti::FPC and
      how to use it on Hypernode. '
    title: How to Configure Lesti::FPC? | Hypernode
redirect_from:
  - /en/hypernode/tools/how-to-configure-lesti-fpc/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-configure-lesti-fpc/ -->

# How to Configure Lesti::FPC

Lesti::FPC is a FPC Full Page Caching module you can use to speed up the frontend of your shop.

More information about the internals of the module can be found on [the website of the developer of the module, Gordon Lesti.](https://gordonlesti.com/lesti-fpc-documentationversion-1-4-5/)

A tutorial on how it works is available on the page [How does Lesti::FPC work](https://gordonlesti.com/how-does-lesti-fpc-work/).

This module also works in combination with `Redis`.

This article will explain how to configure Lesti::FPC and use it on Hypernode. It is however recommended to first enable [Redis Cache](../../ecommerce-applications/magento-1/how-to-configure-redis-for-magento-1.md) as your caching backend before proceeding with this tutorial.

**NB: When you used the [hypernode-importer](how-to-migrate-your-shop-to-hypernode.md#option-2-for-all-customers-migrate-your-shop-via-shell-using-the-hypernode-importer) and you were already using `Lesti::FPC`, you can skip this tutorial, as we already added the configuration for caching using `Lesti::FPC`.**

## Download Lesti::FPC

Go to your public folder:

```bash
cd /data/web/public
```

If the `~/public/.modman` directory is not present, initialise modman to create the directory:

```bash
modman init
```

Use the following command to install the Lesti::FPC module on your shop:

```bash
modman clone git://github.com/GordonLesti/Lesti_Fpc.git
```

## Move the Files to the Correct Folder

Go to the .modman/Lesti_Fpc/app/etc folder and copy the fpc.xml.sample to the `app/etc` directory and rename it to fpc.xml:

```bash
cd ~/public/.modman/Lesti_Fpc/app/etc && cp fpc.xml.sample /data/web/public/app/etc/fpc.xml
```

## Edit Your fpc.xml File

Open the file and delete everything between the `<fpc>` and `</fpc>` tags.

In between the `<fpc>` and `</fpc>` tags, add the `lifetime`, `backend` and `backend_options`:

```xml
<fpc>
  <lifetime>86400</lifetime>
  <backend>Cm_Cache_Backend_Redis</backend>
  <backend_options>
    <server>redismaster</server>
    <port>6379</port>
    <persistent></persistent>
    <database>1</database>
    <password></password>
    <force_standalone>0</force_standalone>
    <connect_retries>1</connect_retries>
    <lifetimelimit>86400</lifetimelimit>
    <read_timeout>10</read_timeout>
    <compress_data>1</compress_data>
    <compress_tags>1</compress_tags>
    <compression_lib>gzip</compression_lib>
  </backend_options>
</fpc>
```

Enable FPC caching in your Magento backend.

Flush your cache after making these adjustments.

## Warm Your Full Page Cache

To warm your full page cache, see the page about cache warming.
