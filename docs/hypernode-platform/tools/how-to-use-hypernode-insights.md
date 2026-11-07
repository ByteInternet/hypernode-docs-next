---
myst:
  html_meta:
    description: Hypernode Insights is a real-time monitoring dashboard for your Hypernode.
      Learn what it shows, how to add cards and how to use annotations.
    title: How to Use Hypernode Insights | Hypernode
---

# How to Use Hypernode Insights

Hypernode Insights is a real-time monitoring dashboard for your Hypernode. It shows the health of your whole stack in one place, without any configuration, so you can spot problems early and see how your Hypernode performs over time. Insights is free and included with every Hypernode.

## What Hypernode Insights Shows

Insights tracks the following parts of your Hypernode:

- CPU and memory usage
- HTTP status codes
- Varnish caches, including the hit rate
- Cron jobs, including the Magento cron jobs
- Databases
- Elasticsearch
- Queues

Besides the graphs, Insights has cards that point out common problems, such as **Big files**, **Big directories** and **Broken links**. Because Insights keeps the history of your metrics, you can also compare the current situation with earlier trends.

## How to Open Hypernode Insights

1. Log in to the [Control Panel](https://my.hypernode.com/).
1. Click the **Insights** button in the top right corner.
1. Choose the Hypernode you want to look at.

## Working With the Dashboard

### Add Cards to Your Dashboard

You choose which cards are shown on your dashboard. To add a card, open the **Add Metrics** menu on your Hypernode dashboard and select the card you want.

### Magento Cron Jobs

Insights detects Magento installations on your Hypernode automatically. The Magento cron card shows the current cron jobs in a table, so you can check the health of your crons without logging in to your Hypernode. Add it with the **Add Metrics** menu.

### Sort Dashboard Tabs

You can put the tabs of your dashboard in the order you prefer. Click a tab and drag it to the position you want.

## Annotations

Annotations mark events on the timeline of your Insights graphs. They help you see if a change in a graph lines up with something that happened. For example, if response times went up, the cache hit rate dropped or memory use grew, you can see straight away if that started before or after a deploy.

Insights adds annotations automatically for selected system events. They are shown on the charts of the metrics they affect, at the time of the event.

You can also add your own annotations, for example for:

- A release or deploy
- A maintenance window
- A cache flush
- A feature rollout
- A one-off debugging action

There are two ways to add your own annotations: with the Hypernode API, or automatically after every successful release with Hypernode Deploy.

### Add Annotations With the Hypernode API

The Hypernode API has two endpoints for annotations:

- `GET /v2/insights-annotation/` lists the annotations you created through the API.
- `POST /v2/insights-annotation/create/` creates a new annotation.

The create endpoint takes the following fields:

- `name`: the name of the annotation, as shown in the graphs.
- `x_axis`: the moment of the event, as a Unix timestamp.
- `app`: the name of your Hypernode, for example `example`.
- `metrics`: the metrics the annotation applies to. Leave it out to show the annotation on all metrics.
- `metadata`: extra information about the event, for example a description.

You can find the API token of your Hypernode in `/etc/hypernode/hypernode_api_token`. To create an annotation for the current moment, run:

```console
app@abcdef-example-magweb-cmbl:~$ curl -X POST \
  -H "Authorization: Token $(cat /etc/hypernode/hypernode_api_token)" \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"Flushed the cache\", \"x_axis\": $(date +%s), \"app\": \"example\", \"metadata\": \"Manual cache flush\"}" \
  https://api.hypernode.com/v2/insights-annotation/create/
```

To list your annotations, run:

```console
app@abcdef-example-magweb-cmbl:~$ curl -H "Authorization: Token $(cat /etc/hypernode/hypernode_api_token)" \
  https://api.hypernode.com/v2/insights-annotation/
```

See the [Hypernode API documentation](https://api.docs.hypernode.io/) for more information.

### Add Annotations Automatically With Hypernode Deploy

From Hypernode Deploy 4.9.0 with `hypernode/deploy-configuration` 3.8.1, Hypernode Deploy can add an annotation after every successful release. See [Install and Configure Hypernode Deploy](../../hypernode-deploy/getting-started/install-and-configure-hypernode-deploy.md) if you don't use Hypernode Deploy yet.

To turn it on, add the `HypernodeAnnotation` after deploy task to your `deploy.php`:

```php
$configuration->addAfterDeployTask(
    new \Hypernode\DeployConfiguration\AfterDeployTask\HypernodeAnnotation()
);
```

By default, the annotation gets the name of the release and the description `Hypernode Deploy`. You can set your own name and description:

```php
$configuration->addAfterDeployTask(
    new \Hypernode\DeployConfiguration\AfterDeployTask\HypernodeAnnotation(
        name: 'Production deploy',
        description: 'Release deployed through Hypernode Deploy',
    )
);
```

Hypernode Deploy finds the app name and API token by itself:

- The app name comes from the hostname of the server you deploy to, for example `example.hypernode.io`. If you deploy to a different hostname, set it with the `app` argument.
- The API token comes from the `HYPERNODE_API_TOKEN` environment variable if it is set, and otherwise from `/etc/hypernode/hypernode_api_token` on your Hypernode. You can also set it with the `api_token` argument.

If the annotation can't be created, the deploy continues. Set `throw_on_error: true` if you want the deploy to fail instead.
