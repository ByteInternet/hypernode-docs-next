---
myst:
  html_meta:
    description: An SSL certificate keeps online interactions and transactions private
      and helps to gain confidence of customers. Read here how to use SSL ordered
      via Byte.nl.
redirect_from:
  - /en/hypernode/ssl/how-to-use-ssl-certificates-on-your-hypernode-when-ordered-via-byte-nl/
  - /knowledgebase/use-ssl-certificates-on-your-hypernode/
---

<!-- source: https://support.hypernode.com/en/hypernode/ssl/how-to-use-ssl-certificates-on-your-hypernode-when-ordered-via-byte-nl/ -->

# How to Use SSL Certificates on your Hypernode When Ordered via Hypernode.nl

This article explains how to install SSL certificates on your Hypernode. An SSL certificate keeps online interactions and transactions private and they help customers gain confidence to provide personal information on your website. We strongly recommend shop owners to use SSL certificates. This way, your shop will become securely accessible using HTTPS.

## Why Use SSL?

SSL sends information across the internet encrypted so that only the intended recipient can understand it. SSL establishes a secure connection between your visitor's browser and your webshop. It allows you to sent private and sensitive information, such as payment credentials, across the internet without having to worry about the problems of eavesdropping, data tampering, and message forgery.

## Service Panel users: SSL on Hypernode

**Service Panel** users (Hypernode.nl) have three options to use SSL for their Hypernode plan(s):

- Order an SSL certificate via Hypernode (recommended)
- Upload your own SSL certificate
- Request a certificate using Let’s Encrypt

We recommend purchasing an SSL certificate through Hypernode, because you’ll benefit from our managed hosting services.

When using a third party SSL certificate or [Let’s Encrypt](../ssl/how-to-use-lets-encrypt-on-hypernode.md), you are responsible for implementing, maintaining and renewing the certificate. We cannot provide any support on custom SSL certificates and related issues.

## Buy an SSL Certificate Via Hypernode (Recommended)

We recommend you to purchase an SSL certificate via Hypernode, because then you’ll benefit from our managed hosting services. Not only do we take care of the technical implementation of the certificate for you, we also renew and validate the certificate on time and provide customer support on SSL issues. This way your e-commerce shop will always have a secure connection.

**Note: If you purchase your SSL certificate via Hypernode for you will need an additional Presence or Presence Plus plan for the domain name you want to order the SSL for (except of course when you already have a Presence plan for that domain).**

In case you do not already have a Presence plan for this domain, start with ordering one. If you do have a Presence plan, please skip the steps below and go straight to ‘Order an SSL certificate’.

### Order a Presence Plan

You need to order a Presence plan to connect the SSL certificate to your Hypernode. A Presence plan acts as a v-host to make a domain known in our systems, otherwise you cannot order an SSL certificate. So, **first** order a Presence plan for domain.com and **then** order an SSL certificate as an add-on to this Presence plan. The steps:

