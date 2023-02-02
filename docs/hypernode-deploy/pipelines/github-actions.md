# GitHub Actions

## Configuring deployment environments

To start using GitHub Actions, we need to prepare the environments we want to deploy to.

For example, these environments can be:

- production
- acceptance (or staging)
- test

### Configuring the production environment

Hypernode Deploy will need a pair of SSH keys for authentication to the server.

First, we generate an SSH keypair on the production server, copy the public key to the `~/.ssh/authorized_keys` file
and encode the private key with base64. We'll use this base64-encoded private key later on.

```console
app@abc-example-magweb-cmbl:~$ ssh-keygen -t ed25519 -C gh-actions-deploy -f gh-actions-deploy -q -P ""
app@abc-example-magweb-cmbl:~$ cat gh-actions-deploy.pub >> ~/.ssh/authorized_keys
app@abc-example-magweb-cmbl:~$ cat gh-actions-deploy | base64 -w0  # encode the private key with base64
LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyWlhrdGRqRUFBQUFBQkc1dmJtV...
```

Now go to your GitHub project and go to **Settings -> Environments**.

1. Create a new environment called `production`, if it doesn't exist yet.
1. Click the `production` environment and click `Add secret`.
1. Set the name of the secret to `SSH_PRIVATE_KEY`.
1. Set the value of the secret to the base64-encoded private key we generated earlier.
1. Click **Add secret**.

### Configuring the acceptance environment

If you have an acceptance (or staging) environment, repeat the same steps for the production environment, but now for
your acceptance environment, with the GitHub environment name `acceptance`.

## Build

To get started, we need to make sure the `.github/workflows` directory structure exists.

```bash
mkdir -p .github/workflows
```

Then create the file `.github/workflows/build.yml` with the contents below.
This workflow will be used in other workflows.

```yaml
name: Build application

on:
  workflow_call:

jobs:
  build:
    runs-on: ubuntu-latest
    container: quay.io/hypernode/deploy:3-php8.1-node18
    steps:
    - uses: actions/checkout@v3
    - uses: actions/cache@v3
      with:
        path: /tmp/composer-cache
        key: ${{ runner.os }}-composer
    - uses: webfactory/ssh-agent@v0.7.0
      with:
        ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}
    - run: hypernode-deploy build -vvv
    - name: archive production artifacts
      uses: actions/upload-artifact@v3
      with:
        name: deployment-build
        path: build/build.tgz
        retention-days: 7
```

## Deploy to production

Create a file called `.github/workflows/deploy_production.yml` with the following contents.

```yaml
name: Deploy application to production

on:
  push:
    branches:
      - 'master'  # production branch

jobs:
  build:
    uses: ./.github/workflows/build.yml

  deploy:
    needs: build
    runs-on: ubuntu-latest
    # Concurrency takes any arbitrary value, but this prevents multiple deployments happening at the same time.
    # We set the concurrency to production for this deployment workflow.
    concurrency: production
    environment:
      name: production
      url: https://www.example.com
    container: quay.io/hypernode/deploy:3-php8.1-node18
    steps:
    - uses: actions/checkout@v3
    - name: download build artifact
      uses: actions/download-artifact@v3
      with:
        name: deployment-build
        path: build/
    - uses: actions/cache@v3
      with:
        path: /tmp/composer-cache
        key: ${{ runner.os }}-composer
    - uses: webfactory/ssh-agent@v0.7.0
      with:
        ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}
    - run: mkdir -p $HOME/.ssh
    - run: hypernode-deploy deploy production -vvv  # Deploy production stage defined in deploy.php
```

## Deploy to acceptance

Create a file called `.github/workflows/deploy_acceptance.yml` with the following contents.

```yaml
name: Deploy application to acceptance

on:
  push:
    branches:
      - 'acceptance'  # acceptance/staging branch

jobs:
  build:
    uses: ./.github/workflows/build.yml

  deploy:
    needs: build
    runs-on: ubuntu-latest
    # Concurrency takes any arbitrary value, but this prevents multiple deployments happening at the same time.
    # We set the concurrency to acceptance for this deployment workflow.
    concurrency: acceptance
    environment:
      name: acceptance
      url: https://acceptance.example.com
    container: quay.io/hypernode/deploy:3-php8.1-node18
    steps:
    - uses: actions/checkout@v3
    - name: download build artifact
      uses: actions/download-artifact@v3
      with:
        name: deployment-build
        path: build/
    - uses: actions/cache@v3
      with:
        path: /tmp/composer-cache
        key: ${{ runner.os }}-composer
    - uses: webfactory/ssh-agent@v0.7.0
      with:
        ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}
    - run: mkdir -p $HOME/.ssh
    - run: hypernode-deploy deploy acceptance -vvv  # Deploy acceptance/staging stage defined in deploy.php
```
