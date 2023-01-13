---
myst:
  html_meta:
    description: "Use Let's Encrypt for free SSL certificates. Want to know more about\
      \ how to use let's Encrypt on Hypernode? "
    title: How to use Let’s Encrypt on Hypernode?
redirect_from:
  - /en/hypernode/ssl/how-to-use-let-s-encrypt-on-hypernode/
  - /knowledgebase/use-lets-encrypt-hypernode/
---

<!-- source: https://support.hypernode.com/en/hypernode/ssl/how-to-use-let-s-encrypt-on-hypernode/ -->

# How to use Let’s Encrypt on Hypernode

## Introduction

Let's Encrypt is a CA Authority that provides free SSL certificates through domain validation and automated retrieval. It is started as a joint effort by big companies in the IT world to provide free and transparent SSL certification and validation through automation.

The key principles behind Let’s Encrypt are, (taken from their website):

- **Free**: Anyone who owns a domain name can use Let’s Encrypt to obtain a trusted certificate at zero cost.
- **Automatic**: Software running on a web server can interact with Let’s Encrypt to painlessly obtain a certificate, securely configure it for use, and automatically take care of renewal.
- **Secure**: Let’s Encrypt will serve as a platform for advancing TLS security best practices, both on the CA side and by helping site operators properly secure their servers.
- **Transparent**: All certificates issued or revoked will be publicly recorded and available for anyone to inspect.
- **Open**: The automatic issuance and renewal protocol will be published as an open standard that others can adopt.
- **Cooperative**: Much like the underlying Internet protocols themselves, Let’s Encrypt is a joint effort to benefit the community, beyond the control of any one organization.

