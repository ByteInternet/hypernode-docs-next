---
myst:
  html_meta:
    description: Follow our step-by-step guide on checking SPF records, return-path,
      and if your Hypernode is listed on a blacklist.
    title: How to prevent your emails being marked as spam | Hypernode
redirect_from:
  - /en/best-practices/email/how-to-prevent-your-email-being-marked-as-spam/
---

<!-- source: https://support.hypernode.com/en/best-practices/email/how-to-prevent-your-email-being-marked-as-spam/ -->

# How to Prevent Your Email Being Marked as Spam

Sometimes email which is sent from a Hypernode is marked as spam by external spam filters. Follow these steps to be for sure the cause is not a misconfiguration.

## Check SPF Records

Check if the inclue:spf.appname.hypernode.io hostname is included in your SPF record (in the DNS zone-file). This hostname contains the IP-address of your Hypernode and the addresses from Byte’s mailservers.

Detailed information on SPF records can be found [here](../../hypernode-platform/dns/how-to-set-up-your-spf-records-for-hypernode.md).

If the IP address of your Hypernode is not included in this record, please send an email to support@hypernode.com, so we will fix the record for you. This could happen after an up- or downgrade of the Hypernode plan.

## Check If the return-path Is Configured Correctly

If you send your emails using a PHP script, the default return-path will be noreply@hypernode.io. This email address will be seen as possible spam address, so you have to change this into something else (e.g. noreply@example.tld) or change it into the email address you also use in your Magento installation. We would advise you to use a valid email address. If the recipient is using SAV (Sender Address Verification), and the email address is not reachable, then a spamfilter could see this as a spam message.

More information about setting your return-path for [Magento 1](../../ecommerce-applications/magento-1/how-to-set-the-return-path-for-a-magento-1-shop.md) and [Magento 2](../../ecommerce-applications/magento-2/how-to-set-the-return-path-for-a-magento-2-shop.md).

## Check If Your Hypernode Is Listed on a Blacklist

Browse to MXToolbox and fill in the IP address of your Hypernode to check if the IP address is listed on a blacklist. If it is listed, you could request a delisting by yourself. Do not forget to check the reason why the IP is listed and fix it to prevent this from happening again.

If emails sent from the Hypernode are still marked as spam, please send an analysis request by email to support@hypernode.com including [a full-header of a marked message](../../best-practices/email/how-to-find-the-mail-headers.md). We will investigate the reason and send you a reply with more details.
