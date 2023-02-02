# Gitlab CI

## Configuring deployment environments

To start using Gitlab CI, we need to prepare the environments we want to deploy to.

For example, these environments can be:

- production
- acceptance (or staging)
- test

### Configuring the production environment

Hypernode Deploy will need a pair of SSH keys for authentication to the server.

First, we generate an SSH keypair on the production server, copy the public key to the `~/.ssh/authorized_keys` file
and encode the private key with base64. We'll use this base64-encoded private key later on.

```console
app@abc-example-magweb-cmbl:~$ ssh-keygen -t ed25519 -C gitlab-ci-deploy -f gitlab-ci-deploy -q -P ""
app@abc-example-magweb-cmbl:~$ cat gitlab-ci-deploy.pub >> ~/.ssh/authorized_keys
app@abc-example-magweb-cmbl:~$ cat gitlab-ci-deploy | base64 -w0  # encode the private key with base64
LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyWlhrdGRqRUFBQUFBQkc1dmJtV...
```

Now go to your Gitlab project and go to **Deployments -> Environments**.

1. Create a new environment called `production`, if it doesn't exist yet.
1. Go to **Settings -> CI/CD -> Variables**.
1. Click `Add variables`.
1. Set **Key** to `SSH_PRIVATE_KEY`.
1. Set **Value** to the base64-encoded private key we generated earlier.
1. Set **Environment scope** to `production`.
1. If you don't have protected branches configured, uncheck the setting **Protect variable**.
1. Check the setting **Mask variable**.
1. Click **Add variable**.

### Configuring the acceptance environment

If you have an acceptance (or staging) environment, repeat the same steps for the production environment, but now for
your acceptance environment, with the Gitlab environment name `acceptance`.

## Build

Create a file called `.gitlab-ci.yml` with the contents below.

This sets the container image, defines the CI/CD stages and defines the build step (part of the build stage).

```yaml
# See https://quay.io/repository/hypernode/deploy?tab=tags for all possible tags.
image: quay.io/hypernode/deploy:3-php8.1-node18

stages:
  - build
  - deploy

build:
  stage: build
  only:
    - merge_requests
    - acceptance
    - master
  script:
    - hypernode-deploy build -vvv
  artifacts:
    paths:
      - build/**
```

Don't forget to set the specifications of the image to what your project needs,
so if for example your project needs PHP 7.4 and Node.js 16, set the image to:

```yaml
image: quay.io/hypernode/deploy:3-php7.4-node16
```

## Deploy to production

Add the following to the `.gitlab-ci.yml` file.

```yaml
# Deploy to production
deploy_production:
  stage: deploy
  only:
    - master  # production branch
  script:
    - hypernode-deploy deploy production
  environment:
    name: production
    url: https://www.example.com
```

## Deploy to acceptance

If you have an acceptance (or staging) stage in your deployment flow, here's an example on how to deploy that.

```yaml
# Deploy to acceptance
deploy_acceptance:
  stage: deploy
  only:
    - acceptance  # acceptance/staging branch
  script:
    - hypernode-deploy deploy acceptance
  environment:
    name: acceptance
    url: https://acceptance.example.com
```
