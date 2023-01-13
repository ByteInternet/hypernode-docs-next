---
myst:
  html_meta:
    description: Our built-in Web Application Firewall is designed specifically to
      protect your application against known vulnerabilities and endpoints that often
      see abuse.
    title: How to use a Cloud firewall on Hypernode? | Security
redirect_from:
  - /en/best-practices/security/how-to-use-a-cloud-firewall-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/best-practices/security/how-to-use-a-cloud-firewall-on-hypernode/ -->

# How To Use a Cloud Firewall on Hypernode

Your Hypernode comes with a built-in Web Application Firewall (WAF). This WAF is designed specifically to protect your application against known vulnerabilities, weaknesses, and endpoints that often see abuse.

If you have an external WAF, often called a SaaS or Cloud Firewall, it can be placed in front of your Hypernode. This is helpful to shield your application from more generic exploits, such as cross-site-scripting, Denial of Service attacks, and SQL injection, or for meeting regulatory or policy requirements.

There are many different Cloud Firewall providers, and applications, to use. Since nearly all Cloud Firewall providers use the same method of connecting to your application, your Hypernode should be able to work with any of them. If you wish to double check that your specific Cloud Firewall is supported on Hypernode, please contact our support team. Some well known services include names such as Cloudflare, AWS WAF, F5 Advanced, Akamai, and Barracuda, though many more are being offered.

## Setup overview

Almost all cloud based firewalls are designed the same way. By changing the DNS of your website to point to the Cloud Firewall, all traffic to your website is routed through the Cloud Firewall. The firewall will then function as a reverse proxy, and forward approved traffic to your webserver.

## Nginx setup

Due to how Cloud Firewalls are set up, all traffic to your Hypernode will seem to originate from a single location; the Cloud Firewall. As such, any malicious traffic that managed to get forwarded by the firewall, will be attributed to the IP address of the firewall. Because of this, extra measures need to be taken to ensure that the Firewall is not blocked by the Hypernode, as this would block not only the malicious traffic, but also legitimate traffic.

Your hypernode comes preconfigured to work with several well known Cloud Firewall providers, such as Cloudflare, and Incapsula.

In order to configure your nginx to recognize the actual origin of traffic flowing through the firewall, you need two bits of information from your Cloud Firewall Provider; Their reverse-proxy IP address or ranges, and the HTTP header used to relay the original IP address. This is usually done using the ‘X-Forwarded-For’ HTTP header.

### Configuring IP addresses

Once you have received a list of IP addresses from your Cloud Firewall provider, you need to mark these as trusted IP’s, so that nginx will accept the traffic origin information from your Cloud Firewall Provider. To do so, create a file in your nginx folder called server.firewall

```
# Snowflake WAF IP addresses
# Source: https://www.example.com/snowflake/waf/ip.txt

set_real_ip_from 198.51.100.12;
set_real_ip_from 198.51.100.13;
set_real_ip_from 198.51.100.14;
set_real_ip_from 203.0.113.0/24;
```

In this example we have marked 3 dedicated IP addresses as trusted (198.51.100.12, .13, and .14), and a range (203.0.113.0/24). We also added a comment showing what these addresses are, and where they are sourced from, to easily allow us to locate them if they ever need updating.

### Configuring the upstream origin HTTP header

Most Cloud Firewalls, such as Cloudflare, Incapsula, and F5, use the “X-Forwarded-For”-header to inform webservers of the origin IP address. If your Cloud Firewall uses a different header, you need to configure this in nginx. To do so, add the following line to your existing configuration file, server.firewall

```
real_ip_header X-Real-IP;
```

In this example, we have configured nginx to read the origin IP address using the X-Real-IP header, provided by your Cloud Firewall.

## DNS Setup

In order to route traffic to your Hypernode through the Cloud Firewall, most setups require you to configure your DNS records to point directly at the Cloud Firewall. However, you will also need to configure where traffic to your website needs to be sent from the Cloud Firewall. Because your DNS points to the Cloud Firewall itself, you can’t simply configure traffic to be forwarded to ‘[www.example.com](http://www.example.com)’, but you will need to supply an alternative location. This is often called an ‘origin’ server.

To ensure that the Cloud Firewall can always connect to your Hypernode, we advise you to configure the Cloud Firewall to use the Hypernode’s name as an origin server, i.e., ‘example.hypernode.io’. If that is not an option, you can also supply the Hypernode’s IP address, though do note that in exceptional cases the IP address might change. As such we would always recommend to use the ‘example.hypernode.io’ address.

## SSL Setup

For optimal security, it is recommended to configure traffic between the Cloud Firewall and your Hypernode to always be encrypted, through an SSL certificate. For most Cloud Firewall setups you can simply use a regular SSL certificate, as you would normally.

In some cases you may be provided with an Origin SSL certificate by your Cloud Firewall provider. In this case, simply upload a Custom Certificate either via the Service panel, or via the Control Panel.
