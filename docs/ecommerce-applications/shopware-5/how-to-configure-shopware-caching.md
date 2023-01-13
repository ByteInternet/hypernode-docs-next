---
myst:
  html_meta:
    description: Shopware 5 provides a built-in HTTP cache which can be enabled in
      production environments. In this document we’ll explain how you can set this
      up.
    title: How to configure caching in Shopware 5? | Hypernode
redirect_from:
  - /en/ecommerce/shopware/how-to-configure-shopware-caching/
---

<!-- source: https://support.hypernode.com/en/ecommerce/shopware/how-to-configure-shopware-caching/ -->

# How to Configure Shopware Caching

Caching is an important tool in improving the performance and user experience of your shop. Therefore Shopware provides a built-in HTTP cache which can be enabled in production environments. In this document we’ll explain how you can set this up.

## Configuring the HTTP Cache

In the backend you can find the cache configuration settings.

- Log in to the back-end, *YOURSHOP.com/backend*
- Navigate to `Configuration` -> `Cache/performance` -> `Cache/performance`
- When your shop is ready for production, you can select the Production mode which enables the HTTP cache to get optimal front end performance.
- In the “Performance” window, navigate to the tab Settings -> HTTP cache
- Check the box Activate HTTP Cache to activate HTTP caching.
- Now warm up your cache by clicking on Warm up the http cache

Note the other check boxes under Configuration:

- **Automatic cache invalidation:** Clears the cache of a product detail page whenever a product is modified.
- **Alternate proxy URL:** Allows you to select a desired proxy, for example with Varnish.
- **Admin view:** Hides the option that product pages are no longer cached, but opened from the backend.

## Flush the Shopware Cache

When making adjustments to the configuration, e.g. installing or updating extensions, it is often required to flush the caches.

You can flush the Shopware cache by one single command from the shell:

```nginx
cd /data/web/public
php bin/console sw:cache:clear
```

Or by following the steps below in the backend:

- Login to the backend via: `YOURSHOP.com/backend`
- Navigate to: `Configuration` -> `Cache/performance` -> `clear shop cache`

**Configure a cronjob to run cache warmer daily**

We recommend to configure a cronjob that runs the cache warmer daily at 06:00 to make sure the performance is always optimal.

```nginx
# HTTP Cache Warmer
0 6 * * * * flock -n ~/. php /data/web/public/bin/console sw:warm:http:cache

```

**Run cache warmer**

After flushing the cache, it's recommended to run the cache warmer manually. This can be done by the following command.

```nginx
cd /data/web/public
php bin/console sw:warm:http:cache
```

## Theme Cache

Theme caching is a new caching system that comes with Shopware 5 themes and features some great optimisations:

- Registered LESS files are compiled into CSS
- All CSS and JavaScript files are merged into single .css and .js files
- The resulting files are minimized

By compiling and merging these files the amount of requests and bandwidth decreases, which results in faster response time and experience for the end user.

**Configuring Theme Cache**

You can configure the theme caching by following the steps below, please keep in mind that the HTTP cache will be flushed by following these steps:

- Navigate to `Configuration` -> `Cache/performance`-> `Cache/performance` -> `settings` -> `Themes`
- Click on "Warm up cache"
- Select your shop"
- Click on "Start process"
