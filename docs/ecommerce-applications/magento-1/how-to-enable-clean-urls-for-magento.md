---
myst:
  html_meta:
    description: To make use of clean URLs in Magento 1, all you need to do is adjust
      the Search Engines Optimization setting in the backend. Follow these steps!
    title: How to enable clean urls for Magento 1? | Hypernode
redirect_from:
  - /en/ecommerce/magento-1/how-to-enable-clean-url-s-for-magento-1/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-enable-clean-url-s-for-magento-1/ -->

# How to Enable Clean URLs for Magento

Clean URLs are less intimidating to visitors and have a positive effect on search index optimization (SEO) as well.
They "Clean up" the URL structure used when visiting a Magento webshop.

Rather then having URLs like: `https://your.shop/index.php/some/product`, after enabling the Search Engines Optimization setting, the URL will instead be rewritten to: `https://your.shop/some/product`.

This setting does not require additional webserver configuration. To make use of clean URLs in Magento, all you need to do is adjust the `Search Engines Optimization` setting in the Magento backend. If you enable this setting, the URLs containing index.php will be rewritten to URL's without the index.php.

## Enable Clean URLs

To enable the use of clean URL's, log in on your Magento admin backend and navigate to:

**For Magento 1:**

`System` -> `Web` -> `Search Engines Optimization`.

**For Magento 2:**

`Stores` -> `Configuration` -> `Web`.

From there, enable `Use Web Server Rewrites` (Select "Yes"), and click `Save Config` to activate your changes.

As redirects are heavily cached in your local browser cache, sometimes it's necessary to flush the cache of your browser.

## Remove index.php From Any URL

To remove the index.php from the URL, use the following snippet and add it to `/data/web/nginx/public.rewrites`:

```nginx
rewrite ^/index.php/(.*) /$1 permanent;
```
