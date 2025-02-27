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

**Hypernode Object Storage**
```bash
something something?
```

**AWS S3**

```bash
bin/magento setup:config:set \
    --remote-storage-driver="aws-s3" \
    --remote-storage-bucket="my_bucket_name" \
    --remote-storage-region="my-aws-region" \
    --remote-storage-key="abcd1234" \
    --remote-storage-secret="abcd1234"
```

**Other S3 compatible providers**

If you're using a different provider than AWS S3, you need to specify the `--remote-storage-endpoint` option.

```bash
bin/magento setup:config:set \
    --remote-storage-driver="aws-s3" \
    --remote-storage-bucket="my_bucket_name" \
    --remote-storage-region="provider-region" \
    --remote-storage-key="abcd1234" \
    --remote-storage-secret="abcd1234" \
    --remote-storage-endpoint="https://my-s3-compatible.endpoint.com"
```

## Syncing the files

Instead of running (which is Magento's official way to do this):

```bash
bin/magento remote-storage:sync
```

you can run the following to really speed up the process:

```bash
hypernode-object-storage objects sync pub/media/ s3://my_bucket_name/media/
hypernode-object-storage objects sync var/import_export s3://my_bucket_name/import_export
```

`hypernode-object-storage objects sync` will run a sync process in the background for you,
and will tell you what the PID of that process is. With the PID you can run the following
command to check up on the progress of the sync: 

```bash
hypernode-object-storage objects show PID
```

Alternatively, you can run the `aws s3 sync` command directly:

```bash
aws s3 sync pub/media/ s3://my_bucket_name/media/
aws s3 sync var/import_export s3://my_bucket_name/import_export
```

In any case, that is much faster than Magento's built-in sync, because `aws s3 sync` uploads files concurrently.

## The storage flag file in the bucket

Magento's S3 implementation creates a test file called `storage.flag`, which is basically created to test if the connection works. So this is not a magic file to mark anything ([source](https://github.com/magento/magento2/blob/6f4805f82bb7511f72935daa493d48ebda3d9039/app/code/Magento/AwsS3/Driver/AwsS3.php#L104)).

## Serving assets from your S3 bucket

To start serving media assets from your S3 bucket, you need to make some adjustments to your nginx configuration. Luckily, `hypernode-manage-vhosts` does this for you! If you are using Hypernode's object storage solution, all you need to do is run the following for relevant vhosts:

```bash
hmv example.com --object-storage
```

In the case that you're using custom object storage, such as Amazon's S3, you will need to supply the bucket name and the bucket URL yourself:
```bash
hmv example.com --object-storage --object-storage-bucket mybucket --object-storage-url https://example_url.com
```

If you have previously set your own custom bucket name and URL, but have since switched to Hypernode's object storage solution, then you can use the `--object-storage-defaults` flag to force overwrite your values to Hypernode's default ones:

```bash
hmv example.com --object-storage --object-storage-defaults
```

Furthermore, if you're using Amazon S3 as your bucket, ensure that your S3 bucket policies are configured correctly, so that only `/media` is publicly readable. For example:

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

## Magento remote storage documentation

- [Configure Remote Storage](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/storage/remote-storage/remote-storage)
- [Configure AWS S3 bucket for remote storage](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/storage/remote-storage/remote-storage-aws-s3)
