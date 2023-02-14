---
myst:
  html_meta:
    description: 'With Hypernode Deploy, you can create and configure an optimized
      Hypernode environment. Learn how to install and configure Hypernode Deploy. '
    title: How to install and configure Hypernode Deploy?
---

# Install and Configure Hypernode Deploy

The first step is to create and configure a `deploy.php` file which can be used by Hypernode Deploy to determine what tasks need to be executed to prepare the application for deployment and of course to what stages/servers the application needs to be deployed to.

## Install the Hypernode Deploy configuration package

```{note}
It is not a required package for Hypernode Deploy to work, so feel free to skip this part.
```

For code completion in your IDE, we recommend installing the [hypernode/deploy-configuration](https://packagist.org/packages/hypernode/deploy-configuration) package as a `dev` dependency.

```console
$ composer require --dev hypernode/deploy-configuration
```

## Create the deploy.php file

Now the `deploy.php` application can be configured. In the following example we configure a Magento 2 application to be deployed with the `en_US` locale to the production stage labelled `magento2.komkommer.store`, which has one server, namely `appname.hypernode.io`.

```php
<?php

namespace Hypernode\DeployConfiguration;

$configuration = new ApplicationTemplate\Magento2(['en_US']);

$productionStage = $configuration->addStage('production', 'magento2.komkommer.store');
$productionStage->addServer('appname.hypernode.io');

return $configuration;
```

```{note}
More configurations can be found at:
- [Hypernode Deploy for Magento 1](../applications/config-for-magento-1.md)
- [Hypernode Deploy for Magento 2](../applications/config-for-magento-2.md)
- [Hypernode Deploy for Shopware 6](../applications/config-for-shopware-6.md)
```

In the next step we're going to configure a CI/CD pipeline to let Hypernode Deploy execute the `deploy.php` configuration.
