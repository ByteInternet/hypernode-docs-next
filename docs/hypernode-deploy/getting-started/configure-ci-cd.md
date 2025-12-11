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

## How Hypernode Deploy pipelines work

Hypernode Deploy uses a **two-step architecture** designed to keep your server runtime fast and efficient:

### 1. Build step (runs in the CI/CD pipeline)

The build step runs entirely within your CI/CD pipeline's infrastructure (GitHub Actions, GitLab CI, or Bitbucket Pipelines) and **never touches your production server**. This is where all the heavy, resource-intensive work happens:
The build step handles all resource-intensive operations: installing dependencies with `composer install`, compiling frontend assets and themes, running code minification and image optimization, and performing any other heavy preparation tasks needed to ready your application for deployment.

By performing these heavy operations in the pipeline, you avoid consuming precious server resources. Your production server stays responsive and dedicated to serving customer requests, not compiling code or building assets.

The build step produces a **build artifact** (typically `build.tgz`) containing your ready-to-deploy application.

### 2. Deploy step (runs in the CI/CD pipeline, deploys to server)

The deploy step also runs in your CI/CD pipeline infrastructure, but this time it:

- Downloads the build artifact created in the build step
- Connects to your Hypernode server via SSH
- Transfers the pre-built application to the server
- Runs deployment tasks like:
  - Database migrations
  - Cache clearing
  - Symlink switching (zero-downtime deployments)
  - Running post-deployment hooks

This way your artifact deploys in seconds, seserver resources stay focused on serving customers, and you can deploy the same tested build to multiple environments without rebuilding.

## Prepare the secrets

Hypernode Deploy needs a few 'credentials' to be able to function. The necessary credentials are:

1. The private SSH key as base64 encoded string. (`SSH_PRIVATE_KEY`)
1. The composer auth.json file as base64 encoded string, optional. (`DEPLOY_COMPOSER_AUTH`)
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

We assume you may want to use the Hypernode Brancher feature to spin up temporary nodes based on a specific Hypernode. SSH into that Hypernode and copy the contents of the `/etc/hypernode/hypernode_api_token` file.

Then go to your Github repository on Github.com and go to **Settings -> Secrets -> Actions**. Click the **New repository secret**, fill in `HYPERNODE_API_TOKEN` as the name, paste the contents of your `hypernode_api_token` file and press **Save**.

```{note}
CI/CD configuration templates can be found here:
- [Github Actions](../pipelines/github-actions.md)
- [Gitlab CI](../pipelines/gitlab-ci.md)
- [Bitbucket Pipelines](../pipelines/bitbucket-pipelines.md)
```

[1]: https://github.com/features/actions
[2]: https://about.gitlab.com/features/continuous-integration/
[3]: https://bitbucket.org/product/features/pipelines
