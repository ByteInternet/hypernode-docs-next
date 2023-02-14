---
myst:
  html_meta:
    description: Get premium protection for your Magento shop with Hypernode. Learn
      how they implement changes to block security threats in under 4 hours.
    title: How Hypernode protects your Magento Shop | Security
redirect_from:
  - /en/support/solutions/articles/48001158433-how-hypernode-protects-your-magento-shop/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001158433-how-hypernode-protects-your-magento-shop/ -->

# How Hypernode protects your Magento shop

Due to the standardisation of the ecosystem of Hypernode and our continuous integration pipeline, we can implement changes to all Hypernodes in no time. From the moment a security issue becomes known, a Magento patch for example, [we are able to block security threads on our complete platform in less than 4 hours](https://www.hypernode.com/blog/security/how-hypernode-identifies-and-blocks-new-security-threats-within-the-hour). This way we can offer our customers premium protection.

But, this is not only applicable for acute security issues. As Magento nerds we know that development files also need to be protected and that the Magmi tool can create a huge security hazard for example. Such risks are proactively taken care of at Hypernode.

## A list of vulnerabilities for which Hypernode customers are protected

The following security issues named in Magereport will not pose a threat to Hypernode customers.

- Security patch 5344 (Shoplift) - In February 2015, we implemented a platform fix within a matter of only 4 hours. Despite this fix, we still advise our customers to patch their shop(s).
- Unprotected Magmi? - Standardly the access to Magmi is blocked. If you would like it to be unblocked, check [our Hypernode documentation](../../hypernode-platform/tools/unblocking-and-accessing-magmi-for-hypernode.md).
- Unmaintained server? - Hypernode always runs on safe software versions.
- Unprotected version control? - For all shops on our platform, it is not possible to visit the git directory from the outside.
- Security patch 5994 (admin disclosure) - We regularly check whether a login is attempted and cover it.
- Cacheleak vulnerability? - We block this leak in the server configuration.
- Unprotected development files? - We block this on server level.
- Security patch 6285 (XSS, RSS) - Within 4 hours of a leak being discovered, we implemented a platform fix. Of course, we advise our customers to still patch their shops.
- Credit Card Hijack detected? - This hack is implemented through Shoplift. We have plugged the leak within 4 hours after being discovered. Therefore there are no Hypernode customers who suffered from this hack.
- EM_Ajaxproducts RCE vulnerability? - We block this on server level.
- Cart2Quote RCE vulnerability? – We block this on server level.

## Hypernode is specifically developed for Magento

Hypernode goes even further than the security of your hosting environment. We dive into the intersection of the Magento application and its hosting, and advise you about it. We always make sure to implement the best practices based on 20+ years of hosting experience.

At Hypernode, unwanted bots are automatically blocked and you are protected against brute force attacks. Due to smart server optimizations and by using the newest technologies, the shops on the Hypernode platform reach a unique speed. Specific Magento development tools such as ModMand and N98 Magerun are installed standardly and customers have access to MageReport Premium. This last tool answers questions such as:

- Is my node too busy? If yes, is this due to valid PHP requests, or are there too many bots on my site?
- Is my shop fast enough? How quick is it compared to similar shops on Hypernode? When performance is low, is it due to i/o operations? Due to much traffic? Due to bots? Or have I used too much memory?
- Has my node reached its limits? Do I need to clean up or switch to a bigger plan?

Want to know more about Hypernode or want to directly order a free month of testing. Check out [our website](https://www.hypernode.com/)!
