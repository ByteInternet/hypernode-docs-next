---
myst:
  html_meta:
    description: 'To unblock Magmi, the Magento mass importer, and offer secure access
      to it for your users and/or developers, use our extensive documentation here. '
    title: How to unblock and access Magmi for Hypernode?
redirect_from:
  - /en/hypernode/tools/unblocking-and-accessing-magmi-for-hypernode/
  - /knowledgebase/unblocking-and-accessing-magmi-for-hypernode/
  - /knowledgebase/securing-access-to-magmi/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/unblocking-and-accessing-magmi-for-hypernode/ -->

# Unblocking and Accessing Magmi for Hypernode

Magmi, the [Magento mass importer](http://magmi.org/), is an alternative product importer offering better performance over the default Magento importer. This makes it a very powerful yet also dangerous tool as it effectively offers full access to your Magento database.

## Offering Secure Access to Magmi

We have noticed a number of our customers have installed Magmi without properly securing their Magmi installation, opening up their shop to being exploited by nefarious actors. For this reason, all Hypernodes now block access to Magmi by default, which is probably how you ended up at this article.

## Unblocking Magmi

To unblock Magmi and offer **secure** access to it for your users and/or developers, use the following steps:

- Log in to your Hypernode using SSH and open the file `/data/web/nginx/magmi.conf` in your favourite editor.
- Hash out (uncomment) the default `location` block at the top of the file which triggers redirection to this support article.

Then pick one of the snippets that applies to your wishes and save it as `server.magmi` or in your `/data/web/nginx/magmi.conf` config file.

*NB: If you don’t want to update IP addresses in all config files with every change of IP address, you can choose to use*\*[include files](../nginx/how-to-create-a-reusable-config-to-include-in-custom-snippets.md).\*

### Protect Your Magmi Installation With HTTP Basic Authentication

Use this snippet if you want your Magmi to be available from any IP on the internet, but with password authentication.

```nginx
location ~* /magmi($|/) {
    auth_basic "Magmi login required";
    auth_basic_user_file /data/web/nginx/magmi.htpasswd;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }
}
```

Don’t forget to [create a user](../nginx/how-to-protect-your-magento-store-with-a-password-in-nginx.md):

```bash
htpasswd -c /data/web/nginx/magmi.htpasswd exampleuser
```

### Protect Your Magmi Installation With an IP Whitelist

Use this snippet if you want your Magmi to be available from just a selected set of IP addresses.

```nginx
location ~* /magmi($|/) {
    allow a.b.c.d;
    deny all;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }
}
```

Be sure to replace `a.b.c.d` with the IP address you wish to whitelist.

*NB: You can add as many* `*allow*` *directives as you would like.*

### Fully Block Magmi Without Redirect to Our Support Documentation

To block Magmi without a redirect to our support documentation, use the following snippet:

```nginx
location ~* /magmi($|/) {
    deny all;

    location ~ \.php$ {
        deny all;
    }
}
```

## HTTPS Only

We strongly recommend enforcing HTTPS-only on Magmi because of the possibility of entering database passwords or transferring other sensitive information.

If you haven’t [enforced HTTPS across your whole site](../nginx/how-to-configure-your-shop-to-only-use-https.md), you can enforce it for Magmi by adding the following line inside the `location` block:

```nginx
if ($scheme = http) {
    return 301 https://$host$request_uri;
}
```
