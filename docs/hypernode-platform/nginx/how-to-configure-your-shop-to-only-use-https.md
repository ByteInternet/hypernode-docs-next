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

## How to Use Let’s Encrypt (LE) Certificates

If you want to request a LE certificate you need to add the `--https` flag with the HMV-command.

`hypernode-manage-vhosts www.example.com --https --force-https`

This command will not only request a LE Certificate but, because of the --force-https flag, it will also redirect all traffic for that specific vhost to HTTPS.

## Changing Your Base URLs

If your SSL certificates are linked to your Hypernode, or you ordered Let’s Encrypt certificates, we can change the base URLs to use only HTTPS. To make this easier, we created a little Python script that changes all your base URLs to HTTPS:

```bash
# Download the script
wget -O change_baseurls.py https://gist.githubusercontent.com/hn-support/0c76ebb5615a5be789997db2ae40bcdd/raw/
## Execute to change the base URLs to HTTPS
python change_baseurls.py
```

## Routing All Traffic Over SSL Using Nginx

If you configure your Magento shop to only use HTTPS, all HTTP traffic will be redirected to HTTPS.

If this is done by Magento, the database and PHP are used for making this redirect, which is expensive in resources.

This is why we must configure this in Nginx, so the redirect does not use unnecessary resources.

Run the following command to configure a vhost to automatically redirect all traffic to HTTPS:

`hypernode-manage-vhosts www.example.com --https --force-https`

## Check Settings of Third Party Solutions

After configuring your shop to only use HTTPS, please do not forget to check HTTP(S) settings of third party solutions to avoid problems, e.g.:

- Payment providers like Adyen.
- Stock providers like Picqer.
- Google Analytics and Google Search Console.
