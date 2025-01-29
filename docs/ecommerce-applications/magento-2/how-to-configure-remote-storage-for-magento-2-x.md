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
- **Note:** Staging ports (8888, 8443) will not be available when horizontal autoscaling is enabled.
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

To start serving media assets from your S3 bucket, you need to make some adjustments to your nginx configuration. Create the following file at `/data/web/nginx/example.com/server.assets.conf` for each relevant vhost:

```nginx
set $backend "haproxy";

location @object_storage_fallback {
    # Proxy to object storage
    set $bucket "my_bucket_name";
    proxy_cache_key "$bucket$uri";
    proxy_cache_valid 200 302 7d;
    proxy_cache_methods GET HEAD;
    proxy_cache_background_update on;
    proxy_cache_use_stale updating;
    proxy_cache asset_cache;
    resolver 8.8.8.8;
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
    add_header Cache-Control "public";
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Cache-Status $upstream_cache_status;
    expires +1y;

    # If object storage fails, fallback to PHP handler
    error_page 404 = @asset_fallback;
    error_page 403 = @asset_fallback;
}

location @php_asset_fallback {
    # Handle with phpfpm
    rewrite ^/media /get.php?$args last;
    rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=$2 last;
    echo_exec @phpfpm;
}

location @haproxy {
    # Handle with haproxy
    include /etc/nginx/proxy_to_haproxy.conf;
    proxy_pass http://127.0.0.1:8080;
}

location @asset_fallback {
    try_files "" $asset_fallback_handler;
}

location ~ ^/static/ {
    expires max;

    # Remove signature of the static files that is used to overcome the browser cache
    location ~ ^/static/version\d*/ {
        rewrite ^/static/version\d*/(.*)$ /static/$1 last;
    }

    location ~* \.(ico|jpg|jpeg|png|gif|svg|svgz|webp|avif|avifs|js|css|eot|ttf|otf|woff|woff2|html|json|webmanifest)$ {
        add_header Cache-Control "public";
        add_header X-Frame-Options "SAMEORIGIN";
        expires +1y;

        try_files $uri $uri/ @asset_fallback;
    }
    location ~* \.(zip|gz|gzip|bz2|csv|xml)$ {
        add_header Cache-Control "no-store";
        add_header X-Frame-Options "SAMEORIGIN";
        expires    off;

        try_files $uri $uri/ @asset_fallback;
    }
    try_files $uri $uri/ @asset_fallback;
    add_header X-Frame-Options "SAMEORIGIN";
}

location /media/ {
    try_files $uri $uri/ @asset_fallback;

    location ~ ^/media/theme_customization/.*\.xml {
        deny all;
    }

    location ~* \.(ico|jpg|jpeg|png|gif|svg|svgz|webp|avif|avifs|js|css|swf|eot|ttf|otf|woff|woff2)$ {
        add_header Cache-Control "public";
        add_header X-Frame-Options "SAMEORIGIN";
        expires +1y;
	      try_files $uri $uri/ @object_storage_fallback;
    }
    location ~* \.(zip|gz|gzip|bz2|csv|xml)$ {
        add_header Cache-Control "no-store";
        add_header X-Frame-Options "SAMEORIGIN";
        expires    off;
	      try_files $uri $uri/ @object_storage_fallback;
    }
    add_header X-Frame-Options "SAMEORIGIN";
}
```

Make sure to change the string `my_bucket_name` to the name of your bucket and keep in mind that your bucket URL might be different depending on your AWS region. For example, you might need to change it from `https://$bucket.s3.amazonaws.com$uri` to `https://s3.amazonaws.com/$bucket$uri` instead.
Furthermore, ensure that your S3 bucket policies are configured correctly, so that only `/media` is publicly readable. For example:

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
