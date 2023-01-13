---
myst:
  html_meta:
    description: "Improve your website speed with Hypernode's PageSpeed Booster. Learn\
      \ how to implement it in just a few clicks and get the most out of your website. "
    title: How to implement the PageSpeed Booster? | Hypernode
redirect_from:
  - /en/troubleshooting/performance/how-to-implement-pagespeed-booster/
---

<!-- source: https://support.hypernode.com/en/troubleshooting/performance/how-to-implement-pagespeed-booster/ -->

# How to Implement PageSpeed Booster

## Requirements

To get started with the PageSpeed Booster (formerly known as Percolate), you must meet the following requirements:

- ***Production environment that is hosted on Hypernode.***
- ***Development/staging environment that is a copy of live and hosted on Hypernode.***
- ***Varnish has to be enabled***
- ***Time to thoroughly test the environment with PageSpeed Booster enabled.***

If you don't have a dev environment, then you can easily acquire one in your Control Panel

After you meet the requirements, you can send us a support ticket that includes the domain name where we can activate PageSpeed Booster on. For example psb.<yourdomainname>.com

After this, we will create a shared Slack channel with you, so we have a central place for the communication.

In this channel, we can quickly communicate during the test period.

Keep in mind that PageSpeed Booster is a complex tool that require a lot of testing before it can be pushed to the live site.

For example, it is possible that your site has errors in the HTML/CSS code. The PageSpeed Booster will find these errors, and they have to be fixed for the PageSpeed Booster to work correctly.

## What is PageSpeed Booster

PageSpeed Booster is a reverse proxy that sits in front of your website, just like Varnish. On pages that can be cached, it uses many static optimisation techniques to greatly increase the pagespeed score and performance of your website.

PageSpeed Booster is build on top of Kubernetes. For each application, a separate PageSpeed Booster instance is started on the cluster. None of the components, settings or version used are shared between applications. This ensures maximum stability and complete control over the update process.

**Internals**

PageSpeed Booster consists of a few components, you should not be bothered by most of them but for the purpose of understanding how PageSpeed Booster works, it is useful to keep these in mind.

- Proxy - Proxy requests to the application backend, creates new optimize jobs and handles API requests.
- Worker - Runs optimize jobs.
- RabbitMQ - Jobqueue for optimize jobs.
- Redis - Caches stored optimized responses.
- MongoDB - Stores optimize state for optimize requests and handled optimize requests.
- Chromium - Render engine.
- Cypress - Test environment.
- Test server - Test server to mock behavior of a real webserver during tests.
- Imgproxy - Service for resizing and optimizing images.

## Configuring PageSpeed Booster on your Development Environment

### Configure SSL and DNS

To setup PageSpeed Booster on your development environment you'll need a unique domain. For example you can use, **psb.example.com**. So make sure to follow these steps:

1. Point the DNS of the test domain, **psb.example.com**, to your development Hypernode.
1. Create the vhost with SSL and Varnish:
   `hypernode-manage-vhosts psb.example.com --https --force-https --varnish`
1. Now point the DNS to the PageSpeed Booster instance with the records you got at the PageSpeed Booster page in your Control Panel.
1. Make sure Varnish is enabled on the server: hypernode-systemctl settings varnish_enabled.
1. Add the user agent **PSB**to the [allowlist for the ratelimiter](../../hypernode-platform/nginx/how-to-resolve-rate-limited-requests-429-too-many-requests.md#whitelisting-additional-user-agents) in\*\*~/nginx/http.ratelimit\*\* file.
1. Disable the [basic-authentication](../../hypernode-platform/nginx/basic-authentication-on-hypernode-development-plans.md#disable-the-basic-authentication) on the development Hypernode.

### Configuring Varnish

By now you've a valid SSL for your test domain, and pointed it to the PageSpeed Booster instance which now works as a proxy. What's left is that you make the required changes to your **.vcl** so that the PageSpeed Booster is able to optimize your pages.

If you're using the default generated .vcl configuration file from the Magento 2 backend you could replace that **.vcl** with **[this template](https://gist.github.com/hn-support/2478eb5ed8328553de813f524ae12f91)** which we already adjusted for the PageSpeed Booster.

## Configure Varnish on your application

The last step will be configuring Varnish on your application. Below you can find our available documentation for configuring Varnish on the application you’re using:

- [How to configure Varnish for Magento 1](../../ecommerce-applications/magento-1/how-to-configure-varnish-for-magento-1-x.md)
- [How to configure Varnish for Magento 2](../../ecommerce-applications/magento-2/how-to-configure-varnish-for-magento-2-x.md)
- [How to configure Varnish for Shopware 5](../../ecommerce-applications/shopware-5/how-to-configure-varnish-for-shopware-5.md)
- [How to configure Varnish for Shopware 6](../../ecommerce-applications/shopware-6/how-to-configure-varnish-for-shopware-6.md)

## Modifying your Current Varnish VCL configuration

If you already have an existing .vcl active with some customisations specific for your shop you'd have to make some changes to your existing .vcl. Make sure to make the following changes:

### Turn off ESI Block Parsing

Configure Varnish to turn off parsing Edge Side Includes. You can do this by editing the following configuration.

```vcl
if (beresp.http.content-type ~ "text") {
    set beresp.do_esi = true;
}
```

Change it to:

```vcl
if (!beresp.http.X-Percolate && beresp.http.content-type ~ "text") {
    set beresp.do_esi = true;
}
```

Edit the lines that are responsible for setting the Cache-Control header to `"no-store, no-cache, must-revalidate, max-age=0";`. How this looks exactly, depends on your Varnish configuration and could differ per project. >The most common configuration looks like:

```vcl
# Not letting browser to cache non-static files.
if (resp.http.Cache-Control !~ "private" && req.url !~ "^/(pub/)?(media|static)/") {
    set resp.http.Pragma = "no-cache";
    set resp.http.Expires = "-1";
    set resp.http.Cache-Control = "no-store, no-cache, must-revalidate, max-age=0";
}
```

We'll change the configuration fragment to check if the `X-Percolate` header is present, by using a condition.

```vcl
# Not letting browser to cache non-static files.
if (!req.http.X-Percolate && resp.http.Cache-Control !~ "private" && req.url !~ "^/(pub/)?(media|static)/") {
    set resp.http.Pragma = "no-cache";
    set resp.http.Expires = "-1";
    set resp.http.Cache-Control = "no-store, no-cache, must-revalidate, max-age=0";
}
```

Remove the following line:

```vcl
unset resp.http.X-Magento-Tags
```

Now, save the new .vcl as for example **psb_varnish.vcl**, and all you need to do is reload the varnish configuration into Varnish. This can be done by loading it with a slightly different identifier followed by activating the new config:

```bash
varnishadm vcl.load psb /data/web/psb_varnish.vcl
varnishadm vcl.use psb
```

## Add PageSpeed Booster as Flush Target

With the addition of Pagespeed booster, you'll have to deal with an extra layer of cache that needs to be flushed when demanded.

Add your Pagespeed booster URL to your Magento `http_cache_hosts` configuration:

```bash
bin/magento setup:config:set \
  --http-cache-hosts=varnish:6081,appname-appname.fsn1.percolate-3.hipex.cloud:80
```

After the change in your **env.php** perform a cache clean:

```bash
bin/magento cache:flush
```
