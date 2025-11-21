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

| Field                                                                                                                                                           | Default Value | Possible Values                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **blackfire_enabled**<br/><sub>A great tool to find performance bottlenecks<br />in Magento</sub>                                                               | False         | True, False                                                                                                                                 |
| **composer_version**<br/><sub>Change the Composer version</sub>                                                                                                 | 2.x           | 1.x, 2.2, 2.6, 2.7, 2.x                                                                                                                     |
| **disable_optimizer_switch**<br/><sub>Disable the optimizer switch</sub>                                                                                        | False         | True, False                                                                                                                                 |
| **elasticsearch_enabled**<br/><sub>Enable Elasticsearch</sub>                                                                                                   | False         | True, False                                                                                                                                 |
| **elasticsearch_version**<br/><sub>Change the Elasticsearch version</sub>                                                                                       | 7.x           | 5.2, 6.x, 7.x                                                                                                                               |
| **enable_ioncube**<br/><sub>Only enable this if you really have to,<br />as Ioncube is a performance killer</sub>                                               | False         | True, False                                                                                                                                 |
| **firewall_block_ftp_enabled**<br/><sub>Indicates whether FTP (which is unsafe) is completely blocked or not</sub>                                              | False         | True, False                                                                                                                                 |
| **magerun2_version**<br/><sub>Change the N98 Magerun version</sub>                                                                                              | latest        | 3.x, 4.x, 5.x, 6.x, 7.x, latest                                                                                                             |
| **mailhog_enabled**<br/><sub>Enable the Mailhog feature</sub>                                                                                                   | False         | True, False                                                                                                                                 |
| **modern_ssh_config_enabled**<br/><sub>Enable modern SSH configuration</sub>                                                                                    | False         | True, False                                                                                                                                 |
| **modern_ssl_config_enabled**<br/><sub>Safer SSL and SSH configuration:<br />you can configure Mozilla Modern SSL and enable<br />stricter SSH encryption</sub> | False         | True, False                                                                                                                                 |
| **mysql_disable_stopwords**<br/><sub>Disable MySQL stopwords</sub>                                                                                              | False         | True, False                                                                                                                                 |
| **mysql_enable_explicit_defaults_for_timestamp**<br/><sub></sub>                                                                                                | False         | True, False                                                                                                                                 |
| **mysql_enable_large_thread_stack**<br/><sub>Enable large thread stacks in MySQL</sub>                                                                          | False         | True, False                                                                                                                                 |
| **mysql_ft_min_word_len**<br/><sub>Set minimum word length for MySQL full-text searches</sub>                                                                   | 4             | 4, 2                                                                                                                                        |
| **mysql_long_query_time**<br/><sub></sub>                                                                                                                       | 2             | 2, 5, 10, 15, 30                                                                                                                            |
| **mysql_tmp_on_data_enabled**<br/><sub>Enable temporary data directory on MySQL</sub>                                                                           | False         | True, False                                                                                                                                 |
| **mysql_version**<br/><sub>Change the MySQL version (note: once set to 5.7 this can't be<br />reverted)</sub>                                                   | 5.7           | 5.6, 5.7, 8.0, 8.4                                                                                                                          |
| **new_relic_browser_monitoring_auto_instrument_enabled**<br/><sub></sub>                                                                                        | True          | True, False                                                                                                                                 |
| **new_relic_distributed_tracing_enabled**<br/><sub></sub>                                                                                                       | True          | True, False                                                                                                                                 |
| **new_relic_enabled**<br/><sub></sub>                                                                                                                           | False         | True, False                                                                                                                                 |
| **nodejs_version**<br/><sub>Change the Node version</sub>                                                                                                       | 22            | 6, 10, 16, 18, 20, 22                                                                                                                       |
| **opensearch_auto_create_index**<br/><sub></sub>                                                                                                                | True          | True, False                                                                                                                                 |
| **opensearch_enabled**<br/><sub>Enable OpenSearch</sub>                                                                                                         | True          | True, False                                                                                                                                 |
| **opensearch_version**<br/><sub>Change the OpenSearch version</sub>                                                                                             | 2.12          | 1.x, 2.6, 2.12                                                                                                                              |
| **openvpn_enabled**<br/><sub>Enables OpenVPN for secure database connections</sub>                                                                              | False         | True, False                                                                                                                                 |
| **password_auth**<br/><sub>Indicates whether password authentication for the Hypernode is<br />allowed instead of only SSH keys</sub>                           | True          | True, False                                                                                                                                 |
| **permissive_memory_management**<br/><sub>Configure memory management policy (OOM kills)</sub>                                                                  | False         | True, False                                                                                                                                 |
| **php_amqp_enabled**<br/><sub>Enable the php-amqp module</sub>                                                                                                  | False         | True, False                                                                                                                                 |
| **php_apcu_enabled**<br/><sub>Enable the php-apcu module</sub>                                                                                                  | True          | True, False                                                                                                                                 |
| **php_legacy_serialize_precision_enabled**<br/><sub></sub>                                                                                                      | True          | True, False                                                                                                                                 |
| **php_version**<br/><sub>Change the PHP version</sub>                                                                                                           | 8.3           | 5.6, 7.0, 7.1, 7.2, 7.3, 7.4, 8.0, 8.1, 8.2, 8.3, 8.4                                                                                       |
| **php_xdebug_enabled**<br/><sub>Enable Xdebug for remote debugging</sub>                                                                                        | False         | True, False                                                                                                                                 |
| **phpmyadmin_enabled**<br/><sub>Enable PHPMyAdmin</sub>                                                                                                         | False         | True, False                                                                                                                                 |
| **rabbitmq_delayed_message_exchange_enabled**<br/><sub></sub>                                                                                                   | False         | True, False                                                                                                                                 |
| **rabbitmq_enabled**<br/><sub>A popular open source message broker</sub>                                                                                        | False         | True, False                                                                                                                                 |
| **redis_eviction_policy**<br/><sub></sub>                                                                                                                       | volatile-lru  | noeviction<br />allkeys-lru<br />allkeys-lfu<br />volatile-lru<br />volatile-lfu<br />allkeys-random<br />volatile-random<br />volatile-ttl |
| **redis_persistent_eviction_policy**<br/><sub></sub>                                                                                                            | allkeys-lru   | noeviction<br />allkeys-lru<br />allkeys-lfu<br />volatile-lru<br />volatile-lfu<br />allkeys-random<br />volatile-random<br />volatile-ttl |
| **redis_persistent_instance**<br/><sub>Enable Redis persistent instance</sub>                                                                                   | False         | True, False                                                                                                                                 |
| **redis_version**<br/><sub>Change the Redis version</sub>                                                                                                       | 7.x           | 5.0, 6.x, 7.x                                                                                                                               |
| **supervisor_enabled**<br/><sub>Enable Supervisor</sub>                                                                                                         | False         | True, False                                                                                                                                 |
| **support_insecure_legacy_tls**<br/><sub></sub>                                                                                                                 | False         | True, False                                                                                                                                 |
| **tideways_enabled**<br/><sub>Enable Tideways</sub>                                                                                                             | False         | True, False                                                                                                                                 |
| **unixodbc_enabled**<br/><sub>Enable UnixODBC</sub>                                                                                                             | False         | True, False                                                                                                                                 |
| **varnish_enabled**<br/><sub>Enable Varnish</sub>                                                                                                               | False         | True, False                                                                                                                                 |
| **varnish_esi_ignore_https**<br/><sub>Ignore HTTPS for Varnish ESI</sub>                                                                                        | True          | True, False                                                                                                                                 |
| **varnish_http_resp_hdr_len**<br/><sub></sub>                                                                                                                   | None          | 4k, 8k, 16k, 32k, 64k, 128k, 256k                                                                                                           |
| **varnish_http_resp_size**<br/><sub></sub>                                                                                                                      | None          | 4k, 8k, 16k, 32k, 64k, 128k, 256k                                                                                                           |
| **varnish_workspace_backend**<br/><sub></sub>                                                                                                                   | None          | 4k, 8k, 16k, 32k, 64k, 128k, 256k                                                                                                           |
| **varnish_large_thread_pool_stack**<br/><sub></sub>                                                                                                             | False         | True, False                                                                                                                                 |
| **varnish_version**<br/><sub>Change the Varnish version</sub>                                                                                                   | 7.x           | 4.0, 6.0, 7.x                                                                                                                               |
| **valkey_enabled**<br/><sub>Enable valkey</sub>                                                                                                                 | False         | True, False                                                                                                                                 |

### Checking a Value for a Setting

To see which value a setting has you can run the following:

`hypernode-systemctl settings php_version`

### Setting a Value for a Setting

To set a setting to a certain value you can run the following:

`hypernode-systemctl settings php_version 8.4`

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

### OpenSearch

- `opensearch_enabled`: Enable OpenSearch
- `opensearch_version`: Change the OpenSearch version

### Enabled IonCube

This options allows you to enable IonCube if needed. Note: IonCube is a huge performance killer, so only enable it if you really need it!

### Firewall block FTP

Indicates whether FTP is completely blocked or not in favour of SFTP. For more information about this setting see this [changelog](https://changelog.hypernode.com/release-5340-block-ftp-access-sftp-used-systems-tweaks/).

### Mailhog

This options enables Mailhog. Mailhog is an email testing tool for developers. Check our [documentation](../../hypernode-platform/tools/how-to-use-mailhog-on-hypernode.md) for a more detailed explanation about Mailhog on Hypernode.

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
