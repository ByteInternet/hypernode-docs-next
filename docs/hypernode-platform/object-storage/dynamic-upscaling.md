---
myst:
  html_meta:
    description: Learn how Dynamic Upscaling works in Hypernode Object Storage
    title: Hypernode Object Storage | Dynamic Upscaling
---

# Dynamic Upscaling

Dynamic Upscaling is a feature that automatically increases your object storage capacity when needed. This ensures that your workspace always has enough space to store your files, backups, media, and other data—without requiring manual upgrades.

## How it works

When Dynamic Upscaling is enabled, the system monitors your usage and upgrades your object storage plan automatically when you reach 99% of your current limit. This helps prevent issues related to running out of storage space and reduces the risk of downtime. Dynamic upscaling will always choose the next suitable plan size based on your current usage. You will be billed according to the upgraded plan after the change.

## Managing Dynamic Upscaling

### Control Panel

Dynamic Upscaling can be enabled or disabled through the Control Panel:

1. Go to the Control Panel
1. Select the Object Storage workspace
1. Toggle the Dynamic Upscaling switch

### Command Line Interface

You can also manage Dynamic Upscaling using the CLI. First, ensure you have the basic commands set up as described in [Basic Commands](basic-commands.md#updating-workspace-settings).

To enable Dynamic Upscaling:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage update --enable-dynamic-upscaling
Enabling dynamic upscaling...
Dynamic upscaling enabled successfully!
```

To disable Dynamic Upscaling:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage update --disable-dynamic-upscaling
Disabling dynamic upscaling...
Dynamic upscaling disabled successfully!
```

To check the current status of Dynamic Upscaling:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage info
UUID         | d8770125-6c90-4770-b00f-1716f699990a
Name         | example-storage
Plan         | OS200GB
Versioning   | Disabled
Dynamic Upscaling | Enabled
Hypernodes   | example
```

```{note}
When Dynamic Upscaling is enabled, your plan will automatically upgrade when you reach 99% of your current storage limit. This may result in higher costs, so monitor your usage regularly.
```
