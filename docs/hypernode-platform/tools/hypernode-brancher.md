---
myst:
  html_meta:
    description: 'Hypernode Brancher is a powerful tool that allows users to create
      and manage temporary servers based on their production Hypernode. Learn more. '
    title: Hypernode Brancher | Everything you need to know
redirect_from:
  - /en/support/solutions/articles/48001227297-hypernode-brancher/
---

# Hypernode Brancher

Hypernode Brancher is a powerful tool that allows users to create and manage temporary servers based on their production Hypernode.

Hypernode Brancher is fully integrated with the Hypernode platform. With just a few simple commands, users can create and manage Brancher nodes.
This is useful for running parallel integration tests, testing software version upgrades, or performing any other tasks that require a temporary and isolated server environment.

Using our Hypernode API, you can also automate the management of Brancher nodes, which enables you to automate your DTAP environment.
This saves time and resources, and it allows users to test and develop their applications with confidence.

Overall, Hypernode Brancher is a valuable addition to the Hypernode toolset, and it can help users improve the reliability and performance of their applications.

```{note}
Hypernode Brancher is currently only available for Hypernodes on the Falcon plans. If you want to see Brancher support for the Eagle plans, please let us know by contacting support@hypernode.com.
```

## What is Hypernode Brancher?

Hypernode Brancher is an extra service that runs alongside our core product Hypernode.
It’s an addon based on your Hypernode subscription and is intended to add additional functionality that’s useful for developing and testing your webshop.

Hypernode Brancher is a mutable and temporary copy of your Hypernode.
It’s based on the latest backup made for your Hypernode, meaning that the state on the Brancher node is at most 24 hours old.

If you wish to get a more recent state on the Brancher node, you can create a new backup on your Hypernode using `hypernode-systemctl create_backup`.
Note that this requires SLA Standard to be enabled on your Hypernode.

Read more about our [backup policy here](../backups/hypernode-backup-policy.md).

## Why should I use it?

Typically, you simulate the environment on your Hypernode via the hypernode-docker image.
This is an easy way to have a near-identical environment which contains all Hypernode tooling without having to test on your actual Hypernode.

However, there are some significant drawbacks to using the Docker image. For one, this isn’t exposed to the internet like a regular Hypernode is.
Requesting SSL certificates, exposing your environment to other colleagues or taking advantage of the full Hypernode automation are all missing in the Hypernode Docker image.
Next to that, we cannot replicate full behaviour on Docker containers because of the lack of systemd, which we heavily utilize on Hypernode.

All of these features are available on Hypernode Brancher, as it’s just another Hypernode.
Next to that, it copies over the state of your Hypernode, meaning that there are no strange side-effects that would happen on production that you wouldn’t be able to reproduce on a Docker container.

The most common use-cases are done by integrating Hypernode Brancher into your integration tests, or as an ad-hoc situation where you want to test a software version upgrade.

### Example: MySQL version upgrade

Let’s say you want to upgrade your MySQL version to 8.0 on your Hypernode. We provide all of the tooling to do this easily, by running the following command:

```console
$ hypernode-systemctl settings mysql_version 8.0
```

However, we do warn you about changing this, as downgrading your MySQL version is not possible.
If you do this upgrade, you should be sure about it and consider the consequences carefully.

One way of testing this change is by using a development Hypernode, and try out the change there.
The problem here lies in the fact that you can only try this once on your development environment, and that it has a different state compared to your production Hypernode.

### Example: Acceptance server per pull request

Another common use-case is to have a separate acceptance server per pull request.
You can give access to this acceptance server to your colleagues, or to your customers, so that they can test your changes before they are merged into the main branch.

You can achieve this by making a separate GitHub Actions workflow.
This workflow will create a new Brancher node based on the current pull request, and leave a comment on the pull request with the URL to the Brancher node.
This way, you can easily test your changes in a real environment, and you can easily clean up the Brancher node when you’re done. This workflow file can look like this:

```yaml
name: Deploy to acceptance server

on:
  pull_request:
...

jobs:
    ...
      - name: deploy to acceptance
        run: hypernode-deploy deploy acceptance -vvv
        env:
          HYPERNODE_API_TOKEN: ${{ secrets.HYPERNODE_API_TOKEN }}
      - name: Get brancher hostname
        run: echo "BRANCHER_HOSTNAME=$(jq .hostnames[0] deployment-report.json -r)" >> $GITHUB_ENV
      - name: Comment hostname on PR
        uses: thollander/actions-comment-pull-request@v1
        with:
          message: |
            Acceptance server is available at https://${{ env.BRANCHER_HOSTNAME }}
```

This fetches the hostname of the Brancher node, and leaves a comment on the pull request with the URL to the Brancher node on every push to the pull request:

![](_res/UxUAfHUX6Vko63WFZAuFzs4qZ9ITqdunWA.png)

### Free Usage Allowance: First 400 Minutes per Hypernode

All Combell Openstack and AWS plans (Falcons and Eagles) include 400 complimentary Brancher minutes for each Hypernode 
as part of the base package. This means you will not be charged for your Brancher minutes usage until it surpasses the 
threshold of 400 minutes per month per Hypernode. We aim to ensure that you enjoy the benefits of our service without
incurring additional costs within this specified limit.

