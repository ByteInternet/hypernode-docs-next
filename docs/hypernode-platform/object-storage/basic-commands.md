---
myst:
  html_meta:
    description: Learn about the basic commands for managing Hypernode Object Storage
    title: Hypernode Object Storage | Basic Commands
---

# Basic Commands

This guide covers the fundamental commands for managing your Hypernode Object Storage workspace. These commands allow you to create, view, update, and cancel your object storage workspace.

## Creating a Workspace

The `create` command initializes a new Object Storage workspace.

```console
hypernode-object-storage create
```

### Options

- `--name`: Specify a custom name for your workspace
- `--plan`: Select a storage plan (e.g., OS50GB, OS200GB)
- `--coupon`: Apply a coupon code for discounts

### Example

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage create --name my-storage --plan OS200GB
```

## Viewing Workspace Information

The `info` command displays details about your current Object Storage workspace.

```console
hypernode-object-storage info
```

### Options

- `--with-credentials`: Display sensitive credentials
- `--verbose`: Show detailed debug information
- `-F {text,json}`: Choose output format (text or JSON)

### Example Output

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage info
UUID         | d8770125-6c90-4770-b00f-1716f699990a
Name         | example-storage
Plan         | OS200GB
Versioning   | Disabled
Hypernodes   | example
Endpoint URL | **sensitive**
Access Key   | **sensitive**
Secret Key   | **sensitive**
```

### JSON Output Example

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage info -F json
{
  "UUID": "2667238b-9976-437f-98f5-cd7491b76fd8",
  "Name": "my workspace",
  "Plan": {
    "code": "OS200GB",
    "name": "Growth Node",
    "description": "Great for expanding stores",
    "price": 2000,
    "storage_size_in_gb": 200,
    "is_popular": true
  },
  "Versioning": false,
  "Hypernodes": "example",
  "Credentials": {
    "management_url": "**sensitive**",
    "access_key": "**sensitive**",
    "secret_key": "**sensitive**"
  }
}
```

## Updating Workspace Settings

The `update` command allows you to modify your Object Storage workspace settings.

```console
hypernode-object-storage update
```

### Options

- `--enable-versioning`: Enable object versioning
- `--disable-versioning`: Disable object versioning

### Example

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage update --enable-versioning
Enabling versioning...
Versioning enabled successfully!
```

```{note}
Enabling versioning increases storage usage as each version of an object is stored separately. Consider your storage plan size when enabling this feature.
```

## Canceling a Workspace

The `cancel` command initiates the cancellation process for your Object Storage workspace.

```console
hypernode-object-storage cancel
```

### Important Notes

1. **Cancellation Timing**

   - Cancellation takes effect at the end of the current billing period
   - You will be billed for the full period

1. **Data Retention**

   - Data remains accessible for 7 days after cancellation
   - Use this period to retrieve any needed data

### Example

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage cancel
Are you sure you want to cancel your Object Storage workspace? [y/N]: y
Cancellation initiated. Your workspace will be canceled at the end of the current billing period.
Data will remain accessible for 7 days after cancellation.
```
