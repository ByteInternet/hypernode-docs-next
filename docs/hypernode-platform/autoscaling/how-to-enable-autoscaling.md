---
myst:
  html_meta:
    description: Step-by-step instructions on enabling Autoscaling through the Control
      Panel or command line
    title: How to enable Autoscaling? | Hypernode
---

# How to Enable Autoscaling?

## What is Autoscaling?

Vertical autoscaling in other words means upgrading your plan automatically when your server needs it, so you don’t need to worry about constant monitoring.

Your plan will be upgraded to the next possible plan within the same provider, increasing your resources while keeping the disk size the same. The upgrade is effective for 24h, after which your Hypernode will return to your regular plan. For more technical overview you can check our docs [How Autoscaling Works](how-does-autoscaling-work.md).

## How to enable Autoscaling?

You can enable Autoscaling two ways: in the Control Panel or directly via command line.

### How to enable Autoscaling in the Control Panel?

You can start using autoscaling by:

1. Log in to [Control Panel](https://my.hypernode.com).
1. Navigate to Hypernodes > Autoscaling.
1. Enable autoscaling.
1. Optionally configure the conditions.

After enabling Autoscaling feature, expect a 5min grace period before Autoscaling takes effect.

Now, rest easy knowing that your server will automatically handle overloads.

## How to enable Autoscaling via command line?

To allow using autoscaling via the command line, follow the steps below:

- Navigate go the Change plan page.
- Click on the CLI tab, enable plan changes via the CLI.

**Please note:** when enabled, **everyone who has SSH access can enable and configure autoscaling from the CLI**, even if they are not the Owner or Admin.

### Enable autoscaling via the CLI

To enable autoscaling via the CLI, you can run the following command:
`hypernode-systemctl autoscaling --enable`

### Manage autoscaling tresholds via the CLI

If you have enabled autoscaling, you can configure the thresholds when it is being autoscaled.
This tresholds does have a default value:

- autoscale_trigger_load_percentage **default: 70**
- autoscale_trigger_load_avg_minutes **default: 15**

If you want to change the default settings, you can use the commands below:

```
hypernode-systemctl settings autoscale_trigger_load_percentage 80
hypernode-systemctl settings autoscale_trigger_load_avg_minutes 50
```

### Disable autoscaling via the CLI

If you want to disable autoscaling via the CLI, you can run `hypernode-systemctl autoscaling --disable`.

**Please note:** if you enable autoscaling the next time, the last configured settings will be used.
