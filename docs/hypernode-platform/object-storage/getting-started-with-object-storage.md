---
myst:
  html_meta:
    description: Getting started with Object Storage
    title: Hypernode Object Storage | Getting Started
redirect_from:
  - /en/hypernode/object-storage/getting-started-with-object-storage/
---

# What is Hypernode Object Storage?

Hypernode Object Storage provides an option to store media files in a persistent, remote storage container.

By default, media files are stored in the same filesystem that contains the application. This is inefficient for complex, multi-server configurations, and can result in degraded performance when sharing resources.

Object storage eliminates redundancy and provides a centralized, scalable solution for storing application assets, session data, and backups.

With Object Storage you get:

- Effortless Data Sharing – Seamless access across all Hypernodes
- Full Access Control & Security – Secure and manage your data with ease
- Safe Backup & Monitoring – Ensure reliability with built-in insights

# How to enable Object Storage and use it with your Hypernode?

## CLI option

```
hypernode-object-storage --help
```

### Creating a Hypernode Object Storage Workspace

1. SSH into your server.
1. Run `hypernode-object-storage create`
1. Fill in the prompts with a name and desired storage.
1. Confirm your order and give it a few minutes before your storage is ready.

Note: You can use one object storage across multiple Hypernodes. But you can only use one object storage space per Hypernode.

If you receive this error, please make sure to enable "Allow billing through CLI in the relevant Hypernode settings page"

```
You do not have permission to order object storage for this Hypernode. Please ask the Hypernode owner to enable 'Allow billing through the CLI' in the Control Panel settings or via the API
```

### Retrieve object storage

1. Run `hypernode-object-storage info`
1. If you want to retrieve your credentials for the workspace pass in the flag `--with-credentials`.

The output should look like this

```
app@hntesthehe ~ # hypernode-object-storage info

+--------------------------------------+--------------+--------+------------+----------------+---------------+---------------+
|                 UUID                 |     Name     |  Plan  | Hypernodes | Management URL |   Access Key  |   Secret Key  |
+--------------------------------------+--------------+--------+------------+----------------+---------------+---------------+
| fdb95093-6e5e-4cf7-a128-26e376ffb77b | hntesthehe14 | OS50GB | hntesthehe | **sensitive**  | **sensitive** | **sensitive** |
+--------------------------------------+--------------+--------+------------+----------------+---------------+---------------+
```

You can use the credentials and the URL now to configure remote storage for your application with the help of [this document](../../ecommerce-applications/magento-2/how-to-configure-remote-storage-for-magento-2-x.md).

## UI option - Control Panel

TBD
