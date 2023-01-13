---
myst:
  html_meta:
    description: Install Magento patch SUPEE 8788 to fix critical vulnerabilities
      that allow remote code execution, preventing hackers from taking control of
      your store.
    title: How to install Magento patch SUPEE 8788 and release 1.9.3?
redirect_from:
  - /en/best-practices/security/how-to-install-magento-patch-supee-8788-and-release-1-9-3/
---

<!-- source: https://support.hypernode.com/en/best-practices/security/how-to-install-magento-patch-supee-8788-and-release-1-9-3/ -->

# How to Install Magento patch SUPEE 8788 and release 1.9.3

## Critical Patch

This patch fixes about 17 issues, some of which are highly critical. They allow remote code execution (RCE), so anyone can take control of a store.

## How to Install the Patch

Follow the regular patch instructions. If you run into problems, please visit the [8788 answers page at the StackExchange](http://magento.stackexchange.com/questions/140550/security-patch-supee-8788-possible-problems).

Notably: the patch contains binary characters. So you should probably not open it with a regular editor, as that will mangle the data.

## How Magereport Detects the Patch

[Magereport](https://www.magereport.com/) checks for the following static assets that should have been removed:

```nginx

/skin/adminhtml/default/default/media/flex.swf
/skin/adminhtml/default/default/media/uploader.swf
/skin/adminhtml/default/default/media/uploaderSingle.swf
```

It also checks for the following files that have been modified:

```nginx
/js/mage/adminhtml/uploader/instance.js should contain "fustyFlowFactory"
/skin/adminhtml/default/default/boxes.css should contain "background:url(images/blank.gif) repeat;"
```

## If You Get an Unexpected Result

Please double check these things first:

1. Are you running multiple Magento installations on the same domain? Due to the way Magento routing works, MageReport cannot distinguish between multiple installations on the same domain. So if you want to test an upgrade, you could put it on its own domain (eg. test.yourdomain.com).
1. Have the SWF files indeed been removed? **If you just copied v1.9.3 over an older version, the old SWF files still exist** (and pose a vulnerability)
1. Do the JS and CSS files indeed contain the required strings? If not, the patch might have quit halfway so you have a half-patched system.
1. Do you use Varnish, Cloudflare, a CDN or another caching layer? Your old site might have been cached. Flush your cache or wait until your cache expires.
1. Do you use **Magento 1.5**? We can only detect proper patch application if you have not removed the uploader.swf by hand. Opposed to the other patches, the Flash file is modified instead of deleted. If you have deleted it yourself (which is quite safe to do anyway), we cannot detect the patch unless we hack your shop. Sorry! (3% of all Magento stores still have 1.5)
1. Do you rewrite requests based on `admin` in the URL? Then we cannot properly establish the patch. But if have these security measures in place, you probably do not need Magereport ?

If you still get unexpected results, please mail your URL to magereport@hypernode.com and we will investigate your case. And hopefully make Magereport better, thanks to your help!
