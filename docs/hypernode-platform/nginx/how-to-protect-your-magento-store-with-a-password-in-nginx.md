---
myst:
  html_meta:
    description: 'Keep your shop secure, by learning how to protect your Magento store
      with a Password in Nginx. '
    title: Protect a Magento store with a password in NGINX | Hypernode
redirect_from:
  - /en/hypernode/nginx/how-to-protect-your-magento-store-with-a-password-in-nginx/
  - /knowledgebase/protect-a-directory-with-a-password-in-nginx/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-protect-your-magento-store-with-a-password-in-nginx/ -->

# How to Protect Your Magento Store With a Password in Nginx

Hypernode makes use of Nginx. Nginx does not use .htaccess files like Apache does. This means that configuration now has to be done in a different format, explained in the Nginx documentation. To protect a directory with a password in Nginx, you can use the same htpasswd file that is used with Apache. To restrict access to a location, you can use the auth basic directive.

## Restricting Access to a Directory

To restrict access to the preview-directory using users and passwords specified in the file `/data/web/nginx/htpasswd`, create a file called `server.basicauth` in `/data/web/nginx` containing:

```nginx
location ^~ /preview/ {
  auth_basic "Restricted area";
  auth_basic_user_file /data/web/nginx/htpasswd;
  location ~ \.php$ {
    echo_exec @phpfpm;
  }
}
```

**NOTE: Make sure to include a PHP handler to the end of a location-block, or PHP scripts inside it will not be executed!**

How to create or update a htpasswd file? This command will ask you for a password and save it to the password database:

```nginx
htpasswd -c /data/web/nginx/htpasswd exampleuser
```

## Restricting Access to a Specific Domain

Create a file called `server.basicauth` in `/data/web/nginx` with the following snippet:

```nginx
if ($http_host = "domainwithbasicauth.com") {
set $auth_basic Restricted;
}

if ($http_host != "domainwithbasicauth.com") {
set $auth_basic off;
}

auth_basic $auth_basic;
auth_basic_user_file /data/web/nginx/htpasswd;
```

This will only restrict access to domainwithbasicauth.com with basic authentication and make all other domains on your Hypernode accessible without any authentication.

Creating a user and a password can be done with the following command:

```nginx
htpasswd -c /data/web/nginx/htpasswd exampleuser
```

## Restricting Access to Your Shop Based on IP & Basic Authentication

If you wish to protect your store based on both ip and basic authentication, you can use the following snippet (fill in the desired ip adres for the x.x.x.x):

```nginx
satisfy any;
allow x.x.x.x;
deny all;
auth_basic "login required";
auth_basic_user_file /data/web/nginx/htpasswd;
```

If you want to protect your backend with both basic authentication and an ip whitelist, you can expand the snippet with an extra check:

```nginx
satisfy any;
allow x.x.x.x;
deny all;
auth_basic "login required";
auth_basic_user_file /data/web/nginx/htpasswd;

location ~ ^/backendurl {
satisfy all;
rewrite / /index.php break;
echo_exec @phpfpm;
}
```
