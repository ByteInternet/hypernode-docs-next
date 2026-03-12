---
myst:
  html_meta:
    description: Create a persistent external symlink in Hypernode Deploy that survives
      releases and rollbacks.
    title: How to set up a persistent external symlink on deployment
---

# Set up a persistent external symlink on deployment

Sometimes it's important to have a persistent symlink that leads to a folder outside of your application, for example a subfolder blog, or external sitemaps.

This pattern is useful when you want to expose content that lives outside the current release directory, while keeping it available and stable across deployments and rollbacks. By registering the path as a "shared file" in Hypernode Deploy, the final path in each release becomes a symlink to the shared area, which you can then point to any external location you need.

## Install the Hypernode Deploy configuration package

Make sure you have Hypernode Deploy set up and configured. If you haven't done this yet, follow the guide in [Install and configure Hypernode Deploy](install-and-configure-hypernode-deploy.md).

## Steps

1. Add the path that should become a symlink to the shared files configuration in your deploy.php config:

```php
$configuration->setSharedFiles([
    'pub/my-symlink'
]);
```

2. Deploy once. This will create the file at `~/apps/<appname>/shared/pub/my-symlink`.

1. Replace the created file with a symlink to your external target. For example:

```bash
ln -s ~/blog ~/apps/<appname>/shared/pub/my-symlink
```

4. Deploy again. The symlink will be available in each new release and will persist across deployments.

## Verify

After deployment, verify the symlink inside the current release:

```bash
ls -l ~/apps/<appname>/current/pub/my-symlink
```

You should see it pointing to your external target (e.g., `~/blog`). If you open the URL that maps to `pub/my-symlink` in your site, the content should load from the external path.
