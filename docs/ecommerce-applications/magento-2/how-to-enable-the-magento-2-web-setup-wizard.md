---
myst:
  html_meta:
    description: There are many open issues on the Magento 2 Github repository regarding
      the usage of the Magento 2 Web Setup Wizard. More details in this article.
    title: How to enable the Magento 2 web setup wizard? | Hypernode
redirect_from:
  - /en/ecommerce/magento-2/how-to-enable-the-magento-2-web-setup-wizard/
  - /knowledgebase/using-magento-2-web-setup-wizard/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-enable-the-magento-2-web-setup-wizard/ -->

# How to Enable the Magento 2 Web Setup Wizard

**NB: 22-01-2016: Updating Magento with the ‘Web Setup Wizard’ is currently the only known way of upgrading Magento 2. Unfortunately we’ve been hearing a lot of sounds from developers and shop owners saying the Web Setup Wizard doesn’t work properly, giving a lot of error messages. Magento is looking into it.**

**NB: 04-08-2017 - We've seen several cases where your Magento 2 installation is deleted while using the Web Setup Wizard. This happens during the update process. Magento deletes the old files, but fails to put the new ones in place, resulting in a broken shop.**

Currently (2021), there are many open issues on the [Magento 2 Github repository](https://github.com/magento/magento2) regarding the usage of the Magento 2 Web Setup Wizard. When you configure your Magento 2 installation as recommended by Magento, a 404 will show instead of the wizard page.

## Configure the Web Setup Wizard to Work

Currently when visiting the Magento 2 Web Setup Wizard, a 404 error is thrown.

To reach the Magento web wizard use the following command:

```nginx
ln -s /data/web/magento2/setup /data/web/public/setup

```

## Deconfigure the Web Setup Wizard

After updating your Magento we recommend you to remove the symlink because it is a vulnerability to have it publicly accessible. Use the following command to remove the public file:

```nginx
unlink /data/web/public/setup

```
