<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001200525-how-to-configure-varnish-for-shopware-6 -->
# How to Configure Varnish for Shopware 6

Customers with Hypernode Professional and Excellence plans can use Varnish to boost their shop. This article explains how you can configure Varnish for your Hypernode.

Although Varnish is extremely awesome when it get's to speeding up websites, Varnish is a complex technique that needs some experience to set it up. We'd recommend to first test varnish on a [staging environment](https://support.hypernode.com/en/ecommerce/shopware/how-to-use-a-basic-staging-environment-with-shopware-6) or a[development plan](https://support.hypernode.com/en/hypernode/tools/how-to-use-hypernode-development-plans) before implementing varnish on a live node.

## Table of Contents
```{contents}
:depth: 3
:backlinks: none
```

### Step One: Enable Varnish on the Hypernode

You can enable varnish on the hypernode using the [systemctl-tool](https://support.hypernode.com/en/hypernode/tools/how-to-use-the-hypernode-systemctl-cli-tool) by running: 

`hypernode-systemctl settings varnish_enabled True`

### Step Two: How to Setup Varnish for the Vhost

The [hypernode-manage-vhosts](https://support.hypernode.com/en/hypernode/nginx/hypernode-managed-vhosts) (HMV) config allows you to enable varnish for every vhost individually. So if you for example have a domain example.com. You should create 2 vhosts:

* example.com
* [www.example.com](http://www.example.com)

To enable varnish for these vhosts you can run the below command:

`hypernode-manage-vhosts example.com www.example.com --varnish`

**Please note: this should create 2 files in your nginx vhost environment. If this is not the case make sure you've 2 files in you vhost-config (/data/web/nginx/example.com). If not, you should make sure to have 2 files:**

`/data/web/nginx/example.com/public.shopware6.conf`

``` nginx
## Redirecting to varnish
location / {
    set $log\_handler varnish;

    proxy\_pass http://127.0.0.1:6081;
    proxy\_read\_timeout 900s;  # equal to fastcgi\_read\_timeout at handlers.conf:16
    proxy\_set\_header X-Real-IP  $remote\_addr;
    proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for;
    proxy\_set\_header X-Forwarded-Proto $scheme;
    proxy\_set\_header X-Forwarded-Port $server\_port;
    proxy\_set\_header Host $http\_host;
}
```
`/data/web/nginx/example.com/varnish.shopware6.conf`

``` nginx
root /data/web/public;

include /etc/nginx/handlers.conf;

index index.php index.html;

location /recovery/install {
    try\_files $uri /recovery/install/index.php$is\_args$args;
}

location /recovery/update/ {
    location /recovery/update/assets {
    }
    if (!-e $request\_filename){
        rewrite . /recovery/update/index.php last;
    }
}

location / {
    try\_files $uri /index.php$is\_args$args;
}

location ~ \.php$ {
    echo\_exec @phpfpm;
}
```
### Step Three: Configure Shopware to work with Varnish

**This step is only necessary if you're on Shopware >= 6.4.**

Go to [Shopware's Reverse Http Cache documentation](https://developer.shopware.com/docs/guides/hosting/infrastructure/reverse-http-cache) to configure Shopware to take Varnish into account.

### Step Four: Implement a .vcl Into Varnish

To actually use Varnish you need to implement a varnish config file, a .vcl. If you're on Shopware >= 6.4, fetch the [Varnish configuration from their documentation](https://developer.shopware.com/docs/guides/hosting/infrastructure/reverse-http-cache#configure-varnish) (copy the code block starting with *vcl 4.0;*). Otherwise, you can use the `.vcl` from our [Github](https://gist.github.com/hn-support/29efb2e58b18ff2ef0f25363bd02dbe9), or you can create your own.

So, the steps to implement the Varnish configuration into Varnish are:

* Create a file on your node, for example: **data/web/shopware6.vcl**with the Varnish config
* Load the .vcl into Varnish: `varnishadm vcl.load shopware6 /data/web/shopware6.vcl`
* Activate the loaded config**,**"shopware6": `varnishadm vcl.use shopware6`

```
app@j6yt8m-example-magweb-cmbl:~$ varnishadm vcl.load shopware6 /data/web/shopware6.vcl
VCL compiled.

app@j6yt8m-example-magweb-cmbl:~$ varnishadm vcl.list
available  auto/cold          0 boot
available  auto/warm          0 shopware6

app@j6yt8m-example-magweb-cmbl:~$ varnishadm vcl.use shopware6
VCL 'shopware6' now active
```
