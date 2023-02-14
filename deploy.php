<?php

declare(strict_types=1);

namespace Hypernode\DeployConfiguration;

use function Deployer\after;
use function Deployer\run;
use function Deployer\task;
use function Deployer\test;

$DOCKER_HOST = '172.17.0.2';
$DOCKER_WEBROOT = sprintf('/data/web/apps/%s/current/pub', $DOCKER_HOST);

# Disable the symlinking of /data/web/public because we're gonna be deploying both staging and prod on 1 Hypernode.
task('deploy:disable_public', function () {
    if (!test('[ -d /data/web/public ]')) {
        run('unlink /data/web/public');
        run('mkdir -p /data/web/public');
    }
    run("echo 'Not used, see /data/web/apps/ instead' > /data/web/public/index.html;");
});

# Create the venv
task('python:venv:create', static function () {
    run('mkdir -p .hypernode');
    run('virtualenv -p python3 .venv');
    run('echo export PYTHONPATH=$(pwd) >> .venv/bin/activate');
});

# Install the requirements
task('python:venv:requirements', static function () {
    run('source .venv/bin/activate && pip install -r requirements/base.txt');
});

task('python:generate_redirects', static function () {
    run('mkdir -p etc/nginx');
    run('source .venv/bin/activate && bin/generate_nginx_redirects > etc/nginx/server.redirects.conf');
});

# Build the documentation
task('python:build_documentation', static function () {
    run('source .venv/bin/activate && bin/build_docs');
    run('ln -s docs/_build/html pub');
});

# HMV configuration for when this is running in a docker
task('deploy:hmv_docker', static function () use (&$DOCKER_HOST, &$DOCKER_WEBROOT) {
    if (test('[ -f /etc/hypernode/is_docker ]')) {
        run(sprintf(
            'hypernode-manage-vhosts %s --disable-https --type generic-php --yes --webroot %s --default-server',
            $DOCKER_HOST,
            $DOCKER_WEBROOT,
        ));
    }
});

task('deploy:docs_vhost:acceptance', static function () {
    run('hypernode-manage-vhosts --https --force-https {{hostname}} --no --webroot {{current_path}}/{{public_folder}}');
})->select('stage=acceptance');

task('deploy:docs_vhost:production', static function () {
    run('hypernode-manage-vhosts --https --force-https docs.hypernode.io --no --webroot {{current_path}}/{{public_folder}}');
})->select('stage=production');

task('deploy:nginx_redirects', static function () {
    run('cp {{release_path}}/etc/nginx/server.redirects.conf /data/web/nginx/server.redirects.conf');
});

$configuration = new Configuration();
$configuration->addBuildTask('python:venv:create');
$configuration->addBuildTask('python:venv:requirements');
$configuration->addBuildTask('python:build_documentation');
$configuration->addBuildTask('python:generate_redirects');
$configuration->addDeployTask('deploy:disable_public');
$configuration->addDeployTask('deploy:hmv_docker');
$configuration->addDeployTask('deploy:docs_vhost:acceptance');
$configuration->addDeployTask('deploy:docs_vhost:production');
$configuration->addDeployTask('deploy:nginx_redirects');

# Just some sane defaults to exclude from the deploy
$configuration->setDeployExclude([
    './.git',
    './.github',
    './deploy.php',
    './.pre-commit-config.yaml',
    './documentation_urls.txt',
    './tox.ini',
    '.DS_Store',
    '.idea',
    '.gitignore',
    '.editorconfig',
    './.venv',
    './bin',
    './hypernode',
    './requirements',
    './tests',
]);

$productionStage = $configuration->addStage('production', 'docs.hypernode.io');
$productionStage->addServer('docs.hypernode.io');

# We can also deploy to a Hypernode Docker instance. To do that you go to
# https://github.com/byteinternet/hypernode-docker, make sure you
# have an instance running by for example doing:
# $ sudo docker run -P docker.hypernode.com/byteinternet/hypernode-buster-docker-php80-mysql57:latest
# and then noting the IP address (in my case 172.17.0.2). You then
# need to make sure your deploykey public key is added to the
# /data/web/.ssh/authorized_keys file. Then you should be able to
# deploy to the container as if it was a 'real' hypernode. Keep in
# mind that the hypernode-docker is not a real VM, it's just a fat
# container. This means that there won't be an init system (no systemd)
# so the processes are running in SCREENs. Also obviously you can not use
# some of the hypernode command-line functionality that depends on the
# Hypernode API (it's not a server managed by the Hypernode automation,
# just a local container running on your PC).
$dockerStage = $configuration->addStage('docker', $DOCKER_HOST);
# Define the target server (docker instance) we're deploying to
$dockerStage->addServer($DOCKER_HOST);

$testingStage = $configuration->addStage("acceptance", "docs");
$testingStage->addBrancherServer("hntestgroot")
    ->setLabels(['stage=acceptance', 'ci_ref=' . (\getenv('GITHUB_HEAD_REF') ?: 'none')]);

return $configuration;
