---
myst:
  html_meta:
    description: Step-by-step instructions on enabling Autoscaling through the Control Panel or command line
    title: How to enable Autoscaling? | Hypernode
---

# How to Enable Autoscaling?

### What is Autoscaling?

Vertical autoscaling in other words means upgrading your plan automatically when your server needs it, so you don’t need to worry about constant monitoring.

Your plan will be upgraded to the next possible plan within the same provider, increasing your resources while keeping the disk size the same. The upgrade is effective for 24h, after which your Hypernode will return to your regular plan. For more technical overview you can check our docs [How Autoscaling Works](how-does-autoscaling-work.md).

### How to enable Autoscaling?

You can enable Autoscaling two ways: in the Control Panel or directly via command line.

### How to enable Autoscaling in the Control Panel?


You can start using autoscaling by:

1. Log in to [Control Panel](https://my.hypernode.com).
2. Navigate to Hypernodes > Autoscaling.
3. Enable autoscaling.
4. Optionally configure the conditions.

After enabling Autoscaling feature, expect a 5min grace period before Autoscaling takes effect.

Now, rest easy knowing that your server will automatically handle overloads.
