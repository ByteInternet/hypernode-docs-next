---
myst:
  html_meta:
    description: Improve Magento search speed and relevancy with ElasticSearch or
      Sphinx Search. Out-of-box integration on Hypernode Pelican, Falcon and Eagle
      plans.
    title: How to improve your Magento search? | Hypernode
redirect_from:
  - /en/best-practices/performance/how-to-improve-your-magento-search/
  - /knowledgebase/how-to-improve-your-magento-search/
---

<!-- source: https://support.hypernode.com/en/best-practices/performance/how-to-improve-your-magento-search/ -->

# How to Improve Your Magento Search

The built-in Magento search option is known for it’s non-existent speed and providing irrelevant search results. Both these aspects have a negative effect on your conversion, because if visitors can’t find what they’re looking for, how do you expect them to purchase from your shop? As a developer there are two things you can do;

1. Tweak the built-in Magento search option
1. Use an external search engine.

We recommend the latter, and specifically: ElasticSearch. If you have a Magento 2 shop, ElasticSearch has one major advantage: you can use this search engine out-of-the-box, without having to install any extension. On all Hypernode Pelican, Falcon and Eagle plans, ElasticSearch is built-in to your Hypernode. If you are on a formerly known plan like Start or Grow, you’ll need to either upgrade, or make use of an external search provider. We have arranged special Hypernode discounts with our partner Bonsai, a specialised managed ElasticSearch provider. Ask our support team for the discount code!

Another alternative is Sphinx Search. Sphinx is an open source search engine that improves the search function in your Magento. Sphinx is fast and provides you with relevant search results. There are many external search engines, but Sphinx came out as the best option due to it’s usability, documentation and speed. Sphinx is supported on your Hypernode (Pelican, Falcon and Eagle plans). You will, however, need extra (paid) plugins for your Magento to make use of Sphinx.

## ElasticSearch

While previously it was already possible to use ElasticSearch with your Hypernode by connecting to an external search provider, we have now made it possible to use ElasticSearch for search in your shop out of the box on Hypernode without requiring any external service or configuration. In[this article](../../hypernode-platform/tools/how-to-use-elasticsearch-on-hypernode.md) we’ll explain a bit more about ElasticSearch and how to enable and configure it.

Please note that due to the relatively heavy resource requirements for ElasticSearch this feature can only be enabled on every plan except the formerly known Grow plan. If you are on a smaller plan and previously already depended on an external paid ElasticSearch provider now might be a good time to consider simplifying your setup.

### ElasticSearch providers

If you are on a lower plan, you’ll need to either upgrade, or make use of an external search provider. There a several companies you can choose for a monthly subscription:

- [Bonsai.io](https://bonsai.io/)
- [Qbox.io](https://qbox.io/)
- [Elastic.co](https://www.elastic.co/cloud/as-a-service)

**If you choose Bonsai, we have made a special deal with Bonsai. Please send a mail to support@hypernode.com for a discount code.**

## Sphinx

Sphinx indexes up to 10-15 MB of text per second per single CPU core 60+ MB/sec per server. Technically, Sphinx is a standalone software package that provides fast and relevant full-text search functionality to client applications. It was specially designed to integrate well with SQL databases storing the data, and to be easily accessed by scripting languages. However, Sphinx does not depend on – or requires – any specific database to function.

We added support for the Sphinx search indexer on Hypernode Pelican, Falcon and Excellent nodes. Using Sphinx requires the `Mirasvit Sphinx Search Ultimate extension`. This paid extension can be purchased through the [Mirasvit website](https://mirasvit.com/magento-extensions/sphinx-search-ultimate.html). If you have a Magento 2 shop, make sure to use the [specific Magento 2 extension](https://mirasvit.com/magento-2-extensions/sphinx-search-ultimate.html).

More information about using Sphinx can be found in [their documentation](http://sphinxsearch.com/docs/). Can’t find an answer to your question? Please contact Mirasvit through their [Support Portal](https://mirasvit.com/contact/).

### Configuring Sphinx on Hypernode

To configure Sphinx Search on Hypernode, all you need to do is install the Magento extention from Mirasvit and correct the settings in the Sphinx configuration panel in the Magento admin.

### Adjusting the Settings of the Mirasvit Sphinx Extension

When adjusting the Sphinx settings, you should make use the following information:

|                         |                                 |
| ----------------------- | ------------------------------- |
| **Name Setting**        | **Value**                       |
| Search Engine           | `External Sphinx Search Engine` |
| Sphinx Host             | `localhost`                     |
| Sphinx Port             | `9312`                          |
| Sphinx Bin Path         | `/usr/bin/searchd`              |
| Cron for Full Schedule  | `0 3 * * *`                     |
| Cron for Delta Schedule | `*/15 * * * *`                  |

### Troubleshooting

- When using the Mirasvit extension, Magento periodically restarts the Sphinx engine. If this happens too fast, the reload of Sphinx can be ratelimited causing the daemon to stop or to hang. To resolve this issue, whitelist the `Zend_Http_Client` as explained in [the instructions how to prevent a user agent from being rate limited](../../hypernode-platform/nginx/how-to-resolve-rate-limited-requests-429-too-many-requests.md#rate-limiting-for-bots-and-crawlers).
- If your shop is using too much memory, the `searchd` daemon can crash due to OOM. To resolve this upgrade to a bigger Hypernode, or improve the memory print of your webshop.
- The `searchd`daemon is started from the Magento backend, but in case of a server reboot, memory issues or an otherwise very busy server the process kan be killed, causing an interruption in your search functionality. To circumvent these issues, add a cron that checks if the daemon is running and starts it if it’s not:
  - For Magento 1:
  ```nginx
  @reboot chronic flock -E 0 -n ~/.sphinx.lock /usr/bin/searchd --config /data/web/public/var/sphinx/sphinx.conf --nodetach 2>&1 >> /tmp/search.log
  * * * * * chronic flock -E 0 -n ~/.sphinx.lock /usr/bin/searchd --config /data/web/public/var/sphinx/sphinx.conf --nodetach 2>&1 >> /tmp/search.log
  ```
  - For Magento 2:
  ```nginx
  @reboot chronic flock -E 0 -n ~/.sphinx.lock /usr/bin/searchd --config /data/web/magento2/var/sphinx/sphinx.conf --nodetach 2>&1 >> /tmp/search.log
  * * * * * chronic flock -E 0 -n ~/.sphinx.lock /usr/bin/searchd --config /data/web/magento2/var/sphinx/sphinx.conf --nodetach 2>&1 >> /tmp/search.log
  ```
- Mirasvit installs several scripts into `/shell/`. This location is blocked by default on Hypernode, for your security. If you wish to enable these files, you can exclude them by adding the following codeblock to `/data/weg/nginx/server.mirasvit`:

```nginx
location = /shell/filename.php {
 echo_exec @phpfpm;
}
```

## SOLR

A third option is SOLR. We don’t offer SOLR anymore due to low demand. If you want to use SOLR, we recommend using [WebSOLR](https://www.websolr.com/) as a hosted third party service.
