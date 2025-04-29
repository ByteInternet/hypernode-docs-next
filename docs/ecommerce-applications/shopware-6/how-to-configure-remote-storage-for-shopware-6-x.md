---
myst:
  html_meta:
    description: Configure remote storage for Shopware 6.x. Learn how to configure
      Shopware 6 to start storing files in your bucket.
    title: How to Configure Remote Storage for Shopware 6.x | Hypernode
---

# How to Configure Remote Storage for Shopware 6.x

Shopware 6.x supports remote storage for different types of files, allowing you to store assets such as product images, documents, and other media in an external storage service instead of the local server.

Using remote object storage in Shopware 6 provides several benefits, including:

- Offloading storage from your server, reducing the load on your server, and improving performance.
- Allows you to make use of [horizontal scaling](../../hypernode-platform/autoscaling/how-does-horizontal-autoscaling-work), as you can easily add more servers without having to worry about syncing files between them.
- Allows for effortless storage capacity scaling, as you can easily increase the storage capacity of your remote storage location.
- Serving assets from a CDN, which can improve the performance of your website.

## Configuring the application

Configuring Shopware 6 to start storing files in your bucket is done by modifying the the general bundle configuration file located at `config/packages/shopware.yml` in your shopware root directory.

**Hypernode Object Storage**

If you're using Hypernode Object Storage, you need to make sure that the configuration file contains the following:

```yaml
shopware:
    filesystem:
      public:
        type: 'amazon-s3'
        config:
            bucket: 'main'
            region: 'EU'
            endpoint: 'management url'
            use_path_style_endpoint: true
            credentials:
              key: 'access key'
              secret: 'secret key'
```

You can get the required management URL, access key, and secret key by running `hypernode-object-storage info` with the `--with-credentials` flag:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage info --with-credentials
+--------------------------------------+----------------+---------+-------------+-------------------------------------+---------------+---------------+
|                 UUID                 |      Name      |   Plan  |  Hypernodes |           Management URL            |   Access Key  |   Secret Key  |
+--------------------------------------+----------------+---------+-------------+-------------------------------------+---------------+---------------+
| 12345678-9012-3456-b7e3-19ab43df4a23 | testappbucket1 | OS200GB |   testapp   |  https://example.ams.objectstore.eu |   abcd1234    |   abcd1234    |
+--------------------------------------+----------------+---------+-------------+-------------------------------------+---------------+---------------+
```

**AWS S3**

If you're using the AWS S3 service, your configuration file should include the following:

```yaml
shopware:
    filesystem:
      public:
        type: 'amazon-s3'
        config:
            bucket: 'your bucket name'
            region: 'your aws region'
            credentials:
              key: 'your aws access key'
              secret: 'your aws secret key'
```

### Shopware remote storage documentation

For more details on configuring remote storage in Shopware, you can refer to the official [Shopware Filesystem documentation](https://developer.shopware.com/docs/guides/hosting/infrastructure/filesystem.html)

## Syncing the files

You can use the following to sync the files between your local and remote storage:

```bash
hypernode-object-storage objects sync public/media/ s3://bucket_name/media/
```

In the case of Hypernode Object Storage, the bucket name will always be `main`.

The `hypernode-object-storage objects sync` command runs the sync process in the background
and provides the Process ID (PID). You can monitor the sync progress using:

```bash
hypernode-object-storage objects show PID
```

Alternatively, you can use the AWS CLI directly:

```bash
aws s3 sync public/media/ s3://bucket_name/media/
```

```{tip}
More information about the `hypernode-object-storage` command can be found in the [Object Storage documentation](../../hypernode-platform/object-storage.md).
```

## Serving assets from your S3 bucket

To serve media assets directly from your S3 bucket, you need to adjust your nginx configuration.
Fortunately, `hypernode-manage-vhosts` [simplifies this process for you](../../hypernode-platform/nginx/hypernode-managed-vhosts.md#object-storage-and-hypernode-managed-vhosts).

### Configuring Amazon S3 bucket policies

If you’re using Amazon S3, ensure that your S3 bucket has ACLs enabled.
