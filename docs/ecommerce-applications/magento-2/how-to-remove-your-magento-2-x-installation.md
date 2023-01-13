---
myst:
  html_meta:
    description: The snippets in this article can be used to remove your Magento 2.x
      installation(s).
    title: How to remove your Magento 2 installation? | Hypernode
redirect_from:
  - /en/ecommerce/magento-2/how-to-remove-your-magento-2-x-installation/
  - https://support.hypernode.com/knowledgebase/remove-magento-installation/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-remove-your-magento-2-x-installation/ -->

# How to Remove Your Magento 2.x Installation

The following snippets can be used to remove your Magento 2.x installation(s).

**This is irreversible so make sure you know what you are doing!**

## Remove a Magento 2.x Installation Using Magerun

For Magento 2 there is not a `magerun` plugin available to uninstall the files yet. We can therefore remove the installation by hand.

### Production Environment

```bash
cd ~/magento2 && n98-magerun2 db:drop
cd ~ && rm -rf /data/web/{magento2,public} && mkdir /data/web/public

```

### Staging Environment

```bash
cd ~/magento2_staging && n98-magerun db:drop
cd ~ && rm -rf /data/web/{magento2_staging,staging} && mkdir /data/web/staging

```

## Manually Remove a Magento 2.x Installation

To manually remove all databases and files of both the staging and production, use the following snippet:

```bash
mysql -Be 'show databases' | sed 1d |\
 grep -vE '^information_schema$|^performance_schema$|^mysql$|^test$' | while read DATABASE
do
    mysql -Be "DROP DATABASE $DATABASE"
done

```

Then remove all Magento files, use the following command:

```bash
cd /data/web
rm -rf /data/web/{public,staging,magento2,magento2_staging}
mkdir /data/web/{public,staging}

```

**Keep in mind**\*:\* After removing your Magento content and database, sometimes you need to remove or adjust your Nginx configuration in `/data/web/nginx` too, in order to start with a clean slate.
