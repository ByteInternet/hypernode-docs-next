---
myst:
  html_meta:
    description: In Nginx you can use the include statement to avoid duplicate configuration
      for multiple locations. In this article we describe some options.
    title: Create a reusable config to include in custom snippets?
redirect_from:
  - /en/hypernode/nginx/how-to-create-a-reusable-config-to-include-in-custom-snippets/
  - /knowledgebase/create-reusable-config-for-custom-snippets/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-create-a-reusable-config-to-include-in-custom-snippets/ -->

# How to Create a Reusable Config to Include in Custom Snippets

## Working With Includes

In Nginx you can use [the include statement](http://nginx.org/en/docs/ngx_core_module.html#include) to avoid duplicate configuration for multiple locations.
This can be very useful to keep your configuration files tidy and clear. In this article we describe some options.

## Create a Whitelist

If you work with additional applications like [Magmi](../tools/unblocking-and-accessing-magmi-for-hypernode.md) or [PHPMyAdmin on a different domain or over ssl](../mysql/how-to-use-phpmyadmin.md), a reusable whitelist or basic auth file can make things much easier, as you only need to manage a single file instead of one for every additional location.

When a new developer joins or when the office IP of your organization changes, you can easily change the config without the need to grep for `allow` statements or multiple `basic_auth` files.

### Create a Configuration Include File

First we need to create a file that we can include in other locations.
We use the `include.*` extension, as these files are not included anywhere in the Nginx config, but can still be used in `/data/web/nginx`, for example ‘include.whitelist’:

```nginx
allow 1.2.3.4;
allow 2.3.4.5;
allow 6.6.6.6;
deny all;
```

This creates the include file we can use for denying access to IP’s other then the ones defined.

When the whitelist is created, the [nginx-config-reloader](https://github.com/ByteInternet/nginx_config_reloader), the daemon that runs on all Hypernodes and detects config changes. This tool moves all config with a correct syntax to `/etc/nginx/app`.

Therefore if we want to include the whitelist in our config snippets, we should use the location `/etc/nginx/app/include.whitelist`.

### Use the Whitelist Include File

If you want to use the whitelist, you can include it in custom locations:

```nginx
location ~* /magmi($|/) {
    include /etc/nginx/app/include.whitelist;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }
}
```

Using this construction, you don’t need to update every location when another IP is added to the whitelist: just add it to the include file that is used in all locations.

## Configure Basic Auth for Multiple Locations

### Create a Basic Auth Config File

In case you haven’t [created a basic auth password file](how-to-protect-your-magento-store-with-a-password-in-nginx.md), do this first.

In this example we use the password file that is [automagically created on Hypernode Development nodes](basic-authentication-on-hypernode-development-plans.md): `/data/web/nginx/htpasswd-development`.

### Include the Configuration File in Custom Snippets

If you want to use the same configuration for multiple locations without duplicate configuration, use the following snippet:

```nginx
auth_basic "Restricted area - Use the password provided by the project manager";
auth_basic_user_file /data/web/nginx/htpasswd-development;
```

Save this file as `/data/web/nginx/include.basic_auth`

Now if you want to include the snippet you can include it in your custom location snippets:

```nginx
location ~* /magmi($|/) {
    include /etc/nginx/app/include.whitelist;
    include /etc/nginx/app/include.basic_auth;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }
}

```

Make sure you only include files from `/etc/nginx/app` and **NOT** from `/data/web/nginx`!

## Use on Staging Environment

As the `include.*` files are not used in our standard Hypernode configuration as with the `http.*`, `public.*`, `staging.*` and `server.*` configuration files, but only used in your own custom configuration, they can safely be reused in the staging configuration as well.

## Recommendations

- Filenames are not that important because these `include.*`snippets are only included in your own configuration and not in the global Nginx config. Just make sure they don’t start with:
  - `staging.*`
  - `server.*`
  - `public.*`
  - `http.*`
- You can use `include.justarandomname` but to keep it easy, choose a logical name.
- It is not possible to use variables that are set at request time with includes. IE: you cannot map files and use `include $filename;`
