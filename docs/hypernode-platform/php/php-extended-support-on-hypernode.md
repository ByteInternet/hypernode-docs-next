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
- The patches are made by Hypernode and are installed automatically.
- It is meant for shops that cannot upgrade yet, for example because of an old Magento version or a module that needs an older PHP version.

For more information, see the [PHP Extended Support page](https://www.hypernode.com/en/php-extended-support/) on our website.

## What It Does Not Cover

PHP Extended Support patches PHP only. Your shop software and modules, and other software such as MySQL and Node.js, do not get fixes through it.

```{important}
MySQL 8.0 is EOL and no longer receives security updates, so use MySQL 8.4. See [Upgrading to MySQL 8.4](../mysql/how-to-use-mysql-on-hypernode.md#upgrading-to-mysql-84).
```

We advise you to plan an upgrade to a supported PHP version, also when you use PHP Extended Support. See [Supported PHP Versions and How to Change Them on Hypernode](supported-php-versions-and-how-to-change-them-on-hypernode.md) for how to change your PHP version.
