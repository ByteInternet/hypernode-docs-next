---
myst:
  html_meta:
    description: Configure your Hypernode server on Deploytime to rapidly test upgrades
      with service upgrades
    title: Configure Hypernode settings on Deployment
---

# Configure Hypernode settings on Deployment

Hypernode Deploy allows you to change configurations to the Hypernode server on-the-fly and on deploy time, this is extremely beneficial when doing a MySQL upgrade or Node.js versions controlled by your source version control.

Here's a list of changes you can make to the Hypernode:

- Hypernode Systemctl Configuration
- Cron Configuration
- Nginx vhost Configuration
- Supervisor Configuration
- Varnish Configuration

## Hypernode Systemctl Configuration

You can use Hypernode's systemctl utility to change crucial settings about the Hypernode server. This can also be configured in your deployments. More information about the systemctl utility can be found [here](../../hypernode-platform/tools/how-to-use-the-hypernode-systemctl-cli-tool.md).

You can simply define these settings configurations by using this code in your `deploy.php` file:

```php
$configuration->setPlatformConfigurations([
    new PlatformConfiguration\HypernodeSettingConfiguration('supervisor_enabled', 'True'),
    new PlatformConfiguration\HypernodeSettingConfiguration('rabbitmq_enabled', 'True'),
    new PlatformConfiguration\HypernodeSettingConfiguration('elasticsearch_enabled', 'False'),
    new PlatformConfiguration\HypernodeSettingConfiguration('opensearch_enabled', 'True'),
    new PlatformConfiguration\HypernodeSettingConfiguration('varnish_enabled', 'True'),
    new PlatformConfiguration\HypernodeSettingConfiguration('nodejs_version', '20'),
]);
```

## Cron Configuration

Lots of applications need a set of cron jobs for the application to function correctly. Instead of having to configure this on the server manually on each change, you can set this up on the Deployment.

For example, start creating the `./etc/cron` folder and putting in the following:

```bash
* * * * * echo 'Hello world!' >> /data/web/cron.log
```

The contents of this file will be written and get replaced to your crontab as a separate block on each deployment, this makes it easy to manage and update the crons.

Now add the cron configuration to your `deploy.php`

```php
$configuration->setPlatformConfigurations([
    new PlatformConfiguration\CronConfiguration('etc/cron')
]);
```

## Nginx vhost Configuration

You can use Hypernode Deploy to apply nginx configurations set up for your vhost, you do this by creating a new folder for your nginx configurations in `./etc/nginx` and placing your configs there.

```{note}
All existing nginx configurations will be replaced on first deployment when there's already nginx configurations known for this vhost name.
```

Now add the nginx configuration to your `deploy.php`

```php
$configuration->setPlatformConfigurations([
    new PlatformConfiguration\NginxConfiguration('etc/nginx')
]);
```

## Supervisor Configuration

Setting up a supervisor configuration is sometimes a requirement for your application, you can easily do this by creating the `./etc/supervisor` folder and creating the supervisor files.

For example, create your `./etc/supervisor/application.conf` file and adding the supervisor configuration to your `deploy.php`

```php
$configuration->setPlatformConfigurations([
    new PlatformConfiguration\SupervisorConfiguration('etc/supervisor')
]);
```

## Varnish Configuration

You can update your varnish configuration by adding a file at `etc/varnish.vcl` , and configuring it in `deploy.php` like so:

```php
$configuration->setPlatformConfigurations([
    new PlatformConfiguration\VarnishConfiguration(
      $configFile: 'etc/varnish.vcl',
      $version: '7.x'
    )
]);
```
