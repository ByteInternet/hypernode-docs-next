---
myst:
  html_meta:
    description: In this article we explain how to protect a directory from being
      accessed through the web, create a location and deny access to it.
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-deny-access-to-locations-and-directories/ -->

# How to Deny Access to Locations and Directories

If you want to protect a directory from being accessed through the web, create a location and deny access to it:

```nginx
#Deny access to domain.com/some/location/
location ~ /some/location {
    deny all;

#Deny access to all .php files
    location ~ \.php$ {
        deny all;
    }
}

```
