---
myst:
  html_meta:
    description: Learn what additional configurations you can make to optimise your
      Magento shop post-migration, ordered by priority and estimated time spend.
    title: Optimise the performance of your Magento shop | Hypernode
redirect_from:
  - /en/best-practices/performance/how-to-optimize-the-performance-of-your-magento-shop/
---

<!-- source: https://support.hypernode.com/en/best-practices/performance/how-to-optimize-the-performance-of-your-magento-shop/ -->

# How to Optimize the Performance of Your Magento Shop

There are several optimisations that are recommended to use on a Hypernode as they improve the load times and stability of the Hypernode.

This list are additional configuration that can be performed after migrating to Hypernode. The list is in order of importance and a time estimate is added to indicate how long it takes to perform these tasks.

## Basic Optimization (>45 mins)

The TTFB (Time To First Byte) is an important metric for webshops and it is something that both server optimization and code optimization can influence. The TTFB is the time that it takes for the server to return the HTML page after the request has been made.

It is a combination of the time the web server is processing the request and the time it takes for Magento to process and generate the HTML for the page itself.

On the server side we already did many optimization and configuration to improve the speed of the web- and MySQL server. You can test the server response time by requesting a small static image or a text-based `css` or `js` page to measure how fast the TTFB of the Hypernode is. What’s left to optimise is the Magento webshop itself.

With every optimization of your webshop, the TTFB should go down a bit and with every additional module, plugin or functionality the TTFB should go up a bit. The first step to optimise your Magento webshop should be deactivating and **removing** all unnecessary and unused extensions.

One of the main causes of bad performance is the use of too much Magento extensions to add functionality. This will cause a long load time.

When your installation is as simple as possible with only the necessary extensions and all others removed, you can do the basic Magento optimization like tweaking the cache settings, enabling log cleaning or turning off visitor logging at all, tuning the flat catalog database settings and optimise slow MySQL queries by inspecting the MySQL slow log.

After you have done the basic optimization, you can use Blackfire or NewRelic to find the bottlenecks in your Magento shop and tune more specific parts of your webshop.

## Upgrading Magento (>60 mins)

Over the last years Magento made many performance improvements to their software. Upgrade to the latest version possible to utilise these improvements.

## Upgrading to PHP 7 (>60 mins)

It is recommended to upgrade your PHP version to PHP 7 as this causes a massive improvement in speed. Before you switch the PHP version, make sure your shop and all extensions are ready to be used with PHP 7 first.

On Hypernode you can easily order [development nodes](../../hypernode-platform/tools/how-to-use-hypernode-development-plans.md) or use the [Hypernode Docker](../../best-practices/testing/hypernode-docker.md) to get your Magento installation running on PHP 7 without risking your production shop.

## Avoid IonCube Extensions (\<5 mins)

IonCube loader is a mechanism to encrypt PHP code to enforce licensing or prevent code edits in extensions. There are still many extensions that are using this technique, causing your shop to slow down by seconds. IonCube is a massive performance killer that should be avoided where possible.

