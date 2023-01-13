---
myst:
  html_meta:
    description: Shopware 5 applications can greatly benefit from Varnish caching.
      Hypernode supports Varnish as a caching layer and configuration is actually
      quite simple.
    title: How to configure Varnish for Shopware 5? | Hypernode
redirect_from:
  - /en/support/solutions/articles/48001207016-how-to-configure-varnish-for-shopware-5/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001207016-how-to-configure-varnish-for-shopware-5/ -->

# How to Configure Varnish for Shopware 5

Shopware 5 applications can greatly benefit from Varnish caching. On the client side, pages load faster, while on the server side, the load decreases.

The Hypernode platform supports Varnish as a caching layer and configuration is actually quite simple.

## Step One: Enable Varnish on the Hypernode

Varnish can be enabled with a simple command using the [hypernode-systemctl CLI](../../hypernode-platform/tools/how-to-use-the-hypernode-systemctl-cli-tool.md):

`hypernode-systemctl settings varnish_enabled True`

## Step Two: Enable Varnish for NGINX Vhost

The [hypernode-manage-vhosts](../../hypernode-platform/nginx/hypernode-managed-vhosts) (HMV) config allows you to enable varnish for every vhost individually. So if you for example have a domain example.com. You should create 2 vhosts:

- example.com
- [www.example.com](http://www.example.com)

`hypernode-manage-vhosts example.com www.example.com --type shopware5 --varnish`

## Step Three: Follow Shopware's Varnish Configuration Documentation

Please follow Shopware's [documentation about configuring Shopware 5 to work with Varnish](https://developers.shopware.com/sysadmins-guide/varnish-setup/). You can skip the step about configuring Varnish, we'll take you through that :-).

## Step Four: Implement Shopware's Varnish configuration

Copy the VCL configuration from [Shopware's documentation](https://developers.shopware.com/sysadmins-guide/varnish-setup/) and save it on your Hypernode, for example at `/data/web/shopware5.vcl`.

Now we can load in the configuration with the following command:

`varnishadm vcl.load shopware5_debug /data/web/shopware5.vcl`

After that, we can start using the configuration with the following command:

`varnishadm vcl.use shopware5_debug`

## Step Five: Verify the Varnish configuration

Go to your site and open the inspector to check the response headers of your page. You should see the following headers:

```
HTTP/1.1 200 OK
Server: nginx
Date: Thu, 13 Jan 2022 10:45:18 GMT
Content-Type: text/html
Content-Length: 162
Connection: keep-alive
Location: http://appname.hypernode.io/
x-url: /
X-Cacheable: YES
X-Varnish: 35225 67815
Age: 17
Via: 1.1 varnish-v4
Cache-Control: max-age=0, private
X-Cache: HIT
X-Cache-Hits: 1
```

If your page is not in the cache yet, `X-Cache` should contain 'MISS' and `X-Cache-Hits` should contain '0'. Otherwise, `X-Cache` should contain 'HIT' and `X-Cache-Hits` should increment each time you visit the page again.

## Step Six: Removing verification headers from Varnish configuration

While the `X-Cache` and `X-Cache-Hits` headers are very useful, it is a good practice to disable these headers after you don't need them anymore. You can disable these headers by prefixing the configuration lines with the '#' character, which comments the lines out. The lines in question (from /data/web/shopware5.vcl) are:

```
# Set a cache header to allow us to inspect the response headers during testing
if (obj.hits > 0) {
    unset resp.http.set-cookie;
    set resp.http.X-Cache = "HIT";
}  else {
    set resp.http.X-Cache = "MISS";
}

set resp.http.X-Cache-Hits = obj.hits;
```

Make it so that the lines look like the following:

```
# Set a cache header to allow us to inspect the response headers during testing
if (obj.hits > 0) {
    unset resp.http.set-cookie;
    #set resp.http.X-Cache = "HIT";
}  else {
    #set resp.http.X-Cache = "MISS";
}

#set resp.http.X-Cache-Hits = obj.hits;
```

Now, we need to reload the varnish configuration again. This can be done by loading it with a slightly different identifier:

`varnishadm vcl.load shopware5 /data/web/shopware5.vcl`

After that, we can use the new configuration with the following command:

`varnishadm vcl.use shopware5`

And that should be it! Please verify that your pages do not contain the `X-Cache` and `X-Cache-Hits` headers.
