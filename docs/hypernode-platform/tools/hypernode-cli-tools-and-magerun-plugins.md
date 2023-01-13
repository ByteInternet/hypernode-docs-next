---
myst:
  html_meta:
    description: 'Hypernode provides many tools to make your life as a developer easier.
      Get a look on all tools available on Hypernode. '
    title: How to Hypernode CLI tools and Magerun plugins?
redirect_from:
  - /en/hypernode/tools/hypernode-cli-tools-and-magerun-plugins/
  - /knowledgebase/hypernode-cli-tools-magerun-plugins/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/hypernode-cli-tools-and-magerun-plugins/ -->

# Hypernode CLI Tools and Magerun Plugins

We provide many tools to make your life as a developer easier. We’ve been asked several times to provide a list with tools. This page is an overview of all tools available on Hypernodes.

## Hypernode-systemctl CLI Tool

The hypernode-systemctl tool allows you to set certain values for your Hypernode via the command line interface. The hypernode-systemctl tool saves valuable time and makes developing and maintaining a Magento shop even more easy. You can change settings via the systemctl CLI tool like:

- Change PHP version
- Enable Ioncube
- Enable Blackfire
- Enable Varnish
- Enable OpenVPN for secure database connections
- Password authentication
- Firewall block
- Safer SSL and SSH configuration

Details can be found in [a separate article about the hypernode-systemctl tool](../tools/how-to-use-the-hypernode-systemctl-cli-tool.md).

## Command Line Utilities

### hypernode-ftp

Tool to create FTP users and credentials

*More info can be found in*\*[the article about how to manage ftp users](../ftp/how-to-configure-ftp-sftp-on-hypernode.md).\*

### hypernode-parse-nginx-log

Parse the json based Nginx access logging and filter specific fields.

*More info can be found in [the article about working with logs](../nginx/how-to-find-the-the-top-10-visitors-by-parsing-the-nginx-access-logs.md).*

### hypernode-cron-flockerizr

Converts your cron file entries to make use of flock.

*More information about how to use flock can be found in [the article about periodic tasks](how-to-use-periodic-tasks-cronjobs-on-hypernode.md).*

### hypernode-fpm-slow-modules

Detects Magento extensions that slow down the shop by parsing the /var/log/php-fpm/php-slow.log

*More info about how to detect slow extensions can be found in*[*the article about interpreting the php-slow-log.*](../../troubleshooting/performance/how-to-spot-slow-extensions-using-the-php-slow-logs.md)

### hypernode-image-optimizer

This tool provides a very easy way of optimizing images to improve performance and save diskspace.

*More information about how to optimize your images can be found*\*[in the documentation about the hypernode-image-optimizer](../../best-practices/performance/how-to-optimize-your-images.md).\*

### hypernode-fpm-status

Prints the current worker status per FPM worker on your screen.

### hypernode-servicectl

As an app user you have the capability of restarting or reloading a select number of services like MySQL, Nginx, php7.1-fpm, Redis, RabbitMQ and Varnish. The command is hypernode-servicectl and it takes an action (restart or reload) and a service (Nginx, php7.1-fpm, etc) as arguments. This can be useful to resolve some user space issues.

The command can be executed as hypernode-servicectl or /usr/bin/hypernode-servicectl. The help menu displays the available options.

```
$ hypernode-servicectl --help
usage: hypernode-servicectl [-h] [--version] [action] [service [service ...]]

Control Hypernode services

positional arguments:
  action      desired action on services (restart|reload)
  service     target service, (mysql|nginx|php7.1-fpm)

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
```

More information on this handy command can be found in this [Hypernode Changelog](https://changelog.hypernode.com/release-5070-new-hypernode-servicectl-utility-restart-services-app-user/) and the one dedicated to [restarting Redis](https://changelog.hypernode.com/release-5840-hypernode-servicectl-can-also-restart-redis/).

### hypernode-importer

The hypernode-importer is a neat tool to fully automagically import your site on a Hypernode.

It can be used to either create a copy of your shop on the Hypernode, or copy your site to a Hypernode Docker.

\*To find more information about how to migrate your Magento to Hypernode, check the [documentation about the hypernode-importer](how-to-migrate-your-shop-to-hypernode.md).

### hypernode-postsuper

This tool enables an app user to delete mail from the mailqueue. On Hypernode we have email policies. If the volume of emails to send is higher than the number of emails being processed for delivery, the queue grows larger and this may consume considerable disk space. With hypernode-postsuper you can clear items from the mail queue.

You can find all available Hypernode commandline tools on the node itself as well, using autocompletion by typing hypernode-

## Provided Bash Aliases to Make Things Easier on the Command Line

### tal (alias for tail -f /var/log/nginx/access.log)

A shortcut to quickly take a realtime look at the access log.

### pnl and parse-nginx-log (alias for hypernode-parse-nginx-log)

Convert Hypernode logging in JSON to a human readable format and filter specific fields.

### pdstatus

Retrieves status.php on the Hypernode.

This script is used for server monitoring and returnes OK when PHP, MySQL, Nginx, OPcache, Redis, Varnish and the disk storage are functioning well.

### cputop

cputop creates a top 10 of most CPU consuming processes on the Hypernode

### livefpm (alias for hypernode-fpm-status)

Creates a real-time overview of the current FPM worker status

### editor

Is an alias to sensible-editor.

This way if you use editor <file> for editing your files, the editor defined in ~/.selected_editor is executed instead of the system wide default editor nano.

## Hypernode Magerun Plugins (Magento 1.x Only)

Hypernode provides several plugins for n98-magerun.

Below you can find a list of all the magerun plugins we created and how to use them.

### hypernode:performance – Generate a performance report based on sitemaps.

This plugin provides a great method to analyze all pages defined in sitemap.xml.

It generates a report of all pages load times, status code and time to first byte.

You can use it as well to analyze differences between a live and a staging environment or calculate the speed gains when moving to Hypernode.

When comparing load times on two sites, a graph report can be generated and downloaded after processing al sitemap links.

### hypernode:patches:list – Determine required patches.

This plugins lists all SUPEE security patches that are required for the version of your Magento installation and checks whether they are applied or not.

The command n98-magerun hypernode:patches:list is a shortcut that provides the same output.

### hypernode:modules:list-updates – Find available updates for installed modules

This plugin lists all installed Magento extensions and their current and available versions, making it very easy to determine which extensions should be updated.

A complete list of all available Magerun commands can be acquired by typing n98-magerun --help

### hypernode:log-analyses – Output the most frequent lines in system.log

This plugin provides a list of recurring log errors that are frequently logged to system.log and their count.

### hypernode:maps-generate – Generates magerun maps for Nginx by store config

This plugin can generate a http.magerunmaps based on your storefront configuration in Magento.

If you have many storefronts this plugin is a lifesaver!

### hypernode:varnish:config-save – Save and apply Turpentine’s VCL configuration to Varnish

This plugin saves your vcl to disk and stores it for later use.

### hypernode:varnish:flush – Flushes all cached Varnish URL’s.

This plugin connects to the Varnish daemon to flush the cache.

### hypernode:crack:admin-passwords – Attempt to crack admin credentials

Test the passwords of your users by using rainbow tables and dictionary lists to detect insecure, weak or otherwise easy to bruteforce passwords yourself before hackers do.

### hypernode:crack:api-keys – Attempt to crack API keys for SOAP / XML-RPC users

Test your API keys for weak and / or insecure combinations.
