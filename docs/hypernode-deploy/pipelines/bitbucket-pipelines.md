# Bitbucket Pipelines

## Configuring deployment environments

To start using Bitbucket Pipelines, we need to prepare the environments we want to deploy to.

For example, these environments can be:

- production
- acceptance (or staging)
- test

### Configuring the production environment

Hypernode Deploy will need a pair of SSH keys for authentication to the server.

First, we generate an SSH keypair on the production server, copy the public key to the `~/.ssh/authorized_keys` file
and encode the private key with base64. We'll use this base64-encoded private key later on.

```console
app@abc-example-magweb-cmbl:~$ ssh-keygen -t ed25519 -C bb-pipelines-deploy -f bb-pipelines-deploy -q -P ""
app@abc-example-magweb-cmbl:~$ cat bb-pipelines-deploy.pub >> ~/.ssh/authorized_keys
app@abc-example-magweb-cmbl:~$ cat bb-pipelines-deploy | base64 -w0  # encode the private key with base64
LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyWlhrdGRqRUFBQUFBQkc1dmJtV...
```

Now go to your Bitbucket repository and enable Bitbucket pipelines being going to **Repository settings -> Pipelines -> Settings** and turn on **Enable Pipelines**.

Now go to **Repository settings -> Pipelines -> Repository variables**.

1. Create a new variable with name `SSH_PRIVATE_KEY`, mark this variable as Secured.
1. Set the **Value** to the base64-encoded private key we generated earlier.
1. Click **Add**.

To add hosts to the Pipeline known hosts go to **Repository settings -> Pipelines -> SSH Keys**

1. Set **Host address** to your hypernode instance (e.g. _appname.hypernode.io_)
1. Click **Fetch** to fetch the hostname fingerprint
1. Click **Add Host** to add host to known hosts
1. Repeat this for all hosts the pipeline will connect to (for example production, staging)

## Build

Create the file `bitbucket-pipelines.yml` with the contents below.
This workflow will be used in other workflows.

```yaml
image: quay.io/hypernode/deploy:3-php8.2-node18

definition:
  steps:
    - step: &hypernode-build
        name: Build
       script:
         - hypernode-deploy build
       artifacts:
         - build/**
```

````{note}
Don't forget to set the specifications of the image to what your project needs. The same goes for the deploy steps.
For example, if your project needs PHP 7.4 and Node.js 16, set the image to:
```yaml
jobs:
  build:
    container: quay.io/hypernode/deploy:3-php7.4-node16
    ...
```
````

## Deploy to production

Add the following to the `bitbucket-pipelines.yml` file.

```yaml
pipelines:
  # Deploy to production
  master:
    - step: *hypernode-build
    - step:
        name: Deploy to production
        deployment: production
        script:
          - hypernode-deploy deploy production
```

## Deploy to acceptance

If you have an acceptance (or staging) stage in your deployment flow, here's an example on how to deploy that.

```yaml
pipelines:
  # Deploy to acceptance
  acceptance: # acceptance/staging branch
    - step: *hypernode-build
    - step:
        name: Deploy to staging
        deployment: staging
        script:
          - hypernode-deploy deploy staging
```
