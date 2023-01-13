---
myst:
  html_meta:
    description: 'It is very important to restrict access to your Magento admin panel.
      Find out how to restrict access to your admin area. '
    title: How to restrict access to your admin area? | Hypernode
redirect_from:
  - /en/hypernode/nginx/how-to-restrict-access-to-your-admin-area/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-restrict-access-to-your-admin-area/ -->

# How to Restrict Access to Your Admin Area

It is very important to restrict access to your Magento admin panel. Hypernodes do have a [Fail2Ban](../../best-practices/security/how-to-protect-magento-against-brute-force-attacks.md), but if your password has been leaked, hackers will have access to all your data and your customers data with all the consequences that entails. One of the best ways to restrict access is by limiting the IP address that can even access the admin section.

The snippet below will restrict access to the admin panel to 80.113.31.106 and 81.114.32.107. All other IP's will be denied. Replace the IP addresses with your IP address(es), if you don't know your current network IP, just visit [icanhazip.com](http://icanhazip.com).

First create a file in '/data/web/nginx/' folder. And name the file to /data/web/nginx/**server.magentobackend** or whatever you use as admin backend name and use the following snippet.

```nginx
location ~ ^/(index\.php/)?magentobackend/? {
allow 80.113.31.106;
allow 81.114.32.107;
deny all;
rewrite / /index.php break;
echo_exec @phpfpm;
}
```
