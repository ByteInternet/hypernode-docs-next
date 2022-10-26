<?php
namespace Hypernode\DeployConfiguration;

use function Deployer\run;
use function Deployer\task;
use function Deployer\currentHost;
use function Deployer\upload;

$DOCKER_HOST = '172.17.0.2';
$DOCKER_WEBROOT = sprintf('/data/web/apps/%s/current/pub', $DOCKER_HOST);

# Disable the symlinking of /data/web/public because we're gonna be deploying both staging and prod on 1 Hypernode.
task('deploy:disable_public', function () {
    run("if ! test -d /data/web/public; then unlink /data/web/public; mkdir /data/web/public; fi");
    run("echo 'Not used, see /data/web/apps/ instead' > /data/web/public/index.html;");
});

# Create the venv
task('python:venv:create', static function () {
    run('mkdir -p {{release_path}}/.hypernode');
    run('virtualenv -p python3 {{release_path}}/.venv');
});

# Install the requirements
task('python:venv:requirements', static function () {
    run('source {{release_path}}/.venv/bin/activate && pip install -r {{release_path}}/requirements/base.txt');
});

# Build the documentation
task('python:build_documentation', static function () {
    run('source {{release_path}}/.venv/bin/activate && cd {{release_path}} && {{release_path}}/bin/build_docs');
    run('ln -s {{release_path}}/docs/_build/html {{release_path}}/pub');
});

# HMV configuration for when this is running in a docker
task('deploy:hmv_docker', static function () use (&$DOCKER_HOST, &$DOCKER_WEBROOT) {
    run(sprintf('if test -f /etc/hypernode/is_docker; then hypernode-manage-vhosts %s --disable-https --type generic-php --yes --webroot %s --default-server; fi', $DOCKER_HOST, $DOCKER_WEBROOT));
});


$configuration = new Configuration();
$configuration->addDeployTask('deploy:disable_public');
$configuration->addDeployTask('python:venv:create');
$configuration->addDeployTask('python:venv:requirements');
$configuration->addDeployTask('python:build_documentation');
$configuration->addDeployTask('deploy:hmv_docker');

# Just some sane defaults to exclude from the deploy
$configuration->setDeployExclude([
    './.git',
    './.github',
    './deploy.php',
    './.gitlab-ci.yml',
    './Jenkinsfile',
    '.DS_Store',
    '.idea',
    '.gitignore',
    '.editorconfig',
    'etc/'
]);

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

return $configuration;
