---
myst:
  html_meta:
    description: This article explains how to enable a sitemap.xml in Magento 2 and
      how to configure NGINX to Use the Same Sitemap for All Storefronts.
    title: How to create a sitemap xml for Magento 2? | Hypernode
redirect_from:
  - /en/ecommerce/magento-2/how-to-create-a-sitemap-xml-for-magento-2-x/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-create-a-sitemap-xml-for-magento-2-x/ -->

# How to Create a Sitemap.xml for Magento 2.x

You can find detailed guidelines for creating a sitemap.xml for Magento 2.x versions in this support documentation article.

## Enabling sitemap.xml in Magento 2

### Configure Magento 2 to Create Sitemaps

- To enable sitemaps inside Magento, log in to your admin
- Make sure your crontab is working properly
- Ensure all storefronts you want to generate sitemaps for are configured
- Navigate to `Stores` -> `Settings` -> `Configuration` -> `Catalog` -> `XML Sitemap`:

In the dropdown menu, adjust the settings for `Category Options`, `Product Options` and `CMS Pages Options` to your needs.

Now open the `Generation Settings` dropdown and select:

- **Enabled**: Yes
- **Start Time**: Insert some time after 00:00 (Don’t choose exactly 00:00 as many other jobs are scheduled around midnight too)
- **Frequency**: Choose `Daily`, or if you have many product changes during the day, select `Hourly` (Hourly is quite heavy on your databases, so don’t do this on Falcon XS, S, and M plans)
- **Error Email Recipient**: The error collector email address of the Magento partner that maintains the website
- **Error Email Sender**: A valid return path that is used for your Magento store (If set), or otherwise a sender that is not blocked by your spam filter
- **Error Email Template**: You can leave this at ‘Use System Value’

After setting the `Generation Settings`, open the dropdown for `Search Engine Submission Settings`, set `Enable Submission to Robots.txt` to `Yes` and save your changes by clicking the big red `Save Config` button at the right side of the top of the page.

Magento is now ready and configured to generate sitemaps. Now we should change the settings for your storefront to create one.

### Configuring a Single Sitemap for All Storefronts

If you want to share a sitemap between storefronts, you need to set up a location where the file is saved and adjust our Nginx config, so the file is publicly accessible.

Let’s start with defining a `sitemap.xml` for your webshop:

- Create a directory to store our sitemap: `mkdir -p /data/web/magento2/pub/sitemaps`
- In the Magento admin, select `Marketing` -> `Seo & Search` -> `Sitemap`
- Click the big red button on the upper right to add a new sitemap.

Now fill in the required information:

- Filename: `sitemap.xml`
- Path: `/sitemaps/`
- In case you have multiple store views, select the corresponding store view
- Select `Save & Generate`

If all goes well, a sitemap.xml file is generated as /data/web/magento2/pub/sitemaps/sitemap.xml

Now scroll to [Configuring Nginx to use one sitemap for all storefronts](#configuring-nginx-to-use-one-sitemap-for-all-storefronts) to add the required Nginx configuration.

### Configure a Sitemap for Each Storefront

Some additional configuration is required if you want to serve a different sitemap.xml for each store view. We assume you have already finished the step [Configure Magento 2 to Create Sitemaps](#configure-magento-2-to-create-sitemaps), so if you haven't done this already, do that step first.

Let's get started:

- Create a directory to store each sitemap: `mkdir -p /data/web/magento2/pub/sitemaps`
- Make sure there is no sitemap in `/data/web/public/sitemap.xml` to avoid an incorrect sitemap being served (change the location of the sitemap.xml in Magento from `/sitemap.xml` to `/sitemaps/sitemap_$storecode.xml` where `$storecode` is the code of your storefront)
- In the Magento admin, select `Marketing` -> `Seo & Search` -> `Sitemap`
- Click the big red button on the upper right to add a new sitemap.

For each store view, fill in the information:

- Filename: Create a sitemap with the known naming convention `sitemap_$storecode.xml`. IE: If your store code is `shop_nl`, then use the filename `sitemap_shop_nl.xml`
- Path: `/sitemaps/`
- Store View: Select the store view (IE: `shop_nl)`
- Select `Save & Generate`

If all went well, a `sitemap.xml` file is generated as `/data/web/magento2/pub/sitemaps/sitemap_shop_nl.xml`

Now you can use [Configure Nginx to use a sitemap.xml per storefront](#configure-nginx-to-use-a-sitemapxml-per-storefront) to add the required Nginx configuration.

## Nginx Configuration

### Configuring Nginx to Use One Sitemap for All Storefronts

Because the `/data/web/magento2/pub/sitemaps` directory where the sitemap is stored is not within the `/data/web/public` directory, some additional configuration in Nginx is required to make your sitemap.xml accessible from the web. To do this, use the [Nginx alias functionality](http://nginx.org/en/docs/http/ngx_http_core_module.html#alias) to create an alias to a path outside the public webroot.

First, log in to your Hypernode using SSH, and open the file `/data/web/nginx/server.sitemap` with your favorite editor. Now create the following snippet:

```nginx
location /sitemap.xml {
    alias /data/web/magento2/pub/sitemaps/sitemap.xml;
}
```

Now test your sitemap by requesting and verifying whether the right sitemap is served:

```bash
curl -v https://www.example.com/sitemap.xml
```

### Configure Nginx to Use a Sitemap.xml per Storefront

To configure multiple sitemaps, you need to add some configuration. First, log in to your Hypernode using SSH, and open the file `/data/web/nginx/server.sitemap` with your favorite editor. Now create the following snippet:

```nginx
location /sitemap.xml {
    alias /data/web/magento2/pub/sitemaps/sitemap_$storecode.xml;
}
```

## Add the Sitemap Location to the Robots.txt

When you can successfully request your sitemap.xml, add it to your `robots.txt`:

```bash
Sitemap: http://www.example.com/sitemap.xml
```

You can add the sitemap manually or use the generated robots.txt Magento 2 provides. If you use the generated robots.txt, keep in mind all manual changes will be overwritten when you save your changes in the Magento admin. For configuring a `robots.txt` in Magento 2, have a look at [this article](../../ecommerce-applications/magento-2/how-to-create-a-robots-txt-for-magento-2-x.md).

## Troubleshooting

- We’ve seen one or two exceptional cases where creating a sitemap was extremely slow. This was caused by some queries that sometimes took 10 minutes (!) to complete. In this particular case, the solution was to disable use_index_extensions in MySQL. To do this, add SET SESSION optimizer_switch='use_index_extensions=on' to the MySQL initStatements in your config.php:

```php
'default' => array(
  'host'           => 'mysqlmaster',
  'dbname'         => 'magento2_db',
  'username'       => 'app',
  'password'       => 'somepass',
  'model'          => 'mysql4',
  'initStatements' => 'SET NAMES utf8; SET SESSION optimizer_switch="use_index_extensions=on"',
  'active'         => '1',
),
```

- Magento 2, by default, splits up the sitemap file into chunks of 10 MB. If you have lots of products, your sitemap will be split up into several files (sitemap-1-1.xml en sitemap-1-2.xml ), which are, in the current construction, not publicly accessible. We’re looking for a solution to make this possible. For now, as a workaround, change the maximum file size of your sitemap.xml to a much bigger value to include all pages in one sitemap.