## How do I use it?

You can use Brancher in three (and soon four) different ways: via our Hypernode API, Hypernode Deploy or the `hypernode-systemctl brancher` CLI tool.

### Hypernode API

You can create new Brancher nodes via the Hypernode API with the following POST request:

```console
$ curl -X POST -H "Authorization: Token <token>" https://api.hypernode.com/v2/app/<appname>/brancher/
```

The appname specified in the request url is the appname on which the Brancher node will be based.
This returns the name of the Brancher node, which is in the format of `<appname>-eph123456`.
To make things easier for you, we have made API client libraries available in [PHP](https://github.com/ByteInternet/hypernode-api-php) and in [Python](https://github.com/ByteInternet/hypernode-api-python).
Go check them out!

Once the Brancher node becomes available, you can control it via the `/v2/app/<appname>-eph123456` endpoint just like a regular Hypernode.

To specify `labels` and/or `clear_services` in the API call, you can set the header `Content-Type: application/json` with a content body like:

```json
{
  "labels": ["some_label"],
  "clear_services": ["cron", "elasticsearch", "mysql", "supervisor"]
}
```

### Hypernode Deploy

Hypernode Deploy is our recommended way of deploying your webshop to Hypernode. which makes it easier for you to manage your application’s codebase.
This platform is fully integrated with Hypernode Brancher, which makes it a breeze for you to try out upgrade scenarios, or pushes to the Staging environment.

Once you set up your Hypernode to make use of Hypernode Deploy, you can run your tests against a Brancher node with just a single command.
This will then run against your fresh Branched version of the Node, making sure that your tests are passing before deploying to production.

You can use Brancher in your Hypernode Deploy `deploy.php` file like this:

```php
<?php

namespace Hypernode\DeployConfiguration;

$configuration = new ApplicationTemplate\Magento2(['en_GB', 'nl_NL']);

$testStage = $configuration->addStage('test', 'example.com');

// We use an automatically created Brancher node based on the parent for the 'test' stage.
// In your testing pipeline, you can simply use the 'test' stage to push changes to the Brancher server,
// and run your tests. Cancel it when your tests fail or after your tests pass to incur minimal costs.
$testStage->addBrancherServer('example')
    ->setLabels(['stage=test'])
    ->setSettings(['clear_services' => ['cron', 'supervisor']);

return $configuration;
```

This will automatically create a Brancher node based on the parent Hypernode and push to it, allowing you to test the changes before making them on the production Hypernode.

In this example, we also set the label `stage=test` and the setting `clear_services` with value `cron` and `supervisor`, which means that the `cron` and `supervisor` configurations found on `example` will not be actively present on the Brancher instance.

### Hypernode-systemctl brancher

You can use the command hypernode-systemctl brancher tool to quickly interact with the Hypernode API in a validated and controlled manner.

```{note}
There's an alias `hypernode-brancher` for the command `hypernode-systemctl brancher`, this might save you some keystrokes :).
```

#### Creating a Brancher node

```console
$ hypernode-systemctl brancher --create
Brancher App created for app 'example'. See hypernode-systemctl brancher --list for the progress
app_name: example-eph123456
parent: example
Host: example-eph123456.hypernode.io
Labels: None
Services with data to be cleared: cron
IP: will become available in a couple of minutes
```

In the above example you see the details of the created Brancher instance.
The output also contains the given labels and services to be cleared, which have the respective defaults of `None` and `cron`.

To apply one or more label(s) to the Brancher instance, you can specify one or more `--label` options when creating the instance:

```console
$ hypernode-systemctl brancher --create --label my_brancher_instance --label 'user=johndoe'
```

To override the services that are cleared by default, pass the `--clear-services` option:

```console
$ hypernode-systemctl brancher --create --clear-services cron elasticsearch mysql supervisor
```

#### Listing available Brancher nodes

```console
$ hypernode-systemctl brancher --list
+--------------------+----------------+---------------------------------+---------+
|        Name        |       IP       |               Host              | Minutes |
+--------------------+----------------+---------------------------------+---------+
| example-ephjopv59  |  83.217.88.80  | example-ephjopv59.hypernode.io  |   4592  |
| example-ephw4zcjr  | 185.111.198.18 | example-ephw4zcjr.hypernode.io  |   4345  |
| example-ephsbuos6  | 37.72.165.123  | example-ephsbuos6.hypernode.io  |   1866  |
+--------------------+----------------+---------------------------------+---------+
```

#### Deleting a brancher node

```console
$ hypernode-systemctl brancher --delete
Brancher App 'example-eph123456' deleted. See hypernode-systemctl brancher --list for the list of remaining brancher apps.
```

And with some creativity you can come up with a one-liner to remove all active Brancher nodes:

```console
$ hypernode-systemctl brancher --list | awk '{print$2}' | grep -eph | xargs -n1 hypernode-systemctl brancher --delete
Brancher App 'example-eph123456' deleted. See hypernode-systemctl brancher --list for the list of remaining brancher apps.
Brancher App 'example-eph234567' deleted. See hypernode-systemctl brancher --list for the list of remaining brancher apps.
```

##### Example cleanup script

To prevent long running Hypernode Brancher nodes from accumulating, you can use the following script to clean up old Brancher nodes. This is configured to delete all Brancher nodes that have been running for more than 4 hours:

```bash
MAX_MINUTES_ALIVE=240
LONG_RUNNING_BRANCHERS=$(hypernode-systemctl brancher --list --machine-readable | jq -r '.[] | select (.minutes>='"${MAX_MINUTES_ALIVE}"') | .name')

if [ -z "${LONG_RUNNING_BRANCHERS}" ]; then
    echo "No long running Brancher nodes found"
    exit 0
fi

for BRANCHER in ${LONG_RUNNING_BRANCHERS}; do
    echo "Deleting Brancher node ${BRANCHER}"
    hypernode-systemctl brancher --delete "${BRANCHER}"
done
```

You can convert this to a single line if you're into that:

```bash
hypernode-systemctl brancher --list --machine-readable | jq -r '.[] | select (.minutes>=240) | .name' | xargs -n1 --no-run-if-empty hypernode-systemctl brancher --delete
```

## Brancher Install Hook

While it's already very valuable to be able to create a running copy of your Hypernode, it is a very common use case to make some configuration changes.

You might want to change the base URLs for your storefronts (including the making vhosts with hypernode-manage-vhosts), perhaps make changes to your environment configuration, etc.

To automatically make these configuration changes, we place a file called `brancher-install-hook`, in the `~/.hypernode` directory.
By default, it looks like the following:

```bash
# Hypernode Checksum: efe0ce9cd6a3170a33386f0230a42e63d03d4524
#!/usr/bin/env bash

# This file gets called after a Brancher node is ready.
# At the beginning of the file, it makes sure that it's actually running
# on a Brancher node, so you don't accidentally run this script in the
# wrong environment.
# You can add your customizations at the bottom of the script to make
# your configurations to the Brancher node and the application.
# Think of configurations like:
#   - Creating the vhost with hypernode-manage-vhosts
#   - Setting the base URL / domain for the application
#   - Setting the payment service provider to test mode
#   - etc.

set -euo pipefail

if ! jq -e '.app_type == "brancher"' /etc/hypernode/app.json > /dev/null; then
    echo "Not executing this on a non-Brancher node"
    exit 1
fi

HOSTNAME="$(jq -r .hn_fqdn /etc/hypernode/app.json)"
BASE_URL="https://${HOSTNAME}/"

cd "${HOME}"

# Add your customization here
```

After a Brancher node is ready, it copies this file from the originating Hypernode and runs the script on the Brancher node.
The output is captured in a logfile on the Brancher node, at `/data/web/brancher-install-hook.log`

```{tip}
To prevent accidentally running this script on your production/staging environment, there's a safeguard implemented by default.
The safeguard checks if the Hypernode is a Brancher node. If that's not the case, it exits immediately.
```

As the default script suggests, add your configuration commands after the `# Add your customizations here` line.

### Example install hook

For a single store Magento application, you could configure the script as follows:

```bash
# Hypernode Checksum: efe0ce9cd6a3170a33386f0230a42e63d03d4524
#!/usr/bin/env bash

# This file gets called after a Brancher node is ready.
# At the beginning of the file, it makes sure that it's actually running
# on a Brancher node, so you don't accidentally run this script in the
# wrong environment.
# You can add your customizations at the bottom of the script to make
# your configurations to the Brancher node and the application.
# Think of configurations like:
#   - Creating the vhost with hypernode-manage-vhosts
#   - Setting the base URL / domain for the application
#   - Setting the payment service provider to test mode
#   - etc.

set -euo pipefail

if ! jq -e '.app_type == "brancher"' /etc/hypernode/app.json > /dev/null; then
    echo "Not executing this on a non-Brancher node"
    exit 1
fi

HOSTNAME="$(jq -r .hn_fqdn /etc/hypernode/app.json)"
BASE_URL="https://${HOSTNAME}/"

cd "${HOME}"

# Add your customization here

APP_DIR="/data/web/apps/magento2.komkommer.store/current"

echo "Brancher hostname is: ${HOSTNAME}"

pushd "${APP_DIR}"
n98-magerun2 config:env:set db.connection.default.host mysqlmaster
bin/magento cache:flush

bin/magento config:set web/unsecure/base_url "${BASE_URL}"
bin/magento config:set web/secure/base_url "${BASE_URL}"
bin/magento cache:flush
popd

hypernode-manage-vhosts "${HOSTNAME}" --https --force-https --type magento2 --webroot "${APP_DIR}/pub"
```

This script does a few things:

1. Make sure the MySQL host is set to `mysqlmaster` and flush the Magento cache. If you already have this in your configuration, this is not necessary.
1. Set the unsecure and secure base URL to the Brancher base URL and flush the Magento cache.
1. Create a vhost with HTTPS enabled for the Brancher base url, set the vhost type to `magento2` and set the webroot to the right path.
