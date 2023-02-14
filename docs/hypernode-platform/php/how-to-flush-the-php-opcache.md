---
myst:
  html_meta:
    description: 'You need to be able to flush the OPcache from the command line in
      case of errors. Follow these steps to flush the PHP OPcade in the CLI. '
    title: How to flush the PHP OPcache? | Hypernode
redirect_from:
  - /en/hypernode/php/how-to-flush-the-php-opcache/
---

<!-- source: https://support.hypernode.com/en/hypernode/php/how-to-flush-the-php-opcache/ -->

# How to Flush the PHP OPcache

Flushing the OPcache can be done from the Magento backend, but if you run into issues regarding the upgrade of Magento itself or it’s extensions, the backend is most often the first to suffer from inaccessibility.

Therefor, you need to be able to flush the OPcache from the command line in case of errors. This can be done using the `opcache_reset()`; PHP function.

If you call this function using the command line, PHP will try to reset the OPcache for the php-cli which won’t work for PHP-FPM. Therefor if you want to flush the OPcache, you should do this by creating a PHP script which we request using `curl` or a web browser.

To do this, first create a flush script:

```bash
mkdir /data/web/public/private
echo '<?php header("Cache-Control: private, no-cache, no-store, max-age=0, must-revalidate, proxy-revalidate"); opcache_reset(); echo "Opcache Flushed"; ?>' > /data/web/public/private/flush_opcache.php
```

Second, create some Nginx config to ensure you only flush the OPcache and not the rest of the interweb:

```nginx
location /private/ {
    allow 1.2.3.4; ## Replace with your own ip address
    allow 2.3.4.5; ## Replace with the ip address of the hypernode itself
    deny all;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }
}
```

Save the snippet as `/data/web/nginx/server.opcache`. Now you can flush the opcache by executing:

```bash
curl http://appname.hypernode.io/private/flush_opcache.php
```

… Or by visiting the URL in your browser.
