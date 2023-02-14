---
myst:
  html_meta:
    description: 'At Hypernode you can request various SSL certificates via the Service
      Panel. Learn more about how to validate your certificate and other questions
      about SSL. '
    title: How to validate your SSL certificate? | SSL FAQ | Hypernode
redirect_from:
  - /en/hypernode/ssl/how-to-validate-your-ssl-certificate-and-more-frequently-asked-questions-about-ssl/
---

<!-- source: https://support.hypernode.com/en/hypernode/ssl/how-to-validate-your-ssl-certificate-and-more-frequently-asked-questions-about-ssl/ -->

# How to Validate Your SSL Certificate and More Frequently Asked Questions About SSL

**Please note that this only applies to Service Panel users who log in via service.byte.nl.**

## What Kind of Certificates Can I Order via Hypernode?

At Hypernode you can request various SSL certificates via the [Service Panel](https://auth.byte.nl/login/). There are three types of certificates:

- SSL single certificate; you can use this on a single domain for the naked domain and the www domain (example.com and [www.example.com](http://www.example.com)).
- SSL wildcard certificate; You can use this to secure all subdomains (\* .example.nl) for your domain name, but also on [www.example.nl](http://www.example.nl) and the naked domain (ie example.nl). However, this certificate does not work on \*. \*. example.nl.
- EV-SSL certificate; you can only use this on the main domain (example.nl). EV stands for Extended Validation and gives you the reliable green bar, known from many bank websites. In terms of technology, an EV-SSL certificate does not differ from the "normal" SSL certificates, but the difference is in the identity investigation. With an EV-SSL certificate, extensive research is done into the identity of the applicant. In that sense, an EV-SSL certificate is "worth" more or more reliable. The contract period for all SSL certificates is one year.

Please take into account that it can take a few days to apply for an SSL certificate. This mainly applies to EV SSL certificates for which the applicant needs to show that they have control over the domain for which the certificate was requested, the company data als needs to be verified. To do so, our supplier (Sectigo) looks at a public registry, such as that of the Chamber of Commerce, and they contact the organisation by phone. EV certificates also require documents to be signed and submitted to our supplier.

## Pricing

The costs for an SSL certificate consist of two aspects: the costs for the actual certificate and the service costs for the certificate.

|          |                       |                   |           |
| -------- | --------------------- | ----------------- | --------- |
| **Type** | **Certificate costs** | **Service costs** | **Total** |
| Single   | € 8,00                | € 30,00           | € 38,00   |
| Wildcard | € 75,00               | € 80,00           | € 155,00  |
| EV       | € 95,00               | € 80,00           | € 175,00  |

The certificate costs you pay for an SSL certificate that you order via Hypernode, is the purchase prise we pay at our supplier. We arrange the entire SSL application for you. You do not have to do anything more than to order the certificate in your Service Panel. Only with EV-SSL you still have to take care of a number of things (as explained [here](#what-kind-of-certificates-can-i-order-via-hypernode)).

In the background, the certificate is requested with the correct data, the validation is done (place file, perform validation), the certificate is retrieved and safely stored in the right place. We ensure that your SSL certificate works properly, even if you change your plan. All you have to take care of is to install the SSL on the right Hypernode (which can be done with [one click](../ssl/how-to-use-ssl-certificates-on-your-hypernode-when-ordered-via-hypernode-nl.md#install-the-ssl-certificate-on-your-hypernode)).

### Your SSL Certificate Is Automatically Renewed

Every year Hypernode renews your SSL certificate well in advance, so that the continuity of your site will not be interrupted. And we ensure that possible safety issues are resolved at lightning speed. For example, POODLE and Heartbleed, these issues were patched at Hypernode within 24 hours (!). Handling SSL will therefore no longer take you any time at all.

## Validation Process

A number of checks are performed with every request for an SSL certificate. The purpose of these checks is to ensure that only the real owner of a domain name can request an SSL certificate. Single and Wildcard certificates only check whether you have control over the domain name. With an EV (Extended Validation) SSL certificate, there is also a check whether the certificate data is valid. These steps are determined by the Certificate Authority & Browser forum, the central organisation in the field of (EV) certificates and therefore cannot be skipped or modified. The steps below are performed for the extended validation. The domain validation step is performed last for an EV certificate and is the only step necessary for Single (domain) and Wildcard SSL certificates.

### Business Validation

The company data stored in the certificate is checked with an independent source, such as the Chamber of Commerce, the Belgian Crossroads Bank for Enterprises, or Dun & Bradstreet for international companies. The company name as known at Hypernode must exactly match the data at the trade register. Only the statutory name can be used here.

If the company validation step fails, for example because the company name at Hypernode does not match, or because the address is incorrect, you can change your data at Hypernode. Then contact our support department and we will update the order with the new information.

### Domain Validation

For a domain validated certificate, the certificate issuer only performs domain validation. When the domain name runs on the Byte name servers, we can do the validation for you. If not, the default method of doing this will be email validation. You will receive an email for this on a standard email address; admin, administrator, hostmaster, postmaster, or webmaster@example.nl. In some cases the address from the whois data is also possible. Unfortunately, other email addresses cannot be used for this, because only these emails are accepted by the CA/B forum. If it is not possible to use one of these email addresses, you can also choose CNAME validation. To do this, a CNAME record must be added to the domain name's DNS that can be verified by the certificate issuer. To request this option, you can send an email to support@hypernode.com, you will then receive the record that needs to be added to the DNS.

### Whois Validation

The Whois register records who owns a domain name. Nowadays it is no longer required that the whois data matches the data of the applicant. An extra check is done for high risk domain names and obvious phishing domains will be immediately rejected.

### EV Documents

When applying for EVs, it is necessary to sign the EV Documents. These documents consist of a Certificate Request Form & Certificate Subscriber Agreement (contract). You will receive a link by email to sign the Sectigo Subscriber Agreement online.

If the EV Documents are not signed, the certificate cannot be delivered. If you do not receive these documents, you can have resend them via the Service Panel.

### Phone Validation

The contact person of the organisation as specified in the request is called. A publicly registered telephone number of the organisation is used for this, for example from the Chamber of Commerce or Google places. This checks whether the organisation concerned has actually applied for the SSL certificate.

If the telephone validation fails, you can contact our support department. We can then schedule a new appointment for the call.

## Can I Request an SSL Certificate on My Hypernode Name?

Please note that you cannot request an SSL certificate for your app name (e.g. example.hypernode.io). You can create a [Let's Encrypt certificate](../ssl/how-to-use-lets-encrypt-on-hypernode.md) for this. If you want SSL for your domain, you need a Presence or Presence Plus plan for each domain for which you want to request an SSL certificate. This is necessary because the domain must be known in our administration before we can order an SSL certificate.

So first make sure that you have ordered a Presence plan, even if your domain is registered externally. Then you order the SSL certificate as an add-on to this Presence plan. Make sure that you have the Contractant role for both plans.

## How Do I Order an SSL Certificate?

You can request an SSL certificate via our Service Panel. You can order this as an add-on to a Presence package. You can find out how to do that [here](../ssl/how-to-use-ssl-certificates-on-your-hypernode-when-ordered-via-hypernode-nl.md#buy-an-ssl-certificate-via-hypernode-recommended).

## How Can I Link the SSL Certificate to the Hypernode?

As soon as your SSL certificate has been issued you can install it on your Hypernode.

You do this via the Service Panel.

1. Select your Hypernode in the Service Panel
1. Go to the **Instellingen** tab and then to **SSL & DNS Instellingen**
1. You will see all domains of which you are a Contracting Party. The domain for which you ordered an SSL certificate has the status "Beschikbaar" in the "SSL-certificaat" column. Click on **installeren**to install the SSL certificate on your Hypernode.

Repeat this for other domains/store fronts if necessary.

## How Can I Cancel My SSL Certificate?

Do you no longer want to use a secure connection for your website? Then you can always cancel the certificate via the Service Panel. Follow the steps below:

- Login to the Service Panel
- Select your domain name.
- Click the **Administratief**tab.
- Click on the**SSL Certificaat**option.
- At the bottom you can indicate that you wish to cancel the certificate (**SSL-certificaat opzeggen**). This can be done immediately or at the end of the contract.

If you cancel immediately and you do not have another SSL installed, keep the following in mind:

Make sure your site can work without SSL: there should no longer be references to HTTPS in your site.

Make sure there are no more redirects to the HTTPS version of your site.

## Can I Use My Own SSL Certificate?

You can also use a (custom) SSL certificate you purchased elsewhere on a Hypernode. You can find out how to install this on your Hypernode [here](../ssl/how-to-use-ssl-certificates-on-your-hypernode-when-ordered-via-hypernode-nl.md#add-a-custom-ssl-certificate).
