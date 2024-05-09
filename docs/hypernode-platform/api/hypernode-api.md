---
myst:
  html_meta:
    description: Learn how to authenticate the Hypernode-API with your systems.
    title: Hypernode-API | Hypernode
---

# Welcome to the Hypernode-API (beta)

First of, lets's be clear and mention that this API is still in beta and subject to change. So for now it's important
to not let any of your critical systems depend on this API.

## Authentication

To authenticate at the Hypernode-API you have to make use of the Hypernode-API token provisioned on your node. The
location for this token is:

```
/etc/hypernode/hypernode_api_token
```

You can use the value in this file to make requests
to `https://api.hypernode.com` by specifying the token in the `Authorization` header like so:

```bash
curl https://api.hypernode.com/v1/app/<your_app_name>/ -X GET --header "Authorization: Token <your_hypernode_api_token>"
```

The API will return a 403 if you do not have permission to call a specified endpoint. If you do not authenticate the API
will return a 401 response. If you encounter a 403 and would like to have access to the specified endpoint please feel
free to contact our support department at support@hypernode.com.

## Functionalities

### Whitelisting

Whitelisting allows you to add IP's for specific purposes. To find out how to use this have a look at [the documentation
for this endpoint](/Documentation/hypernode-api/whitelisting/README.md).

### Hypernode settings

This endpoint allows you to set settings for your Hypernode. For example, you can set your `php_version` or blackfire
tokens here. To find out how to use this have a look at [the documentation for this endpoint](/Documentation/hypernode-api/settings/README.md).

### Chargebee SSO URL

This endpoint allows you to retireve the SSO URL for Chargebee. If you are a customer which registered via Chargebee you
will be able to retrieve the login URL for Chargebee which you can then use to login and manage your subscriptions.
For more information about this endpoint have a look at [this endpoint's documentation](/Documentation/hypernode-api/chargebee/SSO/README.md).

### Perform preinstall

This endpoint allows you to perform a preinstall of magento or akeneo on your Hypernode. For more information about this endpoint have a look at [this enpoint's documentation](/Documentation/hypernode-api/preinstall/README.md).
