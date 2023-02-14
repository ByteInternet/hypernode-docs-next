---
myst:
  html_meta:
    description: 'A 502 Bad Gateway error indicates there has been an internal error
      within PHP. Learn how to resolve 502 Gateway errors. '
    title: How to resolve 502 Gateway errors? | Hypernode
redirect_from:
  - /en/hypernode/php/how-to-resolve-502-gateway-errors/
---

<!-- source: https://support.hypernode.com/en/hypernode/php/how-to-resolve-502-gateway-errors/ -->

# How to Resolve 502 Gateway Errors

A 502 Bad Gateway error indicates there has been an internal error within PHP, which resulted in the site not being rendered and therefore you will see this error in your browser.

## How to Check Whether 502 Errors Have Occured

You can see whether any 502 errors have occured by analyzing the Nginx access logs. An easy way to do this is by using the Parse Nginx Logs (`pnl`) tool. Log in on your Hypernode and run the following command to check whether any such errors occurred today (change `--today` to `--yesterday` in order to check the errors for the day before).

```bash
pnl --today --filter status=502

```

The output will show you which requests could not be handled by PHP.

## What Can Cause 502 Errors

### Memory Depletion

The main cause is that PHP has ran out of memory. This does not normally happen, but if it happens, it is likely due to two reasons:

1. The code base is very large (many installed modules or very large/complex modules)
1. One or more Magento modules leak memory.

Hypernodes can generally cope with high memory usage, but in extreme cases the Hypernode will perform an automatic recovery restart of the PHP service. This might take a few seconds, during which visitors might get a 502 response.

To verify this situation, log in to your Hypernode and check the memory usage (in KB) of PHP processes:

```bash
pgrep -f fpm | xargs ps -o rss=

```

This will generate output like the one below:

```bash
28720
39408
251184

```

This shows memory usage of 28, 39 and 251 MB. The average memory usage per process on our platform (across all customers and sizes) is 63 MB. If you are well above this figure, it might indicate an issue with your code. The solutions are:

1. Fix the code, or replace a faulty Magento module. This requires a memory profiler, or the laborious process of trial and error.
1. Upgrade to a Hypernode with more memory.

Another way of getting more insights in the Hypernode memory usage is by runningg `htop`, this will provide you with a live feed of the resources of the server. You can filter these resources by following these steps:

1. run `htop`.
1. Press "F6".
1. Select "PERCENT_MEM" and hit Enter.
1. Press "Shift+H".

For example MySQL could cache quite some memory overtime. You can release the by MySQL cached memory by restarting MySQL with `hypernode-servicectl restart mysql`.

### Varnish

You could experience a 502 error due to a misconfiguration of Varnish. For example

- Have you configured Varnish caching in the backend? Check if Varnish is enabled on the Hypernode: `hypernode-systemctl settings varnish_enabled`
  this should return `true`.
  If not, enable Varnish: `hypernode-systemctl settings varnish_enabled true`
- Is [HMV](../nginx/hypernode-managed-vhosts.md) enabled? Check if Varnish is enabled for the vhost:
  `hypernode-manage-vhosts --all`
  If not, enable Varnish for the vhost:`hypernode-manage-vhosts example.com --varnish`
- Or if you've just disabled Varnish in the backend, make sure to disable Varnish for the vhosts as well:
  `hypernode-manage-vhosts example.com --disable-varnish`

### Low Level PHP Errors (SEGFAULT)

In very rare cases, PHP might crash for other reasons than memory depletion (a so called “SEGFAULT”). If this happens, the server process will automatically be restarted in a few seconds. A segfault is a bug in the PHP process itself (not in the PHP code). So there isn't a programming error, but the code that has been processes by PHP which will crash eventually. Check if you've changed something recently. Think for example about installing any new modules, test what effects disabling this module has.

If you encounter this often (verify with `/var/log/php-fpm/php-fpm.log`), it will likely help to switch PHP versions (e.g. from PHP 5.6 to 7) or disable IonCube. If this won't work you should consider using a tool like NewRelic to track down the bottleneck.
