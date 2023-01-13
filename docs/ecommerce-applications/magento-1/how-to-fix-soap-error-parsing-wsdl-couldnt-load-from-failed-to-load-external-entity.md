---
myst:
  html_meta:
    description: If you get this error, some configuration or error is with withholding
      the Magento installation from connecting to its API endpoint. Learn how to revolve
      it.
    title: How to fix SOAP error in Magento 1? | Hypernode
redirect_from:
  - /en/ecommerce/magento-1/how-to-fix-soap-error-parsing-wsdl-couldn-t-load-from-failed-to-load-external-entity/
  - /knowledgebase/soap-error-parsing-wsdl-couldnt-load-failed-load-external-entity/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-fix-soap-error-parsing-wsdl-couldn-t-load-from-failed-to-load-external-entity/ -->

# How to Fix SOAP error: Parsing WSDL: Couldn’t load from “”: failed to load external entity

[Magento’s SOAP API](https://devdocs.magento.com/guides/v2.4/get-started/soap/soap-web-api-calls.html?itm_source=devdocs&itm_medium=search_page&itm_campaign=federated_search&itm_term=soap) references its WSDL, making the Magento instance depend on its API endpoint. If it is impossible to connect to the SOAP API from the Hypernode, you will get this error when trying to perform requests.

Hypernodes are configured to support HTTP requests from the server itself, without the need to add your domain to the `/etc/hosts` as suggested in many articles online. If you get this error, some configuration or error is with withholding the Magento installation from connecting to its API endpoint.

Magento constructs the WSDL URL based on your Magento instance base URL. This means that if your Magento store is not accessible from the server itself, the SOAP server will not be able to load WSDL during initialization. As a result, you encounter this error.

# Test If Your SOAP API Is Available for Magento

To verify if it is possible to connect to the Magento API, you can use curl:

```bash
SITE="example.com"
curl -v https://$SITE/index.php/api/index/index/wsdl/1/
```

This should return the XML schema:

```nginx
<definitions xmlns:typens="urn:Magento" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns="http://schemas.xmlsoap.org/wsdl/" name="Magento" targetNamespace="urn:Magento">
    <types>
        <schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="urn:Magento">
            <import namespace="http://schemas.xmlsoap.org/soap/encoding/" schemaLocation="http://schemas.xmlsoap.org/soap/encoding/"/

```

If you are not able to `curl` for the WSDL, chances are high that this may be the issue.

# Troubleshooting

## Check If the User Agent of the SOAP Client Is Rate Limited

If the source IP of the SOAP client is [rate limited](../../hypernode-platform/nginx/how-to-resolve-rate-limited-requests-429-too-many-requests.md), find the corresponding rate limit `zone` in `/var/log/nginx/access.log` and add the user agent to the user agent mapping or the IP rate limit whitelist.

## Check If the IP of the Server Is Allowed to Make HTTP Requests

If you are using a whitelist and or blacklist to allow and deny IPs, make sure the IP of the Hypernode itself and the local host IP (`127.0.0.1`) are both present in the list(s).

## Flush Your `WSDL` Cache

In some cases the WSDL cache file in `/tmp/` is corrupted, causing the same error. If you run into this issue, use the following workaround to recache your WSDL file:

```bash
rm /tmp/wsdl*
n98-magerun cache:flush
```
