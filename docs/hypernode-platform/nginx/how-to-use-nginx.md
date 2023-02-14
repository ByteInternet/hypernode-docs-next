---
myst:
  html_meta:
    description: 'At Hypernode we’ve taken great care to tweak the Nginx server for
      optimal performance and usability. Find out how to use Nginx. '
    title: How to use NGINX? | Hypernode
redirect_from:
  - /en/hypernode/nginx/how-to-use-nginx/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-use-nginx/ -->

# How to Use Nginx

One of the most significant differences between Hypernode and more traditional platforms is using Nginx (pronunciation: ‘Engine X’) over Apache. Nginx has much better performance than Apache, allowing us to serve your webshop to more visitors than Apache would.

## Magento Specific Nginx Configuration

As your Hypernode is designed from the ground up to host Magento, we’ve taken great care to tweak the Nginx server for optimal performance and usability. We’ve moved all the Magento-specific settings we’ve learned over the years, and the ones that Magento Inc. suggests and includes in its .htaccess file, into the main Nginx configuration. Then we added a layer of protection against malicious bots and hackers and a modern, JSON-based logging format.

## Extending Nginx Configuration

Nginx does not use `.htaccess` files as Apache does. This means that configuration previously done in `.htaccess` files now has to be done in a different format, explained in the Nginx documentation.

Custom configuration to Nginx can be made by placing files in the `/data/web/nginx` directory inside your home directory.

### Inclusion Order

The inclusion order of files in `/data/web/nginx` is as follows:

- Files starting with `http.` will be included in the `http {}` context block
- Files starting with `server.` will be included in the `server {}` context block
- Files starting with `staging.` will be included in the `staging {}` context block
- Files starting with `public.` will be included in the `public {}` context block

### Nginx Config Reloader

On Hypernode's we run a small daemon called the nginx-config-reloader.

This very lightweight Python daemon listens for file changes in `/data/web/nginx`. If a new configuration is added or the existing configuration is changed, this daemon picks up on the changes and copies all files to `/etc/nginx/app`.

When this is done, the daemon validates the Nginx configuration files for syntax correctness.

If the syntax is ok, the Nginx web service daemon will be reloaded. If the syntax is not ok, the errors will be written to `/data/web/nginx/nginx_error_output`, and the Nginx service will not be reloaded to avoid crashes due to syntax errors.

This way, an incorrect config will not take down your shop when the config reloads but will warn you instead. Additionally, you can adjust your Nginx config without the need for root privileges.

A syntax error in your configuration is far from perfect because when the Hypernode gets rebooted, the Nginx service will not come up because of the syntax errors.

Tips:

- After changing your Nginx configuration, always check for config errors in `/data/web/nginx/nginx_error_output`
- Your bash terminal will show a warning if the `nginx_error_output` file is present in `/data/web/nginx`
- If your config is incorrect, fix the errors immediately to avoid a broken configuration on reboot.

### Specific Configurations

Some typical scenarios are explained below:

- [How to block/allow IP-addresses in Nginx](how-to-block-allow-ip-addresses-in-nginx.md)
- [How to Protect Your Magento Store With a Password in Nginx](how-to-protect-your-magento-store-with-a-password-in-nginx.md)
- [How to Set the Server Name in Nginx](how-to-set-the-server-name-in-nginx.md)

More specific Nginx configurations can be found in [the category page about Nginx](../nginx.md).

## Modern Logging

Instead of using Apache or NCSA web servers' log format, we’ve opted to create our access logs in a powerful JSON format. The advantage of this format is that it makes the logs easier to parse automatically and easier to expand when we want to add more information without breaking existing tools. And speaking of tools, we’ve included a powerful log analyzer on your Hypernode, called `hypernode-parse-nginx-log`, or `pnl` for short. For more information, see our article on logfiles.

## Converting `.htaccess` Files to Nginx Configuration

When moving from a web server that is running [Apache](https://httpd.apache.org/), to a Hypernode, which is running [Nginx](https://nginx.org/en/), some adjustments are required to ensure your shop is functioning.

Where Apache uses `.htaccess` files per directory to instruct Apache, Nginx does not use them. As a result, all configurations in `.htaccess` files should be converted to Nginx configuration.

### Helper Tools to Convert Apache Configuration to Nginx Configuration

You can easily convert rewrites and other configurations from your `.htaccess` file to Nginx config by [using a converter tool](https://winginx.com/en/htaccess).

These tools are not entirely accurate but can convert many statements from your `.htaccess` to Nginx configuration.

Additionally, the Nginx website provides [some rules of thumb as well.](https://www.nginx.com/blog/converting-apache-to-nginx-rewrite-rules/)

### Find All `.htaccess` Files and Add Denied Directories to the Nginx Config

To find `.htaccess` files that deny access to custom directories, use the following command:

```nginx
find /data/web/public -type f -name .htaccess -exec grep -q 'Deny from all' {} \; -exec echo {} \;
```

This will list all `.htaccess` files that deny access. The ones from the Magento core are already blocked.

The locations that are not in the Magento core should be denied access to using Nginx configuration:

```nginx
location ~* "(/custom/location|/other/location|/third/custom/location)/?" {
    deny all;
}
```

**Because Nginx does not use .htaccess files like Apache, the configuration previously done in .htaccess files now has to be done in a different format, as explained in the**[**Nginx documentation**](http://nginx.org/en/docs/)**.**

Generally, you want rewrite rules if you have moved (parts of) your site to a different folder or URL.

The rewrite rules below should be added to a file called server.rewrites in the Nginx folder on your Hypernode server.

## Internal rewrites

They are used when you want to rewrite within the same domain. For example, to rewrite all URLs in the format of/invoice/345232.pdf to /invoice.php?id=345232, you would use this rewrite line:

```nginx
 rewrite ^/invoice/(\d+).pdf$ /invoice.php?id=$1 break;
```

This will handle the rewrite internally so it is transparent for browsers and search engines.

## External redirects

If you have moved content between domains or want to signal (for example, to search engines) that something has moved, you should use an external redirect.

For example, you want every URL starting with /fr to redirect to <http://yourshop.fr:>

```nginx
 rewrite ^/fr/(.*)$ http://yourshop.fr/$1 permanent;
```

This will also maintain subfolders and query strings (such as <http://yourshop.com/fr/subfolder?arguments>).

If the move is only temporary, you should use redirect instead of permanent.
