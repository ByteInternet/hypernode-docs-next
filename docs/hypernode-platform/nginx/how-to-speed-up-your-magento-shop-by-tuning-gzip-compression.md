---
myst:
  html_meta:
    description: 'You can speed up your Magento shop by Tuning Gzip Compression. Read
      how, in this article. '
    title: How to speed up a Magento shop by tuning GZIP compression?
redirect_from:
  - /en/hypernode/nginx/how-to-speed-up-your-magento-shop-by-tuning-gzip-compression/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-speed-up-your-magento-shop-by-tuning-gzip-compression/ -->

# How to Speed up Your Magento Shop by Tuning Gzip Compression

On Hypernodes, GZIP Compression is already configured to compress responses larger than 1000 bytes.

For experts however, it is possible to make your own adjustments to tune GZIP Compression.

Nginx already applies compression on requests proxied through PHP-FPM, so you should not set `zlib.output_compression = On` in your PHP settings.

**This is an advanced topic. For 90% of the Hypernode users the current GZIP settings will suffice.**

## Optimizing GZIP Compression to Your Own Needs

On the Hypernode you can check `/etc/nginx/nginx.conf` to see the current configuration for Hypernodes:

```nginx
gzip on;
gzip_disable "msie6";

gzip_min_length 1000;
gzip_proxied any;
gzip_types text/xml text/plain text/css text/js
application/xml application/javascript application/json;
```

These settings are static as we carefully picked these settings. In most of the scenario’s these settings are all you need and no additional tuning is necessary.

There are however [several options available that you can tune](http://nginx.org/en/docs/http/ngx_http_gzip_module.html).

### Setting the Compression Level

By default the GZIP compression level is set to 1. On bigger Hypernodes, you can adjust this setting by changing the compression level.

The `gzip_comp_level` settings takes an integer from 0 to 9 as it’s input.

The higher the compression level is set, the more compression is applied.

Setting a higher compression level will cost more CPU cycles, so setting this level too high can cause your shop to slow down.

### GZIP Minimum Response Length

Nginx uses compression when the response length is larger then 1000 bytes. Unfortunately the ‘gzip_min_length’ directive is not overridable.

We’ve ran tests that showed that values \< 850-950 actually caused a /decrease/ in speed, as the gain from compressing such small files is relatively small, and the time taken for compressing the files is actually greater than the time saved in transfer. As such, we would not recommend to change this setting.

### Adding a Vary Header When Compression Is Used

[Google Pagespeed](https://developers.google.com/speed/pagespeed/insights/) and [Yahoo Yslow](http://yslow.org/) both recommend setting a vary header on Accept-Encoding.

This can be done setting the `gzip_vary` to on.

So for example you create a nginx config file `/data/web/nginx/server.encoding` and add the following line:

```nginx
gzip_vary on;
```

Nginx will only add this header when compression is being used, which will depend on the `gzip_min_length` setting.

Another way of adding this header is by manually adding a vary header:

```nginx
add_header Vary Accept-Encoding;
```

### Adding GZIP Types

By default static content ie. javascript, css, xml and html is configured to make use of compression.

If you want to add more content types that should be compressed using GZIP, extend the gzip_types setting with the mimetypes you want to be gzipped.

For example:

```nginx
gzip_types
text/plain
text/css
text/js
text/x-js
text/xml
text/html
text/javascript
application/javascript
application/x-javascript
application/json
application/xml
application/rss+xml
application/xml+rss;
```

### Adding GZIP for Images or Other Binary Files

Images, media files and other binary formats are not recommended to be gzipped as they often already use compression mechanisms.

There are however there are some vector based image image formats that can be compressed:

image/svg

image/svg+xml

image/eps

These mimetypes can easily be added to `gzip_types` to enable compression for these types.

### Using Pre-Compressed Files

It is possible to manually compress certain files using gzip.

Nginx can use this when you set `gzip_static` to ‘on’.

When this setting is enabled, when requesting a file, Nginx will look for .gz and if this one is nonexistent, serve the non-compressed file otherwise.

### Testing GZIP Compression

One lesson learned after hours of debugging is not to make use of the website `checkgzipcompression.com` as this site often returns inconsistent results. Better alternatives to check whether your GZIP is working correctly are [GtMetrix](https://gtmetrix.com/) and [Gift of Speed](https://www.giftofspeed.com/gzip-test).

Another way of testing whether GZIP is working correctly is by using `curl`:

```nginx
curl --compressed -v 2>&1 >/dev/null | grep -E 'Accept-Encoding|Content-Encoding'
> Accept-Encoding: deflate, gzip
```

When GZIP is correctly configured, when using `curl --compressed`, the response headers should show `gzip` as accepted encoding format.

### How to Make GZIP Adjustments

GZIP settings can be set by creating a `http.gzip` file in `/data/web/nginx`. Settings files starting with `http.*` are only added in the http block.

This way you can use http.gzip to adjust the GZIP settings for your production shop and use the `staging.gzip` file to test it first on your staging environment only.
