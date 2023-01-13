---
myst:
  html_meta:
    description: 'The Control Panel offers an overview of your Hypernode’s statistics
      and settings. Read how these settings can easily be adjusted via the command
      line. '
    title: How to change your Hypernode settings | Control Panel
redirect_from:
  - /en/support/solutions/articles/48001155575-how-to-change-your-hypernode-settings/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001155575-how-to-change-your-hypernode-settings/ -->

# How to Change Your Hypernode Settings

The Control Panel offers an overview of your Hypernode’s statistics and settings. These settings can easily be adjusted via the command line. This article offers an in-depth explanation of these values.

## How to Change These Settings

The settings below can be configured through our hypernode-systemctl tool. The hypernode-systemctl tool allows you to set certain values for your Hypernode via the command line interface. In the past we asked you to contact support or to go to your Service Panel to change a setting. The hypernode-systemctl tool saves valuable time and makes developing and maintaining a Magento shop even more easier.

## The Settings in the Control Panel

### Uses floating IP

Whether your node has a dedicated IP.

### Open VPN enabled

Hypernode-vpn offers a secure way of directly connecting to your database.

### Redis persistent instance

Indicates whether another Redis instance will be started which can be used for sessions instead of caching. Please note that this might require some changes on your end. For more information about this setting see [this changelog](https://changelog.hypernode.com/experimental-changes-redis-sessions-aws-performance/).

### MySQL tmp on data

Indicates whether the MySQL tmp directory is located in the `/data/` directory of the `app` user or in the `/tmp/` directory of the `root` user. The `root` user does not have the same amount of space available as the `app` user, so enabling this might prevent MySQL from taking up all disk space at the cost of taking up the space of the `app` user. Mostly useful for large shops who create a lot of temporary tables with MySQL. For more information about this settings see [this changelog](https://changelog.hypernode.com/release-5133-configurable-mysql-temporary-directory-extra-space/).

### Blackfire enabled

Indicates whether Blackfire is enabled. Check out [this article](../../best-practices/performance/how-to-use-blackfire-on-hypernode-to-find-performance-issues.md) on how to set up Blackfire.

### Blackfire server token

The BlackFire server token for your Blackfire setup.

### Blackfire server ID

The BlackFire server ID for your Blackfire setup.

### Monitoring enabled

Whether monitoring is enabled. Development nodes are never monitored.

### ionCube enabled

Indicates whether this node should have the ionCube loader enabled.

### Varnish ESI ignore HTTPS

By setting the `+esi_ignore_https flag`, Varnish will treat HTTPS as HTTP in `<esi:include />` blocks, thereby allowing ESI calls to pass through. However, because these calls are unencrypted and ESI is commonly used to cache information pertaining to authenticated users, it is recommended to only use ESI includes with resources on localhost. If you also want to enable this setting for an already existing Hypernode, please contact support.

Please refer to the [issue](https://github.com/magento/magento2/issues/3897) on the official Magento 2 GitHub repository for more information related to ESI on Magento 2 with Varnish caching enabled.

### Firewall block FTP

Indicates whether FTP is completely blocked or not in favour of SFTP. For more information about this setting see [this changelog](https://changelog.hypernode.com/changelog/release-5340-block-ftp-access-sftp-used-systems-tweaks/).

### New Relic enabled

Indicates whether New Relic is enabled. Check out [this article](../../best-practices/performance/how-to-find-your-performance-bottleneck-with-new-relic.md) on how to set up New Relic.

### Modern SSH config enabled

Indicates whether this node will have a stricter set of SSH encryption algorithms enabled. See [this changelog](https://changelog.hypernode.com/release-5139-stricter-ssh-encryption-algorithms/) for more information about this setting.

### Modern SSL config enabled

Indicates whether this node will have the Mozilla Modern SSL configuration configured. This provides a higher level of security but loses compatibility with some browsers. For more information about this setting see [this changelog](https://changelog.hypernode.com/release-4582-updated-configurable-ssl-ciphers/).

### Override sendmail return-path

Indicates if this node has a return-path set. When you send emails from your Magento shop with no return-path set, the return-path will default to noreply@hypernode.io. This email address may be recognised as a spam address by spam filters, as it is a very generic email used on all Hypernodes without same email configuration.

Check out [this article](../../ecommerce-applications/magento-2/how-to-set-the-return-path-for-a-magento-2-shop.md) for more information.
