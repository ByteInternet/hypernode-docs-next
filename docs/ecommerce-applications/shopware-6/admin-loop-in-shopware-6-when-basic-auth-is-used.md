---
myst:
  html_meta:
    description: When you want to use Shopware 6 on a Hypernode with basic auth you
      need to take into account that Shopware overwrites the Authorization header.
    title: How to prevent an admin loop in Shopware 6 on Hypernode?
redirect_from:
  - /en/support/solutions/articles/48001207548-workaround-for-known-issue-accessing-shopware-6-admin-on-a-development-plan/
---

# Admin loop in Shopware 6 when basic auth is used

On a Hypernode dev plan basic auth is enabled out of the box. You can also configure Nginx to put your site or parts of your site behind basic auth on a production plan. When you want to use Shopware 6 on a Hypernode with basic auth you need to take into account that Shopware overwrites the Authorization header.

Shopware uses OAuth with a bearer token for logging into the admin and using the API. For example if your shop is `http://<appname>.hypernode.io/`, that URL will work fine. But logging in to `http://<appname>.hypernode.io/admin/` will send you into a basic auth loop.

The solution is to whitelist your IP to skip the basic auth on the Hypernode when you come from your specified IP.

```nginx
# $ cat /data/web/nginx/whitelist-development-exception.conf
# You can make certain IP addresses exempt here from the development
# basic auth. Beware though, that google and bing bots will always
# remain blocked on development nodes!

geo $development_exceptions {
    default "Development restricted area";
    # The IP that you want to access the Shopware 6 admin from
    1.2.3.4 "off";
}
```
