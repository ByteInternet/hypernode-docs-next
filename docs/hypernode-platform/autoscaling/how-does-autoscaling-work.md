---
myst:
  html_meta:
    description: Learn how autoscaling dynamically adjusts server resources based on CPU usage metrics, allowing efficient workload management without manual intervention. Configure thresholds, durations, and understand the workflow for seamless autoscaling on Hypernode.
    title: How does Autoscaling work? | Hypernode
---

# How does Autoscaling work?

## Purpose

Autoscaling ensures dynamic server resource adjustments based on CPU usage metrics, efficiently managing workload demands without manual intervention.

## Configuration Parameters

In the control panel, users can define autoscaling conditions to tailor actions to their workload demands:
- **CPU Load Threshold:** Specifies the CPU load percentage that triggers autoscaling using a range slider.
- **Minimum Duration:** Determines the minimum duration, in minutes, for the CPU load to exceed the threshold to activate autoscaling.

## Autoscaling Triggering Process
- **Continuous Monitoring:** The autoscaling agent continually monitors your application's CPU load.
- **Activation Conditions:** Autoscaling is triggered if the CPU load surpasses the defined threshold and duration criteria set by the user.

## Autoscaling Workflow
- **Initial Cooldown period:** A 5-minute cooldown period after enabling autoscaling prevents rapid scaling due to sudden spikes.
- **Scaling Actions:** Autoscaling automatically upgrades the plan to the next available tier within the same provider, catering to increased demand. The upgraded plan remains effective for 24 hours before reverting to the original configuration.

## Continued Autoscaling Process:

If the server remains overloaded post-autoscaling, the next autoscaling trigger is determined based on these criteria:
- **The greater of either**:
  - **User-defined minimum duration for CPU threshold surpassing**: Allows time to assess newly allocated resources' impact on CPU performance.
  - **A fallback duration of 15 minutes**: Ensures a minimum interval for reassessment when the user-defined duration is less than 15 minutes.

This approach selects the longer duration between user-defined settings or the fallback duration before initiating the next autoscaling event. It ensures adequate time for evaluating resource changes on CPU performance.
To halt continued autoscaling behavior, simply turn off the autoscaling feature in your control panel. This prevents subsequent autoscaling triggers after the initial action.

## Enabling Autoscaling

For detailed steps on enabling Autoscaling, please refer to our documentation: [How to enable Autoscaling?](how-to-enable-autoscaling.md)

## Supported providers:

Autoscaling is available for Combell Openstack and AWS cloud hosting providers.
