---
myst:
  html_meta:
    description: 'Read how to configure Nginx for a multistore in this in depth step-by-step
      guide, starting with preparing your Magento shop. '
    title: How to configure NGINX for a multistore? | Hypernode
redirect_from:
  - /en/hypernode/nginx/how-to-configure-nginx-for-a-multistore/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-configure-nginx-for-a-multistore/ -->

# How to Configure Nginx for a Multistore

## Prepare Your Magento Shop

Before configuring Nginx, make sure all storefront configuration is present. Make sure you have the store code for each storefront you want to serve.

The main Magento documentation on configuring multiple storefronts can be found [here for Magento 1](http://docs.magento.com/m1/ce/user_guide/store-operations/stores-multiple.html) and [here for Magento 2](http://devdocs.magento.com/guides/v2.0/config-guide/multi-site/ms_websites.html).

## Setting Up Your Multistore

There are multiple ways to set up your Magento multistore. You can choose between the following options:

- Using different domains (e.g. example.com and example.net etc.)
- Using subdirectories (e.g. example.com/en/ and example.com/fr/ etc.)
- Using a combination of different domains and subdirectories (e.g. example.com and example.net/en/ and example.net/fr/)

Below we have provided the instructions on how to set up each of the scenarios within Nginx on your Hypernode. Please do note that in order to follow the instructions your Hypernode must have [Hypernode Managed Vhosts](hypernode-managed-vhosts.md) enabled. Furthermore, we cannot guarantee that the instructions will work with all plugins and custom configurations since this has only been tested with the default Luma theme and without any customizations.

### Using Different Domains

When you opt for using different domains for each storefront then it will be relatively simple to setup Nginx for your multistore. Simply following the instructions on adding a new vhost with the instructions provided in the [Hypernode Managed Vhosts](hypernode-managed-vhosts.md) documentation. Once you have added the required vhost you need to add a `server.storecode` file to the specific vhost directory (`/data/web/nginx/example.com/`) with the following content:

```nginx
set $storecode "example_storecode";
```

```{important}
If you have a multistore, with hypernode-manage-vhost enabled AND you are using Varnish.
You'd have to prefix the file with `varnish` instead of `server`, like `varnish.storecode`.
This way these multistore requests will go through varnish and will then be rewritten accordingly with the `varnish.storecode` configuration.
```

### Use a different Store Type

Magento uses a default store type of `store`, you can change this to `website` too if this better fits your need, more information about this can be found on `MAGE_RUN_TYPE` in [the Magento 2 official documentation](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/multi-sites/ms-overview).

```nginx
set $storetype "store";
```

### Using Subdirectories

Another option is to use subdirectories instead. Once you have added the required vhost you need to add a `server.storecode` file to the specific vhost directory (`/data/web/nginx/example.com/`) with the following content:

```nginx
location ~ ^/(?<uri_prefix>(nl|fr))/ {
    if ($uri_prefix = fr) {
        set $storecode "be_fr";
    }
    if ($uri_prefix = nl) {
        set $storecode "be_nl";
    }
    rewrite / /$uri_prefix/index.php last;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }
}
```

In addition to the `server.storecode` you need to add a `server.slash` to enforce a trailing slash after the country code to prevent potentially other matches. In this example with `/fr` and `/nl` you'll need the following content:

```nginx
rewrite ^/(nl|fr)$ $1/ permanent;
```

In the example above we have used the subdirectories `/fr` and `/nl`.

Next to the correct Nginx configuration you will also need to create the subdirectories in the webroot folder (normally this would be `/data/web/public`) using symlinks like below:

```bash
ln -s /data/web/public /data/web/public/fr
ln -s /data/web/public /data/web/public/nl
```

### Using a Combination of Different Domains and Subdirectories

The third option is to combine different domains and subdirectories. In that case you need to create a vhost for the different domains you wish to use. In each of the vhost directories ( `/data/web/nginx/example.com/`) you then need to either use the snippet below to simply point the domain to a storefront:

```nginx
set $storecode "example_storecode";
```

**Please note that this is for any domains that do no use the subdirectory structure.**

Or use the following snippet to point the subdirectory for a specific domain to the intended storefront:

```nginx
location ~ ^/(?<uri_prefix>(nl|fr))/ {
    if ($uri_prefix = fr) {
        set $storecode "be_fr";
    }
    if ($uri_prefix = nl) {
        set $storecode "be_nl";
    }
    rewrite / /$uri_prefix/index.php last;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }
}
```

In addition to the `server.storecode` you need to add a `server.slash` to enforce a trailing slash after the country code to prevent potentially other matches. In this example with `/fr` and `/nl` you'll need the following content:

```nginx
rewrite ^/(nl|fr)$ $1/ permanent;
```

Last but not least you will also need to create the subdirectories in the webroot folder (normally this would be `/data/web/public`) using symlinks like below:

```bash
ln -s /data/web/public /data/web/public/fr
ln -s /data/web/public /data/web/public/nl
```

## Example Setup

Below you can find an example setup where all the above options have been combined.

```text
Magento Stores - Base URLs
+----+---------+------------------------------------+--------------------+
| id | code    | unsecure_baseurl           | secure_baseurl             |
+----+---------+------------------------------------+--------------------+
| 1  | default | https://www.example.com/   | https://www.example.com/   |
| 2  | fr      | https://www.example.nl/fr/ | https://www.example.nl/fr/ |
| 3  | en      | https://www.example.nl/en/ | https://www.example.nl/en/ |
| 4  | be_fr   | https://www.example.be/fr/ | https://www.example.be/fr/ |
| 5  | be_nl   | https://www.example.be/nl/ | https://www.example.be/nl/ |
| 6  | nl      | https://www.example.nl/    | https://www.example.nl/    |
+----+---------+------------------------------------+--------------------+
```

First add the following vhosts using the information from the [Hypernode Managed Vhosts](hypernode-managed-vhosts.md) documentation.

- [www.example.com](http://www.example.com)
- [www.example.nl](http://www.example.nl)
- [www.example.be](http://www.example.be)

Once the vhosts have been created, you can create a `server.storecode` file in `/data/web/nginx/www.example.com` with the below content:

```nginx
set $storecode "default";
```

Next you create a `server.storecode` file in `/data/web/nginx/www.example.be` with the following content:

```nginx
location ~ ^/(?<uri_prefix>(fr|nl)) {
    if ($uri_prefix = fr) {
        set $storecode "be_fr";
    }
    if ($uri_prefix = nl) {
        set $storecode "be_nl";
    }
    rewrite / /$uri_prefix/index.php last;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }
}
```

A similar `server.storecode` file needs to be created in `/data/web/nginx/www.example.nl`, but the content will be slightly different than for the `www.example.be` domain:

```nginx
set $storecode "nl";
location ~ ^/(?<uri_prefix>(en|fr)) {
    if ($uri_prefix = en) {
        set $storecode "en";
    }
    if ($uri_prefix = fr) {
        set $storecode "fr";
    }
    rewrite / /$uri_prefix/index.php last;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }
}
```
