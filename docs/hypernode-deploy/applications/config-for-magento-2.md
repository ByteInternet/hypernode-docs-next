# Config for Magento 2

This is a sample configuration that suffices for most magento2 installations:

```php
<?php

namespace Hypernode\DeployConfiguration;

$configuration = new ApplicationTemplate\Magento2(['en_US']);

$productionStage = $configuration->addStage('production', 'magento2.komkommer.store');
$productionStage->addServer('appname.hypernode.io');

return $configuration;
```

By using the Magento2 ApplicationTemplate, a bunch of default configuration gets set in Hypernode Deploy, and should work out-of-the-box for most magento 2 stores.

## Common issues

### Error: The default website isn't defined. Set the website and try again.

When this error is thrown, please assure the `app/etc/config.php` has the keys `scopes` and `themes`. This is needed for the deployment software to be aware of what themes are installed without a database present (during pipeline run).

You can fix this by running the following command and then commiting the result to your codebase:

```console
$ php bin/magento app:config:dump scopes themes
Done. Config types dumped: scopes, themes
```

## Advanced

However, for advanced configurations you can override most steps and variables set by Hypernode Deploy:

### Static Content Locales

When the deployer runs `bin/magento static-content:deploy` it will require locales to know what to build, this variable is set for this. It is included when you run `new ApplicationTemplate\Magento2` or can be overridden with:

```php
$configuration->setVariable('static_content_locales', 'nl_NL en_US');
```

### Magento Themes and Split Static Deployment

For large stores with multiple themes and locales, you can use `setMagentoThemes()` to define specific themes and enable split static deployment for better build performance:

```php
<?php

namespace Hypernode\DeployConfiguration;

$configuration = new ApplicationTemplate\Magento2(['en_US']);

// Option 1: Simple theme list (uses all configured locales)
$configuration->setMagentoThemes(['Vendor/theme1', 'Vendor/theme2']);

// Option 2: Themes with specific locales per theme
$configuration->setMagentoThemes([
    'Vendor/theme1' => 'nl_NL en_US',
    'Vendor/theme2' => 'de_DE'
]);

return $configuration;
```

**Parameters:**

- `$themes` - Array of themes as `['vendor/theme', ...]` or with locale mapping `['vendor/theme' => 'nl_NL en_US', ...]`
- `$allowSplitStaticDeployment` (optional, default: `true`) - Enables split static deployment for better build performance

### Magento Backend Themes

If you're using custom admin themes or need to deploy backend static content separately, use the `setMagentoBackendThemes()` method:

```php
<?php

namespace Hypernode\DeployConfiguration;

$configuration = new ApplicationTemplate\Magento2(['en_US']);

// Set frontend themes
$configuration->setMagentoThemes([
    'Vendor/theme1' => 'nl_NL en_US',
    'Vendor/theme2' => 'de_DE'
]);

// Set backend themes separately
$configuration->setMagentoBackendThemes([
    'Vendor/admin-theme' => 'nl_NL en_US'
]);

return $configuration;
```

This automatically enables split static deployment for optimal build performance.

### Defining custom steps

You potentially need to add custom steps to the deployment, for example to build npm assets or do server actions after deployment.

```php
task('node:install', static function () {
    run("npm ci");
});

task('node:build', static function () {
    run('npm run build');
});

// Add builder task to run in the pipeline, use addDeployTask to run on the server
$configuration->addBuildTask('node:install');
$configuration->addBuildTask('node:build');
```

### Shared Files

Hypernode Deploy deploys to a new folder for every deployment, this way you compare changes, and roll back small releases. There are however some files and folders that need to be present throughout releases. Therefor we have `shared_files` and `shared_folders`. These are symlinked files and folders that are made in a shared directory and get symbolic linked between releases.

#### Override Files

```{note}
If you add these files be aware that your new files will be empty on your first release.
```

```php
$configuration->addSharedFile('pub/sitemap_en_US.xml');
```

#### Override Folders

```{note}
If you add these folders be aware that your new folders will be empty on your first release.
```

```php
$configuration->addSharedFolder('var/reports');
```

### OPcache Clearing

By default, Hypernode Deploy does **not** automatically clear the OPcache after deployment. This is because the Hypernode platform has `validate_timestamps` enabled, which automatically invalidates cached PHP files when they change.

If you're deploying to a Hypernode server which has `validate_timestamps` disabled, you can manually enable OPcache clearing by adding the following to your `deploy.php`:

```php
<?php

namespace Hypernode\DeployConfiguration;

use function Deployer\after;

$configuration = new ApplicationTemplate\Magento2(['en_US']);

// Enable automatic OPcache clearing after deployment
after('deploy:symlink', 'cachetool:clear:opcache');

return $configuration;
```

```{note}
On Hypernode, OPcache is automatically managed via `validate_timestamps`. You typically don't need to enable manual clearing unless you experience caching issues after deployment.
```
