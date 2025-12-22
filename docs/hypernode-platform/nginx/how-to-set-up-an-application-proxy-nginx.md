---
myst:
  html_meta:
    description: Learn how to set up an Nginx application proxy on Hypernode using Managed Vhosts: create a proxy vhost and point it to your app
    title: How to set up an application proxy in Nginx? | Hypernode
---

# How to Set Up an Application Proxy in Nginx

Sometimes you want to serve an application that listens on a local port (for example a Node, Python or PHP service on `localhost:3000`) behind a friendly domain on your Hypernode. Instead of writing a custom Nginx config, you can use Hypernode Managed Vhosts to generate a ready‑made proxy vhost coniguration and then just point it to your application. This keeps your configuration simple and consistent with the rest of your setup.

## Create a proxy vhost

Create a new vhost and set its type to `proxy`. In the example below we create a vhost for `proxy.myapp.hypernode.io`:

```console
app@abc123-example-magweb-cmbl:~$ hmv proxy.myapp.hypernode.io --type proxy
INFO: Managing configs for proxy.myapp.hypernode.io
INFO: No existing config for proxy.myapp.hypernode.io, starting with default options
INFO: Writing HTTP config for proxy.myapp.hypernode.io
```

This command creates a vhost directory under `/data/web/nginx/<your-domain>/` with the proxy templates. You will see the following files:

```console
app@abc123-example-magweb-cmbl:~/nginx/proxy.myapp.hypernode.io$ ls
public.proxy.conf  server.rewrites.conf  staging.proxy.conf
```

## Point the proxy to your application

Open `public.proxy.conf`. The only lines you normally need to change are at the top: the upstream host and port your application listens on. By default they point to `localhost:3000`.

```nginx
set $app_proxy_host localhost;
set $app_proxy_port 3000;

root /data/web/public;

include /etc/nginx/app_proxy_handler.conf;

location / {
    echo_exec @app_proxy_handler;
}
```

Replace `localhost` and `3000` with the correct target for your app if it listens elsewhere. You generally do not need to change anything below those two lines. The included `app_proxy_handler.conf` wires up sensible proxy defaults, SSL, headers and buffering for you. Save the file and Nginx will apply the change.

If you also plan to use the staging mode of this vhost, mirror the same host and port settings in `staging.proxy.conf` so that the staging switch serves the same upstream.