*We know that many shop owners are bound to IonCube due to the use of the xCore (formerly known as Dealer4dealer) extension for their shop.* *xCore* *released a newer extension that is not encoded with IonCube. For more information contact [xCore](https://xcore.nl/).*

## Blocking Unwanted Bots and Crawlers (10 mins)

Bots and crawlers should be reduced to the bare minimum. As processing big sets of data is getting easier, there is also an increase in crawlers and bots by commercial parties that do not really generate any conversion of deliver a service you want to make use of. The more bots are crawling and indexing your site, the more server resources are used for serving these bots. It is highly recommended to only allow the few crawlers that you actively use to save as much cpu and memory for actual users making orders.

For most of the shops these few are only Google and Bing, but sometimes additional crawlers are needed for SEO tuning, monitoring or product updates.

By default not many crawlers are blocked: Only `MJ12` and `Ahrefs` are blocked by default as they caused too much unwanted server load across our platform. If you currently use the services of these 2 parties you are recommended to choose another link crawler that does respect the robots.txt file and the crawl delay.

We offer an [extended list of user agents](https://gist.github.com/hn-support/b70d33d870981f5d6109b58900379643) that you can use to block unwanted crawlers yourself.

To do this, download the block list and the generator script and save the output of the generator script as `/data/web/nginx/server.botblocker`:

```nginx
## Get the blocklist files
wget -O blocklist.txt  https://gist.githubusercontent.com/hn-support/b70d33d870981f5d6109b58900379643/raw
wget https://gist.githubusercontent.com/hn-support/b70d33d870981f5d6109b58900379643/raw/825215d9e9a7abd92b0f110b67ba0bc1f7a9fd93/generate_nginx_blocklist.sh

## Set executable bit on blocklist generation script
chmod +x generate_nginx_blocklist.sh

## Edit the user agent list
editor blocklist.txt

## Generate configuration
./generate_nginx_blocklist.sh
```

## Protecting the Layered Navigation (10 mins)

For many crawlers, even the good ones, the layered navigation of Magento is a bottleneck. Due to the way the layered navigation works, bots can create an exhausted list of URL’s to crawl, for example by increasing the product ID with 1 for every request or by selecting filter combinations.

Bots happen to get stuck in this enormous list of urls, causing an increase in load times and usage of resources that better can be used to real, buying visitors.

Another critical performance killer is the catalog search functionality. Many crawlers recognise the results of a search query as a product page that should be indexed. Because the catalog search for Magento is one of the heaviest features in resource costs, it is highly recommended to block these too.

To reduce these effects caused by crawlers and bots,[block all dynamic entry points that should not be accessible by bots](../../best-practices/performance/how-to-fix-performance-issues-caused-by-bots-and-crawlers.md). If you block these entry points using a status code 410, you tell the bots to drop the URL from the index and stop indexing it in the future.

## Use HTTPS so You Can Take Advantage of HTTP2 (\<10 mins)

On Hypernode we recommend to serve your shop only over HTTPS. This is safer and is better for search indexation optimization.

Most of the available browsers only support HTTP2 when your pages are served over SSL so to use this faster technology, order an SSL certificate and make sure your site [is only served over HTTPS](../../hypernode-platform/nginx/how-to-configure-your-shop-to-only-use-https.md).

## 404 Handling (5 mins)

Make sure 404 pages are not redirected to your catalog search and reduce load times of pages by moving [404 handling from Magento to Nginx](../../best-practices/performance/how-to-set-up-smart-404-handling.md).

## Large `core_url_rewrite` Table (10 mins)

The URL rewrite issue is a Magento core problem that has been around for years and isn’t easy to solve due to various caveats. It basically makes your `core_url_rewrite` table grow over time with unnecessary data.

[Fabio, one of our partners and Magento developer](http://frosit.nl/), created a `n98-magerun` plugin to repair a large core_url_rewrite table by removing the duplicates. You can clone and install the plugin [from its github repository.](https://github.com/frosit/magerun-rewritetoolset)

## Price Rules (\<5 mins)

[Price rules](http://docs.magento.com/m1/ce/user_guide/marketing/price-rules-catalog.html) are known to heavily increase the load on the MySQL server by causing the amount of MySQL queries to go up and by causing queries that take lots of time to process.

Try to use price rules as little as possible and check your MySQL slow log for slow queries that can be improved to improve the load time of your pages.

## Lesti FPC Cache (\<15 mins)

Lesti FPC is a full page cache module that can massively improve the load times of your product pages.

We recommend the use of Lesti FPC on Hypernode, as it reduces server load and makes the shop much faster to load. [How to install can be found in our documentation.](../../hypernode-platform/tools/how-to-configure-lesti-fpc.md)

## Warm Caches and Test URL’s Using the Sitemap (\<10 mins)

When using a full page cache module like Lesti FPC or Varnish, the site gets a lot faster after the first visit when the page has been cached. We recommend to warm the caches periodically. This can be nightly through cron, or manually after adding many new products.

This can be done [using the n98-plugin available on all Hypernodes](../../ecommerce-applications/magento-2/how-to-configure-varnish-for-magento-2-x.md#warming-your-cache). To make use of this script, [a sitemap.xml file should be present](../../ecommerce-applications/magento-2/how-to-create-a-sitemap-xml-for-magento-2-x.md).

## Sessions in Redis (\<15 mins)

On bigger Hypernodes with more memory available, you can reduce disk IO by storing the sessions in Redis instead of in files.

This only works on bigger nodes, as there needs to be some memory available for rendering pages using PHP too.

To store sessions in Redis, take a look at [the instructions on how to configure this](../../ecommerce-applications/magento-1/how-to-configure-redis-for-magento-1.md) ([Magento 2](../../ecommerce-applications/magento-2/how-to-configure-redis-for-magento-2.md))

## Image Optimizations (10 mins)

Big images take more time to download and view than smaller images. We created a resize tool to reduce the size of your images to improve load times. To do this, use the Hypernode-image-optimizer which is installed on all nodes. It’s recommended to run this command nightly through cron. More information can be found in [this article about optimizing your image size](../../best-practices/performance/how-to-optimize-your-images.md).

## Static Content Optimization (15 mins)

Compressing your Javascript and CSS content and improve your page load times by optimizing your static content can be rewarding but only after you optimized the common Magento bottlenecks. If static content optimization can speedup your shop with half a second while there a multiple MySQL queries taking 2 seconds to complete, fix the latter first.

If your shop is low in extensions and fully optimized on the php and MySQL side, code optimizations in your Javascript and CSS can help. If this is the case, take a look at your client-side static content caching and client-side rendering times first.

*With the introduction of `HTTP2`, combining your Javascript files is not always the fastest method anymore. When using `HTTPS2`, lots of smaller files can be quicker to download than one large combined Javascript file, so it can be worthwhile to test which is faster for your shop.*[*A good way to test this is using Curl*](https://gist.github.com/hn-support/885fa037aaad17576cb9f44703c879ef).

## Allow Limited Access to Your Magmi Importer (5 mins)

To secure your Magmi, you can add some Nginx configuration to make sure Magmi is only accessible from the office.

To do this, you can create a whitelist of IP’s that should only be allowed to make use of Magmi.

This whitelist can then be included in Nginx configuration on locations that are restricted.

More information can be found [in our article about creating reusable config](../../hypernode-platform/nginx/how-to-create-a-reusable-config-to-include-in-custom-snippets.md).

In this example your Magmi is accessible through `https://www.example.nl/magmi`.

First create a whitelist:

```nginx
cat <<EOF > /data/web/nginx/include.whitelist
allow 1.2.3.4;
allow 2.3.4.5;
allow 6.6.6.6;
deny all;
EOF
```

Then save the folling snippet as `/data/web/nginx/magmi.conf`:

```nginx
location ~* /magmi($|/) {
    include /etc/nginx/app/include.whitelist;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }
}
```

## Protect Your Shop Against Brute Forcers (\<10 mins)

It is highly recommended to protect your Magento admin backend and custom entry points against brute forcers.

Most of the default and well-known entry points that can be abused for password guessing are already protected.

If you use custom entry points that can be abused, create [additional configuration using a whitelist](../../hypernode-platform/nginx/how-to-create-a-reusable-config-to-include-in-custom-snippets.md) and include it in all location blocks that should be protected.

For additional help to check if your shop is brute force protected, use [MageReport](https://magereport.com/).

## Tuning the Rate Limiting for Specific IP’s (\<5 mins)

As there is only a limited set of PHP-FPM workers available depending on the amount of CPU cores available on the Hypernode, these workers can be depleted by a small set of IP addresses effectively causing downtime for new visitors where no PHP-FPM worker is available for.

This happens faster when the Magento shop is not well optimized and it takes a long time to process a page with PHP.

To make sure a small set of IP addresses can’t take your shop down we use rate limiting based on IP address. A single IP might use up to 80% of the total PHP-FPM worker capacity available.

On smaller nodes (mostly on Hypernode Start and Grow plans) this can cause errors when working in the Magento admin. To resolve these errors, you can whitelist IP’s to make sure they will not be rate limited when working in the Magento admin backend. If you use nightly product imports through the Magento SOAP API, sometimes you need to whitelist the remote ip of the import tool as well.

[To whitelist these IP’s have a look at our article about rate limiting](../../hypernode-platform/nginx/how-to-resolve-rate-limited-requests-429-too-many-requests.md).

## Configure Your API (\<10 mins)

With most of the Magento installations, the API functionality works out-of-the-box on Hypernode.

In some cases however, specific to the use of clean URL’s, a 404 is returned when visiting the Magento API.

To fix this, use [this article about working with the Magento api on Hypernode](../../ecommerce-applications/magento-2/how-to-enable-the-magento-2-api.md).