See their website for more information about how to use [Let's Encrypt](https://letsencrypt.org/).

## Let’s Encrypt and Hypernode Managed Vhosts

**Please note:** If you want to use Let’s Encrypt and have the [Hypernode Managed Vhosts (HMV)](../nginx/hypernode-managed-vhosts.md) system enabled, you need to create a vhost for every domain you want to use Let’s Encrypt on or else it won’t work.

First, check if HMV is enabled on your Hypernode:
`hypernode-systemctl settings managed_vhosts_enabled`
If so, it will give the following output:
`managed_vhosts_enabled is set to value True`
Then run this command to set up a vhost for the domain:
`hypernode-manage-vhosts www.example.com --https --force-https`
This command redirects everything for the domain from http to https and installs a Let’s Encrypt certificate.

**Note**: If you use Let's Encrypt with HMV, the cron for the renewal of the certificates will be placed automatically in the crontab, you don't have to do anything manually!

### Adding an Third Party Certificate When Let’s Encrypt Is Configured

If you have Let's Encrypt configured for your vhost, but want to add a third party certificate, follow the steps below to safely add the new certificate:

1. Remove the Let's Encrypt certificate by running this command: `hypernode-manage-vhosts example.com --disable-https`
1. Install the third party certificate.
1. Run `hypernode-manage-vhosts example.com --https --ssl-noclobber` to configure HTTPS for your vhost without overwriting the third party certificate.

**If Hypernode Managed Vhosts IS NOT ENABLED, you can use the steps below to configure Let’s Encrypt.**

## Configuration

To make use of Let's Encrypt on Hypernodes, we installed the [dehydrated](https://github.com/lukas2511/dehydrated) Let's Encrypt client.
This command-line utility orders and renews a certificate through the LE API and stores the retrieved certificates on disk so we can use them in the Nginx configuration.

### Configure dehydrated

To configure `dehydrated` to manage SSL certificates for a domain, add the domain to the list of domains in `/data/web/.dehydrated/domains.txt`:

For example:

```nginx
your_hypernode_app_name.hypernode.io
test.domainA.com
staging.domainB.com
```

Then run `dehydrated` to request a certificate:

```nginx
dehydrated -c --create-dirs
```

This will create a directory tree in `/data/web/certs` with the configured certificates

*Make sure you add an entry for each domain record you need ssl for. This means that you should add both the `www.example.com` **AND** `example.com` on it's own line to the `domains.txt` file.*

### Add Existing Let's Encrypt Certificates to Be Renewed by Dehydrated

If you want to use a different Let’s Encrypt client you can do so as well, just place your cert.pem, chain.pem and fullchain.pem files in the `/data/web/certs` directory in a subdirectory with as name the domain name the certificate is for.

The directory tree will look like this if you have example.com and example.net:

```nginx
find /data/web/certs

example.com/
example.com/fullchain.pem
example.com/cert.pem
example.com/privkey.pem

example.net/
example.net/fullchain.pem
example.net/cert.pem
example.net/privkey.pem
```

When a certificate is renewed, the old certificate will be renamed to cert-`unique id` for recovery usage.

## Manually Renew Your Certificates

To force renewal on your certificates, even when the certificate is longer valid than 30 days, use the `--force` flags:

```nginx
dehydrated -c --force
```

**Be careful not to exceed the ratelimits at Let's Encrypt!**

### Multiple Domains for One Shop

Both `dehydrated` and out config generator now support multidomain certificates. This implicated that if you want to serve both your `www.` and `apex` domain over SSL, you may add both records on the same line in `.dehydrated/domains.txt` to ensure a valid nginx configuration is created for both domains.

Example:

```nginx
cat ~/.dehydrated/domains.txt

example.hypernode.io

example.com www.example.com test.example.com

example.nl www.example.nl
```

### Configure the Hypernode and Magento to Support Let's Encrypt

After creating certificates you need to update the Nginx configuration. This is done using the script `hypernode-ssl-config-generator`.
When you run this script, an SSL enabled Nginx configuration for your shop is generated in `/data/web/nginx/ssl`

After creating an Nginx configuration, you should adjust your Magento base URLs to support SSL:

- For Magento 1:

```nginx
magerun sys:store:config:base-url:set # set your baseurl to secure (https)
magerun cache:clean
```

- For Magento 2, check your base-urls with `magerun2 sys:store:config:base-url:list`. Then change the base-url with:

```nginx
cd ~/magento2
magerun2 config:store:set web/secure/base_url https://my.hypernode.io
magerun2 cache:clean
```

Read more [here](../dns/how-to-manage-your-dns-settings-for-hypernode.md).

Or, additionally you can make use of the scripts we created to change your baseurl provided for [Magento 1](https://gist.github.com/hn-support/0c76ebb5615a5be789997db2ae40bcdd) or for [Magento 2](https://gist.github.com/hn-support/083aabc8f9125b29098454cee1f25c89).

### Setup a Cron to Automatically Renew Certificates

To periodically check and renew certificates, create a cronjob running dehydrated:

```nginx
PATH="/data/web/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
MAILTO="your@email.com"
0 1 * * * flock -n /data/web/.dehydrated.lock chronic dehydrated --no-lock --cron --create-dirs
```

This will check nightly at 1:00 if there are configured certificates that should be renewed. We use the `--no-lock` option so that flock manages the lock file accordingly and we don't use the outdated lock file mechanism of dehydrated.

## Stop using dehydrated / Cleanup

If you want to switch to an SSL certificate managed by Hypernode (for example you switch to an SSL EV certificate), you can easily remove the configuration and certificated for Let's Encrypt:

- Remove the `ssl/` directory in `/data/web/nginx`
- Remove the `certs/` directory in `/data/web/`
- Remove all domains from the `/data/web/.dehydrated/domains.txt`
- Remove the cronjob from your crontab
- Renew the Nginx configuration by running `hypernode-ssl-config-generator`

If you decide to not use any SSL certificate anymore and switch back to http (not recommended), don't forget to change your Magento base-url settings back to http, please see these docs for [Magento 1](../../ecommerce-applications/magento-1/how-to-change-the-base-url-in-magento-1-x.md) and [Magento 2](../../ecommerce-applications/magento-2/how-to-change-your-magento-2-base-urls.md).

## Troubleshooting

- By default, `dehydrated` renews Let's Encrypt certificates 30 days before expiring.
- Make sure your cron is running, else `dehydrated` will **not** automagically renew certificates before expiration.
- You can request a maximum of 20 domains per week per IP and a maximum of 5 certificates per domain per week. See: [Let's Encrypt about ratelimits](https://letsencrypt.org/docs/rate-limits/)
- "Error creating new cert :: Too many certificates already issued for: \[...\]" This is not an issue with dehydrated but an API limit with boulder (the Let's Encrypt CA request server). At the time of writing this you can only create 5 certificates per domain in a sliding window of 7 days.
- "Certificate request has 123 names, maximum is 100." This also is an API limit from boulder, you are requesting to sign a multi domain certificate with way too many domains.
- "Dehyrdated: Challenge is invalid!" This could have multiple causes but the main reason is that Let's Encrypt could not contact the server challenge. Could be due to a basic auth or a rewrite of the URI. Check the logs for the exact HTTP status code and act accordingly. Whitelist in the necessary Nginx config file so that Let's Encrypt can passthrough the basic authentication.
- "ERROR: Problem connecting to server (post for  acme-v02.api.letsencrypt.org/acme/new-order; curl returned with 35)" This could be because you're using our cronjob to automatically renew your certificates. All our customers are running the cronjob at the same time (01:00) which could result in too many requests at the same moment. By changing the time of your cronjob you can resolve this issue.
- "My certificates are not in the Nginx config" This can be caused by a change in your Nginx config not picked up by the `nginx-config-reloader`. To manually force a reload, touch some files in `/data/web/nginx`: with the command below or run `hypernode-ssl-config-generator`

```nginx
touch /data/web/nginx/http.magerunmaps
```

- Error code: MOZILLA_PKIX_ERROR_REQUIRED_TLS_FEATURE_MISSING" This error appears in Firefox and is caused by an inconsistency in our configuration. We changed this configuration by disabling OCSP stapling. If you keep getting this error, please recreate your Let's Encrypt certificate:

```nginx
rm -rf /data/web/certs dehydrated -c
```

- To accept these terms of service run `/usr/bin/dehydrated --register --accept-terms`. When you run `dehydrated` for the first time you will be asked to accept their [terms of service](https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf) by running the following command:

```nginx
/usr/bin/dehydrated --register --accept-terms
```
