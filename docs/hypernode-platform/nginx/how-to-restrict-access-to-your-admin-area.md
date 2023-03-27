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

It is very important to restrict access to your Application's admin panel. Hypernodes do have a [Fail2Ban](../../best-practices/security/how-to-protect-magento-against-brute-force-attacks.md), but if your password has been leaked hackers can use it to gain access to all your (customer) data. One of the best ways to restrict access is by limiting the IP address that can even access the admin section.

The snippet below will restrict access to the admin panel on `/magentobackend/` to `198.51.100.16` and the `233.252.0.0/24` range. All other IP's will be blocked. You can simply place this configuration in a file in '/data/web/nginx/' folder, called `server.adminbackend`.

```nginx
location ~ ^/(index\.php/)?magentobackend/? {
  allow 198.51.100.168;
  allow 233.252.0.0/24;

  deny all;

  rewrite / /index.php break;
  echo_exec @phpfpm;
}
```
