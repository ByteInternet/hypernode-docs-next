# GitHub Actions

```{note}
This guide assumes you have already configured Hypernode Deploy with a `deploy.php` file in your project root. If you haven't set this up yet, please follow the [installation and configuration guide](../getting-started/install-and-configure-hypernode-deploy.md) first.
```

## Configuring SSH authentication

Hypernode Deploy will need a pair of SSH keys for authentication to the server.

First, we generate an SSH keypair on one of your servers (e.g., production), copy the public key to the `~/.ssh/authorized_keys` file
on all servers you want to deploy to, and encode the private key with base64. We'll use this base64-encoded private key later on.

```console
app@abc-example-magweb-cmbl:~$ ssh-keygen -t ed25519 -C gh-actions-deploy -f gh-actions-deploy -q -P ""
app@abc-example-magweb-cmbl:~$ cat gh-actions-deploy.pub >> ~/.ssh/authorized_keys
app@abc-example-magweb-cmbl:~$ cat gh-actions-deploy | base64 -w0  # encode the private key with base64
LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyWlhrdGRqRUFBQUFBQkc1dmJtV...
```

```{note}
If you have multiple environments (production, acceptance, staging), make sure to add the public key to each server through the Control Panel.
```

Now go to your GitHub project and go to **Settings -> Secrets and variables -> Actions**.

1. Click **New repository secret**.
1. Set the **Name** to `SSH_PRIVATE_KEY`.
1. Set the **Value** to the base64-encoded private key we generated earlier.
1. Click **Add secret**.

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
    # See https://quay.io/repository/hypernode/deploy?tab=tags for all possible tags.
    container: quay.io/hypernode/deploy:latest-php8.4-node22
    steps:
    - uses: actions/checkout@v3
    - uses: actions/cache@v3
      with:
        path: /tmp/composer-cache
        key: ${{ runner.os }}-composer
    - run: mkdir -p $HOME/.ssh
    - run: hypernode-deploy build -vvv
      env:
        SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
    - name: archive production artifacts
      uses: actions/upload-artifact@v4
      with:
        name: deployment-build
        path: build/build.tgz
        retention-days: 7
```

````{note}
Don't forget to set the specifications of the image to what your project needs. The same goes for the deploy steps.
For example, if your project needs PHP 8.4 and Node.js 22, set the image to:
```yaml
jobs:
  build:
    container: quay.io/hypernode/deploy:latest-php8.4-node22
    ...
```
````

## Deploy to production

Create a file called `.github/workflows/deploy_production.yml` with the following contents.

```yaml
name: Deploy application to production

on:
  push:
    branches:
      - 'master'
      - 'main'

jobs:
  build:
    uses: ./.github/workflows/build.yml
    secrets: inherit

  deploy:
    needs: build
    runs-on: ubuntu-latest
    # Concurrency takes any arbitrary value, but this prevents multiple deployments happening at the same time.
    # We set the concurrency to production for this deployment workflow.
    concurrency: production
    environment:
      name: production
      url: https://www.example.com
    container: quay.io/hypernode/deploy:latest-php8.4-node22
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
    - run: mkdir -p $HOME/.ssh
    - run: hypernode-deploy deploy production -vvv  # Deploy production stage defined in deploy.php
      env:
        SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
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
    secrets: inherit

  deploy:
    needs: build
    runs-on: ubuntu-latest
    # Concurrency takes any arbitrary value, but this prevents multiple deployments happening at the same time.
    # We set the concurrency to acceptance for this deployment workflow.
    concurrency: acceptance
    environment:
      name: acceptance
      url: https://acceptance.example.com
    container: quay.io/hypernode/deploy:latest-php8.4-node22
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
    - run: mkdir -p $HOME/.ssh
    - run: hypernode-deploy deploy acceptance -vvv  # Deploy acceptance/staging stage defined in deploy.php
      env:
        SSH_PRIVATE_KEY: ${{ secrets.SSH_PRIVATE_KEY }}
```

## Next steps

After you've added these files, commit your changes and make sure the changes are newly present on the branches configured in your pipeline files. By default, these branches are `master` (or `main`) and `acceptance`.

Once pushed, you will see a GitHub Action automatically run in your repository's "Actions" tab.
