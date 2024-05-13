---
myst:
  html_meta:
    description: Learn about available endpoints for logbook for Hypernode-API.
    title: Hypernode API Logbook | Hypernode
redirect_from:
  - /#/Documentation/hypernode-api/flows/README
---

# Hypernode API Logbook

The following endpoints are available:

```python
GET: https://api.hypernode.com/logbook/v1/logbooks/<your_app_name>/flows/
```

Curl example:

```
curl https://api.hypernode.com/logbook/v1/logbooks/<your_app_name>/flows/ -X GET --header "Authorization: Token <your_token>"
```

## GET

`GET` can be used for retrieving the state of pending, running and previous actions on your Hypernode. This can be helpful for anticipating when a change that you have requested through either the API or the control panel will be propagated.

The JSON formatted output looks like:

```python
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "uuid": "be1c54d7-c8ff-4890-8610-ba254224b6e9",
      "state": "running",
      "name": "xgrade_app",
      "created_at": "2020-07-15T10:03:32Z",
      "updated_at": "2020-07-15T10:03:33Z",
      "progress": {
        "completed": 8,
        "running": [
          "stop_mysql_on_volume",
          "verify_node_fits_on_new_product",
          "ensure_nodes"
        ],
        "total": 34
      },
      "logbook": "vdloo",
      "tracker": {
        "description": null,
        "uuid": null
      }
    },
    {
      "uuid": "fc432957-517e-4fc7-8bd6-e48ab3183d56",
      "state": "success",
      "name": "create_backup",
      "created_at": "2020-07-15T00:07:09Z",
      "updated_at": "2020-07-15T00:07:24Z",
      "progress": {
        "completed": 2,
        "running": [],
        "total": 2
      },
      "logbook": "vdloo",
      "tracker": {
        "description": null,
        "uuid": null
      }
    },
  ]
}
```

Also check out the [hypernode-log](https://support.hypernode.com/changelog/release-5664-follow-migration-process-from-the-commandline/) commandline tool which implements this API.

```bash
$ hypernode-log
ACTION                        	START               	END                 	STATE   	TASKS	RUNNING
update_node                   	2018-08-29T10:05:41Z	2018-08-29T10:11:07Z	success 	4/4 	finished
destroying_node               	2018-08-29T09:42:06Z	2018-08-29T09:42:44Z	success 	7/7 	finished
restore_backup_flow           	2018-08-29T09:20:10Z	2018-08-29T09:26:38Z	success 	21/21	finished
update_node                   	2018-08-29T09:07:07Z	2018-08-29T09:13:34Z	success 	4/4 	finished
ensure_s3_backup_configured   	2018-08-29T09:07:05Z	2018-08-29T09:09:26Z	success 	5/5 	finished
ensure_monitoring_for_app     	2018-08-29T09:07:04Z	2018-08-29T09:09:13Z	success 	6/6 	finished
emergency_rescue              	2018-08-29T09:06:57Z	2018-08-29T09:07:05Z	success 	32/32	finished
xgrade_app_flow               	2018-08-29T08:55:25Z	2018-08-29T09:07:03Z	success 	24/24	finished
```
