---
myst:
  html_meta:
    description: Varnish is a complex technique that needs some experience to set
      it up. This article explains how you can configure Varnish 4 or 6 for your Hypernode.
    title: How to configure Varnish for Magento 2? | Hypernode
redirect_from:
  - /en/ecommerce/magento-2/how-to-configure-varnish-for-magento-2-x/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-configure-varnish-for-magento-2-x/ -->

# How to Configure Varnish for Magento 2.x

Customers with Hypernode Pelican, Falcon (formerly known as Professional) and Eagle (formerly known as Excellence plans can use Varnish to boost their Magento shop. This article explains how you can configure Varnish 4 or 6 for your Hypernode. If you want to know which Varnish version you need to configure, please check the [Magento documentation](https://devdocs.magento.com/guides/v2.4/install-gde/system-requirements.html) first. Do you have a Magento 1 shop, please check [this article](../../ecommerce-applications/magento-1/how-to-configure-varnish-for-magento-1-x.md).

Although Varnish is extremely awesome when it get's to speeding up websites, Varnish is a complex technique that needs some experience to set it up. Don't implement varnish on production nodes without testing Varnish first on a [development node](../../hypernode-platform/tools/how-to-use-hypernode-development-plans.md) or the [Hypernode Docker](../../best-practices/testing/hypernode-docker.md).

## Enable Varnish for Magento 2.x

As Magento 2 supports Varnish out of the box, there is no need for the turpentine extension anymore in Magento 2. Simply follow the steps below to configure Varnish 4.0, 6.0 or 7.x for Magento 2.

**First configure the Varnish version (4.0, 6.0 or 7.x) via the [hypernode-systemctl tool](../../hypernode-platform/tools/how-to-use-the-hypernode-systemctl-cli-tool.md)**

```console
$ hypernode-systemctl settings varnish_version 7.x
```

**Enable Varnish via the [hypernode-systemctl tool](../../hypernode-platform/tools/how-to-use-the-hypernode-systemctl-cli-tool.md)**

```console
$ hypernode-systemctl settings varnish_enabled True
```

**Enable Varnish via the [Control Panel](https://auth.hypernode.com/)**

- Click on "Hypernodes"
- Click on "Caching"
- Select the Hypernode
- Click on "Enable Varnish"

## Configure Varnish on the Vhost

Since the introduction of [hypernode-manage-vhosts](https://changelog.hypernode.com/changelog/release-7166-hypernode-manage-vhosts-enabled-by-default/) Hypernode may work somewhat different than you might be used to. With HMV enabled, it requires one more step to configure Varnish for your shop/vhost. Remember, for each domain, there should be a vhost created. You can list an overview of all configured vhosts with `hypernode-manage-vhosts --list`. While you do that, note that there is a column, "varnish". By default this is set to "False". Which means that Varnish isn't configured for this vhost. You can configure Varnish for the vhost by running the following command:

```console
$ hypernode-manage-vhosts EXAMPLE.COM --varnish
```

## Configure Magento 2.x for Varnish

### Configure Magento to use Varnish

The first step is to configure Magento to make use of the Varnish caching backend and to know which Varnish port needs to be used when flushing the cache.

```console
$ cd /data/web/magento2
$ bin/magento config:set system/full_page_cache/caching_application 2
$ bin/magento setup:config:set --http-cache-hosts=varnish:6081
```

Now when you flush your caches in cache management, your Varnish full_page cache will be flushed too.

### Generating the VCL

Run the following commands to generate the VCL configuration from Magento. The second command will remove the health check probe, which is not needed for full-page caching.

In this example, we pass the option `--export-version=6`, change the version number to the Varnish version you're using. As of writing, the following options are supported: 4, 5 and 6. If you're using Varnish 7, you can go with `--export-version=6`.

```console
$ bin/magento varnish:vcl:generate --export-version=6 --backend-host="127.0.0.1" --access-list localhost > /data/web/magento2.vcl
$ sed -i -E '/[[:space:]]*\.probe[[:space:]]*=[[:space:]]*\{/,/[[:space:]]*}/d' /data/web/magento2.vcl
```

**Note:** If you are using a cluster setup, you need to add some additional configuration to your VCL.
The `acl purge` block inside your vcl should contain the private ip range of your cluster.
You can find your private ip range using the `hypernode-cluster-info` command on one of your cluster nodes.

As example, our private ip range is `192.168.1.0/24`.
You can add this to the `acl purge` block. It should like something similar as the example below:

```
acl purge {
    "localhost";
    "192.168.1.0/24";
}
```

## Import Your VCL into the Varnish Daemon

Import your VCL into Varnish and save as `magento2`:

```console
$ varnishadm vcl.load magento2 /data/web/magento2.vcl
```

The output should say: *your VCL is compiled*. If you receive a `Permission denied` error, and have recently activated Varnish, please close all ssh sessions, and log back in to reload your new permissions.

Now tell Varnish to activate the loaded VCL:

```console
$ varnishadm vcl.use magento2
```

In the examples we used the name ‘magento2’ for our VCL, but you can use any name you prefer.

### Test if the Correct VCL is Uploaded

List all VCL’s with the following command:

```console
$ varnishadm vcl.list
```

The VCL you just imported and activated should have the status `active`. If all went well, varnish is now functioning with a working VCL.

### The "Boot" profile

To make sure your .vcl stays active even after a restart of Varnish we run a script every 5 minutes which saves the running config to /data/var/varnish/default.vcl which will be used once Varnish restarts. the "boot" profile will check what the last running .vcl was, and use that config in the "boot" profile.

This will mean that your loaded .vcl profile won't be existing the next time you'll look, and that your own .vcl profile is renamed to "boot". This is expected behaviour.

## Flush Your Varnish Cache When Using Magento 2

To flush the Varnish cache of your Magento store on the command line you can use `/data/web/magento2/bin/magento cache:flush full_page` This will purge the Varnish cache of the local Varnish instance.

Additionally you can flush your cache through the Magento admin backend or use `varnishadm` directly:

```console
$ varnishadm "ban req.url ~ ."
```

Or if you want to flush the cache for a single domain in a multisite setup:

```console
$ varnishadm "ban req.http.host == example.com"
```

## Warming Your Cache

Magento 2 doesn't need to use turpentine anymore, so we can't use the cache crawler provided with turpentine. As an alternative you can use an extension to warm your cache or the cache warmers we provided on our Github account, [here](https://gist.github.com/hn-support/60016f4b7986ad2cce693bdf2f3501b4) and [here](https://gist.github.com/hn-support/bc7cc401e3603a848a4dec4b18f3a78d).

## Enable Debug Headers

If you are implementing Varnish on Magento 2, you might want to view some caching headers that indicate whether the page is cacheable or not. To do this, put your Magento install in `Developer mode`. Now if you request a page through curl, you can see the `X-Magento-Cache-Debug` header:

```console
$ curl -I -v --location-trusted 'example.hypernode.io' > /dev/null | grep X-Magento
```

Which will show the debug headers:

```console
$ curl -I -v --location-trusted 'example.hypernode.io' > /dev/null | grep X-Magento
X-Magento-Cache-Control: max-age=86400, public, s-maxage=86400
X-Magento-Cache-Debug: MISS
```

## Troubleshooting

- If you are receiving `Permission denied` errors while running `varnishadm` or other Varnish CLI commands, and you have just activated Varnish, close any existing ssh sessions, and log back in to reload your updated permissions.
- If your Varnish setup is not working over SSL, check [this article](../../hypernode-platform/ssl/how-to-use-ssl-certificates-on-your-hypernode-when-ordered-via-hypernode-com.md#redirecting-to-https-when-using-varnish)

### 502 Errors

Sometimes while you enable Varnish, or even while Varnish was already enabled and there is something else changed on the shop you might get a **502** error. In the nginx error.logs (/var/log/nginx/error.log) you'll find the related error:

"*upstream sent too big header while reading response header from upstream*"

This error can 9 out of 10 times be fixed by adding some Nginx config. You can create a file, i.e. **~/nginx/server.header_buffer** with the following content:

```nginx
fastcgi_buffers 16 16k;
fastcgi_buffer_size 32k;
proxy_buffer_size 128k;
proxy_buffers 4 256k;
proxy_busy_buffers_size 256k;
```

### 503 Errors

- There is a bug when Varnish is activated on Magento 2.2.0, resulting in a "503 backend fetch" error. Please see Magento Github issue [10165](https://github.com/magento/magento2/issues/10165). For now, we advise you to either wait with upgrading to Magento 2.2.0 when using Varnish until this bug is fixed or use an adjusted .vcl as a temporary workaround:
- In Magento 2.4.x (and possibly earlier versions as well) a solution could be to disable the **product_identities_extender** plugin. This is a default Magento plugin which doesn't seem to work properly with Varnish enabled. All credit for this solution goes to [Tree of Information](https://www.treeofinformation.nl/) whom have spend a long time investigting this issue.

### Restart Varnish

If you ever need to restart Varnish you can use the following systemctl command for that:

```console
$ hypernode-servicectl restart varnish
```

## Performance improvement

The default Nginx + Varnish configuration is already optimized for performance. However, there are some additional tweaks you can do to improve the performance of your Varnish setup.

One of which is to bypass /static and /media requests from Varnish. The benefits of doing this are:

- Asset requests don't go through from `nginx -> varnish -> nginx`
- Lower load on nginx and varnish
- Lower amount of logs written to disk for both nginx and varnish

This can be done by adding the following to your Nginx configuration:

```{code-block} nginx
---
caption: server.magento2.conf
---
# Static content block:
location /static/ {
    expires max;

    # Remove signature of the static files that is used to overcome the browser cache
    location ~ ^/static/version {
        rewrite ^/static/(version\d*/)?(.*)$ /static/$2 last;
    }

    # Magento 2 recommends adding the .html, .json and .webmanifest extensions too, but those are resources fetched with
    # XHR method, which should be managed in user space and not system wide.
    #location ~* \.(ico|jpg|jpeg|png|gif|svg|svgz|webp|avif|avifs|js|css|swf|eot|ttf|otf|woff|woff2|html|json|webmanifest)$ {
    location ~* \.(ico|jpg|jpeg|png|gif|svg|svgz|webp|avif|avifs|js|css|swf|eot|ttf|otf|woff|woff2)$ {
        add_header Cache-Control "public";
        add_header X-Frame-Options "SAMEORIGIN";
        expires +1y;

        if (!-f $request_filename) {
            rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=$2 last;
        }
    }

    location ~* \.(zip|gz|gzip|bz2|csv|xml)$ {
        add_header Cache-Control "no-store";
        add_header X-Frame-Options "SAMEORIGIN";
        expires    off;

        if (!-f $request_filename) {
            rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=$2 last;
        }
    }

    if (!-f $request_filename) {
        rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=$2 last;
    }
    add_header X-Frame-Options "SAMEORIGIN";
}

# Media content block:
location /media/ {
    try_files $uri $uri/ /get.php?$args;

    location ~ ^/media/theme_customization/.*\.xml {
        deny all;
    }

    location ~* \.(ico|jpg|jpeg|png|gif|svg|svgz|webp|avif|avifs|js|css|swf|eot|ttf|otf|woff|woff2)$ {
        add_header Cache-Control "public";
        add_header X-Frame-Options "SAMEORIGIN";
        expires +1y;
        try_files $uri $uri/ /get.php?$args;
    }

    location ~* \.(zip|gz|gzip|bz2|csv|xml)$ {
        add_header Cache-Control "no-store";
        add_header X-Frame-Options "SAMEORIGIN";
        expires    off;
        try_files $uri $uri/ /get.php?$args;
    }

    add_header X-Frame-Options "SAMEORIGIN";
}

location ~* ^/(static|get)\.php$ {
    echo_exec @phpfpm;
}

# If you don't include handlers.conf in public.magento2.conf or staging.magento2.conf, uncomment the following line:
#include handlers.conf;
```

```{tip}
If you don't need static asset generation on your environment, you can also leave out all the if statements in the `/static` block.
```
