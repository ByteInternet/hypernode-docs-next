---
myst:
  html_meta:
    description: The WSDL cache is used for API soap calls to Magento. Read here how
      to flush it in case of corruptions causing errors on all API calls to Magento.
redirect_from:
  - /en/ecommerce/magento-1/how-to-flush-the-wsdl-cache/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-flush-the-wsdl-cache/ -->

# How to Flush the WSDL Cache

The WSDL cache is used for API soap calls to Magento. In some very rare cases this cache can get corrupted, causing errors on all API calls to Magento. In most of the cases this causes one of the following errors:

- `Resource path not callable`
- `Invalid API path`
- `Is not a valid method`

This can be resolved in some cases by removing the WSDL cache file so this file is refetched with the next api call. To clear the WSDL cache, remove the cache files in `/tmp`:

```bash
rm /tmp/wsdl-*
```

**NB: This does not solve the following error: `SOAP error: Parsing WSDL: Couldn’t load from "": failed to load external entity.` This error is related to [Magento not being able to access it’s own API](https://support.hypernode.com/knowledgebase/soap-error-parsing-wsdl-couldnt-load-failed-load-external-entity/)**
