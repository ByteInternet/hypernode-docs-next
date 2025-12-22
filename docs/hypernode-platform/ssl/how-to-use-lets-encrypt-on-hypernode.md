---
myst:
  html_meta:
    description: "Use Let's Encrypt for free SSL certificates. Want to know more about
      how to use let's Encrypt on Hypernode? "
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

**Please note:** The [Hypernode Managed Vhosts (HMV)](../nginx/hypernode-managed-vhosts.md) system requires a vhost for every domain you want to use Let’s Encrypt on.
Then run this command to set up a vhost for the domain:
`hypernode-manage-vhosts www.example.com --https --force-https`
This command redirects everything for the domain from http to https and installs a Let’s Encrypt certificate.

**Note**: If you use Let's Encrypt with HMV, the cron for the renewal of the certificates will be placed automatically in the crontab, you don't have to do anything manually!

### Adding an Third Party Certificate When Let’s Encrypt Is Configured

If you have Let's Encrypt configured for your vhost, but want to add a third party certificate, follow the steps below to safely add the new certificate:

1. Remove the Let's Encrypt certificate by running this command: `hypernode-manage-vhosts example.com --disable-https`
1. Install the third party certificate.
1. Run `hypernode-manage-vhosts example.com --https --ssl-noclobber` to configure HTTPS for your vhost without overwriting the third party certificate.

## Troubleshooting

- By default, `dehydrated` renews Let's Encrypt certificates 30 days before expiring.
- Make sure your cron is running, else `dehydrated` will **not** automagically renew certificates before expiration.
- You can request a maximum of 20 domains per week per IP and a maximum of 5 certificates per domain per week. See: [Let's Encrypt about ratelimits](https://letsencrypt.org/docs/rate-limits/)
- "Error creating new cert :: Too many certificates already issued for: \[...\]" This is not an issue with dehydrated but an API limit with boulder (the Let's Encrypt CA request server). At the time of writing this you can only create 5 certificates per domain in a sliding window of 7 days.
- "Certificate request has 123 names, maximum is 100." This also is an API limit from boulder, you are requesting to sign a multi domain certificate with way too many domains.
- "Dehyrdated: Challenge is invalid!" This could have multiple causes but the main reason is that Let's Encrypt could not contact the server challenge. Could be due to a basic auth or a rewrite of the URI. Check the logs for the exact HTTP status code and act accordingly. Whitelist in the necessary Nginx config file so that Let's Encrypt can passthrough the basic authentication.
- "ERROR: Problem connecting to server (post for  acme-v02.api.letsencrypt.org/acme/new-order; curl returned with 35)" This could be because you're using our cronjob to automatically renew your certificates. All our customers are running the cronjob at the same time (01:00) which could result in too many requests at the same moment. By changing the time of your cronjob you can resolve this issue.
- "My certificates are not in the Nginx config" This can be caused by a change in your Nginx config not picked up by the `nginx-config-reloader`. To manually force a reload, touch some files in `/data/web/nginx`: with the command below or run `hypernode-ssl-config-generator`

```bash
touch /data/web/nginx/http.magerunmaps
```

- Error code: MOZILLA_PKIX_ERROR_REQUIRED_TLS_FEATURE_MISSING" This error appears in Firefox and is caused by an inconsistency in our configuration. We changed this configuration by disabling OCSP stapling. If you keep getting this error, please recreate your Let's Encrypt certificate:

```bash
rm -rf /data/web/certs dehydrated -c
```

- To accept these terms of service run `/usr/bin/dehydrated --register --accept-terms`. When you run `dehydrated` for the first time you will be asked to accept their [terms of service](https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf) by running the following command:

```bash
/usr/bin/dehydrated --register --accept-terms
```
