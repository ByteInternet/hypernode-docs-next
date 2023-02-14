---
myst:
  html_meta:
    description: Learn how to resolve a 413 request error. Hypernode provides easy-to-follow
      instructions and tips to help you identify and fix the problem quickly.
    title: How to resolve a 413 request? | Hypernode
redirect_from:
  - /en/troubleshooting/performance/how-to-resolve-a-413-request-entity-too-large-error/
---

<!-- source: https://support.hypernode.com/en/troubleshooting/performance/how-to-resolve-a-413-request-entity-too-large-error/ -->

# How to Resolve a 413 Request Entity Too Large Error

When your shop is giving a `413 Request Entity Too Large` error, the data send to the server in a POST request is larger than the max allowed body size in Nginx.

To solve this issue create a Nginx include file as `/data/web/nginx/server.bodysize` and set the following setting:

```nginx
client_max_body_size 300M;
```

The default in our Nginx configuration is set to `client_max_body_size 120m;` but you can easily override this value yourself in case of bigger sizes of POST data.

*Keep in mind that changing this setting to a higher value can increase memory usage on the server. Don’t change this value on Hypernodes with high memory usage as it can easily make your shop run out of resources when under attack or in case of high load.*
