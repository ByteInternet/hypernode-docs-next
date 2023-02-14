---
myst:
  html_meta:
    description: 'If your Magento 2 Cron is stuck or long-running this could be because
      of a default setting in Magento 2 causing the consumers to never end. '
    title: How to optimize Magento 2 queue consumers? | Hypernode
redirect_from:
  - /en/support/solutions/articles/48001186343-how-to-optimize-magento-2-queue-consumers-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001186343-how-to-optimize-magento-2-queue-consumers-on-hypernode/ -->

# How to optimize Magento 2 Queue consumers on Hypernode

If your Magento 2 Cron is stuck or long-running this could be because of a [default setting in Magento 2](https://devdocs.magento.com/guides/v2.4/config-guide/prod/config-reference-envphp.html#consumers_wait_for_messages) causing the consumers to never end. This article describes how you can solve this issue by using the configuration below.

## Check for long-running consumer processes

First check if there are any long running consumer processes by running the command below.

```
ps --sort etime -A -o etime,pid,user,args | grep php | grep -vE 'php-fpm|\-\-mode daemon|grep'
```

## Edit your env.php

Edit your ~/magento2/app/etc/env.php and change your consumers_wait_for_messages configuration from 1 to 0.

```
'queue' => [
    'consumers_wait_for_messages' => 0
]
```

Flush your Magento cache after changing your env.php.

## Kill the long-running processes

Kill the consumer crons that are still stuck.

```
pkill -f queue:consumers
```

That's it, now your consumer processes should not be stuck anymore.

## Configure only_spawn_when_message_available to reduce CPU and memory usage

If your shop runs on Magento 2.4.1 or higher, it’s possible to reduce the CPU and memory usage by adding the `queue/only_spawn_when_message_available` parameter in app/etc/env.php. By combining this setting with the `queue/consumers-wait-for-messages` setting, the consumer will only run when a message is available in the queue and it will be terminated when there are no more messages to process. The combination of these settings can be beneficial for Magento shops that run on smaller Hypernodes with less resources where the consumers can run infrequently. An example of this configuration can be found below:

```
'queue' => [
    'consumers_wait_for_messages' => 0,
    'only_spawn_when_message_available' => 1
]
```
