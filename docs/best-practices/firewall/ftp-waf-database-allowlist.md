---
myst:
  html_meta:
    description: Learn how to manage IP addresses on the Hypernode allowlists
    title: How to allowlist FTP, WAF and database? | Hypernode
---

# How to allowlist FTP, WAF and database

In the text below we will explain how you can add an IP to the whitelist by using the control panel or CLI (command-line interface). Whitelisting an IP can be for multiple reasons like, connecting via FTP, connecting to a database or for security scans like ForusP.

## Adding IP Addresses in the allowlist via the control panel for FTP, WAF and database

Follow these steps to whitelist an IP addresses for FTP:

- Go to the [control panel](https://my.hypernode.com)
- Log in with your credentials
- Once logged in, select the Hypernode you wish to configure
- Click on **Allowlist** from the menu
- Select **Rule type** and choose here for example **FTP** from the dropdown
- Enter the IP address you want to add to the whitelist
- Provide a descriptive name for the entry for example **Office webshop**. Use descriptive names when adding entries to help identify their purpose in the future.
- Click on **Save** to apply the changes

## Using the hypernode-systemctl whitelist command (CLI)

The `hypernode-systemctl whitelist` command allows you to manage allowlist entries for different services on your Hypernode. You can use it to add, remove, or list allowlist entries for FTP, WAF, database, and SSH.

### Command structure

```
hypernode-systemctl whitelist [-h] {add,remove,get} ...
```

- **add**: Add an IP address to the allowlist for a specific service.
- **remove**: Remove an IP address from the allowlist for a specific service.
- **get**: List current allowlist entries. You can filter by service type.

### Supported types

You can specify the type of service for which you want to manage the allowlist:

- `ftp`
- `waf`
- `database`
- `ssh`

### Adding an IP with a description

You can add a description to help identify the purpose of the allowlist entry:

```
hypernode-systemctl whitelist add [--description DESCRIPTION] {waf,database,ftp,ssh} ip
```

**Example:**

```
hypernode-systemctl whitelist add --description "Office SSH access" ftp 1.2.3.4
```

### Removing an IP from the allowlist

To remove an IP address from the allowlist for a specific service, use the following command:

```
hypernode-systemctl whitelist remove {waf,database,ftp,ssh} ip
```

**Example:**

```
hypernode-systemctl whitelist remove ftp 1.2.3.4
```

### Listing allowlist entries

To view all allowlist entries, use:

```
hypernode-systemctl whitelist get
```

To filter by type (e.g., only FTP):

```
hypernode-systemctl whitelist get --type ftp
```

This will show all currently allowlisted IPs for the specified service.
