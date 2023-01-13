---
myst:
  html_meta:
    description: Learn how to configure Cloudflare on your Hypernode to improve website
      performance, reduce network latency, and block threats.
    title: How to Use Cloudflare | Hypernode
redirect_from:
  - /en/best-practices/cdn/how-to-use-cloudflare-with-hypernode/
---

<!-- source: https://support.hypernode.com/en/best-practices/cdn/how-to-use-cloudflare-with-hypernode/ -->

# How to Use Cloudflare with Hypernode

To get started with Cloudflare on your Hypernode create an account at Cloudflare and change the nameservers of your domain to the Cloudflare nameservers.

Hypernodes are fully configured and support Cloudflare out of the box.

## Why Use Cloudflare

Cloudflare uses multiple datacenters across the world to ensure their point of presence is always close to your visitors. This way page load times and bandwidth usage can be reduced significantly up to twice as fast regardless of their location thanks to caching and smart network routing based on your location.

You always connect to the server closest to your location, reducing network latency as much as possible.

Cloudflare blocks threats, limits abusive bots and crawlers from wasting your bandwidth and server resources and offers an extensive caching suite comparable with Varnish, but without all the complexity in configuration. Using Cloudflare can reduce the amount of requests done on your Hypernode considerably. This is especially useful for high-traffic websites.

**Please note: Cloudflare is not 100% waterproof. Unfortunately, using Cloudflare might still leave you vulnerable to a certain extend. An example of such vulnerabilities can be found**[**here**](https://blog.christophetd.fr/bypassing-cloudflare-using-internet-wide-scan-data/)**.**

## Configuring Cloudflare

To setup Cloudflare for your shop, use the following steps:

1. Create an [account at Cloudflare](https://support.cloudflare.com/hc/en-us/articles/201720164-How-do-I-sign-up-for-CloudFlare-)
1. Login to your [Cloudflare admin panel](https://www.cloudflare.com/a/login)
1. Turn on caching and other performance optimization.
1. Copy all DNS Records from your current domain provider to the Cloudflare DNS admin
1. Change the nameservers of your domain(s)
1. Turn off all performance and caching functionality for your Magento admin panel:
   Caching (**Use cache level: Bypass**)
   Performance
   Rocket Loader JS optimization
   Mirage mobile image optimization
1. Test, test some more and after that, test it all again.

## Configuration of Cloudflare for Magento

Cloudflare provides [a very large knowledge base](https://support.cloudflare.com/hc/en-us) for dealing with a wide variety of issues and optimizations.

For using Cloudflare with Magento, please check [the article on their knowledge base](https://support.cloudflare.com/hc/en-us/articles/203904600-Using-CloudFlare-with-Magento) and their [Page Rules and Magento optimization article](https://www.cloudflare.com/features-page-rules/optimize-magento/).

## Extensions for Cloudflare

There are several extensions that provide Cloudflare integration for Magento.

Cloudflare itself provides only an extension for [Magento 2](https://www.cloudflare.com/integrations/magento/), that is still in beta.

## Using SSL With Cloudflare

Cloudflare offers SSL offloading. You can upload your SSL certificates to Cloudflare to make use of SSL. If you choose to do this, always manually order your SSL certificates so you can use the same certificate on both the Cloudflare servers and the Hypernode.

If you use manual SSL certificates, make sure you monitor when your certificate is about to expire.

## Redirection From HTTP to HTTP

Redirecting from HTTP to HTTPS can cause a *Too many redirects* error. This error comes from a cached redirect that is served on both HTTP and HTTPS connection, causing the site to redirect from HTTP to HTTPS.

To redirect all requests to HTTPS when using Cloudflare SSL, you should instead use [a page rule with the Always Use HTTPS action.](https://support.cloudflare.com/hc/en-us/articles/203295200-End-to-end-HTTPS-with-Cloudflare-Part-2-SSL-certificates)

## Blocking IP’s When Using Cloudflare

We created some configuration for Nginx that shows the remote IP of the visitor in the access.log instead of the remote IP of the Cloudflare servers.

This way you can block remote visitors without blocking all traffic coming from the same Cloudflare server. This does not work when using Railgun.

For example have a look at [our documentation about blocking or whitelisting IP’s in Nginx](../../hypernode-platform/nginx/how-to-block-allow-ip-addresses-in-nginx.md).

Another option is to configure a blocklist in the [Cloudflare Admin](https://www.cloudflare.com/a/login).

## Don’t Use Railgun on Hypernodes

Cloudflare provides a service called [Railgun.](https://blog.cloudflare.com/cacheing-the-uncacheable-cloudflares-railgun-73454/) The key to this service is a local proxy daemon that sends all requests from Cloudflare through a tunnel to the proxy instance that does the actual web requests.

Our tests with Railgun on Hypernodes showed a performance gain of just a few milliseconds, making it not a very significant performance optimization when working with Magento.

As we do not support Railgun (yet), we’ve seen some implementations running the Railgun daemon on a separate server. Doing so is not recommended as it will make all HTTP requests from Cloudflare arrive from the same remote IP.

When someone is trying to brute force your server or in case of an attack, our protection mechanisms will block the attacker. When you use Railgun, our mechanisms will not block the remote IP but block the IP of the Railgun daemon instead, blocking all traffic coming from Cloudflare and therefore block all visitors to your shop.
