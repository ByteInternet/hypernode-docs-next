---
myst:
  html_meta:
    description: 'Some shop owners prefer a domain name starting with www, others
      prefer without. Read how to redirect from or to WWW in this article. '
    title: How to redirect from or to www? | Hypernode
redirect_from:
  - /en/hypernode/nginx/how-to-redirect-from-or-to-www/
  - /knowledgebase/redirect-from-or-to-www/
  - /knowledgebase/redirect-specific-domains-urls-https/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-redirect-from-or-to-www/ -->

# How to Redirect From or to WWW

Many constructions are possible when it gets to the base URL. Some shop owners prefer a domain name starting with www, others prefer without.

There are some restrictions when choosing your base URL.

If you use the wwwizer servers, which are sometimes used when your domain is not hosted at Hypernode and thus the DNS can’t be automagically changed in case of up or downgrades, your domain will always redirect to [www](http://www).

More info can be found [on our page about setting your DNS](../dns/how-to-manage-your-dns-settings-for-hypernode.md).

## Redirect From Apex to WWW

**When Hypernode Managed Vhosts is enabled**

To redirect all traffic to www you have to create both a vhost for the Apex and for the `www`. For the non-www vhost you can create the vhost as type wwwizer. This will redirect all traffic to the `www`. version of that vhost. This can be achieved by running: `hypernode-manage-vhosts example.com --type wwwizer`.

```text
| servername      | type     | default_server | https | force_https | varnish | ssl_config   |
| example.com     | wwwizer  | False          | False | False       | True    | intermediate |
| www.example.com | magento2 | False          | False | False       | False   | intermediate |
```

<!-- Legacy nginx instructions removed: Hypernode platform uses Managed Vhosts across the board. -->

## Redirect From WWW to Apex

To redirect all traffic from www to the apex domain use the following Nginx snippet:

```nginx
if ($http_host ~ ^www\.(?<domain>.+)$ ) {
    return 301 https://$domain$request_uri;
}
```

Save this snippet in `/data/web/nginx/server.rewrites` or in case you are using Varnish public.rewrites.

## Redirect When Using Varnish

When you are using Varnish, the redirect will be cached, causing a redirect loop.

To prevent this, you can use the public prefix, which is included before Varnish and thus will not be cached.

Save your file as `/data/web/nginx/public.rewrites`
