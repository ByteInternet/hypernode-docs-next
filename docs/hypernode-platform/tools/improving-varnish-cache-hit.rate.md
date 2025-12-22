---
myst:
  html_meta:
    description:  Learn how to improve your Varnish cache hit rate on Hypernode by identifying automatic cache purges, analyzing hit/miss patterns, and optimizing URL normalization to boost performance and efficiency.
    title: Improving Varnish Cache Hit Rate on Hypernode
---

# Improving Varnish Cache Hit Rate

An improved **Varnish hit rate** ensures that more pages are served directly from cache. This reduces backend resource usage on your Hypernode and allows your shop to handle more concurrent visitors without performance degradation.  
A low hit ratio usually indicates a caching misconfiguration or cache invalidation happening too frequently.

---

## Understanding Cache Hit Rate

- **HIT:** The response is served directly from Varnish cache  
- **MISS:** The request is forwarded to the backend (for example, PHP/Magento)

A consistently low hit rate means that:

- Pages are bypassing Varnish  
- Cache entries are being purged too often  
- URLs are fragmented due to parameters or inconsistencies  

---

## Common Issue: Automatic Cache Busting

If you notice that your cache is cleared at consistent times, this often points to an automated process that flushes the cache.

### Typical causes

- External integrations that frequently update stock or pricing  
- Magento cron jobs triggering full cache purges  
- Extensions that invalidate more cache than necessary  

### What to do

- Review all third-party integrations that update catalog or pricing data  
- Inspect Magento cron jobs for full cache invalidation tasks  
- Reduce the scope or frequency of full cache purges  
- Prefer targeted purges (specific URLs or entities) instead of clearing the entire cache  

---

## Checking Cacheability and Hit/Miss Behavior

When Varnish is frequently purged or bypassed, your hit rate will drop. You can analyze this behavior using the tools below.

### Useful tools

#### `varnishlog`
View detailed logs of Varnish requests and responses. Look for recurring **MISS** patterns on URLs that should be cacheable.

#### `varnishstat`
Provides counters for cache hits, misses, and backend requests.

#### Hypernode Insights (if available)
Use hit/miss graphs to identify when cache invalidations occur and correlate them with deployments or cron activity.

---

## Checking Varnish Headers Using cURL

You can verify whether a page is cached directly from your own terminal.

```bash
curl -I https://www.example.com/ \
  | egrep 'Age:|Via:|X-Cache|X-Magento-Cache-Debug|Cache-Control'
```

### What to look for

- **Age** header increasing → cached response  
- **X-Cache: HIT** → served from Varnish  
- **Cache-Control** headers that allow caching  
- Absence of **Set-Cookie** for cacheable pages  

---

## Checking Cache Statistics on Your Hypernode

### Snapshot of hits and misses

Untested example (single run):

```bash
varnishstat -1 -f MAIN.cache_hit,MAIN.cache_miss,MAIN.backend_req
```

### Tested (live overview of cached URLs)

```bash
varnishncsa -F '%U%q %{Varnish:hitmiss}x' | grep hit
```

This helps identify which URLs are effectively cached and which are not.

---

## Handling Marketing and Tracking URL Parameters

Marketing parameters such as `utm_source`, `utm_medium`, or `gclid` can dramatically increase the number of unique cache entries.  
Each parameter variation creates a new cache object, lowering your overall hit rate.

### Best practice

Normalize URLs so that these parameters do not influence caching decisions.

#### Examples of parameters to strip

- `utm_*`  
- `gclid`  
- `fbclid`

This normalization should happen before Varnish decides whether a request is cacheable.

> **Tip:** The [`elgentos/magento2-varnish-extended`](https://github.com/elgentos/magento2-varnish-extended) extension improves handling of marketing parameters and enhances the default Magento 2 VCL.

---

## URL Normalization

Different URL variations can fragment your cache and reduce efficiency.

### Common normalization examples

- **Trailing slashes**  
  `/category` → `/category/`
- **Lowercase query parameters**  
  `?Color=Red` → `?color=red`
- **Remove session IDs or irrelevant parameters**

By normalizing URLs, similar requests map to the same cache object, reducing duplication and improving hit rates.