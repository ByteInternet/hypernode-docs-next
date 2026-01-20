# Migrating from Hipex Deploy to Hypernode Deploy

If you're making use of Hipex Deploy and are in the process of migrating to a Hypernode server, you need to also switch from Hipex Deploy to Hypernode Deploy. We've tried our best to make this upgrade as seamless as possible.

# Changing the configuration file
The `deploy.php` configuration file needs minimal changes, actually just the hostname of the hypernode.

``` php
// Hipex config
$productionStage = $configuration->addStage('production', 'mystore.com', 'myuser');
$productionStage->addServer('production1234.hipex.io');

// Hypernode config
$productionStage = $configuration->addStage('production', 'mystore.com', 'app');
$productionStage->addServer('hntestgroot.hypernode.io');
```

That's it, no need for other changes in the `deploy.php` file.
You could do a few more changes to have proper autocompletion in the `deploy.php`  file. That's possible by replacing the composer package `hipex/deploy-configuration` with `hypernode/deploy-configuration:^1.0` and changing the `HipexDeployConfiguration` namespace with `Hypernode\DeployConfiguration` within the `deploy.php` file.

# Changing the CI file

Whether you're using Github Actions, Bitbucket Pipelines, Gitlab CI or even something else, you most likely are making use of the Hipex deploy container image:

```
hipex/deploy:v2.13.0-alpha.3-php8.1-node18
```

Change the container image to the following:

```
quay.io/hypernode/deploy:1.0-php8.1-node18
```

Please make sure you specify the right PHP and Node.js version in the image tag.

This is the only change really needed for the CI file. We do suggest changing the `hipex-deploy` command to `hypernode-deploy`, as we currently provide it as a compatibility feature.