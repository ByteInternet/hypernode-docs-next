---
myst:
  html_meta:
    description: Enable Tideways profiling on Hypernode. Learn how to activate it,
      set the API key, configure sampling, and set an environment name.
    title: How to set up Tideways on Hypernode
redirect_from:
  - /en/best-practices/performance/how-to-set-up-tideways/
---

# How to Set Up Tideways on Hypernode

[Tideways](https://tideways.com/) is an application performance profiling and monitoring tool. On Hypernode you can enable Tideways in minutes using the CLI and control panel.

## Prerequisites

- A Tideways account and project. Create a new project in Tideways and note the project API key.

## How to Activate Tideways

### Activation Via the CLI

First, enable Tideways and set your project API key:

```bash
hypernode-systemctl settings tideways_enabled True
hypernode-systemctl settings tideways_api_key <api_key_here>
```

After enabling, it can take a short while for data to appear in Tideways. We recommend generating some traffic on your shop to produce samples.

#### Optional: Configure Sample Rate

Sampling controls the percentage of requests that will be stored in Tideways, which helps manage cost. For example, to store 25% of samples:

```bash
hypernode-systemctl settings tideways_sample_rate 25
```

#### Optional: Set Environment Name

You can assign an environment label (for example when this node is a staging server):

```bash
hypernode-systemctl settings tideways_env_name staging
```

#### Optional: Collect Keys for Redis Instrumentation

Enable Redis key collection to see which keys are accessed by Redis operations in your traces. This provides more detailed insights when debugging Redis-related performance issues.

```bash
hypernode-systemctl settings tideways_redis_keys_enabled True
```

**Please note:** This setting can have privacy implications if your application uses personal identifiable information (such as email addresses or IP addresses) inside Redis keys. For more information, see the [Tideways documentation on Redis instrumentation](https://support.tideways.com/documentation/setup/configuration/advanced-instrumentation.html#collect-keys-for-redis-instrumentation).

### Activation through Control Panel

It’s also possible to configure Tideways in the Control Panel.

1. Go to your **Hypernode** in the Control Panel
1. Click **Settings**
1. Go to the tab **Performance & Monitoring**
1. Enable the toggle for **Tideways**, and set your API key in **Tideways API key**
