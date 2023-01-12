---
myst:
  html_meta:
    description: 'The hypernode-systemctl tool allows you to set certain values for
      your Hypernode via the CLI. Learn how to use hypernode-systemctl CLI Tool. '
    title: How to use the hypernode-systemctl CLI Tool?
redirect_from:
  - /en/hypernode/tools/how-to-use-the-hypernode-systemctl-cli-tool/
  - /knowledgebase/hypernode-systemctl-cli-tool/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-use-the-hypernode-systemctl-cli-tool/ -->

# How to Use the hypernode-systemctl CLI Tool

The `hypernode-systemctl` tool allows you to set certain values for your Hypernode via the command line interface. In the past we asked you to contact support or to go to your Service Panel or Control Panel to change a setting. The `hypernode-systemctl` tool saves valuable time and makes developing and maintaining a Magento shop even more easier.

## Which Settings Can Be Changed on Your Hypernode?

To see which values you can set and which values they are allowed to have take a look at [our API docs](https://community.hypernode.io/#/Documentation/hypernode-api/settings/README). You can list all available options and the values that can be set by running:

`hypernode-systemctl settings --help`

- `blackfire_enabled`: a great tool to find performance bottlenecks in Magento
- `blackfire_server_token`
- `blackfire_server_id`
- `disable_optimizer_switch`
- `elasticsearch_enabled`: Enable Elasticsearch
- `elasticsearch_version`: Change the Elasticsearch version
- `enable_ioncube`: Only enable this if you really have to, as Ioncube is a performance killer
- `firewall_block_ftp_enabled`: indicates whether FTP (which is unsafe) is completely blocked or not
- `mailhog_enabled`: Enable the Mailhog feature
- `managed_vhosts_enabled`: Enable the managed_vhosts nginx configuration
- `modern_ssh_config_enabled`
- `modern_ssl_config_enabled`: Safer SSL and SSH configuration: you can configure Mozilla Modern SSL and enable stricter SSH encryption
- `mysql_version`: Change the MySQL version (note: once set to 5.7 this can't be reverted)
- `mysql_disable_stopwords`
- `mysql_tmp_on_data_enabled`
- `mysql_ft_min_word_len`
- `mysql_enable_large_thread_stack`
- `openvpn_enabled`: Enables [OpenVPN](https://community.hypernode.io/#/Documentation/hypernode-vpn/README?) for secure database connections
- `override_sendmail_return_path`: Override the return-path (Due to the bug in Magento 2)
- `password_auth`: indicates whether password authentication for the Hypernode is allowed instead of only SSH keys.
- `permissive_memory_management`: Configure [memory management policy](https://changelog.hypernode.com/release-5946-configurable-memory-management-policy-and-rss-bruteforce-detection/) (OOM kills)
- `php_version`: Change the PHP version
- `php_apcu_enabled`: Enable the PHP-apcu
- `redis_persistent_instance`
- `rabbitmq_enabled`: a popular open source message broker
- `supervisor_enabled`
- `unixodbc_enabled`
- `varnish_enabled`: Enable Varnish
- `varnish_version`
- `varnish_secret`
- `varnish_esi_ignore_https`

### Checking a Value for a Setting

To see which value a setting has you can run the following:

`hypernode-systemctl settings php_version`

### Setting a Value for a Setting

To set a setting to a certain value you can run the following:

`hypernode-systemctl settings php_version 7.1`

If an invalid value is provided you will be notified of this during the setting procedure.

## Options Explained

### Blackfire

- `blackfire_enabled`Indicates whether Blackfire is enabled. Check out [this article](../../best-practices/performance/how-to-use-blackfire-on-hypernode-to-find-performance-issues.md) on how to set up Blackfire.
- `blackfire_server_token`The BlackFire server token for your Blackfire setup.
- `blackfire_server_id` The BlackFire server ID for your Blackfire setup.

### Disable optimizer switch

Indicates whether `use_index_extensions` and `mrr` are turned off. If turned off this can improve performance due to an issue in PHP 5.6 related to Multi-Range Read Optimization. For more information about this setting see this [changelog](https://changelog.hypernode.com/release-5340-block-ftp-access-sftp-used-systems-tweaks/).

### Elasticsearch

- `elasticsearch_enabled`: Enable Elasticsearch
- `elasticsearch_version`: Change the Elasticsearch version

### Enabled IonCube

This options allows you to enable IonCube if needed. Note: IonCube is a huge performance killer, so only enable it if you really need it!

### Firewall block FTP

Indicates whether FTP is completely blocked or not in favour of SFTP. For more information about this setting see this [changelog](https://changelog.hypernode.com/release-5340-block-ftp-access-sftp-used-systems-tweaks/).

### Mailhog

This options enables Mailhog. Mailhog is an email testing tool for developers. Check our [documentation](../../hypernode-platform/tools/how-to-use-mailhog-on-hypernode.md) for a more detailed explanation about Mailhog on Hypernode.

### Managed Vhosts

Eanble the Hypernode Managed Vhosts option to setup the Hypernode with a specific Nginx config which allows you to setup multiple domain names with their own independent Nginx configuration. See our [documentation](../nginx/hypernode-managed-vhosts.md) for more information.

### Modern SSH config enabled

Indicates whether this node will have a stricter set of SSH encryption algorithms enabled. See [this changelog](https://changelog.hypernode.com/release-5139-stricter-ssh-encryption-algorithms/) for more information about this setting.

### Modern SSL config enabled

Indicates whether this node will have the Mozilla Modern SSL configuration configured. This provides a higher level of security but loses compatibility with some browsers. For more information about this setting see [this changelog](https://changelog.hypernode.com/release-4582-updated-configurable-ssl-ciphers/).

### MySQL

- `mysql_version`: Change the MySQL version (note, once set to 5.7 this can't be reverted)
- `mysql_disable_stopwords`

This setting makes it possible to disable the built-in stopword file for MyISAM search indexes. Read the [changelog](https://changelog.hypernode.com/release-6079-opt-in-disable-stopwords-for-myisam-search-indexes/) for more information.

- `mysql_ft_min_word_len`

This setting will make it possible to configure the ft_min_word_len for MySQL. The ft_min_word_len is the minimum length of the word to be included in a MyISAM FULLTEXT index. So, if you sell things in your Magento shop like **wol** or a **sok**, you can now change this setting from the default value of 4 to the smaller value 2.

- `mysql_tmp_on_data_enabled`

Indicates whether the MySQL tmp directory is located in the `/data/` directory of the `app` user or in the `/tmp/` directory of the `root` user. The `root` user does not have the same amount of space available as the `app` user, so enabling this might prevent MySQL from taking up all disk space at the cost of taking of the space of the `app` user. Mostly useful for large shops who create a lot of temporary tables with MySQL. For more information about this settings see [this changelog](https://changelog.hypernode.com/release-5133-configurable-mysql-temporary-directory-extra-space/).

- `mysql_enable_large_thread_stack`

This option allows you to use a larger MySQL thread_stack from 192K to 512K. Check our [changelog](https://changelog.hypernode.com/release-7083-opt-in-large-mysql-thread_stack/) for more information.

### Open VPN enabled

Our Hypernode-vpn solution implements a standard OpenVPN TLS tunnel to the Hypernode. Which can be used to talk to the MySQL database securely. You simply enable OpenVPN on your Hypernode and all the required packages and configuration are installed automatically. The automation will generate a default user configuration which you can use to connect to the Hypernode.

### Override sendmail return-path

Indicates if this node has a return-path set. When you send emails from your Magento shop with no return-path set, the return-path will default to noreply@hypernode.io. This email address may be recognised as a spam address by spam filters, as it is a very generic email used on all Hypernodes without same email configuration.

Check out [this article](../../ecommerce-applications/magento-2/how-to-set-the-return-path-for-a-magento-2-shop.md) for more information.

### Password Auth

Indicates whether password authentication for the node is allowed instead of only SSH keys. By default this option is `True`. Set this option to `False` if you prefer to login with SSH-keys

### Permissive Memory Management

Configure the OOM-killer to be permissive of short term memory usage, allowing memory hungry processes to run without executing overly drastic measures. For more information see our [documentation](../../troubleshooting/performance/how-to-debug-out-of-memory-oom-events.md).

### PHP

- `php_version`: Change the PHP version
- `php_apcu_enabled`: Enable the PHP-apcu.

### Redis persistent instance

Enable this feature to start another Redis instance for sessions instead of caching. Please note that this might require some changes on your end. For more information about this setting see [this changelog](https://changelog.hypernode.com/experimental-changes-redis-sessions-aws-performance/).

### RabbitMQ Enabled

This options enables RabbitMQ which allows you to run tasks in the background. RabbitMQ is message-queueing software where queues can be defined. Applications can connect to the queue and transfer a message onto it. This way you can (for example) import many products into Magento without having to wait a substantial time until the process is finished. The import takes place in the background. Check our [documentation](../../best-practices/database/how-to-run-rabbitmq-on-hypernode.md) for more information.

### Supervisor Enabled

This option allows you to use Supervisor. Supervisor allows you to use programs that need to run all the time on your Hypernode. These (usually long running) programs should not fail if there is an error. To accomplish this Supervisor watches your programs and restarts them if they might fail. Supervisor works great for use cases where a web hook or metrics always needs to run. See the [changelog](https://changelog.hypernode.com/release-6892-supervisord-support/) for more information on Supervisor.

### UnixODBC

Enable this option to install the necessary drivers for unixODBC to be able to run.

### Varnish

- `varnish_enabled`: Enable Varnish
- `varnish_version`: Allows you to change the version
- `varnish_secret`
- `varnish_esi_ignore_https`

By setting the `+esi_ignore_https` flag, Varnish will treat HTTPS as HTTP in `<esi:include />` blocks, thereby allowing ESI calls to pass through. However, because these calls are unencrypted and ESI is commonly used to cache information pertaining to authenticated users, it is recommended to only use ESI includes with resources on localhost. If you also want to enable this setting for an already existing Hypernode, please contact support.

Please refer to the [issue](https://github.com/magento/magento2/issues/3897) on the official Magento 2 GitHub repository for more information related to ESI on Magento 2 with Varnish caching enabled.

## Use the hypernode-systemctl Tool to Whitelist IP’s

Besides changing settings, the hypernode-systemctl tool also allows you to whitelist certain IP's for certain purposes. To find out which values are allowed to be set see [our API documentation](https://community.hypernode.io/#/Documentation/hypernode-api/whitelisting/README). Or run the following command:

`hypernode-systemctl whitelist --help`

This tool works with the same whitelists (FTP, WAF and external database) as the Service and Control Panel. So if you would whitelist a certain IP through the hypernode-systemctl tool, it would then also show in the Service and Control Panel and vice versa. You can use the two tools interchangeably.

### Seeing Your Current Whitelists

To see which whitelists are currently set you can run the following:

`hypernode-systemctl whitelist get`

You will see all IP's whitelisted per type (external database access, FTP and WAF).

If you want to specify a specific whitelist you can run the following:

`hypernode-systemctl whitelist get database`

### Adding to Whitelist

To add more values to your whitelists you can run the following. Please note that descriptions are optional:

`hypernode-systemctl whitelist add "database, waf or ftp" 1.2.3.4 --description "my description"`

### Removing From Whitelist

To remove values from your whitelists you can run the following:

`hypernode-systemctl whitelist remove database 1.2.3.4`

## Hypernode-systemctl bash-completion

The command `hypernode-systemctl` supports bash-completion for easier navigation through the many options this command offers. Simply type the command and press tab to see the available subcommands you can use.
