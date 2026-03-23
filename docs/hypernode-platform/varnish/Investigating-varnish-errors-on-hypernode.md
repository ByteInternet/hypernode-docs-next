---
myst:
  html_meta:
    description: Learn how to investigate and resolve Varnish errors on Hypernode
      by checking NGINX and Varnish logs, identifying header and workspace issues,
      and applying the correct buffer and workspace settings.
    title: Investigating Varnish errors on Hypernode
---

# Investigating Varnish errors

When Varnish is enabled, two common HTTP errors can occur: **502 Bad Gateway** and **503 Service Unavailable**. Both are related to how NGINX and Varnish handle response headers and buffers, but they have different causes and solutions. This article guides you through identifying and resolving both.

## 502 Bad Gateway

### What causes it?

One common cause of a `502 Bad Gateway` error with Varnish enabled is that NGINX receives response headers from Varnish that exceed its configured buffer sizes.

This can happen after enabling Varnish or after a change that increases the
size of response headers, for example:

- large cookies
- many `Set-Cookie` headers
- additional custom response headers

### Step 1: Check the NGINX Error Log

Inspect `/var/log/nginx/error.log` and look for the following message:

```console
upstream sent too big header while reading response header from upstream
```

If this message is present, increase the NGINX buffer sizes used for upstream.

### Step 2: Solution

Create a custom NGINX config file at `~/nginx/server.header_buffer` with the following content:

```console
fastcgi_buffers 16 16k;
fastcgi_buffer_size 32k;
proxy_buffer_size 128k;
proxy_buffers 4 256k;
proxy_busy_buffers_size 256k;
```

This increases the buffer sizes NGINX uses when reading response headers from upstream (Varnish), which resolves the "too big header" issue in the vast majority of cases.

```{tip}
After creating the file, NGINX will be reloaded automatically
```

## 503 Service Unavailable (Backend Fetch Failed)

### What causes it?

A 503 error occurs when Varnish itself runs out of workspace memory while processing the response from the backend (e.g. PHP-FPM). This is an internal Varnish issue, visible in the Varnish log as an `out of workspace (Bo)` error.

### Step 1: Check the NGINX Access Log

Start by checking `/var/log/nginx/access.log` for any `503` responses. Look for a line similar to the following:

```log
./access.log:{"time":"2026-02-26T06:55:31+00:00", "remote_addr":"122.173.26.219", "remote_user":"", "host":"www.domain.com", "request":"GET /some/url/", "status":"503", "body_bytes_sent":"552", "referer":"", "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "request_time":"0.000", "handler":"varnish", "country":"NL", "server_name":"www.domain.com", "port":"443", "ssl_cipher":"TLS_AES_128_GCM_SHA256", "ssl_protocol":"TLSv1.3"}
```

### Step 2: Check the Varnish Log

If you confirmed a `503` response, inspect the Varnish logs using `varnishlog` to identify the root cause. Look for lines like the following:

```
- FetchError     workspace_backend overflow
- BackendClose   24 boot.default
- Timestamp      Error: 1772091843.439388 0.032699 0.000160
- BerespProtocol HTTP/1.1
- Error          out of workspace (Bo)
- LostHeader     503
- BerespReason   Service Unavailable
- BerespReason   Backend fetch failed
- Error          out of workspace (Bo)
```

The key indicators are:

- `FetchError: workspace_backend overflow` — Varnish could not allocate enough workspace to process the backend response.
- `Error: out of workspace (Bo)` — the backend object workspace (`Bo`) is too small for the response headers being returned.

### Step 3: Solution

#### Increase the Varnish backend workspace

Increase the backend workspace limit using the `hypernode-systemctl` CLI:

```console
hypernode-systemctl settings varnish_workspace_backend 256k
```

A value of `256k` is a good starting point; increase further if the error persists.

#### Increase the response header buffer sizes

If the backend is sending unusually large response headers, also raise the following settings:

```console
# Maximum size of a single response header line
hypernode-systemctl settings varnish_http_resp_hdr_len 8k

# Maximum total size of all response headers combined
hypernode-systemctl settings varnish_http_resp_size 32k
```

```{important}
After changing these settings, Varnish will restart automatically. Allow a moment for it to reload before testing.
```

### Verification

After applying the changes, monitor the Varnish log to confirm `503` errors are no longer occurring:

```console
varnishlog -q "BerespStatus == 503"
```

If errors continue, consider gradually increasing the workspace values further (e.g., `512k` for `varnish_workspace_backend`).

If the problem persists after applying these fixes, contact support for further assistance.

```{information}
For more information about Varnish configuration and tuning, see our [documentation on improving Varnish hit rate](https://docs.hypernode.com/hypernode-platform/varnish/improving-varnish-hit-rate-on-hypernode.html) and the official
[Varnish documentation](https://varnish-cache.org/docs/).
```
