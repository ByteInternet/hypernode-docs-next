---
myst:
  html_meta:
    description: Learn how autoscaling dynamically adjusts server resources based
      on CPU usage metrics, allowing efficient workload management without manual
      intervention. Configure thresholds, durations, and understand the workflow for
      horizontal autoscaling without downtime on Hypernode.
    title: How does horizontal Autoscaling work? | Hypernode
---

# How does horizontal Autoscaling work

This article explains how Horizontal autoscaling works, what the requirements are and how you can enable it.

## How does it work

With horizontal autoscaling, additional Hypernodes will be added automatically to your main Hypernode at peak times. The extra Hypernodes will be used as PHP fpm workers.
Since there's no configuration or IP changes needed, Horizontal autoscaling has zero-downtime.

For Horizontal autoscaling you can configure some conditions. If the conditions are met from the configured settings in the Control Panel, Horizontal autoscaling will be triggered.
You can configure the following conditions:

- **CPU Load Threshold:** CPU load that is continuously monitored by the autoscaling agent. The percentage value you see is the actual load divided by the number of CPUs you have. For example, if your actual load is 2, but you have 4 CPUs, your CPU load percentage is 50%. The default setting is 70%.
- **Minimum Duration in Minutes:** Minimum amount of time the server is overloaded before autoscaling gets triggered. We monitor your CPU load every minute; autoscaling will be triggered once the CPU load condition is met for the minimum amount of time set in the Control Panel. The default setting is 15 minutes.

## Horizontal autoscaling process

### Upscaling

Once the configured conditions are met and autoscaling is triggered, we spin up extra Hypernode(s) which meets the extra calculated amount of resources you need.
We create a snapshot of your main Hypernode and attach that snapshot to the extra provisioned Hypernodes.
All the services, such as MySQL, Elasticsearch and Redis, keep running on your original Hypernode. We add the additional Hypernodes as PHP-fpm workers and will handle the incoming requests.
The load of the different autoscaling nodes will be balanced from your original Hypernode.

If the Hypernodes remains overloaded post-autoscaling, the extra needed resources will be added to handle the traffic. The autoscaling trigger is determined based on these criteria.
The greater of either:

- User-defined minimum duration for CPU threshold surpassing: Allows time to assess newly allocated resources' impact on CPU performance.
- A cooldown period of 15 minutes: Ensures a minimum interval for reassessment when the user-defined duration is less than 15 minutes.

This approach selects the longer duration between user-defined settings or the fallback duration before initiating the next autoscaling event. It ensures adequate time for evaluating resource changes on CPU performance. Autoscaling is capped at the biggest plan available on each cloud provider.

### Downscaling

If the monitor agent notices that the used resources are below the configured thresholds, the downscale operation will begin. This will lead to removing the additional servers that are no longer needed.

Downscale will happen by detaching the autoscaling instances from the main Hypernode one by one.
After a downscale operation has been completed, there will be a cooldown of 15 minutes to monitor the behaviour of the newly available resources before downscaling again.

If the amount of used resources is still below the configured threshold, another downscale operation will be triggered.

If there is need for extra resources instead, extra resources will be added again.

## Horizontal autoscaling requirements

Horizontal autoscaling is available on all the Falcon cloud plans (OpenStack).

Next to the provider, horizontal autoscaling does have a couple of additional requirements.

We will divide them between Hypernode-specific and Application-specific requirements

### Hypernode Specific Requirements

#### Operating system

- The operating system of the Hypernode should be Debian Bookworm. If you would like to upgrade the os of your Hypernode, feel free to contact our support team for help. https://www.hypernode.com/en/contact/

#### Make sure the Hypernode is a production plan

For now, we don't support horizontal autoscaling for development plans.

#### Enable and configure Varnish

To make use of Horizontal autoscaling, Varnish should be enabled and configured on the Hypernode.
You can check if Varnish is enabled on your Hypernode by running

```console
hypernode-systemctl settings varnish_enabled
```

Example output if Varnish is enabled:

```console
varnish_enabled is set to value True
```

If Varnish is not enabled, you can [enable Varnish](../varnish/how-to-enable-varnish-on-hypernode.md) by following the documentation
If varnish is enabled on your Hypernode, your Magento store should also be configured to make use of varnish.
You can verify if the Varnish host is configured correctly by running the following command from the Magento root:

```console
php bin/magento config:show  system/full_page_cache/varnish/backend_host
```

The output should show `varnish` as backend. If it is configured as something else (like `localhost` or `127.0.0.1`), you can update it by running which sets the backend host to `varnish` instead.

```console
php bin/magento config:set  system/full_page_cache/varnish/backend_host varnish
```

