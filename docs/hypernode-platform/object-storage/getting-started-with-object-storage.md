---
myst:
  html_meta:
    description: Getting started with Object Storage
    title: Hypernode Object Storage | Getting Started
redirect_from:
  - /en/hypernode/object-storage/getting-started-with-object-storage/
---

# What is Hypernode Object Storage?

Hypernode Object Storage provides an option to store media files, assets, backups, documents, etc in a persistent, remote storage container.

Object storage eliminates redundancy and provides a centralized, scalable solution for storing application assets, session data, and backups.

By default, media files are stored in the same filesystem that contains the application. This is inefficient for complex, multi-server configurations, and can result in degraded performance when sharing resources.

With Object Storage you get:

- Effortless Data Sharing – Seamless access across all Hypernodes
- Full Access Control & Security – Secure and manage your data with ease
- Safe Backup & Monitoring – Ensure reliability with built-in insights

# Getting started with Object Storage

## CLI option

```console
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

```console
app@testhypernode ~ # hypernode-object-storage info

+--------------------------------------+--------------+--------+------------+----------------+---------------+---------------+
|                 UUID                 |     Name     |  Plan  | Hypernodes | Management URL |   Access Key  |   Secret Key  |
+--------------------------------------+--------------+--------+------------+----------------+---------------+---------------+
| d8770125-6c90-4770-b00f-1716f699990a | test-storage | OS50GB | testnode12 | **sensitive**  | **sensitive** | **sensitive** |
+--------------------------------------+--------------+--------+------------+----------------+---------------+---------------+
```

You can use the credentials and the URL now to configure remote storage for your application with the help of [this document](../../ecommerce-applications/magento-2/how-to-configure-remote-storage-for-magento-2-x.md).

### Cancel/Delete object storage

1. To cancel an Object storage, you can ssh into the Hypernode that is linked to that object storage.
1. Run `hypernode-object-storage cancel`

Note: The cancellation will be in effect from the end of the month.
Also if you change your mind or forgot to pull some data. It will still be available for 7 days after the cancellation. You can always reach out to the support team for help if that happens.

## UI option - Control Panel

Coming soon
