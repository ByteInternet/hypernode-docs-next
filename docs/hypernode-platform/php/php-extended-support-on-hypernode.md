---
myst:
  html_meta:
    description: With PHP Extended Support, Hypernode patches PHP versions that have
      reached end of life, so your shop keeps receiving security fixes until you can
      upgrade.
    title: PHP Extended Support on Hypernode | Hypernode
---

# PHP Extended Support on Hypernode

When a PHP version reaches end of life (EOL), PHP stops releasing security fixes for it. With PHP Extended Support, Hypernode patches these older PHP versions itself, so you can keep your current PHP version while it still receives security fixes.

- It covers PHP versions below 8.2 that PHP no longer supports. See [Supported PHP Versions and How to Change Them on Hypernode](supported-php-versions-and-how-to-change-them-on-hypernode.md) for the list of PHP versions and their status.
- The patches are made by Hypernode together with our security partner Freexian, and are installed automatically.
- It is meant for shops that cannot upgrade yet, for example because of an old Magento version or a module that needs an older PHP version.

For more information, see the [PHP Extended Support page](https://www.hypernode.com/en/php-extended-support/) on our website.

## Example: PHP2Shell

When PHP fixed the PHP2Shell vulnerabilities (CVE-2026-109618 and CVE-2026-109619) in October 2026, it only released fixes for PHP 8.2 to 8.5. Older PHP versions were patched by Hypernode through PHP Extended Support.

## How to Check If Your PHP Version Is Patched

A patch made by Hypernode does not change the PHP version number. Check the build date instead:

```bash
php -v
```

If you are unsure whether your Hypernode is patched, contact support.

## What It Does Not Cover

PHP Extended Support patches PHP only. Your shop software and modules, and other software such as MySQL, do not get fixes through it.

```{important}
MySQL 8.0 is EOL and no longer receives security updates, so use MySQL 8.4. See [Upgrading to MySQL 8.4](../mysql/how-to-use-mysql-on-hypernode.md#upgrading-to-mysql-84).
```

We advise you to plan an upgrade to a supported PHP version, also when you use PHP Extended Support. See [Supported PHP Versions and How to Change Them on Hypernode](supported-php-versions-and-how-to-change-them-on-hypernode.md) for how to change your PHP version.
