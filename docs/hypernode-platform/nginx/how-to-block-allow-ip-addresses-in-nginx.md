---
myst:
  html_meta:
    description: 'Hypernode makes use of Nginx. Blocking and allowing IP-addresses
      is easily done in Nginx. Learn how in this article. '
    title: How to block IP addresses in NGINX? | Hypernode
redirect_from:
  - /en/hypernode/nginx/how-to-block-allow-ip-addresses-in-nginx/
  - /knowledgebase/blocking-allowing-ip-addresses-in-nginx/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-block-allow-ip-addresses-in-nginx/ -->

# How to block/allow IP-addresses in Nginx

Hypernode makes use of Nginx (pronunciation: ‘Engine X’). Nginx performs better than Apache for the same amount of visitores, this allows us to serve your webshop to more visitors than Apache could. Nginx does not use .htaccess files like Apache. This means that configuration previously done in .htaccess files now has to be done in a different format.

Blocking and allowing IP-addresses is done using the [access module](http://nginx.org/en/docs/http/ngx_http_access_module.html).

## Denying everyone across the site

To deny all access from certain addresses, create a file in `/data/web/nginx` named `server.blacklist`, with the following contents:

```nginx
deny 1.2.3.4; # Deny a single IP
deny 5.6.7.0/24; #Deny a IP range
```

## Denying everyone across the site, except for certain addresses

To deny all access, except certain addresses, add a file named `server.whitelist`, with the following contents:

```nginx
allow 1.2.3.4; # Allow a single remote host
deny all; # Deny everyone else
```

## Denying or allowing only a specific location

To deny access to everybody except certain addresses to a specific directory or request, create a file called `server.private-dir` containing:

```nginx
location ^~ /myadmin {
allow 1.2.3.4;
deny all;
   rewrite / /index.php break;
   echo_exec @phpfpm;
}
```

## Denying access to your staging environment

If you want to allow only a specific ip address to your staging area, you can add the following snippet to a `staging.whitelist`, replacing yourdomain.hypernode.io with your base-url and YOURIP with the desired ip address.

```nginx
if ($http_host ~ "yourdomain.hypernode.io:8443")  {
  set $block_me_now A;
}
if ($remote_addr != YOURIP) {
  set $block_me_now "${block_me_now}B";
}
if ($block_me_now = AB) {
    return 403;
    break;
}
```
