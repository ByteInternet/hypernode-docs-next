---
myst:
  html_meta:
    description: Learn about Chargbee SSO endpoints for Hypernode-API.
    title: Chargbee SSO | Hypernode
---

# Chargebee SSO URL endpoint

The following endpoints are available:

```
GET: https://api.hypernode.com/v1/chargebee/sso/<your_email>/
```

This endpoint allows you to retrieve the SSO login URL for Chargebee, which you can then use
to login to Chargebee and manage your subscriptions. You can request the URL like so:

```bash
curl https://api.hypernode.com/v1/chargebee/sso/<your_email>/ -X GET --header "Authorization: Token <your_hypernode_api_token>"
```

The returned JSON should contain an `access_url` if there is a Chargebee account associated with your email:

```json
{
  "id": "portal_XpbGElGQgEHspHB",
  "token": "cuqdrWacuITd2cabvf97KJD73SpNcd7BICB",
  "access_url": "https://hypernode.chargebee.com/portal/v2/authenticate?token=cuqdrWacuITd2cabvf97KJD73SpNcd7BICB",
  "status": "created",
  "created_at": 1515494835,
  "expires_at": 1515498435,
  "object": "portal_session",
  "customer_id": "XpbGEt7QgEHsnL7O"
}
```

For more information see the official Chargebee API docs:
https://www.chargebee.com/checkout-portal-docs/api-portal.html

If there is no Chargebee account associated with your account a 404 with the following will be returned:

```json
{
  "detail": "Not found."
}
```
