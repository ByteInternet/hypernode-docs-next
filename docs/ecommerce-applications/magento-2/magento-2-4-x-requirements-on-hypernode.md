---
myst:
  html_meta:
    description: Which PHP, MySQL, OpenSearch, Valkey, Varnish, nginx and Composer versions
      your Magento 2.4.x release needs, which Hypernode settings provide them, and which
      requirements are met and which are not yet available on Hypernode.
    title: Magento 2.4.x requirements | Hypernode Documentation
---

# Magento 2.4.x Requirements

Every Magento 2.4.x release pins the versions of the services around it: PHP, the database, the search engine, the cache backend, the full-page cache, the web server and Composer. [Adobe publishes exactly which combinations it tests](https://experienceleague.adobe.com/en/docs/commerce-operations/installation-guide/system-requirements), and tightens that list with every Magento patch release. Adobe supports only those combinations; if your versions do not match, Adobe Support may ask you to align your environment before investigating an issue.

This page maps the Adobe requirements for each supported 2.4.x release line to the settings you can change on your Hypernode, and shows per component whether each requirement is met or not yet available. The matrix reflects Adobe's requirements for the latest patch release of every line (October 13, 2026) and the Hypernode platform as of November 27, 2026.

```{note}
Adobe publishes separate requirement tables for Commerce on Cloud and for on-premises installations like Hypernode, where you manage the stack yourself through the [Hypernode settings](../../hypernode-platform/tools/how-to-use-the-hypernode-systemctl-cli-tool.md). All requirements on this page come from Adobe's on-premises tables.
```

## What Adobe requires and what Hypernode offers

For each release line, the table lists the versions Adobe names for the latest patch release. When Adobe lists multiple versions, any of them satisfies the requirement.

| Component          | Hypernode offers           | 2.4.4-p18      | 2.4.5-p17       | 2.4.6-p15       | 2.4.7-p10             | 2.4.8-p5     | 2.4.9       |
| ------------------ | -------------------------- | -------------- | --------------- | --------------- | --------------------- | ------------ | ----------- |
| PHP                | 8.1, 8.2, 8.3, 8.4, 8.5    | ✓ 8.1          | ✓ 8.1           | ✓ 8.2, 8.1      | ✓ 8.3, 8.2            | ✓ 8.4, 8.3   | ✓ 8.5       |
| Database           | MySQL 8.0, 8.4             | ✗ MariaDB 10.6 | ✗ MariaDB 10.11 | ✗ MariaDB 10.11 | ✗ MariaDB 10.11, 11.8 | ✓ MySQL 8.4  | ✓ MySQL 8.4 |
| Search             | 1.x, 2.6, 2.12, 2.19, 3.3  | ✓ 2.19         | ✓ 2.19          | ✓ 2.19, 3       | ✓ 2.19, 3             | ✓ 3 (3.3)    | ✓ 3 (3.3)   |
| Cache and sessions | Valkey 8.1                 | ✓ Redis 7.2    | ✓ Valkey 8.1    | ✓ Valkey 8.1    | ✓ Valkey 8.1          | ✓ Valkey 8.1 | ✗ Valkey 9  |
| Varnish            | 4.0, 6.0, 7.x              | ✓ 7.7          | ✗ 8             | ✗ 8             | ✗ 8                   | ✗ 8          | ✗ 8         |
| Composer           | 1.x, 2.2, 2.6 through 2.11 | ✓ 2.2.26+      | ✓ 2.2.26+       | ✓ 2.2.26+       | ✓ 2.10                | ✓ 2.10       | ✓ 2.10      |

✓ available on Hypernode and meets the requirement · ✗ not available on Hypernode. Details per component in the sections below.

```{note}
Adobe raised the requirements with the latest patch releases: nginx 1.30 and Varnish 8 appear in the current tables of every line (Varnish 7.7 for 2.4.4). At earlier patch levels of these lines, Adobe listed Varnish 7.x and nginx 1.22 through 1.28, and MySQL 8.0 up to 2.4.7-p9.
```

```{warning}
The platform defaults are PHP 8.3, OpenSearch 2.12, Varnish 7.x, Composer 2.x and Redis (Valkey disabled). Nodes installed since 2025 run MySQL 8.0 or newer. Check the settings on your node before an upgrade.
```

## Good to know

Items in progress appear in [changelog.hypernode.com](https://changelog.hypernode.com) when they land.

**Worth knowing:**

- In progress, without an ETA: Valkey 9 (required by 2.4.9), Varnish 8 and MariaDB (listed by Adobe for every line; Hypernode provides MySQL) are being worked on.

- Adobe lists exact PHP versions instead of a floor: 8.5 is validated only for 2.4.9, so run the PHP version Adobe lists for your release ([the PHP version documentation](../../hypernode-platform/php/supported-php-versions-and-how-to-change-them-on-hypernode.md)). PHP 8.1, required by 2.4.4 and 2.4.5, is past its upstream end of life (December 2025) but remains selectable.

- Changing `opensearch_version` deletes all search indexes: switch and reindex as part of the upgrade itself, and Elasticsearch can keep running until the upgrade window ([the OpenSearch documentation](../../hypernode-platform/tools/how-to-use-elasticsearch-on-hypernode.md)).

- Switching to Valkey is a drop-in swap: the Magento configuration stays the same and `redis-cli` keeps working through symlinks; Redis 7.x remains selectable through `redis_version` ([the Valkey documentation](../../hypernode-platform/tools/how-to-use-valkey-on-hypernode.md), [Redis configuration for Magento 2](how-to-configure-redis-for-magento-2.md)).

- Composer 2.2 through 2.11 are selectable; 2.11 satisfies every Composer requirement, including the 2.2.26+ floors ([the Composer documentation](../../hypernode-platform/tools/how-to-use-composer-2-on-your-hypernode.md)).

- nginx runs 1.22.1 as part of the managed platform image and has no setting; a newer nginx arrives automatically with a future platform update and, as far as we can assess, does not block 2.4.9.

- `rabbitmq_enabled` turns RabbitMQ on (on plans that support it); the version is not selectable, and a delayed message exchange plugin has its own toggle ([how to run RabbitMQ](../../best-practices/database/how-to-run-rabbitmq-on-hypernode.md)).
    - Adobe requires RabbitMQ 4.3 (or ActiveMQ Artemis 2) for 2.4.5 through 2.4.9, and RabbitMQ 3.9 or 3.13 for 2.4.4; ActiveMQ Artemis is not offered.
    - Enable it only for queue consumers (B2B, MediaGallery, async operations).
- Legacy engines remain selectable for older setups: Elasticsearch 5.2, 6.x and 7.x (8 is not offered; OpenSearch covers the same requirements).

(magento-2-4-x-database-note)=

## MySQL and MariaDB on Hypernode

MySQL 8.0 reached end of support in April 2026. Since then, Adobe no longer validates MySQL with 2.4.4, 2.4.5, 2.4.6 or 2.4.7: the current tables list MariaDB only for these lines, and Adobe recommends migrating to a compatible MariaDB version. Hypernode does not offer MariaDB as a managed database.

In practice this means:

- On Hypernode, stay on `mysql_version` 8.0 for 2.4.4, 2.4.5 and 2.4.6. MySQL 8.0 is the version Adobe validated for these lines before the end-of-support date.
- From 2.4.7 onwards, run `mysql_version` 8.4. Adobe pairs 2.4.7 with MariaDB 10.11 or 11.8 and no longer validates MySQL with it. Since MySQL 8.0 is past its end of support, 8.4 is the database for 2.4.7 and higher on Hypernode; for 2.4.8 and 2.4.9 it is also the version Adobe lists.
- Older MySQL versions (5.6, 5.7) do not meet any current requirement.

Getting to MySQL 8.4 for 2.4.7 and higher:

- The upgrade goes in steps: 5.7 first moves to 8.0, and only 8.0 moves to 8.4. Upgrading directly from 5.7 to 8.4 is not supported. Treat the 8.0 step as temporary: 8.0 and 5.7 no longer receive security updates.

- Before the switch to 8.4, every MySQL user must use the `caching_sha2_password` authentication plugin, otherwise the platform refuses the upgrade. Find the exceptions with:

    ```sql
    SELECT user, host, plugin FROM mysql.user WHERE plugin != 'caching_sha2_password';
    ```

    and convert them with:

    ```sql
    ALTER USER 'user'@'host' IDENTIFIED WITH caching_sha2_password BY '<password>';
    ```

- The switch briefly restarts MySQL. Take a snapshot right before, with the shop in maintenance mode, using `hypernode-systemctl create_backup`. Afterwards you can only roll back by restoring that snapshot: moving from 8.4 back to 8.0 is not possible.

The full procedure is in [how to use MySQL on Hypernode](../../hypernode-platform/mysql/how-to-use-mysql-on-hypernode.md).

## Recommended settings per release

If you are about to upgrade, set the stack for the release you are moving to before you start: the database first (the slowest change), then PHP. The commands are the same for every release, only the versions differ:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-systemctl settings php_version <php>
app@abcdef-example-magweb-cmbl:~$ hypernode-systemctl settings mysql_version <mysql>
app@abcdef-example-magweb-cmbl:~$ hypernode-systemctl settings opensearch_version <opensearch>
app@abcdef-example-magweb-cmbl:~$ hypernode-systemctl settings valkey_enabled true
app@abcdef-example-magweb-cmbl:~$ hypernode-systemctl settings composer_version <composer>
```

| Release | PHP (`php_version`) | MySQL (`mysql_version`) | OpenSearch (`opensearch_version`) | Composer (`composer_version`) |
| --- | --- | --- | --- | --- |
| 2.4.9 | 8.5 | 8.4 | 3.3 | 2.10 |
| 2.4.8-p5 | 8.4 | 8.4 | 3.3 | 2.10 |
| 2.4.7-p10 | 8.3 | 8.4 | 3.3 (2.19 also satisfies) | 2.10 |
| 2.4.6-p15 | 8.2 | 8.0 | 2.19 (3.3 also satisfies) | 2.2 |
| 2.4.5-p17 and 2.4.4-p18 | 8.1 | 8.0 | 2.19 | 2.2 |

- `valkey_enabled true` applies to every line.
- The commands do not cover Varnish and nginx: they stay on 7.x and 1.22.1, the newest versions Hypernode offers ([how to enable Varnish](../../hypernode-platform/varnish/how-to-enable-varnish-on-hypernode.md)).
- RabbitMQ has no command here either: enable it only when your shop uses queue consumers.
- For the database background on 2.4.4 through 2.4.7, see [the database note](magento-2-4-x-database-note).

## Before you upgrade

1. Try the upgrade on a test copy first: [Hypernode Brancher](../../hypernode-platform/tools/hypernode-brancher.md) creates a temporary copy of your Hypernode where you can change the stack and run the upgrade without touching the live shop (available on Falcon and Eagle plans). If it works there, the versions that are older than Adobe currently lists (Valkey 8.1, Varnish 7.x, nginx 1.22.1) also work for your shop.
2. Match the stack to your target release with the `hypernode-systemctl settings` commands above, starting with the database and PHP.
3. Check Adobe's requirements page close to your upgrade date; it changes with every Magento patch release.
4. Check [changelog.hypernode.com](https://changelog.hypernode.com) for the availability of Valkey 9, Varnish 8 and nginx 1.30.
5. Run the upgrade itself per [the Magento 2 upgrade guide](how-to-update-magento-2.md), and verify the versions afterwards: `php -v`, `mysql --version`, `composer --version`, and the cache backend in `app/etc/env.php`.

If a requirement you need is not available on Hypernode, contact our support team. We can go through your current stack and the upgrade you are planning with you.
