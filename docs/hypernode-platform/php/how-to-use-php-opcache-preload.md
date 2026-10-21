---
myst:
  html_meta:
    description: Learn how to enable and configure PHP OPcache preload on your
      Hypernode.
    title: How to Use PHP OPcache Preload on Hypernode | Hypernode
---

# How to Use PHP OPcache Preload on Hypernode

PHP OPcache preload compiles your application's files into OPcache before the first request arrives, instead of compiling classes one by one as requests touch them. This article explains how to enable preload on your Hypernode and how to write the preload script for your shop.

Preloading gives you faster first requests after a php-fpm restart, less CPU spent on compilation, and a lower time-to-first-byte. On PHP 8.0 and higher, preload also unlocks the JIT, which we enable alongside preload.

Preloading runs once, when php-fpm starts. Everything compiled stays in OPcache for the life of the FPM process.

## Requirements

- PHP 7.4 or higher. Preload does not exist in older PHP versions.
- Preload applies to PHP-FPM only, not to CLI.
- Preload works for all PHP versions configured on your Hypernode, both the main and the alternative versions.
- The feature is off by default and is enabled per Hypernode.

## Enable Preload

The setting is `php_opcache_preload_enabled` (default: `False`). Enable it with:

```bash
hypernode-systemctl settings php_opcache_preload_enabled True
```

You can also set it via the Control Panel or the [Hypernode API](https://community.hypernode.io/#/Documentation/hypernode-api/settings/README). Enabling or disabling the setting triggers a configuration run on your Hypernode, which writes the FPM configuration and restarts php-fpm. This usually completes within a few minutes.

Check the current value at any time with:

```console
$ hypernode-systemctl settings php_opcache_preload_enabled
True
```

## Create Your Preload Script

When the feature is enabled, Hypernode creates an empty file `/data/web/.php-opcache-preload.php`, owned by `app:app`. This is your file: put your preload code in it. Every file that is loaded while this script runs, via `require`, `include`, or the autoloader, is preloaded.

### Example: Magento 2

Preload the classes your shop uses on every request:

```php
<?php
require '/data/web/magento2/vendor/autoload.php';

foreach ([
    \Magento\Framework\App\Bootstrap::class,
    \Magento\Framework\App\Http::class,
    \Magento\Framework\App\Request\Http::class,
] as $class) {
    class_exists($class); // triggers the autoloader, which compiles the class into OPcache
}
```

### Example: Shopware 6 and Symfony

Symfony generates a preload file for you. Include it:

```php
<?php
$preload = '/data/web/shop/var/cache/prod/Shopware_KernelContainerPreload.php';
if (is_file($preload)) {
    require $preload;
}
```

```{tip}
Keep your preload script conservative. Preload the classes your hot paths actually use, not your entire vendor directory. Preloading everything wastes OPcache memory and slows down FPM startup.
```

## What Happens Under the Hood

- Hypernode installs a root-owned wrapper script at `/usr/lib/hypernode/php-opcache-preload.php` and points `opcache.preload` at it, never directly at your file.
- The wrapper includes your file only if it:
  1. exists,
  1. resolves to a regular file whose real path ends in `.php`,
  1. resolves inside `/data/web/` or `/data/shared/web/`. Symlinks pointing elsewhere are ignored.
- Your script runs as `app` (`opcache.preload_user=app`), never as root.
- On PHP 8.0 and higher, we also set `opcache.jit=tracing` and `opcache.jit_buffer_size=100M`.
- Errors in your script cannot take your site down. If your preload file is missing, invalid, or throws an error, the wrapper logs it and php-fpm starts normally.

## Apply Your Changes

Preload runs only at FPM startup. After creating or editing your preload script, restart php-fpm:

```bash
hypernode-servicectl restart php8.4-fpm
```

```{note}
Replace `php8.4-fpm` with your PHP version, for example `php8.2-fpm`. Alternatively, you can restart all FPM workers at once with `pkill -u app php-fpm`.
```

For more information about restarting services, see [this article about Hypernode CLI tools](../tools/hypernode-cli-tools-and-magerun-plugins.md).

```{warning}
Preloaded files are immutable in OPcache: `opcache_reset()` does not re-read preloaded code. This means flushing the OPcache with a flush script, as described in [this article about flushing the PHP OPcache](how-to-flush-the-php-opcache.md), does not pick up new code. After deploying new code, restart php-fpm so the preload picks up the new files. If your deployment tool does not restart FPM already, add it to your deploy hook.
```

## Verify That Preload Works

1. Check the preload statistics from FPM. Create `/data/web/public/private/preloadinfo.php` and protect it the same way as the flush script in [this article about flushing the PHP OPcache](how-to-flush-the-php-opcache.md):

   ```php
   <?php
   header("Cache-Control: private, no-cache, no-store, max-age=0, must-revalidate, proxy-revalidate");
   $s = opcache_get_status();
   echo "Preloaded scripts: " . count($s['preload_statistics']['scripts'] ?? []) . PHP_EOL;
   ```

1. Check the error log for messages from the wrapper:

   ```console
   $ grep "hypernode preload" /var/log/php-fpm/php-fpm.log
   ```

Alternative PHP versions log to `/var/log/php-alt-fpm/<version>/php-fpm.log`.

## Disable Preload

Disable the feature with:

```bash
hypernode-systemctl settings php_opcache_preload_enabled False
```

The FPM configuration is removed and php-fpm restarts. Your `/data/web/.php-opcache-preload.php` is intentionally left in place. The file is yours, so you decide whether to keep or delete it.

## Troubleshooting

### Nothing Gets Preloaded

Check the FPM error log for `hypernode preload:` messages. In most cases the file was missing, was not a regular `.php` file, or resolved via a symlink outside `/data/web` or `/data/shared/web`.

### Your Preload Code Throws an Error

The error is logged as `hypernode preload: error loading preload: ...` and skipped, and FPM keeps running. Fix your script and restart php-fpm.

### New Code Is Not Picked Up After a Deploy

This is expected. Preloaded code is immutable in OPcache. Restart php-fpm with `hypernode-servicectl restart php8.4-fpm` (adjust the PHP version to your setup) after a deploy.

## Related Articles

- [How to Flush the PHP OPcache](how-to-flush-the-php-opcache.md)
- [How to Use Alternative PHP Versions](how-to-use-alternative-php-versions.md)
- [How to Use the Hypernode Systemctl CLI Tool](../tools/how-to-use-the-hypernode-systemctl-cli-tool.md)
