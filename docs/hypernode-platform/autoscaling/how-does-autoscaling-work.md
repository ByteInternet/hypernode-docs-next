---
myst:
  html_meta:
    description: Learn how autoscaling dynamically adjusts server resources based
      on CPU usage metrics, allowing efficient workload management without manual
      intervention. Configure thresholds, durations, and understand the workflow for
      seamless autoscaling on Hypernode.
    title: How does Autoscaling work? | Hypernode
---

# How does Autoscaling work?

Vertical autoscaling is triggered once the conditions are met from the configured settings in the Control Panel. You can configure the following:

- **CPU Load Threshold:** CPU load that is continuously monitored by the autoscaling agent. The percentage value you see is the actual load divided by the number of CPUs you have. For example, if your actual load is 2, but you have 4 CPUs, your CPU load percentage is 50%. The default setting is 70%.
- **Minimum Duration in Minutes:** Minimum amount of time the server is overloaded before autoscaling gets triggered. We monitor your CPU load every minute; autoscaling will be triggered once the CPU load condition is met for the minimum amount of time set in the Control Panel. The default setting is 15 minutes.

### Autoscaling workflow
To minimize downtime during the process, we employ a live volume swapping method. We install a new Hypernode without copying the data over the network to the new hosting environment. Next, we detach the volume using the API and mount it on the new machine before adjusting the DNS.

The feature is available on the cloud plans (OpenStack and AWS).

## Autoscaling process
Once set conditions are met and autoscaling is triggered, you get upgraded to the next available plan for 24 hours. When your Hypernode is in the boosted state, you can still adjust the settings, but you cannot change your plan. If you wish to do so, please contact support@hypernode.com.

If the server remains overloaded post-autoscaling, the next autoscaling trigger is determined based on these criteria.
The greater of either:
- User-defined minimum duration for CPU threshold surpassing: Allows time to assess newly allocated resources' impact on CPU performance.
- A cooldown period of 15 minutes: Ensures a minimum interval for reassessment when the user-defined duration is less than 15 minutes.

This approach selects the longer duration between user-defined settings or the fallback duration before initiating the next autoscaling event. It ensures adequate time for evaluating resource changes on CPU performance. Autoscaling is capped at the biggest plan available on each cloud provider.

### How to halt continued Autoscaling
Simply turn off the autoscaling feature in your control panel. This prevents subsequent autoscaling triggers after the initial action. 

### Returning to the Initial Plan After 24 Hours
Regardless of the number of times your Hypernode was autoscaled, you will go back to your initial plan after 24 hours from your initial upgrade.

## Enabling Autoscaling

For detailed steps on enabling Autoscaling, please refer to our documentation: [How to enable Autoscaling?](how-to-enable-autoscaling.md)
