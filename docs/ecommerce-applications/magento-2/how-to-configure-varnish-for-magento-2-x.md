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

## Enable Varnish 4.0 or 6.0 for Magento 2.x

As Magento 2 supports Varnish out of the box, there is no need for the turpentine extension anymore in Magento 2. Simply follow the steps below to configure Varnish 4.0 or 6.0 for Magento 2.

**First configure the Varnish version (4.0 or 6.0) via the [hypernode-systemctl tool](../../hypernode-platform/tools/how-to-use-the-hypernode-systemctl-cli-tool.md)**

```console
$ hypernode-systemctl settings varnish_version 4.0
```

**Or if you want to switch to Varnish 6.0**

```console
$ hypernode-systemctl settings varnish_version 6.0
```

**Enable Varnish via the [hypernode-systemctl tool](../../hypernode-platform/tools/how-to-use-the-hypernode-systemctl-cli-tool.md)**

```console
$ hypernode-systemctl settings varnish_enabled true
```

**Enable Varnish via the [Service Panel](https://service.byte.nl/)**

- Log in on the Service Panel
- Go to the tab "Instellingen"
- Click on "Varnish"
- Use the switch to enable Varnish

**Enable Varnish via the [Control Panel](https://auth.hypernode.com/)**

- Click on "Hypernodes"
- Click on "Caching"
- Select the Hypernode
- Click on "Enable Varnish"

## Configure Varnish on the Vhost

Since the introduction of \*\*[hypernode-manage-vhosts](https://changelog.hypernode.com/changelog/release-7166-hypernode-manage-vhosts-enabled-by-default/)\*\*Hypernode may work somewhat different than you might be used to. With HMV enabled, it requires one more step to configure Varnish for your shop/vhost. Remember, for each domain, there should be a vhost created. You can list an overview of all configured vhosts with `hypernode-manage-vhosts --list`. While you do that, note that there is a column, "varnish". By default this is set to "False". Which means that Varnish isn't configured for this vhost. You can configure Varnish for the vhost by running the following command:

```console
$ hypernode-manage-vhosts EXAMPLE.COM --varnish
```

## Configure Magento 2.x for Varnish

- Log in to the Magento Admin/Backend as an administrator.
- Navigate to **Stores > Configuration > Advanced > System > Full Page Cache**
- From the **Caching Application** list, click `Varnish Caching`
- Enter a TTL value
- Expand Varnish Configuration and insert the correct information:
  - `Backend Host`: 127.0.0.1
  - `Backend Port`: 8080
- Save your VCL by clicking the button **`Save config`** in the top right
- Click *Export VCL for Varnish 4 or *Export VCL for Varnish 6**

### Configure Your Backend Servers Through the Commandline

If you want to flush the Varnish cache from the Magento backend, you need to add the Varnish server in your Magento config to `http-cache-hosts`.

To do this, run the following command:

```console
$ cd /data/web/magento2;
$ bin/magento setup:config:set --http-cache-hosts=127.0.0.1:6081;
```

Now when you flush your caches in cache management, your varnish full_page cache will be flushed too.

### Test and Upload Your VCL

After downloading your VCL, check (in notepad or something similar) if the following configuration is present:

```vcl
backend default {
  .host = "127.0.0.1";
  .port = "8080";
}
```

If your VCL checks out, upload it to your Hypernode (using SCP, FTP or FTPS or whichever client you prefer)

#### Remove Health Check Probe from Configuration

**Note:** The default VCL might have the following configuration:

```vcl
backend default {
     .host = "localhost";
     .port = "8080";
     .first_byte_timeout = 600s;
     .probe = {
         .url = "/pub/health_check.php";
         .timeout = 2s;
         .interval = 5s;
         .window = 10;
         .threshold = 5;
    }
}
```

Make sure you change this to the aforementioned configuration (without the health_check probe), since this will break on our Nginx configuration and will therefore result in a `503 Guru Meditation` error.

## Import Your VCL into the Varnish Daemon

Import your VCL into Varnish and save as `mag2`:

```console
$ varnishadm vcl.load mag2 /data/web/default.vcl

```

The output should say: *your VCL is compiled*. If you receive a `Permission denied` error, and have recently activated Varnish, please close all ssh sessions, and log back in to reload your new permissions.

Now tell Varnish to activate the loaded VCL:

```console
$ varnishadm vcl.use mag2

```

In the examples we used the name ‘mag2’ for our VCL, but you can use any name you prefer.

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

## VCL Tip

In our experience the by default generated .vcl from your Magento backend often doesn't work very well. You can check this for example by running `varnishhist`, this will show you a graph with the HITS, (`|`) and MISSES (`#`). So if you're seeing a lot of MISSES (`#`) you could use **[this .vcl](https://gist.github.com/hn-support/f4d29af73d76d0f7879a2fa9d10d8411)**. We found out that this .vcl is often performing quite well.

\*\***please note that this is just another standard .vcl, if this doesn't work either or you have specific requirements you should contact a Varnish implementation specialist.**

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
