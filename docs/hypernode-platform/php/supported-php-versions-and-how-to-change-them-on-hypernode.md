---
myst:
  html_meta:
    description: On Hypernode you can choose from a range of PHP versions. Check out
      which ones and how to change them here.
    title: Support PHP versions and how to change them on Hypernode
redirect_from:
  - /en/hypernode/php/supported-php-versions-and-how-to-change-them-on-hypernode/
  - /knowledgebase/php-versions-magento-shop-hypernode/
---

<!-- source: https://support.hypernode.com/en/hypernode/php/supported-php-versions-and-how-to-change-them-on-hypernode/ -->

# Supported PHP Versions and How to Change Them on Hypernode

On Hypernode you can choose from a range of PHP versions. Check out which ones and how to change them here.

## Available PHP Versions on Hypernode

On Hypernode you can choose from a range of PHP versions:

- **PHP 8.1** (Fully supported)\*
- **PHP 7.4** (Fully supported)
- **PHP 7.3** (Security updates only since 6 Dec 2020)
- **PHP 7.2** (EOL, No updates since 10 Nov 2020)
- **PHP 7.1** (EOL, No updates since 1 Dec 2019)
- **PHP 7.0**(EOL, No updates since 3 Dec 2018, deprecated)
- **PHP 5.6**(EOL, No updates since 31 Dec 2018, deprecated, we strongly recommend you to upgrade, will likely be phased out by us somewhere in 2022)

You can easily switch the PHP version of your Hypernode, but please thoroughly test a PHP change before implementing it on a live environment!

\*Some things to keep in mind: at this point in time with PHP 8.1 you will not be able to use Ioncube, New Relic or Blackfire. If you test out PHP 8.1 and things don’t work as you expect, you of course can switch back to a previous version.

## How to Check the PHP Version you Use on Hypernode

There are several methods to see what version you're using on Hypernode. The fastest method is to run the following command through the command line:

```nginx
php -v
```

If you can't easily access the command line, you can place a file named 'phpinfo.php' in /data/web/public, containing the following code:

```nginx
<?php
phpinfo();
```

Then when you access this file, either via your Hypernode at `example.hypernode.io/phpinfo.php`, or on your website at `www.example.com/phpinfo.php`, you can find the PHP version in the top. Don't forget to remove this file after you're done, as this is not something that should be left available.

## Changing the PHP Version you Use on Hypernode

It's quite easy to change the PHP version used on your Hypernode. You can change this at any time, and upgrade and downgrade as needed. Please note that each change may take up to 10 minutes to be applied to your Hypernode, so keep that in mind when testing.

### Via the hypernode-systemctl Tool

The easiest way to switch is by using the [hypernode-systemctl tool](../tools/how-to-use-the-hypernode-systemctl-cli-tool.md).

To see what version your Hypernode is configured with, you can run the following command:

```nginx
hypernode-systemctl settings php_version
```

To see what versions are available, you can use this command:

```nginx
hypernode-systemctl settings php_version list
```

To upgrade to another version simply provide the version like so:

```nginx
hypernode-systemctl settings php_version 8.1
```

Afterwards you can use the livelog command to track progress of the upgrade.

### Via the Service Panel

You can also switch the PHP version of a Hypernode via the Service Panel (service.byte.nl)

1. Log in to your Service Panel.
1. Select your Hypernode by clicking the app name.
1. Go to tab **Instellingen**.
1. Click the **PHP.**
1. Choose a PHP version.

Afterwards you can navigate back to 'Hypernode Log' option, to track progress of the upgrade.

### Via your Control Panel

Via the Control Panel you can change the PHP version by following the following steps

1. Log on to your Control Panel.
1. Select the Hypernode.
1. Hover over Hypernode in the sidebar on the left and select **PHP Settings**.
1. Choose a PHP version and click **Change.**

Afterwards it may take up to 10 minutes before your upgrade has completed.

## Testing a PHP Version

Unfortunately it is not possible to test with 2 PHP versions on one Hypernode. Before switching your PHP version we recommend you to test your shop to see if everything works as it should in the new PHP version. Testing your shop without having your customers notice anything can be done with [Docker for Hypernode](../../best-practices/testing/hypernode-docker.md). Docker is a tool that gives you the opportunity to set up a virtual staging environment. You can also temporarily order a [Hypernode development package](../tools/how-to-use-hypernode-development-plans.md) to test your shop on.

## The Importance of Upgrading PHP

An important part of maintaining a Magento shop is upgrading software regularly. By upgrading we do not only mean upgrading Magento and all its extensions and plugins in use, but also upgrading server-side software, tools - and scripting language like PHP.

It is always recommended to stay up-to-date and not only because you benefit from improvements and bug fixes. By taking small steps at the time you will save much time and effort in the long term, as upgrading at once from a very outdated release to the latest release will very likely result in errors.

## PHP Compatibility

Before upgrading PHP you should check if your webshop is compatible with the PHP version you would like to use. Be sure to look both at the vendor's requirements, and any modules in use, to see which PHP versions are officially supported.

### Supported PHP versions for Magento 2.3

According to the [Magento Documentation](https://devdocs.magento.com/guides/v2.3/install-gde/system-requirements.html#php), Magento 2.3 supports PHP 7.3 only. However, many Magento users are reporting that Magento 2.3 also works with PHP 7.1 and 7.2. Of course we always advise to follow the official supported versions advertised by Magento, and any module in use on your webshop.

- 7.3 (Official)
- 7.2 (Reported by Community)
- 7.1 (Reported by Community)

### Supported PHP versions for Magento 2.4

According to the [Magento Documentation](https://devdocs.magento.com/guides/v2.4/install-gde/system-requirements.html#php), Magento 2.4 supports PHP 7.4 only, and PHP 7.3 is not tested or recommended. However, many Magento users are reporting that Magento 2.4 also works with PHP 7.2 and 7.3. Of course we always advise to follow the official supported versions advertised by Magento, and any module in use on your webshop.

- 8.1 (Will be officially supported starting in version 2.4.4)
- 7.4 (Official)
- 7.3 (Not recommended)
- 7.2 (Reported by Community)

### Supported PHP versions for Magento CE 1.9.4 and later

According to Magento's Documentation, Magento 1.9.4 supports PHP 5.6, 7.0, 7.1, and 7.2. We strongly advise using at least PHP 7.1, and 7.2 if at all possible.

- PHP 7.2 (Recommended for Magento 1.9)
- PHP 7.1 (EOL, No updates since 1 Dec 2019)
- PHP 7.0 (EOL, No updates since 3 Dec 2018, Deprecated, will be removed at the end of 2021 from Hypernode)
- PHP 5.6 (EOL, No updates since 31 Dec 2018, Deprecated, will be removed at the end of 2021 from Hypernode)

**Please use the above information as an indication! Always check with your vendors, and technical partners, before deciding on a PHP version.**

## PHP Modules

### Ioncube compatibility

We support Ioncube for PHP 5.6 and PHP 7.x, but this extension is not enabled by default as it is a big performance killer. If you wish to have Ioncube enabled, please manually enable it via [the hypernode-systemctl tool](../tools/how-to-use-the-hypernode-systemctl-cli-tool.md).