- [Log in](http://auth.byte.nl/) to the Service Panel
- Click the ‘Bestel Direct’ button on the right
- Choose your domain name under ‘Kies een domeinnaam’ and click on ‘controleer beschikbaarheid’. If you want to keep the domain registered elsewhere you can choose the option ‘hosting only verhuizen’
- Select ‘Domeinregistratie’
- Select ‘Presence or ‘Presence Plus’
- Click on the ‘Controleren & Afronden’ button to check your order details
- If all is OK, click on the “Bevestig & Betaal’ button to finalise your order

### Order an SSL Certificate

The following steps will help you to purchase an SSL certificate for your domain:

- [Log in](http://auth.byte.nl/) to the Service Panel
- Select the domain for which you need an SSL certificate
- In the ‘Administration’ tab you click on ‘SSL-certificaat’
- Select the type of SSL certificate you want to order (Single, Wildcard or EV)
- Select a validation e-mail address
- Agree with the terms and conditions
- Click ‘Bestel’

We will email you once your certificate is received and installed.

### Install the SSL Certificate on your Hypernode

When the certificate is ready, you can easily add it to your Hypernode by visiting the ‘SSL & DNS instellingen’ overview mentioned here above. The domain for which you ordered a SSL certificate will now have a status ‘Beschikbaar’ in de ‘SSL Certificaat’ column. Simply choose ‘Installeren’ to add it to your Hypernode.

**Keep in mind:**

- You can only link SSL certificates from plans that have the same Contractant role as your Hypernode plan. Make sure these roles match!
- You cannot link Let’s Encrypt certificates via your Service Panel as these certificates are managed locally on the node itself.

## Add a Custom SSL Certificate

Using a SSL certificate from a third party is a possibility too, although we don’t recommend it. When using a third party SSL certificate, you are responsible for implementing, maintaining and renewing the certificate.

If you wish to upload your own custom SSL certificate, you will need a few .PEM files:

- The unencrypted private key
- The certificate
- The CA certificate Chain file (Intermediate certificates)

To upload your custom SSL, follow the steps below:

- [Log in](http://auth.byte.nl/) to the Byte Service Panel
- Select your Hypernode plan
- Click on the ‘Instellingen’ tab
- Click ‘SSL & DNS instellingen’
- Click ‘Beheer SSL Certificaten’
- Click ‘Koppel handmatig een certificaat’
- Fill in the Private Key, Certificate and Certificate Authority (only .PEM files)
- Click ‘Volgende’
- Check whether you uploaded the correct certificate
- Click ‘Add certificate’

## Use Let’s Encrypt

For the more technical equipped developers we provide [Let’s Encrypt](../ssl/how-to-use-lets-encrypt-on-hypernode.md).

Let’s Encrypt is a way to order free SSL certificates through domain validation. This has a few limitations:

- You are responsible for your own Let’s Encrypt certificates, we do not provide support for Let’s Encrypt.
- Let’s Encrypt does not provide wildcard and/or EV certificates
- Let’s Encrypt SSL Certificates are only valid for a 3 months period.

See [our documentation about configuring Let’s Encrypt on your Hypernode](../ssl/how-to-use-lets-encrypt-on-hypernode.md) on how to setup Let’s Encrypt on your Hypernode.

## How Do I remove a Custom SSL certificate From My Hypernode?

Removing an SSL certificate from your Hypernode is easily done via your Service Panel following the steps below:

- [Log in](http://auth.byte.nl/) to the Service Panel
- Select your Hypernode plan
- Navigate to the ‘Instellingen’ tab and click ‘SSL & DNS instellingen’
- Click ‘Beheer SSL Certificaten’
- Click the waste bin button on the right of the certificate you wish to remove
- Click ‘Delete SSL certificate’

Your SSL certificate is now removed from your Hypernode. If you wish to add it again, simply go back to the overview page and click ‘Koppel handmatig een certificaat’.

To remove Let’s Encrypt certificates you need to log in to your hypernode and[delete the created certificates](../ssl/how-to-use-lets-encrypt-on-hypernode.md#stop-using-dehydrated--cleanup) over SSH.

## Changing Your Base URLs

If your SSL certificates are linked to your Hypernode, or you ordered Let’s Encrypt certificates, we can change the base URLs to use only HTTPS. To do this, we created a little Python script that changes all your base URLs to HTTPS.

To use this:

```nginx
## Download the script

wget -O change_baseurls.py https://gist.githubusercontent.com/hn-support/0c76ebb5615a5be789997db2ae40bcdd/raw/

## Execute to change the base URLs to HTTPS

python change_baseurls.py
```

## Forcing Your Entire shop to Use SSL

You can easily force your entire shop to go over HTTPS using a simple redirect.

### Redirecting all traffic (when Varnish is not used)

To redirect all traffic from HTTP to HTTPS, open the `server.rewrites` with your editor:

```nginx
editor /data/web/nginx/server.rewrites
```

Then add the following snippet:

```nginx
if ($scheme = http) { return 301 https://$host$request_uri; }
```

Now finish saving the option using `CTRL+o` followed by `CTRL+x`.

To check if all went well, check if `/data/web/nginx/nginx_error_output` is present containing an error message. If you can’t find this file, your config reload went well.

Now test your result by visiting the domain!

It is also possible to [selectively redirect to HTTP or HTTPS](../nginx/how-to-redirect-from-or-to-www.md) depending on the domain, by using a mapping.

Redirecting all traffic to https and www

If you want to redirect your domain to both https and www, add this snippet to `server.rewrites`

```nginx
if ($http_host ~* "^(?!www\.).*$") {

    return 301 https://www.$http_host$request_uri;

}

if ($scheme = http) {

    return 301 https://$host$request_uri;

}
```

### Redirecting to HTTPS When Using Varnish

If you are using Varnish on your Hypernode, the given redirect will be cached by Varnish causing the site to go down with a 'too many redirects' error, as the redirect will be served from the cache on both HTTP and HTTPS.

To resolve this, make use of a `public.rewrites` instead of a `server.rewrites`.

All files in /data/web/nginx starting with public.\* will be included in front of the Varnish instance, and will therefore not be cached.

## Things to Remember When Using an SSL Certificate

- Don’t forget to point the DNS for your domain to your Hypernode. More information about how this is done [can be found in the article DNS settings Hypernode](../dns/how-to-manage-your-dns-settings-for-hypernode.md).
- You will need a storefront in Magento with a secure_base_url. Otherwise Magento will redirect you to the main store. You can change the base urls using the script mentioned above, you can also do this using the following support documentation.

## SSL on Your (non-www) Naked Domain While Using the Www-izer

If you use the www-izer forwarders in the DNS settings for your domain name, people that visit <https://yourdomain.com> directly will get an error message, either indicating that there is no https available or a plain connection refused error.
If Hypernode manages your DNS, or you’ve configured your DNS to point directly to the Hypernode, this will not be a problem.

For more information please read the article [DNS Settings Hypernode](../dns/how-to-manage-your-dns-settings-for-hypernode.md)

## Enable SSL Stapling

To enable SSL Stapling for your SSL certificate, create the following configuration in /data/web/nginx/http.ocsp:

```nginx
ssl_stapling on;

ssl_stapling_verify on;
```

## Check Settings of Third Party Solutions

After configuring your shop to only use HTTPS, please do not forget to check HTTP(S) settings of third party solutions to avoid problems, e.g.:

- Payment providers like Adyen
- Stock providers like Picqer
- Google Analytics and Google Search Console

## How to Generate Certificate Signing Request on Nginx using OpenSSL

Log into your Hypernode with SSH and run the following command:

```nginx
openssl req -new -newkey rsa:2048 -nodes -keyout myserver.key -out myserver.csr
```

**Note:** Replace yourdomain with the domain name you're securing. For example, if your domain name is mydomain.com, you would type mydomain.key and mydomain.csr where server is the name of your server.

This will begin the process of generating two files: the Private-Key file for the decryption of your SSL Certificate, and a certificate signing request (CSR) file used to apply for your SSL Certificate.

Enter the requested information:

\*\*- Common Name (CN):\*\*The fully-qualified domain name, or URL, you want to secure.

If you are requesting a Wildcard certificate, add an asterisk (\*) to the left of the common name where you want the wildcard, for example \*.mydomain.com.

**- Organization (O):** The legally-registered name for your business. If you are enrolling as an individual, enter the certificate requestor's name.

**- Organization Unit (OU):** If applicable, enter the DBA (Doing Business As) name.

**- City or Locality (L):** Name of the city where your organization is registered/located. Do not abbreviate.

\*\*- State or Province (S):\*\*Name of the state or province where your organization is located. Do not abbreviate.

\*\*- Country (C):\*\*The two-letter International Organization for Standardisation (ISO) format country code for where your organisation is legally registered.

**Note:** If you do not want to enter a password for this SSL, you can leave the Passphrase field blank.

Your `.csr` file will then be created.

Open the CSR file with a text editor and copy and paste it (including the BEGIN and END tags) into the Certificate order form.

Save (backup) the generated .key file as it will be required later when installing your SSL certificate in Nginx.
