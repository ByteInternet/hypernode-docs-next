---
myst:
  html_meta:
    description: Overview of critical security vulnerabilities that affect Magento and
      PHP shops, such as PHP2Shell, StyleSmuggler, PolyShell and CosmicSting. Learn
      what Hypernode does and what you need to do.
    title: Security Vulnerabilities | Security | Hypernode
---

# Security Vulnerabilities

This chapter describes critical vulnerabilities that affected Magento, Adobe Commerce and PHP shops. Each article explains what Hypernode did to protect your shop and what you need to do yourself. For the full technical analysis, including indicators of compromise, each article links to the research by Sansec.

| Vulnerability | CVE | Affects | Hypernode protection | Your action |
| --- | --- | --- | --- | --- |
| [PHP2Shell](vulnerabilities/php2shell-critical-php-vulnerabilities-cve-2026-109618-cve-2026-109619-and-cve-2026-115560.md) | CVE-2026-109618, CVE-2026-109619, CVE-2026-115560 | PHP 5.4 up to and including 8.5.11 | PHP updated and patched by Hypernode | Check your PHP version and scan your shop |
| [StyleSmuggler](vulnerabilities/how-to-deal-with-the-stylesmuggler-vulnerability-cve-2026-75650-on-hypernode.md) | CVE-2026-75650 | Magento Open Source and Adobe Commerce 2.4.4 to 2.4.9 | NGINX block, provisioned automatically | Apply hotfix VULN-39341 |
| [PolyShell](vulnerabilities/how-to-deal-with-the-polyshell-vulnerability-cve-2026-48356-on-hypernode.md) | CVE-2026-48356 | All Magento Open Source and Adobe Commerce versions before the fix | NGINX blocks execution of uploads | Install the July 2026 patch and remove uploaded files |
| [CosmicSting](vulnerabilities/how-to-deal-with-the-cosmicsting-vulnerability-cve-2024-34102-on-hypernode.md) | CVE-2024-34102 | Magento and Adobe Commerce 2.4.7 and earlier | Attack requests are logged | Install the patch and rotate the encryption key |

```{note}
Installing Magento patches is the responsibility of the customer or their developer. Hypernode does not scan or clean up customer shops. If you need help, you can find a developer in our [partner directory](https://www.hypernode.com/en/partners/).
```

```{toctree}
---
caption: Chapters
maxdepth: 1
glob:
---
vulnerabilities/*
```
