---
myst:
  html_meta:
    description: Varnish is a complex technique that needs some experience to set
      it up. This article explains how you can configure Varnish for your Magento
      1 shop.
    title: How to configure Varnish for Magento 1? | Hypernode
redirect_from:
  - /en/ecommerce/magento-1/how-to-configure-varnish-for-magento-1-x/
  - /knowledgebase/varnish-on-magento1/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-configure-varnish-for-magento-1-x/ -->

# How to Configure Varnish for Magento 1.x

Customers with Hypernode Pelican, Falcon (formerly known as Professional) and Eagle (formerly known as Excellence) plans can use Varnish to boost their Magento shop. To manage and configure Varnish for Magento 1.x you’ll need Turpentine. This article explains how you can configure Varnish for your Hypernode. Do you have a Magento 2.x shop, please check [this article](../../ecommerce-applications/magento-2/how-to-configure-varnish-for-magento-2-x.md)

Although Varnish is extremely awesome when it get's to speeding up websites, Varnish is a complex technique that needs some experience to set it up. Don't implement Varnish on production nodes while still under development but use [development node](../../hypernode-platform/tools/how-to-use-hypernode-development-plans.md) or a local staging environment like the [Hypernode Docker](../../best-practices/testing/hypernode-docker.md) instead.

## Table of Contents

- [Enable Varnish for Magento 1.x](#enable-varnish-for-magento-1x)
  - [All Customers: Via the hypernode-systemctl CLI Tool](#all-customers-via-the-hypernode-systemctl-cli-tool)
  - [Dutch Customers: Via Your Service Panel](#dutch-customers-via-your-service-panel)
  - [International Customers: Via Your Control Panel](#international-customers-via-your-control-panel)
- [Install Turpentine](#install-turpentine)
  - [Configure Turpentine](#configure-turpentine)
- [Test Your Shop With Varnish](#test-your-shop-with-varnish)
- [Enable Debug Headers](#enable-debug-headers)
- [Warming Your Cache](#warming-your-cache)
- [Troubleshooting](#troubleshooting)

## Enable Varnish for Magento 1.x

Before installing Turpentine we recommend enabling Varnish on your Hypernode using the instructions below.

### All Customers: Via the hypernode-systemctl CLI Tool

Activating Varnish and set which version to use on your Hypernode can be done via the [hypernode-systemctl tool](../../hypernode-platform/tools/how-to-use-the-hypernode-systemctl-cli-tool.md).

### Dutch Customers: Via Your Service Panel

Only *Dutch customers* can also easily activate Varnish via their [Service Panel](https://service.byte.nl/). Go to `Instellingen` and change Varnish to `Actief`. Once you’ve changed this setting and enabled Varnish in Magento, Varnish will store all information in it’s own cache. Only when Varnish needs data that hasn’t been cached it will connect with the server.

### International Customers: Via Your Control Panel

English speaking customers who ordered their Hypernode via Hypernode.com have access to their [control panel](https://my.hypernode.com/). Find your Hypernode, click on `Settings` and go to `Caching`. There you can enable Varnish with 1 click on the button.

## Install Turpentine

Installing Turpentine works best with the Magento Connect Manager:

- Log on to your backend
- Navigate to System > Magento Connect > Magento Connect Manager
- Fill in your admin credentials
- Paste the following key in the field next to **Paste extension key to install**: `http://connect20.magentocommerce.com/community/Nexcessnet_Turpentine`
- Install
- Click *Proceed*
- Turpentine will now be installed
- Log off and on again so Turpentine will appear in your admin
- Flush your Magento cache via the backend (System → Cache Management)

When the Magento Connect Manager is not available, Turpentine needs to be installed manually:

- Download and install the tarball package from the [Downloads page on GitHub](https://github.com/nexcess/magento-turpentine) (note that this is not the "Download as tar.gz" option) and install through Magento Connect Downloader or Magento's `mage` command.
- Install with [Modman](https://github.com/colinmollenhour/modman). You would just need to use: `modman clone https://github.com/nexcess/magento-turpentine.git`

*Note*: If you install with `modman`, you should also set `System > Configuration > Developer > Template Settings > Allow Symlinks` to "Yes".

### Configure Turpentine

After installing Turpentine and flushing the Magento cache, you can start configuring Turpentine:

- Log on to your [Byte Service Panel](http://auth.byte.nl)
- Select your Hypernode plan
- Click on the tab **Instellingen**
- Select the option `Varnish`
- You’ll notice Varnish cache is non-active. This is necessary for testing your shop with Varnish. (See `Test your shop with Varnish` below)
- Don’t close this page, you’ll need this information later
- Log on to your Magento backend
- Navigate to System -> Configuration
- Select **Varnish Options** under `Turpentine`
- In the `Servers`section, fill in the following information:
  - *Varnish version*: leave this on `auto`
  - *Varnish server list*: varnish:6082
  - *Varnish authentication key*: Paste the content from your Service Panel here
- Select `Caching Options` under `Turpentine`
- Check if the following information is correct:
  - *Backend host*: This should say `varnish`
  - *Backend port*: This should say `8080`
  - *Crawler ip's*: Remove `localhost`/`127.0.0.1` from the crawler ip's
- Navigate to System -> Cache Management
- Enable **>Varnish Pages** and **>Varnish ESI Blocks**
- Click **Apply Varnish Config** below to complete the configuration

## Test Your Shop With Varnish

We highly recommend you to test Varnish on a staging environment first. This way you’ll make sure your shop is completely optimized and ready to use Varnish.

There are 2 ways to create a Hypernode staging environment for testing Varnish;

1. [Hypernode development plan](../../hypernode-platform/tools/how-to-use-hypernode-development-plans.md)
1. The [Hypernode Docker](../../best-practices/testing/hypernode-docker.md)

We recommend you to use a development node (which can be cancelled any time). **A basic staging environment doesn’t work well with Varnish.**

## Enable Debug Headers

If you want debugging headers, please remember to enable those in the admin backend under Varnish settings.![](_res/BJj7akZFXFDSDdvPGDrQQM0i8qbLu6NBjg.png)

**Depending on the version of turpentine you use, sometimes it's needed to add your ip to the `debug_acl` in the `vcl`. This enabled debug headers for your IP address.**

## Warming Your Cache

Turpentine is shipped with a cache warmer. To use this script copy it to your home directory:

```bash
mkdir -p ~/bin; cp ~/public/.modman/magento-turpentine/util/warm-cache.sh ~/bin/

```

Now you can warm your Varnish cache by retrieving the `sitemap.xml`:

```bash
~/bin/warm-cache.sh -u http://example.com/magento/sitemap.xml

```

This will crawl all URLs defined in the `sitemap.xml`:

```bash
app@gz20le-support-magweb-do:~$ bash ~/bin/warm-cache.sh -u https://example.com/sitemap.xml
Getting URLs from sitemap...
Warming 152 URLs using 2 processes...
HTTP/1.1 200 0.87 secs: 18320 bytes ==> /kamelen.html
HTTP/1.1 200 1.34 secs: 14710 bytes ==> /dromedarissen.html
HTTP/1.1 200 0.75 secs: 17726 bytes ==> /geiten.html
HTTP/1.1 200 0.74 secs: 17974 bytes ==> /tux.html
HTTP/1.1 200 0.79 secs: 14856 bytes ==> /vogelbekdier.html

```

## Troubleshooting

If your Varnish setup is not working over SSL, check [this article](../../hypernode-platform/ssl/how-to-use-ssl-certificates-on-your-hypernode-when-ordered-via-hypernode-nl.md#redirecting-to-https-when-using-varnish).
