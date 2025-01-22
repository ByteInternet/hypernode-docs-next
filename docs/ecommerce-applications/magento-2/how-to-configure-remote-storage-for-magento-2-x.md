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

One can run the following instead to really speed up the process:

```bash
aws s3 sync pub/media/ s3://my_bucket_name/media/
aws s3 sync var/import_export s3://my_bucket_name/import_export
```

This is much faster than Magento's built-in sync, because `aws s3 sync` uploads files concurrently.

## The storage flag file in the bucket

Magento's S3 implementation creates a test file called `storage.flag`, which is basically created to test if the connection works. So this is not a magic file to mark anything ([source](https://github.com/magento/magento2/blob/6f4805f82bb7511f72935daa493d48ebda3d9039/app/code/Magento/AwsS3/Driver/AwsS3.php#L104)).

## Serving assets from your S3 bucket

To start serving media assets from your S3 bucket, you need to make some adjustments to your nginx configuration.

We recommend that you create a configuration file `/data/web/nginx/http.asset_proxy_cache.conf` defining the cache storage location, structure, size constraints, and cache expiration policies.

```nginx
proxy_cache_path /data/var/nginx-asset-cache levels=1:2 keys_zone=asset_cache:10m max_size=1g inactive=1w;
```

Then update your nginx configuration in the following manner.

```nginx
location /media {
    # ...
    location ~* \.(ico|jpg|jpeg|png|gif|svg|js|css|swf|eot|ttf|otf|woff|woff2)$ {
        resolver 8.8.8.8;
        set $bucket "<my_bucket_name>";
        proxy_pass https://$bucket.s3.amazonaws.com$uri;
        proxy_pass_request_body off;
        proxy_pass_request_headers off;
        proxy_intercept_errors on;
        proxy_hide_header "x-amz-id-2";
        proxy_hide_header "x-amz-request-id";
        proxy_hide_header "x-amz-storage-class";
        proxy_hide_header "x-amz-server-side-encryption";
        proxy_hide_header "Set-Cookie";
        proxy_ignore_headers "Set-Cookie";
        
        # include the following if you defined proxy_cache_path previously
        proxy_cache_key "$bucket$uri";
        proxy_cache_valid 200 302 7d;
        proxy_cache_methods GET HEAD;
        proxy_cache_background_update on;
        proxy_cache_use_stale updating;
        proxy_cache asset_cache;
    }
    # ...
}
```

Keep in mind your bucket URL might be different depending on your AWS region. For example, you might need to change it to `https://s3.amazonaws.com/$bucket$uri` instead.
Also make sure your S3 bucket policies are configured correctly, so that only `/media` is publicly readable. For example:

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
