---
myst:
  html_meta:
    description: Use RabbitMQ to run resource-intensive tasks in the background on
      Hypernode. Learn how to enable and access RabbitMQ on Hypernode.
    title: How to Run RabbitMQ | Hypernode
redirect_from:
  - /en/best-practices/database/how-to-run-rabbitmq-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/best-practices/database/how-to-run-rabbitmq-on-hypernode/ -->

# How to Run RabbitMQ on Hypernode

RabbitMQ is available on all Hypernode plans. Check the changelog [here](https://changelog.hypernode.com/changelog/platform/release-6052-rabbitmq-on-hypernode/).

## What is RabbitMQ?

Because Magento is a heavy and slow application, tasks are preferably executed in the background. To run tasks in the background you need queues. RabbitMQ is message-queueing software where queues can be defined. Applications can connect to the queue and transfer a message onto it. This way you can (for example) import many products into Magento without having to wait a substantial time until the process is finished. The import takes place in the background.

The main idea behind queues is to avoid doing a resource-intensive task immediately and having to wait for it to complete. Instead you can schedule the task to be done later. The task is wrapped-up as a message and sent to a queue. A worker process running in the background will pop the tasks and eventually execute the job.

## Details RabbitMQ on Hypernode

- Hypernode installs and runs RabbitMQ if the hosting plan supports it AND if you have explicitly enabled it
- RabbitMQ can be enabled / disabled via the hypernode-api or hypernode-systemctl commandline tool
- RabbitMQ will be disabled automatically when you downgrade your hosting plan that does not support it
- When upgrading or downgrading your hosting plan, any exchanges, queues, users and persistent messages (non-transient) will be transferred to your new Hypernode. Even if your new hosting plan does not support RabbitMQ, the data will be kept.
- The data is also kept if RabbitMQ disabled. After re-enabling it again, you still have your queues, users, etc.

## Enabling RabbitMQ

Enabling RabbitMQ can be done via de [commandline tool](../../hypernode-platform/tools/how-to-use-the-hypernode-systemctl-cli-tool.md) or the [Hypernode API](https://community.hypernode.io/#/Documentation/hypernode-api/README).

As an app user you enable RabbitMQ this way:

```bash
hypernode-systemctl settings rabbitmq_enabled True
```

Use `False` to turn it off.

If your hosting plan does not support RabbitMQ, you will receive the following message:

```console
app@uaijq6-test-magweb-do:~$ hypernode-systemctl settings rabbitmq_enabled --value True
Looks like something went wrong: b'{"rabbitmq_enabled":["RabbitMQ cannot be enabled for this app. Please upgrade to a plan that supports RabbitMQ if you want to make use of this feature."]}'
```

## Restarting RabbitMQ

You can run this command to restart RabbitMQ:

```bash
hypernode-servicectl restart rabbitmq-server
```

## Accessing RabbitMQ

- RabbitMQ only binds on localhost
- The default admin account is username `guest` and password `guest`. You can change and add users via the admin interface.
- You can access the admin interface e.g. by forwarding the tcp port via SSH:

`ssh app@appname.hypernode.io -L 55672:localhost:15672`

Use your browser to go to `localhost:55672` and logon using guest/guest.

Another way to access the admin interface is via [hypernode-vpn](https://changelog.hypernode.com/changelog/release-6064-rabbitmq-can-be-accessed-via-the-hypernode-vpn/)

## RabbitMQ and Magento

You need to make some changes in Magento in order to use RabbitMQ. For example in `/data/web/magento2/app/etc/env.php`:

```php
'queue' =>
        array (
            'amqp' =>
                array (
                    'host' => 'localhost',
                    'port' => '5672',
                    'user' => 'guest',
                    'password' => 'guest',
                    'virtualhost' => '/',
                ),
        ),
```
