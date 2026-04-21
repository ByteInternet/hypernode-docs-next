---
myst:
  html_meta:
    description: The PURGE method is disabled by default, learn how to safely enable
      it.
    title: How to Control PURGE Method | Hypernode
---

# How to Control PURGE Method

Due to security and performance considerations, the `PURGE` method is disabled by default.

It's possible to enable it, but be careful to only open it to clients you trust. We'll show you how in this article.

## What is the PURGE Method?

The `PURGE` method is an HTTP request method used to clear cached content from reverse proxy caches like Varnish. When a `PURGE` request is sent to a URL, it instructs the cache server to remove the cached version of that content, forcing it to fetch a fresh copy from the origin server on the next request.

## Why is PURGE Disabled by Default?

By default, Hypernode blocks all `PURGE` requests through a configuration file located at `nginx/server.block_purge_requests.conf`.

This blocking is in place because:

- **Security Risk**: Without proper access controls, anyone could purge your cache, leading to performance degradation
- **Performance Impact**: Malicious actors could repeatedly purge your cache, forcing your server to regenerate content constantly
- **VCL Configuration Issues**: Many Varnish configurations use `client.ip` instead of `X-Real-IP` for ACL checks, which can allow unauthorized purging since requests appear to come from 127.0.0.1

## How to Safely Enable PURGE Method

If you need to enable the `PURGE` method for your application (e.g., for cache invalidation after content updates), you can do so by modifying or removing the blocking configuration. Here are the recommended approaches:

### Allow PURGE from Specific IP Addresses

The safest approach is to allow `PURGE` requests only from trusted IP addresses. Replace the content of `nginx/server.block_purge_requests.conf` with:

```nginx
# Deny all PURGE requests by default, allow from specific IPs
if ($request_method = PURGE) {
    set $purge_allowed 0;

    if ($remote_addr = "10.0.0.10") {
        set $purge_allowed 1;
    }

    if ($purge_allowed = 0) {
        return 401;
    }
}
```

### Allow PURGE with Authentication

You can require authentication for `PURGE` requests by checking for specific headers or parameters:

```nginx
# Deny all, allow with authentication
if ($request_method = PURGE) {
    set $purge_auth 0;

    # Allow with proper authentication header/token
    if ($http_x_purge_token = "your-secret-token") {
        set $purge_auth 1;
    }

    if ($purge_auth = 0) {
        return 401;
    }
}
```

### Comment Out the Block

For development environments only, you can temporarily disable the blocking by commenting out all lines.

```{caution}
This approach removes all protection and should only be used in development environments.
```

## Varnish Configuration

If you're using Varnish, ensure your VCL configuration properly handles purge requests and uses the real client IP:

```vcl
import std;

acl purge {
    "127.0.0.1";   # allow localhost
    "10.0.0.0"/24; # allow your cluster private IP range
}

sub vcl_recv {
    if (req.method == "PURGE") {
        set req.http.X-Purge-IP = std.ip(req.http.X-Real-IP, client.ip);
        if (std.ip(req.http.X-Purge-IP, "0.0.0.0") !~ purge) {
            return (synth(405));
        }
        return (purge);
    }
}
```
