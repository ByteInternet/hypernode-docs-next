---
myst:
  html_meta:
    description: Learn how to improve your Varnish cache hit rate on Hypernode by
      identifying automatic cache purges, analyzing hit/miss patterns, and optimizing
      URL normalization to boost performance and efficiency.
    title: Improving Varnish Cache Hit Rate on Hypernode
---

# Improving Your Varnish Cache Hit Rate

A higher Varnish cache hit rate means more requests are served directly from the cache.
This reduces resource usage on your Hypernode, improves page load speed, and helps your shop handle more concurrent visitors without performance degradation.

A low hit rate often indicates that cache is not being reused effectively, typically caused by misconfiguration, frequent invalidation, or too much variation in URLs.

This guide takes you step-by-step from verifying that your cache is active to diagnosing and improving your hit ratio.

## Before You Begin

Typical cache hit rates:

- **Below 10%** → Cache is barely reused
- **30–70%** → Improvement possible (depends on shop type and traffic patterns)
- **Above 80%** → Generally healthy for most shops

Keep in mind:

- Staging environments typically have low hit rates
- B2B webshops often have lower hit rates due to personalization
- Recently flushed caches temporarily reduce hit rates until the cache warms up

Cache hit rate should always be evaluated in context. Traffic volume, personalization, and recent deployments directly affect cache reuse.

## When a Low Hit Rate Is Expected

A low hit rate does not always indicate a problem. It is normal when:

- Traffic volume is low
- The cache was recently flushed
- Most visitors are logged in
- The shop uses heavy personalization
- You are working in a staging environment

Investigate further only if traffic is stable, the cache is warmed up, and the hit rate remains consistently low.

## Step 1 — Verify Varnish Is Enabled

Ensure Varnish is properly enabled on your vhost and configured in your
application (e.g. Magento 2).

For Magento 2, verify:

- That Varnish is enabled on the vhost
- Varnish is selected as the caching application
- The correct VCL is generated and loaded
- Full Page Cache (FPC) is enabled

For a step-by-step guide on activating and configuring Varnish in Magento 2, please refer to our [documentation here](https://docs.hypernode.com/ecommerce-applications/magento-2/how-to-configure-varnish-for-magento-2-x.html#how-to-configure-varnish-for-magento-2-x)

```{tip}
Tip: The [elgentos/magento2-varnish-extended](https://github.com/elgentos/magento2-varnish-extended) extension improves Magento’s default VCL configuration and marketing parameter handling.
```

## Step 2 — Check if Pages Are Being Cached

Using `varnishncsa` from the CLI to see in real time which pages are cached and which are not:

```console
varnishncsa -F '%U%q %{Varnish:hitmiss}x'
```

Look for:

- `hit` → Served from Varnish
- `miss` → Served from backend

Alternatively, you can use `curl` to inspect response headers:

```console
curl -I https://yourdomain.com
```

Review the following headers:

- **`Set-Cookie`**\
  If a Set-Cookie header (such as PHPSESSID) is present, Varnish will typically not cache the response.

- **`Cache-Control`**\
  Should **not** contain `private`, `no-store`, or `no-cache`.

- **`Age`**\
  Indicates how long (in seconds) the object has been cached.

- **`X-Magento-*`**\
  Provides Magento cache/debug information (visible in developer mode).

If most responses return `MISS` (for example in `X-Magento-Cache-Debug` or similar headers), caching is not being reused effectively.

You can also inspect these headers in your browser via:
Developer Tools → Network tab → Select request → Response Headers

## Step 3 — Measure Your Cache Hit Rate

Run:

```console
varnishstat -1 -f MAIN.cache_hit -f MAIN.cache_miss
```

This shows:

- `MAIN.cache_hit` → Cached responses served
- `MAIN.cache_miss` → Requests sent to backend

A high miss count relative to hits indicates room for improvement.

For live monitoring of which requests are hitting Varnish, use:

```console
varnishlog
```

Look for:

- `VCL_call HIT` → Served from Varnish
- `VCL_call MISS` → Served from backend
- `Age` → Indicates how long (in seconds) the object has been cached.
- `X-Magento-*` headers → Provides Magento cache/debug information (visible in developer mode).

Alternatively, reuse the varnishncsa command from Step 2 for live hit/miss monitoring.

## Step 4 — Common Causes of Low Hit Rates

### 1. Pages Bypassing Varnish

Some pages are intentionally not cached:

- Checkout
- Customer account pages
- Requests containing `Set-Cookie` headers

This is expected behavior.

### 2. Frequent Cache Invalidations

If cache clears happen frequently, cache reuse becomes nearly impossible.

Common causes:

- Stock or pricing integrations
- Magento cron jobs performing full cache purges
- Extensions invalidating excessive cache entries

Best practice:
Perform targeted purges (specific URLs or cache tags) instead of full cache
flushes.

### 3. Marketing & Tracking Parameters

Tracking parameters create separate cache entries for identical content.

Examples:

- `utm_source`
- `utm_medium`
- `gclid`
- `fbclid`

Example problem:

- /product-x
- /product-x?utm_source=google

These generate separate cache objects unless the URLs are normalized.

Solution:
Strip non-essential tracking parameters in VCL.

```{tip}
The [elgentos/magento2-varnish-extended](https://github.com/elgentos/magento2-varnish-extended) module improves this behavior.
```

### 4. URL Normalization Issues

Different URL formats fragment your cache.

Examples:

- `/category` vs `/category/`
- `?Color=Red` vs `?color=red`
- Unsorted query parameters
- Session IDs in URLs

Normalize URLs to ensure identical content maps to a single cache object in Varnish.

### 5. Non-Cacheable Magento Blocks

In Magento, a single block marked as non-cacheable can disable Full Page Cache (FPC) for the entire page.

Search for non-cacheable blocks:

```console
grep -R "cacheable=\"false\"" app/code vendor
```

If found:

- Verify the block truly needs to be dynamic
- Remove cacheable="false" if unnecessary
- Use AJAX or Customer Data Sections for dynamic content

Even one unnecessary non-cacheable block can severely impact hit rate.

## Optional — Enable Magento Developer Mode for Debugging

Enable developer mode temporarily for debugging purposes:

```console
magerun2 deploy:mode:set developer
```

Or:

```console
php bin/magento deploy:mode:set developer
```

## Debugging Tools

### varnishlog

Inspect detailed request handling:

```console
varnishlog
```

Look for recurring MISS patterns on pages that should be cacheable.

### varnishncsa

Show hit/miss per URL:

```console
varnishncsa -F '%U%q %{Varnish:hitmiss}x'
```

Filter for hits:

```console
varnishncsa -F '%U%q %{Varnish:hitmiss}x' | grep hit
```

### Hypernode Insights (If Available)

Use Hypernode Insights to:

- Monitor hit/miss ratios
- Detect purge spikes
- Correlate cache drops with deployments or cron jobs
