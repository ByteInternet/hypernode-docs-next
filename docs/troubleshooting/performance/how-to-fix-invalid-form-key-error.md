---
myst:
  html_meta:
    description: Are you getting an invalid form key error? Learn how to debug and
      fix this common issue with the help of Hypernode's step-by-step guide.
    title: How to fix invalid form key error? | Hypernode
redirect_from:
  - /en/troubleshooting/performance/how-to-fix-invalid-form-key-error/
---

<!-- source: https://support.hypernode.com/en/troubleshooting/performance/how-to-fix-invalid-form-key-error/ -->

# How to Fix Invalid Form Key Error

If you get the dreaded “Invalid form key” error while logging in or working in the admin, something is wrong with your setup.

Since version 1.9.2.2 (and patch SUPEE-6788), Magento requires a secret form token to prevent XSRF attacks. Here are some solutions. For these solutions we assume that you have Magerun installed, because on Hypernode it is installed by default.

## Wrong cookie domain or path?

If you cannot log in, check that your shop uses the right cookie domain and path. For example:

```bash
magerun config:get web/cookie/*
+-------------------------------+---------+----------+-------+
| Path | Scope | Scope-ID | Value |
+-------------------------------+---------+----------+-------+
| web/cookie/cookie_domain | default | 0 | |
| web/cookie/cookie_httponly | default | 0 | 0 |
| web/cookie/cookie_lifetime | default | 0 | 86400 |
| web/cookie/cookie_path | default | 0 | |
| web/cookie/cookie_restriction | default | 0 | 0 |
+-------------------------------+---------+----------+-------+

```

Here, no cookie domain or path is configured, which is ok (nonrestrictive). If the wrong domain or path is configured, you can correct this with:

```bash
magerun config:set web/cookie/cookie_domain ""
magerun cache:flush

```

## Check cookie domain and path in Magento 2

For Magento 2, you can use the following command to check the cookie domain and path

```bash
magerun2 config:store:get web/cookie/cookie_domain

```

To correct the path, use the following:

```bash
magerun2 config:store:set web/cookie/cookie_domain ""
magerun2 cache:flush

```

## PHP choking on too many form values?

Create a file `/data/web/public/.user.ini` with this line:

```php
max_input_vars = 75000

```

## Last resort: disable admin form key

If you are locked out of your admin panel, you could use this as last resort:

```bash
magerun config:set admin/security/use_form_key 0
magerun cache:flush

```

However, this should only be used as a temporary measure, so you can figure out what is wrong with your setup.

## Need help?

Magento is no easy open source CMS. Although we’re very skilled in hosting Magento shops, making them fast and keeping conversion high, we’re no Magento developers. Luckily, we know a lot of agencies that do know a lot about how Magento works. If you need help, don’t hesitate to [contact one of these agencies](https://www.magereport.com/page/support).
