---
myst:
  html_meta:
    description: Getting started with Object Storage
    title: Hypernode Object Storage | Getting Started
redirect_from:
  - hypernode-platform/object-storage/getting-started-with-object-storage
---

# Getting started with Hypernode Object Storage

You can run the CLI command with the `--help` command to find out about all the options and arguments.

```bash
hypernode-object-storage --help
```

## Creating a Hypernode Object Storage Workspace

**Command-line interface (CLI)**

1. SSH into your server.
1. Run `hypernode-object-storage create`
1. Fill in the prompts with a name and desired storage.
1. Confirm your order and give it a few minutes before your storage is ready.

**Control Panel**

1. Go to the [Control Panel](https://my.hypernode.com).
1. Click the **Order a workspace** button in the top-right.
1. Select the desired options for your workspace and proceed to checkout.


```{note}
You can use one object storage across multiple Hypernodes. But you can only use one object storage space per Hypernode.
```

## Retrieve object storage information

**Command-line interface (CLI)**

1. Run `hypernode-object-storage info`
1. If you want to retrieve your credentials for the workspace pass in the flag `--with-credentials`.

The output should look like the following:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage info
UUID         | d8770125-6c90-4770-b00f-1716f699990a
Name         | example-storage
Plan         | OS50GB
Versioning   | Disabled
Hypernodes   | example
Endpoint URL | **sensitive**
Access Key   | **sensitive**
Secret Key   | **sensitive**
```

**Control Panel**
1. Go to the [Control Panel](https://my.hypernode.com).
1. Click on the **Object Storage** tab in the left sidebar.
1. Click your workspace.
1. Click the **Show credentials** button in the top-right corner.

You can use the credentials and the URL now to configure remote storage for your application with the help of the following articles:

1. [How to configure remote storage for Magento 2.x](../../ecommerce-applications/magento-2/how-to-configure-remote-storage-for-magento-2-x.md)
1. [How to configure remote storage for Shopware 6.x](../../ecommerce-applications/shopware-6/how-to-configure-remote-storage-for-shopware-6-x.md)
