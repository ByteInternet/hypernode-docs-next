---
myst:
  html_meta:
    description: Learn how the SSH firewall allowlist works on Hypernode and how to
      manage SSH access securely
    title: How does the SSH allowlist work? | Hypernode
---

# How does the SSH allowlist work?

The SSH firewall allowlist on Hypernode works differently from the allowlists for FTP, WAF, and database. Understanding this difference is crucial to avoid accidentally locking yourself out of your server.

## Default behavior: SSH vs. other allowlists

- **FTP, WAF, and database**: By default, all incoming connections are blocked. Only IP addresses that are explicitly allowlisted will be able to connect.
- **SSH**: By default, SSH is open to the entire internet. Anyone can attempt to connect to your server via SSH unless you add entries to the SSH allowlist.

## What happens when you add an SSH allowlist entry?

As soon as you add one or more entries to the SSH allowlist, the firewall will immediately block all SSH access except for the IP addresses on the list. This means:

- If your current IP is not on the allowlist, you will lose access and may see a "Timed Out" or "Connection refused" error when trying to connect via SSH.
- This is different from FTP, WAF, and database, where you must add entries to allow any access at all.

> **Warning:**
> If you add an SSH allowlist entry, make sure to include your own IP address! Otherwise, you may lock yourself out of your server.

## Example: Whitelisting your IP for SSH

To allow your current IP address to access SSH, use the following command (replace `1.2.3.4` with your actual IP):

```
hypernode-systemctl whitelist add --description "My office IP" ssh 1.2.3.4
```

You can add multiple IPs if you need to allow access from several locations:

```
hypernode-systemctl whitelist add --description "Home" ssh 5.6.7.8
hypernode-systemctl whitelist add --description "Colleague" ssh 9.10.11.12
```

## Removing an IP from the SSH allowlist

To remove an IP from the SSH allowlist:

```
hypernode-systemctl whitelist remove ssh 1.2.3.4
```

If you remove all entries from the SSH allowlist, SSH will again be open to the entire internet.

## Troubleshooting: Locked out after adding an SSH allowlist entry

If you are locked out after adding an SSH allowlist entry (for example, you see a "Timed Out" error), you will need to:

- Use the Hypernode control panel to add your IP to the SSH allowlist.
