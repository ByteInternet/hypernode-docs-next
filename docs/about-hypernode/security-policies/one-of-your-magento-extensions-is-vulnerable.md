---
myst:
  html_meta:
    description: One of your Magento extensions is vulnerable, it means there is a
      bug that can be exploited by hackers. Learn what steps to take to fix the issue.
    title: 'Your Magento Extensions is Vulnerable: What to Do | Hypernode'
redirect_from:
  - /en/about/security/one-of-your-magento-extensions-is-vulnerable/
---

<!-- source: https://support.hypernode.com/en/about/security/one-of-your-magento-extensions-is-vulnerable/ -->

# One of your Magento Extensions is Vulnerable

If you’ve been directed to this article, you probably received a warning that one of the extensions in your Magento shop is vulnerable.

## What are the consequences?

If one of the extensions in your Magento shop is vulnerable, it means there is a bug in the extension that can be used for evil.

This can include creditcard theft, sending email spam in your name, stealing customer data, using your shop for DDoS attacks, retrieving sensitive information from your shop, etc.

## Special attention to online credit card theft

A hot topic over the past few years are digital skimmers. A hacker group (also know as Magecart) use code inserted into websites to steal credit card details. As of October 2018 more than 20 extensions have been abused by hackers. Details can be found[in this blog explaining the attack method PHP Object Injection (POI)](https://sansec.io/labs/2018/10/23/magecart-extension-0days/). Former Hypernode owner Willem will update the list of vulnerable extensions regularly.

## How do I fix it?

Fixing this breach is not an easy task. If you don’t have a lot of knowledge of Magento’s security, we recommend you to hire a Magento developer or specialist experienced in Magento security.

### There is already an update available for my extension

If there is an update available for the given extension, upgrade as soon as possible to avoid abuse of your webshop and customer data.

Use the update instructions provided by the developer or maintainer of the extension to update.

After updating you should still have your webshop checked. It’s possible that your shop was already hacked, and is now infected and contains other malicious code. This code can be hidden in such places that it’s impossible to tell from Magento.

### There is no update available for my extension

In case there is no update that fixes the vulnerability available yet, always contact the developer or maintainer that created the extension. In some cases there is a fix or an offline update (a zip file) available.

If there is not a fix available yet, this leaves you with only one option: Disable the extension, even if you lose some fundamental functionality in your webshop.

It is not an option to simply ignore the problem, as we’ve seen several occasions where within less than 8 hours after discovery of the vulnerability, it was actively abused.

Afterwards you should still have your webshop checked. It’s possible that your shop was already hacked, and is now infected and contains malicious code. This code can be hidden in such places that it’s impossible to tell from Magento.

## More information

To verify if your shop is hacked or not, [use the article about recovering a hacked Magento shop](../../best-practices/security/how-to-recover-a-hacked-magento-shop.md)

## Need help?

Magento is no easy open source CMS. Although we’re very skilled in hosting Magento shops, making them fast and keeping conversion high, we’re no Magento developers. Luckily, we know a lot of agencies that do know a lot about how Magento works. If you need help, don’t hesitate to contact [one of these agencies](https://www.magereport.com/page/support).
