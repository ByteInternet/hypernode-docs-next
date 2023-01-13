---
myst:
  html_meta:
    description: Due to clean-url-rewrites, that can result in a 404 error, some additional
      configuration is required to make use of the Magento 1 API.
    title: How to enable the Magento 1 API? | Hypernode
redirect_from:
  - /en/ecommerce/magento-1/how-to-enable-the-magento-1-api/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-enable-the-magento-1-api/ -->

# How to Enable the Magento 1 API

The Magento API is supposed to work out-of-the box on Hypernodes, but due to clean-url-rewrites sometimes the API does not work and returns a 404 error.
To resolve this issue, some additional configuration is required.

Use the following snippet and save it as `/data/web/nginx/server.api` to configure Nginx for routing all API requests to api.php:

```nginx
location /api {
    allow 198.51.100.1;
    allow 203.0.113.0/24;
    deny all;

    rewrite ^/api/rest /api.php?type=rest last;
    rewrite ^/api/v2_soap /api.php?type=v2_soap last;
    rewrite ^/api/soap /api.php?type=soap last;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }
}
```

NB: If you don’t want to update IP addresses in all config files with every change of IP address, you can choose to use [**include files**](../../hypernode-platform/nginx/how-to-create-a-reusable-config-to-include-in-custom-snippets.md).
