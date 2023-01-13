---
myst:
  html_meta:
    description: Our experts monitor your Hypernode 24/7 and are ready to intervene
      if needed to ensure the highest possible stability. Learn more about our Monitoring
      here!
    title: 24/7 Monitoring and Alerting | Support | Hypernode
redirect_from:
  - /en/about/support/24-7-monitoring-and-alerting/
---

<!-- source: https://support.hypernode.com/en/about/support/24-7-monitoring-and-alerting/ -->

# 24/7 Monitoring and Alerting

At Hypernode we understand like no other that the availability and stability of the application is a top priority for our customers. This stability depends on many different factors, including the stability of the Hypernode itself. To ensure the highest possible stability, our experts monitor your Hypernode 24 hours a day, 7 days a week. If something threatens the stability of the Hypernode, an engineer stands ready to intervene.

## Monitoring

It is our responsibility to monitor all the offered services on the Hypernode. As such we have setup a global monitoring network that checks your Hypernode’s availability from locations in Europe, the United States, and Eastern Asia. Each location checks the availability roughly every 2 minutes. An alert is raised if too many errors are received globally, and an Emergency Rescue is started. If the automated Emergency Rescue can’t fix the issue, the alert is escalated to the Hypernode Emergency Recovery Operative (Hero).

### What Do We Monitor

Our monitoring is focused at the Hypernode hosting software services that come preinstalled on your Hypernode; Nginx, MySQL, and Redis, and the optional extra services; Varnish, and RabbitMQ. Each service is checked to see if it’s still running and responsive. We also monitor the root filesystem, where free space is required for logs and temp files that could otherwise cause any of these services to fail.

### What Do We Not Monitor

The big thing missing from the list of things we monitor, is your application, or “Does Magento work”. The reason for this is twofold. First, while we do know a lot about hosting software, and we know quite a bit about the hosted applications and Magento, we don’t know your specific implementation. We also don’t know what is ‘normal’ or ‘expected’ behavior for your application. For example, if your application starts giving errors because it’s overloaded, due to a new marketing campaign aimed at your Chinese customers, you don’t want our automated systems to interpret that as a DDoS, and block all of China. You also wouldn’t want our Emergency Rescue to restart MySQL, because your application is throwing errors since you’re mid-upgrade.

## Alerting

When the Emergency Rescue process can’t fix the issue, or takes longer than expected, an alert is raised to the Hypernode Emergency Recovery Operative (Hero), to manually investigate and fix the issue. The Hero is stand-by 24/7, both during, and outside of office hours. The alert automatically escalates to the entire team, if the Hero doesn’t respond to the alert within 30 minutes. Both on- and off-duty engineers are continuously alerted until the issue is acknowledged by a Hero.

Once a Hero acknowledges an issue, they will work to fix it. This may be as simple as clearing up disk space, restarting services, or blocking abusive visitors. Sometimes the issue needs to be escalated to a cloud provider, if the issue is not caused by the Hypernode.

### Fixes With a Permanent Impact

Most fixes don’t impact the application. However, sometimes fixing a temporary problem has a (semi) permanent impact on the application. For example, if the Hero determines the cause of an issue to be a DDoS from a far away country, we may configure the Hypernode to reject any and all traffic from this country. This could obviously have an impact to the application if there is also legitimate traffic from said country.

We will inform you if any permanent impact fixes are applied which could have a negative impact on the application. The next business day we’ll let you know what the issue was, how we fixed it. If requested, we’ll roll back these changes. We’ll also work with you to configure your application to better withstand such issues, to prevent similar fixes from having to be applied at a later date.
