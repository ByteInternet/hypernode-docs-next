---
myst:
  html_meta:
    description: Learn how to configure the "Converter for Media – Optimize images
      | Convert WebP & AVIF" plugin on your Hypernode server. Follow step-by-step
      instructions to verify your VHOST type, update NGINX configuration, and test
      the plugin for optimal performance and compatibility with WordPress/WooCommerce.
    title: How to Configure "Converter for Media – Optimize images | Convert WebP
      & AVIF" Plugin on Hypernode
---

<!-- source: https://support.hypernode.com/en/ecommerce/woocommerce/how-to-configure-converter-for-media-plugin-for-wordpress-woocommerce/ -->

# How to Configure Converter for Media – Optimize images Convert WebP & AVIF Plugin on Hypernode

For the WordPress/WooCommerce plugin [Converter for Media – Optimize images | Convert WebP & AVIF](https://nl.wordpress.org/plugins/webp-converter-for-media/), an adjustment is required in your Hypernode NGINX configuration. To make it easier for you, follow the instructions below to get the plugin working correctly on Hypernode.

## Verify your VHOST type

First, check if your VHOSTS has the correct type by running the following command:

```bash
hmv --list

```

Running this command will give you an output like this:

```console
+-------------------+----------+----------------+-------+-------------+---------+--------------+
|     servername    |   type   | default_server | https | force_https | varnish |  ssl_config  |
+-------------------+----------+----------------+-------+-------------+---------+--------------+
| test.hypernode.io | magento2 |      True      |  True |     True    |  False  | intermediate |
+-------------------+----------+----------------+-------+-------------+---------+--------------+
```

As you can see, the type is incorrect because it needs to be set to WordPress. To change this, use the following command:

```bash
hmv --type wordpress --https test.hypernode.io
```

After running this command, your VHOSTS will be set to WordPress. Make sure to replace `test.hypernode.io` with your actual domain name.

## Update NGINX configuration for the plugin

To ensure that "Converter for Media – Optimize images | Convert WebP & AVIF" works correctly, apply the following configuration:

```nginx
# BEGIN Converter for Media
set $ext_avif ".avif";
if ($http_accept !~* "image/avif") {
    set $ext_avif "";
}

set $ext_webp ".webp";
if ($http_accept !~* "image/webp") {
    set $ext_webp "";
}

location ~ /wp-content/(?<path>.+)\.(?<ext>jpe?g|png|gif|webp)$ {
    add_header Vary Accept;
    add_header Cache-Control "private";
    expires 365d;
    try_files
        /wp-content/uploads-webpc/$path.$ext$ext_avif
        /wp-content/uploads-webpc/$path.$ext$ext_webp
        $uri =404;
}
# END Converter for Media
```

Place the above configuration in `/data/web/server.media.conf.` Once you save the file, NGINX will automatically reload, and if something goes wrong, you will be notified.

## Test the Configuration

To test the configuration, you can use the following command:

```bash
➜  ~ curl -IL -H "Accept: image/webp" https://test.hypernode.io/wp-content/upload/test.jpg

HTTP/2 200
server: nginx
date: Mon, 13 May 2024 08:49:44 GMT
content-type: image/webp
content-length: 53624
last-modified: Wed, 08 May 2024 13:34:25 GMT
etag: "663b7f61-d178"
expires: Tue, 13 May 2025 08:49:44 GMT
cache-control: max-age=31536000
vary: Accept
cache-control: private
accept-ranges: bytes
```

By following these instructions, you should be able to configure and test the "Converter for Media – Optimize images | Convert WebP & AVIF" plugin to work correctly on your Hypernode server.
