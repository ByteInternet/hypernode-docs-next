---
myst:
  html_meta:
    description: 'Get the full picture of your Magento store security. Get an in-depth
      look into potential vulnerabilities and provides clear advice on how to address
      them. '
    title: MageReport Premium | All you need to know | Hypernode
redirect_from:
  - /en/services/magereport/magereport-premium/
---

<!-- source: https://support.hypernode.com/en/services/magereport/magereport-premium/ -->

# MageReport Premium

[MageReport Premium](http://magereport.com/) provides Hypernode customers with extra information about the performance of their Magento shop. This article explains the difference between MageReport and MageReport Premium and gives more information about the performance checks and charts. MageReport Premium offers a [checklist](https://www.magereport.com/scan/checklist/) with a complete overview of all your shops and the status per check.

*Want access to MageReport Premium? MageReport Premium is developed for our optimised Magento hosting platform: Hypernode. Check out [Hypernode.com](https://www.hypernode.com/) for more information.*

## Hypernode Customers Get Even More

Anyone can scan their Magento shop with [MageReport.com](http://magereport.com/) to check whether there are any security issues. However, when logged on with their Hypernode account, Hypernode customers can access additional data such as Performance checks and charts. MageReport Premium offers a [checklist](https://www.magereport.com/scan/checklist/) with a complete overview of all your shops and the status per check. MageReport (Premium) offers:

- Security level checks *(MageReport & MageReport Premium)*
- Performance checks *(MageReport Premium only)*
- Charts *(MageReport Premium only)*

The Performance checks and charts offer specific information about your shop’s performance and help you optimize your Hypernode. That’s why MageReport for Hypernode users is called MageReport Premium.

Accessing [MageReport Premium](http://magereport.com/) is easy by logging on to MageReport.com with your Hypernode customer account. Choose ‘Sign in with Byte’(for Service Panel users) or 'Sign in with Hypernode' (for Control Panel users) on your top right.

## Security Level

The Security level checks are accessible for any Magento shop owner (Hypernode or not) and show you the safety of your Magento shop. If a check comes out red, navigate to the given support documentation how-to and find out how to fix the vulnerability. All Security level how-to’s can be found in the [Security category](../../best-practices/security.md).

## Performance Checks

The Performance checks in MageReport Premium tell you how to make your shop even faster, by showing the bottlenecks in your Magento.

### Number of Active Caches

This feature shows you how many caching options in your Cache Management (System –> Cache Management) have been enabled. The higher the number of active caches, the better. Caching stores data, so that future requests can be served faster. Read [Magento Cache Management](../../ecommerce-applications/magento-2/how-to-flush-the-magento-2-x-caches.md) for more information.

### Var/log Directory Size

This check tells you how big your var/log directory has gotten. We recommend keeping your var/log directory below 100 MB. To keep your Magento shop optimised and fast, you’ll need to clean these logs. Cleaning your logs can be done automatically or manually. We recommend your to do it manually, since it’s more efficient. Read [Magento Log Cleaning](../../ecommerce-applications/magento-1/how-to-clean-the-magento-1-x-logs.md) for more information on how to clean up these logs.

### Disk Usage

A full disk slows your Hypernode down. You can always [upgrade to a bigger node](https://service.byte.nl/planinfo/), but in most cases cleaning up your disk is sufficient. More information about cleaning up your disk is explained in [How to Free up Disk Space.](../../hypernode-platform/tools/how-to-free-up-disk-space)

### Bot Traffic

When your shop has at least 1600 PHP requests in one day and 30% of those are bots, the bot traffic check in MageReport turns red. Search engines indexing your webshop are very welcome, though too many bots can quickly consume your shop’s resources. Bots and crawlers often get stuck in the layered navigation of your Magento shop, causing them to crawl every combination of your products and parameters, creating millions of URLs to index and causing bad performance. Read how to optimize your shop by controlling these bots and crawlers in [Fixing bad performance caused by search engines](../../best-practices/performance/how-to-fix-performance-issues-caused-by-bots-and-crawlers.md).

### Response Time

This check shows you your average PHP response time in seconds. Keeping your load time below 1 second is preferable to keep your shop fast. The faster the webshop, the higher the conversion. A good tool to further analyse performance bottlenecks, and improve your response time, is New Relic. Read all about New Relic in [Find your performance bottleneck with New Relic](../../best-practices/performance/how-to-find-your-performance-bottleneck-with-new-relic.md).

### Memory Usage

We recommend you to keep at least 20% free to speed up file access and to make sure your Hypernode doesn’t slow down, or worse, stop working. If your shop is using more than 80%, consider upgrading to a bigger Hypernode to guarantee the continuity of your shop. Optimising your Hypernode with caching tools such as [Varnish](../../ecommerce-applications/magento-2/how-to-configure-varnish-for-magento-2-x.md) and Redis helps reduce the memory usage. Use New Relic to pinpoint which pages are slurping memory and find the cause.

### Optimize Images

Not optimising images properly results in extremely slow loading time. Quick loading images are important and a quick loading website keeps visitors engaged. Resizing images can take up a lot of time, so we took care of this for you. We developed a tool that’ll optimize all your images for you. You just need to take a few steps, explained in this Magento image optimisation how-to, and you’re all set!

*NB: MageReport.com checks for a cronjob that optimizes your images periodically. If you optimised your images only once, the check will come out red.*

## Stability

### Storefronts Configured Correctly?

Hypernode is cloud-based hosting, which means your IP can change. To make sure your visitors can still reach your Magento shop after a configuration change, you’ll need to redirect your storefronts using a CNAME. With `n98-magerun` or `n98-magerun2` you can find which storefronts are configured in in your webshop:

```nginx
n98-magerun sys:store:config:base-url:list
```

```nginx
magerun2 sys:store:config:base-url:list
```

This tool shows the storefronts configured in your shop and the storecode. In MageReport Premium you can check whether your DNS is configured correctly. See our manual on [configuring DNS](../../hypernode-platform/dns/how-to-manage-your-dns-settings-for-hypernode.md)for more information.

*If you’re using Cloudflare the check will say your storefronts aren’t configured correctly and your shop is not live. Right now MageReport can’t detect if a shop is using Cloudflare, so you can ignore this.*

## Charts

Most charts give you more specific information about a Performance check.

### PHP Requests per Minute

This chart shows the average number of PHP requests per minute. It includes visitors and bots requesting webpages. The orange line indicates requests done by bots. Bots and crawlers take up a lot of resources, especially in Magento, and can cause your shop to slow down. Read how to optimize your shop by controlling these bots and crawlers in [Fixing bad performance caused by bots and crawlers](../../best-practices/performance/how-to-fix-performance-issues-caused-by-bots-and-crawlers.md).

### Average PHP Response Time (Seconds)

The faster a page loads, the longer visitors will stay on your shop. Like the performance check ‘Response time’, the average PHP response time chart shows you (in seconds) how long it takes for pages to load. A well optimised Magento shop should be able to keep the response time below one second.

A good tool to further analyse performance bottlenecks, and improve response time, is New Relic. Read all about New Relic in [Find your performance bottleneck with New Relic.](../../best-practices/performance/how-to-find-your-performance-bottleneck-with-new-relic.md)

### Long Running Processes

This chart shows you the duration of long running processes. We recommend you to keep FPM processes running under 5 to 10 minutes, SQL processes no longer than 60 minutes and SSH processes no longer than 24 hours. If the proces duration is longer than the given criteria, you should consider them stuck and fix them. Long running processes or stuck processes are often the result of errors in your PHP code, a missing index (in SQL) or a deadlock. Read more about how to stop long running processes in [How to Identify and Stop Long Running Processes](../../troubleshooting/performance/how-to-identify-and-stop-long-running-processes.md).

### CPU Usage

A line of 50% or higher in this chart indicates your Hypernode is very busy. If your Hypernode uses a lot of resources, check for an increase of web requests (chart: PHP requests per minute). A periodic cronjob can also cause an increase in CPU usage. Optimising your Hypernode with caching tools such as [Varnish](../../ecommerce-applications/magento-2/how-to-configure-varnish-for-magento-2-x.md) and [Redis](../../ecommerce-applications/magento-2/how-to-configure-redis-for-magento-2.md) helps reduce the CPU usage. Consider upgrading to a bigger node if your shops consistently use more than 50% of the available CPU.

### Redis Memory in Use

This chart shows you the percentage of memory in use by Redis and the hitratio (percentage of requests served out of Redis cache). The more data is cached, the more the memory usage increases. The memory usage decreases when expired cache items are removed. Red vertical lines (not always showing), mean your cache was full and Redis deleted the least requested ([LRU](https://en.wikipedia.org/wiki/Cache_algorithms#LRU)) items. You’ll notice this can happen when less than 100% is used according to the graph. This is because the graph shows you the average usage (in %) per week.

We recommend you to upgrade to a bigger node if you're using more memory than your Hypernode offers. If all available memory is in use, Redis will delete cache items to free up memory, which could lead to a reduced hit ratio depending on your configuration. Every Hypernode has access to Redis, starting from 768 MB, depending on the plan. Please [check our website](https://www.hypernode.com/magento-cloud-hosting/#plans)for an overview of the Hypernode plans and their specs.