Additionally make sure the IP range `10.0.0.0/24` is set to the `acl_purge` section in the Varnish VCL file. The `acl_purge` section should look something similar:loaded Varnish VCL.

```console
acl purge {
    "localhost";
    "10.0.0.0/24";
}
```

#### Make sure to use MySQL 5.7 or higher

The configured MySQL version should be 5.7 or above. You can check the enabled MySQL version by running the following command.

```console
hypernode-systemctl settings mysql_version
```

Example output if MySQL version is 8.0:

```console
mysql_version is set to value 8.0
```

If your MySQL version is still set to 5.6, you can consider [upgrading](../mysql/how-to-use-mysql-on-hypernode.md) the MySQL version to a supported version for autoscaling.

After the version validation, please verify the MySQL host is set to `mysqlmaster`. You can verify this by running `cat app/etc/env.php | grep -i mysql | grep -i host` from the magento root.

You should see something similar to `'host' => 'mysqlmaster',`. If this is not the case please make sure the database connection host is set to `mysqlmaster` instead of `localhost` or `127.0.0.1` in the magento configuration file at `<magento_root>/app/etc/env.php`.

#### Disable supervisor services

Make sure supervisor is disabled and that there are no supervisor services configured.

#### Disable Podman services

Make sure podman is disabled and that there are no podman services running.

#### Disable Rootless Docker

In addition to disabling Podman services, ensure that Rootless Docker is also disabled. 

#### Configure hostnames correctly

The database, cache, session and queue of the application must be configured with correct hostnames instead of `localhost` or `127.0.0.1`. This way the services will be available across multiple hypernodes when the app is autoscaled.

Make sure the env variables (db, cache, session, queue) are not using localhost.

### Application Specific Requirements - Magento2

#### Supported CMS

Horizontal autoscaling is available for Magento 2.4.7 and higher.
To make use of Horizontal autoscaling, there are a couple of other requirements the application should meet.

#### Enable and configure Redis Persistent

Redis persistent is another requirement before you can make use of Horizontal autoscaling.
The persistent instance will be used to store the sessions so we can access the same sessions from the Horizontal autoscale Hypernodes.

You can check if Redis Persistent is enabled on your Hypernode by running

```console
hypernode-systemctl settings redis_persistent_instance
```

Example output if Redis Persistent is enabled:

```console
redis_persistent_instance is set to value True
```

If Redis Persistent instance is not enabled, you can enable the second Redis instance for sessions you run the command:

```console
hypernode-systemctl settings redis_persistent_instance --value True
```

Make sure Redis session is configured as [described](../../ecommerce-applications/magento-2/how-to-configure-redis-for-magento-2.md#configure-magento-2-to-use-redis-as-the-session-store) in our docs
Please notice the Redis host in the setup documentation. The Redis host should be set to `redismaster` instead of `localhost` or `127.0.0.1`.

#### Make sure Elasticsearch/Opensearch is configured properly

Please make sure Elasticsearch or Opensearch host is set to `elasticsearchmaster` in the Magento2 configuration file at `<magento_root>/app/etc/env.php`
More information about [Elasticsearch on Hypernode](../../hypernode-platform/tools/how-to-use-elasticsearch-on-hypernode.md)

#### Make sure RabbitMQ configured properly

Please make sure RabbitMQ host is set to `rabbitmqmaster` in the Magento2 configuration file at `<magento_root>/app/etc/env.php`
More information about [RabbitMQ o Hypernode](../../best-practices/database/how-to-run-rabbitmq-on-hypernode.md)

There is a rabbitmq user provisioned by Hypernode called hypernode-admin as a non-default user. But you can also configure RabbitMQ with a new different user of your own.
But please make sure to configure RabbitMQ without the default guest user.

#### Make sure Database storage is disabled & Remote storage is enabled and configured.

Please make sure to enable remote storage for your application and configure it correctly as only AWS-s3 remote storage drivers are supported.

Make sure that the `remote_storage` key is present in the Magento2 configuration file at `<magento_root>/app/etc/env.php` with the correct config.

More information about [S3 Remote Storage with Magento2](https://experienceleague.adobe.com/en/docs/commerce-operations/configuration-guide/storage/remote-storage/remote-storage-aws-s3)

## Enabling Horizontal Autoscaling

For detailed steps on enabling horizontal Autoscaling, please refer to our documentation: [How to enable horizontal Autoscaling?](how-to-enable-horizontal-autoscaling.md)

## Horizontal Autoscaling Pricing

To know more about the pricing, you can visit our documentation: [Horizontal Autoscaling Pricing](pricing-for-horizontal-autoscaling).
