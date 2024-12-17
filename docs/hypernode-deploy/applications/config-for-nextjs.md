# Config for Magento 2

```{note}
NextJS is not officially supported on the Hypernode Platform. So please use this at your own risk,.
```

Configuration to use as Hypernode Deploy deploy.php for a NextJS webserver application:

```php
<?php

declare(strict_types=1);

namespace Hypernode\DeployConfiguration;

use function Deployer\run;
use function Deployer\task;
use function Deployer\test;
use function Deployer\within;

task('node:install', static function () {
    run('npm ci');
});

task('node:build', static function () {
    run('npm run build');
});

task('deploy:pm2:install', static function() {
    if (!test('grep -q "/data/web/.local/bin" ~/.bashrc')) {
        run('echo "export PATH=/data/web/.local/bin:$PATH" >> ~/.bashrc');
        run('source ~/.bashrc');
    }

    run('npm install -g pm2 --prefix /data/web/.local');
});

task('deploy:pm2:restart', static function() {
    within('{{release_path}}', function () {
        run('pm2 startOrRestart ecosystem.config.js --env prod');
    });
});

$configuration = new Configuration();

$configuration->setPlatformConfigurations([
    new PlatformConfiguration\NginxConfiguration('etc/nginx'),
    new PlatformConfiguration\HypernodeSettingConfiguration('supervisor_enabled', 'False'),
    new PlatformConfiguration\HypernodeSettingConfiguration('rabbitmq_enabled', 'False'),
    new PlatformConfiguration\HypernodeSettingConfiguration('elasticsearch_enabled', 'False'),
    new PlatformConfiguration\HypernodeSettingConfiguration('opensearch_enabled', 'False'),
    new PlatformConfiguration\HypernodeSettingConfiguration('varnish_enabled', 'False'),
    new PlatformConfiguration\HypernodeSettingConfiguration('nodejs_version', '20'),
]);

$configuration->addBuildTask('node:env');
$configuration->addBuildTask('node:install');
$configuration->addBuildTask('node:build');

$configuration->addDeployTask('deploy:pm2:install');
$configuration->addDeployTask('deploy:pm2:restart');

$configuration->setSharedFiles([
    '.env'
]);

$configuration->setDeployExclude([
    './.git',
    './deploy.php',
    '.gitignore',
    './etc'
]);

$productionStage = $configuration->addStage('production', 'my-next-application.nl');
$productionStage->addServer('app.hypernode.io');

$acceptanceStage = $configuration->addStage('acceptance', 'my-next-application.nl');
$acceptanceStage->addBrancherServer('app')
    ->setLabels(['stage=acceptance']);

return $configuration;
```

This will:

- Configure the Hypernode settings optimal for the least load of non-used applications and servers.
- Install [PM2](https://pm2.keymetrics.io/) if not present on the server.
- Sets up a vhost for application.
- Sets up the nginx configuration to proxy to the NextJS server.

You will still need to add the nginx configuration file, so create the `./etc/nginx/server.headless.conf` file:

```nginx
location / {
    proxy_pass http://localhost:3000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection 'upgrade';
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_cache_bypass $http_upgrade;

    # Optional: set maximum response time to 60 seconds
    proxy_read_timeout 60s;
    proxy_connect_timeout 60s;
}

# Optional: specific location for static assets if they are served by Next.js
location /_next/ {
    proxy_pass http://localhost:3000;
    proxy_cache_bypass $http_upgrade;
}
```

And to save configuration about pm2, add the `ecosystem.config.js` file:

```
module.exports = {
    apps: [
      {
        name: 'my-next-app',
        exec_mode: 'cluster',
        instances: 'max', // Or a number of instances
        script: 'node_modules/next/dist/bin/next',
        args: 'start'
      }
    ]
  }
```