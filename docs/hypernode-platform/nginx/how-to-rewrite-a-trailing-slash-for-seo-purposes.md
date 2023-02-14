---
myst:
  html_meta:
    description: 'Search engines don’t like duplicate content. To rewrite trailing
      slashes some additional Nginx configuration is required. Follow these steps
      to rewrite them. '
    title: How to rewrite a trailing slash for SEO? | Hypernode
redirect_from:
  - /en/hypernode/nginx/how-to-rewrite-a-trailing-slash-for-seo-purposes/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-rewrite-a-trailing-slash-for-seo-purposes/ -->

# How to Rewrite a Trailing Slash for SEO Purposes

Search engines don’t like duplicate content. To rewrite trailing slashes some additional Nginx configuration is required.

If you rewrite **all** URLs, some issues may occur with the Magento backend admin and some other endpoints.

To resolve this issue, use the following snippet to **strip** all trailing slashes and add this to your `/data/web/nginx/server.rewrites`:

```nginx
if ($uri !~ /admin|/webpos) {
    rewrite ^/(.*)/$ /$1 permanent;
}
```

Or this snippet if you want to **add** trailing slashes:

```nginx
if ($uri !~ /admin|/webpos) {
    rewrite ^/(.*)/$ /$1/ permanent;
}
```

Replace `/admin` and `/webpos` with URLs that should not be rewritten in a regex of URLs separated by pipes (`|`).
