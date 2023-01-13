---
myst:
  html_meta:
    description: Configure your CI/CD pipeline with Hypernode Deploy. Get up and running
      quickly with easy-to-follow steps and secure credentials to ensure your data
      is safe.
    title: How to configure CI/CD on Hypernode?
---

# Configure CI/CD

There are many CI/CD pipelines available, but it's probably best to stick with the pipeline system that's tied with your VCS (version control system), like [Github Actions][1] for Github, [Gitlab CI][2] for Gitlab and [Bitbucket Pipelines][3] for Bitbucket.

In this example we'll be covering the Github Actions CI/CD configuration.

## Prepare the secrets

Hypernode Deploy needs a few 'credentials' to be able to function. The necessary credentials are:

1. The private SSH key. (`SSH_PRIVATE_KEY`)
1. The composer auth.json file, optional. (`DEPLOY_COMPOSER_AUTH`)
   - This is only necessary when your project needs to access private Composer repositories.
1. The Hypernode API token, optional. (`HYPERNODE_API_TOKEN`)
   - This is only necessary when you make use of Hypernode API driven features like Brancher.

These credentials can usually be stored as 'secret' environment variables in the pipeline system.

### Private SSH key

If you don't have a dedicated SSH key used for deploying the application, open up a terminal and run the following command:

```console
$ ssh-keygen -f deploy.key -N ''
Generating public/private rsa key pair.
Your identification has been saved in deploy.key
Your public key has been saved in deploy.key.pub
The key fingerprint is:
SHA256:qEYqQ7WfL8MEHDnjntKUQwJQl1+RjAnX/gvGHS9a60w timon@thinkus
The key's randomart image is:
+---[RSA 3072]----+
|=.. +o.=.o       |
| . B..o =        |
|  =.=. o         |
|  .B. ... .      |
| .+.= ..So o     |
|.. *.o. + = .    |
|o o =o . +E+     |
| o . +. .oo      |
|      o. .o      |
+----[SHA256]-----+
```

Copy the contents of the private key file (`deploy.key` in example above).

Then go to your Github repository on Github.com and go to **Settings -> Secrets -> Actions**. Click the **New repository secret**, fill in `SSH_PRIVATE_KEY` as the name, paste the contents of your key file and press **Save**.

Then copy the contents of the public key file (`deploy.key.pub`) and paste the contents as a new line entry in the `~/.ssh/authorized_keys` file of each relevant server (for this example staging and production). This enables us to authenticate ourselves to the servers from the CI/CD system.

### Composer authentication

***Optional step***

We assume you have an `auth.json` file in either your project directory or your Composer home directory. Copy the contents of this file.

Then go to your Github repository on Github.com and go to **Settings -> Secrets -> Actions**. Click the **New repository secret**, fill in `DEPLOY_COMPOSER_AUTH` as the name, paste the contents of your `auth.json` file and press **Save**.

### Hypernode API authentication

***Optional step***

We assume you want to use the Hypernode Brancher feature to spin up temporary nodes based on a specific Hypernode. SSH into that Hypernode and copy the contents of the `/etc/hypernode/hypernode_api_token` file.

Then go to your Github repository on Github.com and go to **Settings -> Secrets -> Actions**. Click the **New repository secret**, fill in `HYPERNODE_API_TOKEN` as the name, paste the contents of your `hypernode_api_token` file and press **Save**.

## Create the workflow file

Create the `.github/workflows` directory structure:

```console
$ mkdir -p .github/workflows
```

In that directory, create a file named `deploy.yaml` and fill in the following contents:

```yaml
name: Build and deploy application

on:
  push:
    branches:
      - 'master'  # Your main/master/production branch
      - 'staging' # Your staging/acceptance branch
```

### Build step

The first thing we want to run is the `build` step, which does all the dirty work to prepare the application for the web. Add the following configuration to the `deploy.yaml` file.

```yaml
env:
  COMPOSER_CACHE_DIR: /tmp/composer-cache

jobs:
  build:
    runs-on: ubuntu-latest
    # Here we use the Hypernode Deploy v3 image with PHP 8.1 and Node.js 18
    container: quay.io/hypernode/deploy:3.0-php8.1-node18
    steps:
      - uses: actions/checkout@v2
      - uses: actions/cache@v2
        with:
          path: /tmp/composer-cache
          key: ${{ runner.os }}-composer
      - uses: webfactory/ssh-agent@v0.5.4
        with:
          ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}
      - run: hypernode-deploy build -vvv
        env:
          DEPLOY_COMPOSER_AUTH: ${{ secrets.DEPLOY_COMPOSER_AUTH }}
      - name: archive production artifacts
        uses: actions/upload-artifact@v3
        with:
          name: deployment-build
          path: build/build.tgz
```

### Deploy step

For the deployment part, add a job called `deploy` to the `jobs` configuration.

```yaml
...

jobs:
  build:
    ...
  deploy:
    needs: build
    runs-on: ubuntu-latest
    # Here we use the Hypernode Deploy v3 image with PHP 8.1 and Node.js 18
    container: quay.io/hypernode/deploy:3.0-php8.1-node18
    steps:
      - uses: actions/checkout@v2
      - name: download build artifact
        uses: actions/download-artifact@v3
        with:
          name: deployment-build
          path: build/
      - uses: webfactory/ssh-agent@v0.5.4
        with:
          ssh-private-key: ${{ secrets.SSH_PRIVATE_KEY }}
      - run: mkdir -p $HOME/.ssh
      - name: deploy to staging     # Staging deployment happens here
        if: github.ref == 'refs/heads/staging'
        run: hypernode-deploy deploy staging -vvv
      - name: deploy to production  # Production deployment happens here
        if: github.ref == 'refs/heads/master'
        run: hypernode-deploy deploy production -vvv
      - name: cleanup acquired resources
        if: ${{ always() }}
        run: hypernode-deploy cleanup
```

```{note}
CI/CD configuration templates can be found here:
- [Github Actions](../pipelines/github-actions.md)
- [Gitlab CI](../pipelines/gitlab-ci.md)
- [Bitbucket Pipelines](../pipelines/bitbucket-pipelines.md)
```

[1]: https://github.com/features/actions
[2]: https://about.gitlab.com/features/continuous-integration/
[3]: https://bitbucket.org/product/features/pipelines
