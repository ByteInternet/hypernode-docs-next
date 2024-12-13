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

These are the steps that will be executed by running your deployment:

## Advanced

However, for advanced configurations you can override most steps and variables set my Hypernode Deploy:

### Static Content Locales

When the deployer runs `bin/magento static-content:deploy` it will require locales to know what to build, this variable is set for this. It is included when you run `new ApplicationTemplate\Magento2` or can be overriden with:

```php
$this->setVariable('static_content_locales', 'nl_NL en_US');
```

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
$configuration->addSharedFile('var/reports');
```
