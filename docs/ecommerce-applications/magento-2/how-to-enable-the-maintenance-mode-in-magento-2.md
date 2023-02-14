---
myst:
  html_meta:
    description: Shop owners want to perform upgrades, install extensions or do the
      necessary maintenance on a shop. For this you use Maintenance Mode in Magento
      2.
    title: How to enable maintenance mode in Magento 2? | Hypernode
redirect_from:
  - /en/ecommerce/magento-2/how-to-enable-the-maintenance-mode-in-magento-2/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-enable-the-maintenance-mode-in-magento-2/ -->

# How to Enable the Maintenance Mode in Magento 2

Maintenance mode is a shortcut to serve a temporary error notification to all customers that are visiting your shop informing them to come back at a later time, as it is currently not possible to place an order.

Periodically shop owners and maintainers want to perform upgrades, install extensions or do the necessary maintenance on a shop.

To do this in a secure manner, without customers being able to placing orders that get lost during the operation, maintenance mode is available on your Magento shop.

## Maintenance Mode for Magento 2

In contrast to Magento 1, Magento 2 provides an internal mechanism to add IP addresses that should be able to access the site while in maintenance mode, so we don’t need additional configuration in the `index.php` to allow developers access to the site while the maintenance flag is set.

### Enable the Maintenance Mode in Magento 2 by Setting the maintenance.flag

Instead of placing a `maintenance.flag` file in the webroot, Magento 2 looks for a `.maintenance.flag` file in the `var/` directory.

To do this, log in on your Hypernode, and create the maintenance flag:

```nginx
touch /data/web/magento2/var/.maintenance.flag
```

If you site is set to maintenance mode **ON**, an error message will be shown to all visitors of your site:

### Allow a Developer Access to a Magento Installation in Maintenance Mode

To allow your developers access to the Magento 2 site while in maintenance mode, add the IP addresses to the var/.maintenance.ip file. This will allow a comma-separated list of IP addresses access to your shop:

```nginx
echo 1.2.3.4 1.2.3.5 1.2.4.5 >> /data/web/magento2/var/.maintenance.ip
```

Alternatively you can do this using the bin/magento cli tool:

```nginx
cd ~/magento2
chmod +x bin/magento
bin/magento maintenance:enable --ip=1.2.3.4 --ip=2.3.4.5
```

When the IP addresses are set in the `.maintenance.ip` file, you can use `n98-magerun` to achieve the same:

```nginx
n98-magerun2 sys:maintenance --on
n98-magerun2 sys:maintenance --off
```

### Additional Information

For additional information, take a look at the [Magento 2 documentation about enabling the maintenance mode.](https://devdocs.magento.com/guides/v2.3/install-gde/install/cli/install-cli-subcommands-maint.html)

## Serve a Custom Error Message When in Maintenance Mode

To serve the error page in your own style, we should add some layout files in the directory from where error pages are served.

For Magento 2 you can find it in: `/data/web/magento2/pub/errors`.

A default selection of static files used for error pages is already present in the default directory.

It is not recommended to change files in the default directory as this can cause errors when later security patches need to change the core error files. Therefore, to change the styling or your own error page, first copy the default directory to another directory:

Magento 2:

```nginx
cd /data/web/magento2/errors
cp -rv default custom/
```

Next copy the `local.xml.sample` to `local.xml`:

```nginx
cp local.xml.sample local.xml
```

Now change `<skin>default</skin>` to `<skin>custom</skin>` in both `local.xml` and `design.xml` to activate the custom skin we just created:

```nginx
editor local.xml design.xml
```

After this change, the static content for error pages is served from `/errors/custom` rather than from `/errors/default`.

*You can now start designing and adjust the custom error files to your preferences by changing the files in the `custom/` directory.*
