---
myst:
  html_meta:
    description: Learn what an Emergency Rescue on Hypernode is, why it shows up in
      your logs, and how to use the incident files to find out what caused it.
    title: Emergency Rescue on Hypernode and How to Investigate It | Hypernode
---

# Emergency Rescue on Hypernode and How to Investigate It

An Emergency Rescue is started automatically when our global monitoring sees too many errors on your Hypernode. It tries to fix the problem without anyone having to act, usually by restarting services that fail under heavy load. If it can't, the alert goes to the Hypernode Emergency Recovery Operative (Hero). See our guide on [24/7 monitoring and alerting](../../about-hypernode/support/24-7-monitoring-and-alerting.md) for how this works.

You do not need to do anything when a rescue is started.

## Why It Shows Up With Your Name

In the logs of the Control Panel you may see "Emergency Rescue" entries with your name, or the name of the account owner, and an IP of `None` with source `Hypernode Events`. Nobody logged in. The entry is created by the automated system and uses the account owner's name for the audit trail.

## The Livelog Line

In `livelog` or the Control Panel logs you may see a line like `emergency_rescue`. This is how an Emergency Rescue shows up. It is an action by the platform. Nothing in the Control Panel or in your shop started it, and it does not mean an attacker or a team member did something.

## What It Does and Does Not Look At

- It checks if your Hypernode services (Nginx, MySQL, Redis, Varnish and RabbitMQ) are available and responding.
- It does not look at your application. It does not trigger on slow PHP requests, so it can't be set to start at a PHP response time of, for example, 4 seconds. Use an APM tool such as [Tideways](../../best-practices/performance/how-to-set-up-tideways.md) or [New Relic](../../best-practices/performance/how-to-find-your-performance-bottleneck-with-new-relic.md) for that.
- A rescue can start without needing to change anything. This happens when the errors are gone again by the time it checks.

## Services Restarting Without a Crash

After a rescue you may see a service, for example MySQL, stop and start again in the system logs without an out-of-memory kill or a crash. This is the rescue restarting it. Several rescues in a row point to overload that lasts, often caused by bots.

## Find Out What Caused It

When a rescue is caused by an [out-of-memory (OOM) event](how-to-debug-out-of-memory-oom-events.md), Hypernode saves a snapshot of the state of your Hypernode in a folder named after the time of the rescue:

```console
app@abcdef-example-magweb-cmbl:~$ ls /data/web/incidents
```

```{important}
The folder names are in UTC. Convert the time shown in the Control Panel to UTC first, or you will open the wrong folder.
```

Each folder contains files like these:

- `fpm-status`: the PHP-FPM workers and what they were doing. `BUSY` workers show requests that were running.
- `mysql-process-list`: the MySQL queries that were running.
- `process-list`: the running processes.
- `tcp-connections`: the open network connections.

### Most Common Cause: PHP-FPM Workers Are Full

Most rescues we see are caused by all PHP-FPM workers being busy. New requests then have to wait, and the monitoring sees errors. Check the PHP-FPM log:

```console
app@abcdef-example-magweb-cmbl:~$ grep "reached pm.max_children" /var/log/php-fpm/php-fpm.log
```

If you see lines here shortly before the rescue, the workers were all in use. To see what the PHP-FPM workers are doing right now, use [livefpm](../../hypernode-platform/tools/what-kind-of-request-is-my-hypernode-serving.md#livefpm).

The usual causes are:

- Bots and crawlers requesting uncacheable pages, such as layered navigation filter URLs. See our guide on [bots and crawlers](../../best-practices/performance/how-to-fix-performance-issues-caused-by-bots-and-crawlers.md).
- Scanners requesting hundreds of paths that don't exist. See our guide on [blocking spammers and scanners](../../hypernode-platform/nginx/how-to-block-spammers-and-scanners.md).
- An integration that requests your REST API very often.
- Slow requests or slow database queries in your own code. An APM tool helps to find these.

To deal with unwanted traffic, work in this order:

1. Return `410 Gone` to bots on layered navigation query strings. See [How to Fix Performance Issues Caused by Bots and Crawlers](../../best-practices/performance/how-to-fix-performance-issues-caused-by-bots-and-crawlers.md).
1. [Rate limit](../../hypernode-platform/nginx/how-to-resolve-rate-limited-requests-429-too-many-requests.md) the crawler that causes most of the requests.
1. Filter the rest with [Botstopper](../../hypernode-platform/botstopper/how-to-use-botstopper.md).
1. Only then look at capacity.

Check the access log afterwards to confirm the `410` and `429` responses are given.

Increasing the number of PHP-FPM workers does not solve this. The extra workers fill up with the same requests, and they use more CPU and memory.

The number of PHP workers is fixed by your plan. If your shop needs more headroom after you have dealt with unwanted traffic, a larger plan gives you more.
