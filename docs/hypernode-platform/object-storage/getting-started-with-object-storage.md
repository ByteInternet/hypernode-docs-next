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

Object Storage eliminates redundancy and provides a centralized, scalable solution for storing application assets, session data, and backups.

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

Note: You can use one Object Storage across multiple Hypernodes. But you can only use one Object Storage space per Hypernode.

If you receive this error, please make sure to enable "Allow billing through CLI in the relevant Hypernode settings page"

```
You do not have permission to order Object Storage for this Hypernode. Please ask the Hypernode owner to enable 'Allow billing through the CLI' in the Control Panel settings or via the API
```

### Retrieve Object Storage

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

### Cancel/Delete Object Storage

1. To cancel an Object Storage, you can ssh into the Hypernode that is linked to that Object Storage.
1. Run `hypernode-object-storage cancel`

Note: The cancellation will be in effect from the end of the month.
Also if you change your mind or forgot to pull some data. It will still be available for 7 days after the cancellation. You can always reach out to the support team for help if that happens.
### Managing objects in object storage

You can manage your objects using the `hypernode-object-storage objects` subcommand.
It supports all common operations--listing, copying, moving, and deleting files--while also allowing you to sync files in the background and monitor the progress of an ongoing sync.

```console
app@testhypernode ~ # hypernode-object-storage objects --help
usage: hypernode-object-storage objects [-h] {sync,cp,ls,mv,rm,show} ...

Manage objects in object storage

positional arguments:
  {sync,cp,ls,mv,rm,show}
    sync                Synchronize files between a local directory and an object storage location
    cp                  Copy a file or object from one location to another
    ls                  List objects in an S3 bucket or folder
    mv                  Move or rename a file or object
    rm                  Delete an object from S3
    show                Display the current status of an ongoing sync process

options:
  -h, --help            show this help message and exit
```

It is important to note that `hypernode-object-storage objects` supports all optional flags available in `aws s3`, allowing you to customize its behavior for advanced configurations.

#### Syncing files and monitoring progress

Syncing files between your local directory and object storage is simple. Run the following command:

```console
app@testhypernode ~ # hypernode-object-storage objects sync /example/local/path/ s3://example/bucket/uri/
Syncing objects from /example/local/path/ to s3://example/bucket/uri/...
Sync process started with PID 1234 in the background.
```

The `sync` operation runs in the background, and you can monitor its progress by using the `show` command, for example:

```console
app@testhypernode ~ # hypernode-object-storage objects show 1234
Completed 9.7 GiB/~30.0 GiB (118.2 MiB/s) with ~5 file(s) remaining (calculating...)
```

If you run the `show` command after the sync operation has finished, you’ll see output like this:

```console
app@testhypernode ~ # hypernode-object-storage objects show 1234
Process 1234 does not exist anymore
```

## UI option - Control Panel

Coming soon
