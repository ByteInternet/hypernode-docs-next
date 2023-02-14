---
myst:
  html_meta:
    description: Hypernode makes use of Nginx. This article explains how to set the
      server name in Nginx.
    title: How to set a server name in NGINX? | Hypernode
redirect_from:
  - /en/hypernode/nginx/how-to-set-the-server-name-in-nginx/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-set-the-server-name-in-nginx/ -->

# How to Set the Server Name in Nginx

Hypernode makes use of Nginx. Nginx has much better performance than Apache, and allows us to serve your webshop to many more visitors than Apache would. Some Magento module licenses, like [OneStepCheckout](http://www.onestepcheckout.com/), are tied to a specific server name (accessible in the environment variable `SERVER_NAME`). This article explains how to set the server name in Nginx.

## Set the Same server_name for Each Storefront

To explicitly set the server name to be example.com, create a file called `server.server_name` in `/data/web/nginx` containing:

```nginx
set $custom_server_name example.com;
```

This sets the `server_name` to example.com for all used storefronts.

## Dynamically Setting the server_name Depending on Your Used Storefront

If you use several licenses for multiple storefronts, you can easily set the `server_name` dynamically using a mapping.

To do this, first make sure no `server_name` is set already in any configuration. Then create a file called `http.servername` in `/data/web/nginx` with the following content:

```nginx
map $host $custom_server_name {
 hostnames;
   .example.nl example.nl;
   .example.net example.net;
   .example.com example.com;
}
```

This way for each domain used in Magento, the `server_name` is set to the given name in the mapping.

Using the “.” at the beginning of the hostname string, makes sure both example.nl and \*.example.com will be used in the mapping.

## External Resources

To configure which name to use in Nginx, you can use the [server names module](http://nginx.org/en/docs/http/server_names.html).
