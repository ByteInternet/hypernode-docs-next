# Config for Shopware 6

This is a sample configuration that suffices for most Shopware 6 installations:

```php
<?php

namespace Hypernode\DeployConfiguration;

$configuration = new ApplicationTemplate\Shopware6();

$productionStage = $configuration->addStage('production', 'shopware6.komkommer.store');
$productionStage->addServer('appname.hypernode.io');

return $configuration;
```

By using the Shopware6 ApplicationTemplate, a bunch of default configuration gets set in Hypernode Deploy, and should work out-of-the-box for most shopware 6 stores.