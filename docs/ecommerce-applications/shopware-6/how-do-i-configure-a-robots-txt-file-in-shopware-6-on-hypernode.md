---
myst:
  html_meta:
    description: Learn how to configure a robots.txt file in Shopware 6 on 
      Hypernode to optimize search engines.
    title: How do I configure a robots.txt file in Shopware 6 on Hypernode?
---

<!-- source: https://support.hypernode.com/en/ecommerce/shopware/how-do-i-configure-a-robots-txt-file-in-shopware6-on-hypernode/ -->

# How do I configure a robots.txt file in Shopware 6 on Hypernode

In this article, we explain how to set up a `robots.txt` file in Shopware 6 on Hypernode to optimize the indexing of your webshop by search engines.

A `robots.txt` file allows you to instruct search engine crawlers on which parts of your website they are allowed or not allowed to index. This helps prevent duplicate content, saves additional resources, and results in more efficient indexing and better SEO performance.

## Setup for a single robots.txt file without multistore

Create a new text file named `robots.txt` and place this file in the `public` directory of your Shopware 6 installation. You can insert the example text below into this file:

```text
User-agent: *
Allow: /
Disallow: */?
Disallow: */account/
Disallow: */checkout/
Disallow: */widgets/
Disallow: */navigation/
Disallow: */bundles/

Disallow: */imprint$
Disallow: */privacy$
Disallow: */gtc$

Sitemap: https://YOUR_DOMAIN/sitemap.xml
```

Adjust the `Sitemap` rule with the exact URL to your sitemap.

Use the [robots.txt tester](https://support.google.com/webmasters/answer/6062598) in Google Search Console to verify if the configuration is correct and the desired pages are being blocked or allowed.

## Setup for a Multistore Robots.txt shopware 6 Webshop

In the root of your Shopware 6 installation, navigate to the `public` directory. Create a new folder called `robots`:

```bash
mkdir public/robots
```

Within the newly created `robots` directory, create a separate `robots.txt` file for each domain. For example:

- `public/robots/www.example.com.txt`
- `public/robots/shop.example.com.txt`

Each file should contain the rules specific to the corresponding domain. Below is an example for `www.example.com`:

```text
User-agent: *
Allow: /
Disallow: */?
Disallow: */account/
Disallow: */checkout/
Disallow: */widgets/
Disallow: */navigation/
Disallow: */bundles/

Disallow: */imprint$
Disallow: */privacy$
Disallow: */gtc$

Sitemap: https://www.example.com/sitemap.xml
```

Adjust the `Sitemap` URL and other rules according to the specific requirements of each domain.

Edit or create a new NGINX configuration file at `/data/web/nginx/server.robots` and add the following rewrite rule:

```nginx
rewrite ^/robots\.txt$ /robots/$host.txt;
```

This rule ensures that requests to `/robots.txt` are dynamically redirected to the correct file based on the domain making the request.
