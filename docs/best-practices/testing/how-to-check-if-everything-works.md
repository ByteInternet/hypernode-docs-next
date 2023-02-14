---
myst:
  html_meta:
    description: Before changing the DNS settings of your original domain to Hypernode,
      it’s important to first check if everything in your shop is working as it should.
    title: How to check if everything works on your Hypernode? | Testing
redirect_from:
  - /en/best-practices/testing/how-to-check-if-everything-works/
---

<!-- source: https://support.hypernode.com/en/best-practices/testing/how-to-check-if-everything-works/ -->

# How to Check If Everything Works

Before changing the DNS settings of your original domain to Hypernode, it’s important to first check if everything in your shop is working as it should.

Use the steps below to test everything in your shop.

**NB:** When browsing your preview shop, double check that you don’t end up on your production shop by following a hardcoded link.

A bigger checklist is available [on the Github account](https://gist.github.com/peterjaap/10016278)of one of our well appreciated technical partners Peter Jaap (Elgentos).

- Test all storefronts *(use the storefront view in MageReport Premium (only for Magento 1.x versions)).*
- Test front pages, categories and product pages.
- Test the catalog search functionality and additional indexers like [Elasticsearch](../../best-practices/performance/how-to-improve-your-magento-search.md#elasticsearch) or [Sphinx](../../best-practices/performance/how-to-improve-your-magento-search.md#sphinx)
- Verify whether the search pages are fully functional and if you don’t get 404 errors when visiting the products in the results.
- Test [restricted areas](../../hypernode-platform/nginx/how-to-deny-access-to-locations-and-directories.md) and [password protected directories](../../hypernode-platform/nginx/how-to-protect-your-magento-store-with-a-password-in-nginx.md) (downloads, etc).
- Test if you can add new products through the Magento admin.
- Test the admin functionality by flushing your cache, reindex your indexers and navigate through the Magento admin.
- Test if your webshop [can send mail](../../hypernode-platform/email/policy-for-sending-email-on-hypernode.md) that [can be received](../../ecommerce-applications/magento-2/how-to-set-the-return-path-for-a-magento-2-shop.md) without [ending up in the spamfolder](../../best-practices/email/how-to-prevent-spam-being-sent-from-your-name-or-email-address.md).
- [Test if your cronjobs work](../../hypernode-platform/tools/how-to-use-periodic-tasks-cronjobs-on-hypernode.md).
- Test if all caching mechanisms using Memcached are replaced with Redis:

```nginx
grep -Ri memcache /data/web/public/app/etc
```

- Test if your timezone is set correctly. Instructions how to do this can be found in the article [Magento and UTC on Hypernode](../../ecommerce-applications/magento-2/how-to-set-magento-2-x-to-the-utc-timezone.md).
- Test if additional software (such as WordPress) works as well.
- Verify that connections with external systems (CRM, inventory, analytics, etc) still work and keep working when the IP address of the node changes.
  In some cases you need to notify your external supplier of the new IP. Find your IP with the `ping example.hypernode.io` command.
- Have you made a backup of the content and database?
- Test if you shop contains hardcoded paths to the old location.
- View the Nginx error logging in `/var/log/nginx/error.log` to see if there are critical PHP errors that should be fixed.
- View the Magento logging in `/data/web/public/var/log`.
  Especially the system.log and the `exceptions.log`.
- When an error raises during a request, in many cases a report file is created in `/data/web/public/var/report`. Check the reports for errors.
  To list the reports in order of appearance (the newest at the bottom of the list) use `ls -ltr /data/web/public/var/report`.
- Add some products to your cart and test whether you are able to go to checkout.
  Cancel your payment order to see if the callback requests and redirect from the payment provider to your shop is functional.
- Test for images, css, js and mixed content warnings.
- Test if all static content is loaded: View the console in your browser to check if there are javascript errors or 404 errors on stylesheets and js files.
- Test if [the Magento API is accessible when used](../../ecommerce-applications/magento-2/how-to-enable-the-magento-2-api.md).
- Test if the sitemap is accessible for [Magento 1](../../ecommerce-applications/magento-1/how-to-create-a-sitemap-xml-for-magento-1-x.md)or [Magento 2](../../ecommerce-applications/magento-2/how-to-create-a-sitemap-xml-for-magento-2-x.md).
- Test if [you can easily download the robots.txt file](../../ecommerce-applications/magento-1/how-to-create-a-robots-txt-for-your-magento-1-shop.md) (Or for [Magento 2](../../ecommerce-applications/magento-2/how-to-create-a-robots-txt-for-magento-2-x.md)).
- Test product and price import and export routines.
- Test product push mechanisms for search engines.

If every box has been checked, you can change the DNS settings of your original domain to Hypernode. Instructions on how to do this, can be found in the article [Go Live With Your Hypernode.](../../best-practices/testing/how-to-go-live-with-your-hypernode.md)
