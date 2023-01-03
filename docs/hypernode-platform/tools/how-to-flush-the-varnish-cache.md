---
myst:
  html_meta:
    description: Flushing the Varnish cache can be done using the Magento backend
      panel, but if needed, you might want to be able to flush the cache from the
      command line.
redirect_from:
  - /en/support/solutions/articles/48000982378-how-to-flush-the-varnish-cache/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48000982378-how-to-flush-the-varnish-cache/ -->

# How to Flush the Varnish Cache

Flushing the Varnish cache can be done using the Magento backend panel, but in case of problems, when the backend is not accessible, you might want to be able to flush the cache from the command line to fix any Varnish related caching issues.

You can flush the cache for a single domain, a specific URL or just the cache as a whole.

- Flush a single domain:
  `varnishadm "ban req.http.host ~ www.mydomain.com"`
- Flush a specific file type:
  `varnishadm "ban req.url ~ .css"`
- Flush a specific file type of a single domain:
  `varnishadm "ban req.http.host ~ www.mydomain.com" && req.url ~ .css"`
- Flush a specific URL
  `varnishadm "ban req.url ~ /admin/something"`
- Flush the cache as a whole:
  `varnishadm "ban req.url ~ ."`
