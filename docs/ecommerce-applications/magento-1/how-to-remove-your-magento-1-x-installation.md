---
myst:
  html_meta:
    description: Although Magento 1 has been End of Life, it is still possible to
      host your Magento 1 store at Hypernode by using OpenMage. Learn how in this
      article.
    title: How to remove your Magento 1 installation? | Hypernode
redirect_from:
  - /en/ecommerce/magento-1/how-to-remove-your-magento-1-x-installation/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-remove-your-magento-1-x-installation/ -->

# How to Remove Your Magento 1.x Installation

The following snippets can be used to remove your Magento 1.x installation(s).

**This is irreversible so make sure you know what you are doing!**

## Remove a Magento 1 Installation Using Magerun

In order to uninstall/remove a Magento 1.x installation, run the following command:

```bash
n98-magerun --root-dir=/data/web/public uninstall --installationFolder=/data/web/public --force

```

This will delete the default database (`YOURAPPNAME_preinstalled_Magento`), and recursively delete the `/data/web/public` directory. Any instances of Magento installed in other directories will not be touched.

## Manually Remove a Magento 1.x Installation

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
rm -rf /data/web/{public,staging}
mkdir /data/web/{public,staging}

```

*Keep in mind:* After removing your Magento content and database, sometimes you need to remove or adjust your Nginx configuration in `/data/web/nginx` too, in order to start with a clean slate.
