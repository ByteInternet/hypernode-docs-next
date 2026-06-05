---
myst:
  html_meta:
    description: 'With the hypernode-haproxyctl tool you can inspect and manage the
      HAProxy service. Learn how to use the hypernode-haproxy CLI Tool. '
    title: How to use the hypernode-haproxyctl CLI Tool?
---

# How to Use the hypernode-haproxyctl CLI Tool

Hypernode clusters use [HAProxy](https://www.haproxy.org/) to distribute HTTP requests from the loadbalancer to the application servers. With the `hypernode-haproxyctl` CLI tool you can inspect and manage the HAProxy service.

## Viewing the current status

With the `status` subcommand, you can see the current status of HAProxy and its backends.

```console
app@abcdef-examplelb-magweb-tbbm ~ $ hypernode-haproxyctl status
HAProxy v2.6.12-1+deb12u3 (released: 2025/10/03, uptime: 98d 22h33m56s)
FRONTEND (OPEN): request rate(160), session rate(7), conn rate(7)
exampleapp1 (UP): request rate(0), session rate(25), conn rate(0)
exampleapp2 (UP): request rate(0), session rate(32), conn rate(0)
exampleapp3 (UP): request rate(0), session rate(28), conn rate(0)
exampleapp4 (UP): request rate(0), session rate(38), conn rate(0)
exampleapp5 (UP): request rate(0), session rate(35), conn rate(0)
BACKEND (UP): request rate(0), session rate(160), conn rate(0)
```

The output has three sections:

- **FRONTEND**: The internet-facing entry point. Shows how many requests and connections are coming in per second.
- **exampleapp1-N**: Your individual app servers. Common states are `UP`, `DOWN` and `DRAIN`.
- **BACKEND**: The combined pool of all app servers. `UP` means at least one server is healthy.

If a server shows `DOWN` unexpectedly, it likely needs attention. `DRAIN` and `MAINTENANCE` are usually intentional states used during maintenance.

## Managing backends

When troubleshooting or performing maintenance on an app server, you can use the `drain` subcommand to gracefully remove it from rotation:

```console
app@abcdef-examplelb-magweb-tbbm ~ $ hypernode-haproxyctl drain exampleapp1
```

The `drain` command allows existing connections to finish while preventing new traffic from being sent to the server. This is ideal for performing maintenance without disrupting active users.

Once maintenance is complete, you can use the `enable` subcommand to bring the server back into rotation:

```console
app@abcdef-examplelb-magweb-tbbm ~ $ hypernode-haproxyctl enable exampleapp1
```
