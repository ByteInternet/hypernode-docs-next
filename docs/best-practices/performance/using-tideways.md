---
title: Using Tideways
---

# Using Tideways

[Tideways](https://www.tideways.com/) is a profiling tool .....

## Enabling Tideways

Enabling the Tideways integration is very easy, it's only a few steps.
This can be done in the CLI (command-line interface) of your Hypernode or with the [Control Panel](https://my.hypernode.com/).

### Using the CLI

First you need to log in to your Hypernode with SSH.
After logging in, run the following commands:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-systemctl settings tideways_api_key my-tideways-api-key
Operation was successful and is being processed. Please allow a few minutes for the settings to be applied. Run 'livelog' to see the progress.
app@abcdef-example-magweb-cmbl:~$ hypernode-systemctl settings tideways_enabled True
Operation was successful and is being processed. Please allow a few minutes for the settings to be applied. Run 'livelog' to see the progress.
```

### Using the Control Panel

## Tideways with Varnish

If you are using Varnish in front of your application, you can use the
`X-Tideways-Profiler` header to pass the profiling information to the backend
application. This is useful if you want to profile a specific request, but
don't want to enable profiling for all requests.

To enable this feature, you need to add the following configuration to your
Varnish configuration:

```vcl
if (req.esi_level > 0) {
    # ESI request should not be included in the profile.
    # Instead you should profile them separately, each one
    # in their dedicated profile.
    # Removing the Tideways header avoids to trigger the profiling.
    # Not returning let it go trough your usual workflow as a regular
    # ESI request without distinction.
    unset req.http.X-Tideways-Profiler;
}

# bypass if tideways request
if (req.http.X-Tideways-Profiler && client.ip ~ profile) {
    return (pass);
}
```
