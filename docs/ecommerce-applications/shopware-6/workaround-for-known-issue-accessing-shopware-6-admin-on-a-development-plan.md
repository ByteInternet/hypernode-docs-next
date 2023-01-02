<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001207548-workaround-for-known-issue-accessing-shopware-6-admin-on-a-development-plan/ -->

# Workaround for Known Issue Accessing Shopware 6 Admin on a Development Plan

On a Hypernode Development plan the basic authentication is enabled out of the box. When you want to use Shopware 6 on a Hypernode with basic auth you need to take into account that Shopware overwrites the Authorization header.

Shopware uses OAuth with a bearer token for logging into the admin and using the API. For example if your shop is <http://mytestappname.hypernode.io/>, that URL will work fine. But logging in to <http://mytestappname.hypernode.io/admin/> will send you into a basic auth loop.

The solution is to whitelist your IP from the basic auth on the Hypernode to not use basic auth when you come from your specified IP. You can whitelist your IP in the `/data/web/nginx/whitelist-development-exception.conf` file.

```nginx
# $ cat /data/web/nginx/whitelist-development-exception.conf
# You can make certain IP addresses exempt here from the development
# basic auth. Beware though, that google and bing bots will always
# remain blocked on development nodes!

geo $development_exceptions {
    default "Development restricted area";
    1.2.3.4 "off"; # The IP that you want to access the Shopware 6 admin from
}

If your IP changes too often to whitelist you can always consider whitelisting `0.0.0.0/0`
```

If your IP changes too often to whitelist you can always consider whitelisting **0.0.0.0/0**but be careful, this indicates you're whitelisting the whole internet.
