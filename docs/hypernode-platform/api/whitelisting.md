---
myst:
  html_meta:
    description: Learn about available endpoints for whitelisting for Hypernode-API.
    title: Whitelisting | Hypernode
---

# Hypernode-API whitelisting

The following endpoints are available:

```python
GET:    https://api.hypernode.com/v1/whitelist/<your_app_name>/
POST:   https://api.hypernode.com/v1/whitelist/<your_app_name>/
DELETE: https://api.hypernode.com/v1/whitelist/<your_app_name>/
```

## GET

`GET` can be used for fetching whitelists. You can specify a whitelist type by appending a url parameter like so:

```
https://api.hypernode.com/v1/whitelist/<your_app_name>/?type=database
```

Will return a list with values in JSON format. Example:

```
[
  {
    "id": 1,
    "created": "2018-08-09T15:14:14Z",
    "domainname": "myapp.hypernode.io",
    "type": "database",
    "description": "some description",
    "ip": "1.2.3.4"
  },
  {
    "id": 2,
    "created": "2018-08-09T15:02:19Z",
    "domainname": "myapp.hypernode.io",
    "type": "waf",
    "description": "",
    "ip": "1.2.3.4"
  }
]
```

## POST

`POST` can be used for adding IP's to whitelists. You can specify the following data in the post request:

```
type: <waf|database|ftp> - Which whitelist to add the IP to
ip: <1.2.3.4> - The IP to whitelist
description: string - Optional; Description of the IP you're trying to add.
```

## DELETE

`DELETE` can be used to remove IP's from whitelists. You can specify the following data in the delete request:

```
type: <waf|database|ftp> - Which whitelist to remove the IP from
ip: <1.2.3.4> - The IP to remove from the whitelist
```
