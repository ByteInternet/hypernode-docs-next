---
myst:
  html_meta:
    description: Configure remote storage for Magento 2.x. Learn how to configure
      Magento 2 to start storing files in your bucket using a single command.
    title: How to Configure Remote Storage for Magento 2.x | Hypernode
---

# How to Configure Remote Storage for Magento 2.x

Magento 2.x supports remote storage for media files, import/export files, and other files.
This feature allows you to store files in a remote storage location, such as an Amazon S3 bucket, instead of storing them on the server itself.

This can be useful for many reasons, such as:

- Offloading storage from your server, reducing the load on your server, and improving performance.
- Allows you to make use of [horizontal scaling](../../hypernode-platform/autoscaling/how-does-horizontal-autoscaling-work), as you can easily add more servers without having to worry about syncing files between them.
- Allows for effortless storage capacity scaling, as you can easily increase the storage capacity of your remote storage location.
- Serving assets from a CDN, which can improve the performance of your website.

## Configuring the application

Configuring Magento 2 to start storing files in your bucket is done using a single command.

Before configuring remote storage, make sure that the deprecated database media storage backend is disabled.

```bash
bin/magento setup:config:set system/media_storage_configuration/media_storage 0
```

**Hypernode Object Storage and other S3 compatible providers**

If you're using Hypernode Object Storage or a different provider than AWS S3, you need to specify the `--remote-storage-endpoint` option.

For Hypernode Object Storage, use `main` as the bucket name and `EU` as the region. You can retrieve the remaining parameters by running `hypernode-object-storage info --with-credentials`.

```console
app@abcdef-example-magweb-cml:~$ hypernode-object-storage info --with-credentials
+--------------------------------------+----------------+---------+-------------+-------------------------------------+---------------+---------------+
|                 UUID                 |      Name      |   Plan  |  Hypernodes |           Management URL            |   Access Key  |   Secret Key  |
+--------------------------------------+----------------+---------+-------------+-------------------------------------+---------------+---------------+
| 12345678-9012-3456-b7e3-19ab43df4a23 | testappbucket1 | OS200GB |   testapp   |  https://example.ams.objectstore.eu |   abcd1234    |   1234abcd    |
+--------------------------------------+----------------+---------+-------------+-------------------------------------+---------------+---------------+
```

If you're using a different object storage provider, replace these values with the relevant details from your provider.

```bash
bin/magento setup:config:set \
    --remote-storage-driver="aws-s3" \
    --remote-storage-bucket="main" \
    --remote-storage-region="EU" \
    --remote-storage-key="abcd1234" \
    --remote-storage-secret="1234abcd" \
    --remote-storage-endpoint="https://my-s3-compatible.endpoint.com"
```

Running the Magento object storage command may not include all necessary settings in the configuration.

If you're using Hypernode object storage, you need to add the following parameters to your env.php to complete the setup:

```php
'use_path_style_endpoint' => true,
'path_style' => true,
```

The complete and functional Magento configuration should resemble the following example:

```php
'remote_storage' => [
    'driver' => 'aws-s3',
    'config' => [
        'endpoint' => '',
        'bucket' => 'main',
        'region' => 'EU',
        'use_path_style_endpoint' => true,
        'path_style' => true,
        'credentials' => [
            'key' => '',
            'secret' => ''
        ]
    ]
],
```

**AWS S3**

If you're using an AWS S3 bucket, you only need your bucket name, AWS region, and access and secret keys.

```bash
bin/magento setup:config:set \
    --remote-storage-driver="aws-s3" \
    --remote-storage-bucket="my_bucket_name" \
    --remote-storage-region="my-aws-region" \
    --remote-storage-key="abcd1234" \
    --remote-storage-secret="1234abcd"
```

## Syncing the files (efficiently)

Magento provides an official method for syncing files using the following command (not recommended):

```bash
bin/magento remote-storage:sync
```

However, for better performance, you can use the following alternative:

```bash
hypernode-object-storage objects sync pub/media/ s3://my_bucket_name/media/
hypernode-object-storage objects sync var/import_export s3://my_bucket_name/import_export
```

The `hypernode-object-storage objects sync` command runs the sync process in the background
and provides the Process ID (PID). You can monitor the sync progress using:

```bash
hypernode-object-storage objects show PID
```

Alternatively, you can use the AWS CLI directly:

```bash
aws s3 sync pub/media/ s3://my_bucket_name/media/
aws s3 sync var/import_export s3://my_bucket_name/import_export
```

Both methods are significantly faster than Magento’s built-in sync, as aws s3 sync handles uploads concurrently.

```{tip}
More information about the `hypernode-object-storage` commands can be found in the [Object Storage documentation](../../hypernode-platform/object-storage.md).
```

## The storage flag file in the bucket

Magento's S3 implementation creates a test file called `storage.flag`, which is basically created to test if the connection works. So this is not a magic file to mark anything ([source](https://github.com/magento/magento2/blob/6f4805f82bb7511f72935daa493d48ebda3d9039/app/code/Magento/AwsS3/Driver/AwsS3.php#L104)).

## Serving assets from your S3 bucket

To serve media assets directly from your S3 bucket, you need to adjust your nginx configuration.
Fortunately, `hypernode-manage-vhosts` [simplifies this process for you](../../hypernode-platform/nginx/hypernode-managed-vhosts.md#object-storage-and-hypernode-managed-vhosts).

### Configuring Amazon S3 bucket policies

If you’re using Amazon S3, ensure that your S3 bucket policies are properly configured so that only the `/media` directory is publicly accessible. For example:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowPublicReadOnlyForMedia",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::<your-bucket-name>/media/*"
    }
  ]
}
```

## Remote storage tweaks module

After configuring remote storage for Magento 2, you might run into some slower pages in the admin product grid. This is caused by an inefficient image loading mechanism found in the Magento core code. For now we have written a Magento 2 module to fix this performance problem.

You can find the module on [GitHub](https://github.com/ByteInternet/magento2-remote-storage-tweaks/) and [Packagist](https://packagist.org/packages/hypernode/magento2-remote-storage-tweaks).

## Magento remote storage documentation

- [Configure Remote Storage](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/storage/remote-storage/remote-storage)
- [Configure AWS S3 bucket for remote storage](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/storage/remote-storage/remote-storage-aws-s3)
