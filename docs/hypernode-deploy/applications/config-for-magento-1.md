---
myst:
  html_meta:
    description: Example Hypernode Deploy deploy.php configuration for a Magento 1
      shop, using the Magento 1 application template.
    title: Hypernode Deploy Config for Magento 1 | Hypernode
---

# Config for Magento 1

This is a sample configuration that suffices for most Magento 1 installations:

```php
<?php

namespace Hypernode\DeployConfiguration;

$configuration = new ApplicationTemplate\Magento1();

$productionStage = $configuration->addStage('production', 'magento1.komkommer.store');
$productionStage->addServer('appname.hypernode.io');

return $configuration;
```

By using the Magento1 ApplicationTemplate, a bunch of default configuration gets set in Hypernode Deploy, and should work out-of-the-box for most Magento 1 shops.

```{warning}
Magento 1 reached its end of life in June 2020 and no longer receives official security patches. If you still run Magento 1, we advise you to plan a migration to Magento 2 or another supported platform.
```
