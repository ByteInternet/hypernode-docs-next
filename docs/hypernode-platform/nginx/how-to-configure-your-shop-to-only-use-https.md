---
myst:
  html_meta:
    description: 'We recommend serving your site only over HTTPS traffic. This is
      safer and is better for search index optimization. Configure your shop with
      these steps. '
    title: How to configure your shop to only use https? | Hypernode
redirect_from:
  - /en/hypernode/nginx/how-to-configure-your-shop-to-only-use-https/
  - /knowledgebase/configuring-shop-use-https/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-configure-your-shop-to-only-use-https/ -->

# How To Configure Your Shop to Only Use HTTPS

On Hypernode we recommend serving your site only over HTTPS traffic. This is safer and is better for search index optimization.

Most of the available browsers only support HTTP/2 when your pages are served over SSL so to use this faster and newer HTTP technology, order an SSL certificate and make sure your site is only served over HTTPS.

You can find more in-depth information in [this article about SSL on Hypernode](../ssl/how-to-use-ssl-certificates-on-your-hypernode-when-ordered-via-hypernode-com.md).

## How to Use SSL Certificates via Hypernode.com

Please check out [this article](../ssl/how-to-use-ssl-certificates-on-your-hypernode-when-ordered-via-hypernode-com.md) for the different SSL options when you use the Hypernode Control Panel.

## How to Use SSL Certificates via Hypernode.nl

Please check out [this article](../ssl/how-to-use-ssl-certificates-on-your-hypernode-when-ordered-via-hypernode-nl.md) for the different SSL options when you use the Byte Service Panel.

## Order Let’s Encrypt Certificates

### On Hypernodes With Hypernode Managed Vhosts Enabled

**Please note: If you want to use Let’s Encrypt and have the Hypernode Managed Vhosts (HMV) system enabled, you need to configure LE during the creation of the vhost. Using the old method with dehydrated won't work!**

First, check if HMV is enabled on your Hypernode:

`hypernode-systemctl settings managed_vhosts_enabled`

If so, it will give the following output:

`managed_vhosts_enabled is set to value True`

If you want to request a LE certificate you need to add the `--https` flag with the HMV-command.

`hypernode-manage-vhosts www.example.com --https --force-https`

This command will not only request a LE Certificate but because of the --force-https flag it will also redirects all traffic for that specific vhost to HTTPS.

### On Hypernodes Without Hypernode Managed Vhosts Enabled

To order [Let’s Encrypt](../ssl/how-to-use-lets-encrypt-on-hypernode.md) certificates for all storefronts, use the following command:

```bash
## Create an entry for each storefront
for DOMAIN in $( n98-magerun sys:store:config:base-url:list --format=csv | sed 1d | cut -d , -f 3 | perl -pe "s/https?://(www.)?//" | tr -d "/" | sort -u ); do
    echo -e "$DOMAIN www.${DOMAIN}" >> ~/.dehydrated/domains.txt
done

## Order the certificates
dehydrated -c --create-dirs
```

Don’t forget to [add the cron to renew your certificates](../ssl/how-to-use-lets-encrypt-on-hypernode.md) to the crontab if you are using Let’s Encrypt!

## Changing Your Base URLs

If your SSL certificates are linked to your Hypernode, or you ordered Let’s Encrypt certificates, we can change the base URLs to use only HTTPS. To make this easier, we created a little Python script that changes all your base URLs to HTTPS:

```nginx
## Download the script wget -O change_baseurls.py https://gist.githubusercontent.com/hn-support/0c76ebb5615a5be789997db2ae40bcdd/raw/ ## Execute to change the base URLs to HTTPSpython change_baseurls.py
```

## Routing All Traffic Over SSL Using Nginx

If you configure your Magento shop to only use HTTPS, all HTTP traffic will be redirected to HTTPS.

If this is done by Magento, the database and PHP are used for making this redirect, which is expensive in resources.

This is why we must configure this in Nginx, so the redirect does not use unnecessary resources.

Run the following command to add the configuration to Nginx that routes all traffic over HTTPS:

```nginx
echo 'if ($scheme = http) { return 301 https://$host$request_uri; }' >> /data/web/nginx/public.ssl_redirect
```

**Please note that if you have [Hypernode Managed Vhosts](hypernode-managed-vhosts.md) enabled, you can skip this.**

## Check Settings of Third Party Solutions

After configuring your shop to only use HTTPS, please do not forget to check HTTP(S) settings of third party solutions to avoid problems, e.g.:

- Payment providers like Adyen.
- Stock providers like Picqer.
- Google Analytics and Google Search Console.
