---
myst:
  html_meta:
    description:  Learn how to improve your Varnish cache hit rate on Hypernode by identifying automatic cache purges, analyzing hit/miss patterns, and optimizing URL normalization to boost performance and efficiency.
    title: Improving Varnish Cache Hit Rate on Hypernode
---

# Improving Your Varnish Cache Hit Rate

A higher Varnish cache hit rate means more pages are served directly from cache.
This reduces backend resource usage on your Hypernode, improves page load speed, and helps your shop handle more concurrent visitors without performance degradation.

A low hit rate often indicates that cache isn’t being reused effectively, typically caused by misconfiguration, frequent invalidation, or too much variation in URLs.

This guide takes you step-by-step from verifying that your cache is active to diagnosing and improving your hit ratio.

## Before You Begin

Typical cache hit rates:
- **Below 10%** → Cache is barely reused  
- **30–70%** → Improvement possible (depends on shop type)  
- **Above 80%** → Generally healthy  

Keep in mind:
- Staging environments typically have low hit rates  
- B2B webshops often have lower hit rates due to personalization  


# Step 1 — Verify Varnish Is Enabled

Ensure Varnish is properly enabled on your Hypernode and configured in your
application (e.g. Magento 2).

For Magento 2, verify:
- Varnish is selected as the caching application
- The correct VCL is generated and loaded
- Full Page Cache (FPC) is enabled

For a complete guide on how to configure Varnish in Magento 2 see: 
https://docs.hypernode.com/ecommerce-applications/magento-2/how-to-configure-varnish-for-magento-2-x.html#how-to-configure-varnish-for-magento-2-x

```{tip}
Tip: The [elgentos/magento2-varnish-extended](https://github.com/elgentos/magento2-varnish-extended) extension improves Magento’s
default VCL configuration and marketing parameter handling.
```

# Step 2 — Check if Pages Are Being Cached

Use `curl` to inspect response headers:

```console
curl -I https://yourdomain.com
```

Look for:
- `X-Cache: HIT` → Served from Varnish
- `X-Cache: MISS` → Served from backend
- `Age` → How long the object has been cached
- `X-Magento-*` headers → Useful Magento cache debug info only visible when developer mode is enabled.

If most responses return `MISS`, caching is not being reused effectively.

You can also inspect these headers in your browser via:
Developer Tools → Network tab → Select request → Response Headers

---

# Step 3 — Measure Your Cache Hit Rate

Run:

```console
varnishstat -1 -f MAIN.cache_hit -f MAIN.cache_miss
```

This shows:
- `MAIN.cache_hit` → Cached responses served
- `MAIN.cache_miss` → Requests sent to backend

A high miss count relative to hits indicates room for improvement.

For live monitoring:

```console
varnishstat
```

---

# Step 4 — Common Causes of Low Hit Rates

## 1. Pages Bypassing Varnish

Some pages are intentionally not cached:
- Checkout
- Customer account pages
- Requests containing `Set-Cookie` headers

This is expected behavior.

## 2. Frequent Cache Invalidations

If cache clears happen frequently, reuse becomes impossible.

Common causes:
- Stock or pricing integrations
- Magento cron jobs performing full cache purges
- Extensions invalidating excessive cache entries

Best practice:
Perform targeted purges (specific URLs or cache tags) instead of full cache
flushes.

---

## 3. Marketing & Tracking Parameters

Tracking parameters create separate cache entries for identical content.

Examples:
- `utm_source`
- `utm_medium`
- `gclid`
- `fbclid`

Example problem:
- /product-x
- /product-x?utm_source=google

These generate separate cache objects unless normalized.

Solution:

Strip non-essential tracking parameters in VCL.

```{tip}
The [elgentos/magento2-varnish-extended](https://github.com/elgentos/magento2-varnish-extended) module improves this behavior.
```
---

## 4. URL Normalization Issues

Different URL formats fragment your cache.

Examples:
- `/category` vs `/category/`
- `?Color=Red` vs `?color=red`
- Unsorted query parameters
- Session IDs in URLs

Normalize URLs to ensure identical content maps to a single cache object.

---

## 5. Non-Cacheable Magento Blocks

In Magento, a single block marked as non-cacheable can disable Full Page Cache
for the entire page.

Search for non-cacheable blocks:

```console
grep -R "cacheable=\"false\"" app/code vendor
```
If found:
- Verify the block truly needs to be dynamic
- Remove cacheable="false" if unnecessary
- Use AJAX or Customer Data Sections for dynamic content

Even one unnecessary non-cacheable block can severely impact hit rate.

# Optional — Enable Magento Developer Mode for Debugging

Developer mode provides more detailed error output:
```console
magerun2 deploy:mode:set developer
```

Or: 
```console
php bin/magento deploy:mode:set developer
```

# Debugging Tools

## varnishlog
Inspect detailed request handling:
```bash
varnishlog
```
Look for recurring MISS patterns on pages that should be cacheable.

## varnishncsa
Show hit/miss per URL:
```bash
varnishncsa -F '%U%q %{Varnish:hitmiss}x'
```
Filter for hits:
```bash
varnishncsa -F '%U%q %{Varnish:hitmiss}x' | grep hit
```

## Hypernode Insights (If Available)
Use Hypernode Insights to:
- Monitor hit/miss ratios
- Detect purge spikes
- Correlate cache drops with deployments or cron jobs