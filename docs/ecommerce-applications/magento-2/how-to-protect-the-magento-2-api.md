---
myst:
  html_meta:
    description: Hypernode has protected unauthorized access for specific API methods
      for all our customers. Not hosted on Hypernode? Follow these instructions!
    title: How to protect the Magento 2 API? | Hypernode
redirect_from:
  - /en/ecommerce/magento-2/how-to-protect-the-magento-2-api/
  - /knowledgebase/protecting-the-magento-2-api/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-protect-the-magento-2-api/ -->

# How to Protect the Magento 2 API

```{note}
The Magento team released security update [Magento 2.0.3](https://magento.com/security/patches/magento-203-security-update) on March 30th 2017. This release contains a security fix that restricts access to anonymous web APIs. [Read more.](https://magento.com/security/best-practices/restricting-access-anonymous-web-apis) We recommend you to [update your Magento](how-to-update-magento-2.md) version to Magento 2.0.3 instead of blocking the API.
```

In March 2016, Paul Bosselaar and others discovered that the Magento 2 API by default discloses information that can be considered private:

- All products, including offline/disabled products, pricing rules, stock information. A competitor could monitor your stock and see exactly how many products you sell and when.
- Admin token generation. This requires admin credentials, but there is no rate limit. Magento forced an obscured admin login URL, but that is of no use when an attacker can brute force the API.
- Site and store configuration. The API will tell you which other stores/URLs are configured for this shop.

At the time of writing (2016), Magento has [responded](https://github.com/magento/magento2/issues/3719) that “this is as designed”. We discussed this with our partners and some were highly surprised. So to be on the safe side, we have protected unauthorized access for specific API methods for all our customers.

Some quick conclusions:
Your shop is running on Hypernode? We have got you covered!
You’re shop is hosted somewhere else? See below for instructions

## I'm a Hypernode User

Several API methods that might leak confidential data are protected by default:

```
V1/products
V1/store/storeViews
V1/store/storeConfigs
```

If you need to allow one or more of these URLs to be accessable, you can easily modify the default configuration. Log in on your Hypernode and edit the file `/data/web/nginx/server.magento2api`.

Modify the lines of the following block:

```nginx
location ~ ^/(pub/)?(rest|soap)(/.+)?/V1/(products|store/storeViews|store/storeConfigs)/?$ {
    return https://support.hypernode.com/knowledgebase/protecting-the-magento-2-api/;
}
```

When full access to the API is needed, the easiest way to do this is done with `/data/web/nginx/server.magento2api` to emtpy the file. An alternative would be to put all the lines in comment to deactivate the protection.

If you do not require the API, it is recommended to block it entirely. Edit the file `/data/web/nginx/server.magento2api`, remove all lines and add

```nginx
location ~ ^/(pub/)?(rest|soap)/ {
    return 403;
}
```

## I'm Not a Hypernode User

You will need to do some extra work yourself. First, contact your hosting provider and ask them to help you. Otherwise you can block the API using .htaccess in case of Apache. Perhaps the Nginx rules above might work, but we do not provide support on them for non-Hypernode environments. Good luck!
