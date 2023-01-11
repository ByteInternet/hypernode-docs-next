---
myst:
  html_meta:
    description: 'Congratulations on your new Hypernode! Find out how to migrate your
      shop to Hypernode for testing on this page. '
redirect_from:
  - /en/hypernode/tools/how-to-migrate-your-shop-to-hypernode/
  - /knowledgebase/migrating-your-magento-to-hypernode/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-migrate-your-shop-to-hypernode/ -->

# How to Migrate Your Shop to Hypernode

![Step 2 - Copy your shop to Hypernode](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/48023612566/original/RVSFfRgQvCqHofVt1b6KSSqmK_WI6QwyPA.png?1579610273)

Congratulations with your brand new Hypernode! In case you already have a shop, the first step is to migrate your shop to Hypernode in order to test it. There are several ways to achieve this, which are described below.

\***Please note that the `hypernode-importer` is compatible with the following shop types:**

- Magento 1
- Magento 2
- Shopware 5
- Shopware 6

Before importing your shop, make sure your [vhost](../nginx/hypernode-managed-vhosts.md) is of the right `type`. You can verify that by listing the existing vhosts with the following command: `hypernode-manage-vhosts --list`. This will generate a list of every vhost, their type and some additional information that might be interesting.

If your vhost isn't the right `type`, you should chance the type of the vhost. You can achieve this by the following command:

```bash
hypernode-manage-vhosts example.com --type TYPE
```

## Migrate Your Shop via Shell Using the `hypernode-importer`

Are you a Control Panel (my.hypernode.com)user? Please use the Hypernode Importer tool via Shell.
*The `hypernode-importer` tool is suitable for both Magento 1 and 2 shops as well as for Shopware 5 and 6 shops*

This tool executes the following tasks:

- Copying the database
- Copying all the content
- Replacing caching through `memcached` with `Redis`
- Adjusting symlinks and paths
- Repairing the modman directory if existent
- And several other options.

The `hypernode-importer` is a very comprehensive tool as it has several alternative options and scenario's. You can import from a local database dump, use a local compressed file, copying additional databases, setting maintenance mode on the source server and skipping files that should not be copied. Please use the `hypernode-importer --help` flag to list all available options.

Please follow these steps:

- [Log in to your Hypernode with SSH](../ssh/how-to-log-in-to-the-hypernode-with-ssh.md)
- Use the `hypernode-importer`to automatically migrate the shop to your Hypernode. All data currently on your Hypernode will be overwritten. Its usage is simple:
  - `--host` Enter the SSH hostname
  - `--user` Enter the SSH user
  - `--path` Enter the full path to the rootfolder of the shop
  - `--port`\* Enter the SSH-portnumber, if not given is uses the default: 22
  - `--set-default-url`\* Sets the Base-URL to *<http://APPNAME.hypernode>.io/*
  - `--skip-db-import`\* Skips the database import
  - `--skip-file-import`\* Skips the files import
  - Use `--help` to list additional options

\*\* these are optional\*

- Example command: `hypernode-importer --host SSH_HOSTNAME --user SSH_USER --path /full/path/to/shop --set-default-url`
- Sit back while we do the work :-)

## Done Migrating?

Done? Now it's time to[check if everything works](../../best-practices/testing/how-to-check-if-everything-works.md) as it should!

## Tips and Tricks

- You could also use `screen` or `tmux` to migrate your shop in a terminal session. Use `man screen` or `man tmux` to learn more about these commands.
- The Shop importer first uses `rsync` to copy the file content and retrieves the database credentials required to dump the database from the copied configuration files. This implies that if you already imported another shop before, you should first remove the old content of the other shop before migrating a new one.

*Starting over and need a fresh Magento or Shopware install? With the `preinstall` option can start over with just one single command*
