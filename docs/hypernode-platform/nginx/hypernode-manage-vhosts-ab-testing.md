---

myst:
html_meta:
description: Learn how to use A/B testing on Hypernode using the NGINX split_clients module and Hypernode Managed Vhosts (HMV).
title: How to configure A/B testing with Hypernode Managed Vhosts?
redirect_from:

* /en/hypernode/nginx/ab-testing-hmv/

---

<!-- source: internal knowledge + nginx.org documentation -->

# A/B Testing with Hypernode Managed Vhosts

Hypernode Managed Vhosts (HMV) supports A/B testing by using the native NGINX `split_clients` module. This allows you to route users to different versions of your application based on a defined percentage split.

This setup is useful when you want to test different codebases, features, or layouts without deploying changes to all users at once.

## How A/B Testing Works

The `split_clients` module assigns users to a variant based on a hashed value. This ensures:

* Consistent routing for the same user
* Even distribution based on percentages
* No need for external tools

Each user is mapped to a variant using values like:

* IP address
* User agent
* Time-based values

## Enabling A/B Testing with HMV

To create an A/B testing setup, run:

```bash
hypernode-manage-vhosts example.com --type ab-test
```

This generates the required configuration files inside:

```
/data/web/nginx/example.com/
```

You will see:

* http.vhost_split_clients.conf
* server.ab-proxy.conf

## Example Configuration

### Split configuration

```nginx
split_clients "cache${remote_addr}${http_user_agent}${date_gmt}" $vhost_variant {
    50% a.example.com;
    50% b.example.com;
}
```

This defines a 50/50 split between two variants.

### Proxy configuration

```nginx
location / {
    resolver 8.8.8.8;
    proxy_pass http://${vhost_variant};
}
```

Requests are routed dynamically based on the assigned variant.

## Setting Up Variants

You must create separate vhosts for each variant:

* a.example.com → version A
* b.example.com → version B

These should be standard vhosts using HMV:

```bash
hypernode-manage-vhosts a.example.com
hypernode-manage-vhosts b.example.com
```

Each vhost can point to a different codebase or deployment.

## Custom Traffic Splits

You can adjust the percentages to control traffic distribution.

Example: 70/30 split

```nginx
split_clients "cache${remote_addr}${http_user_agent}${date_gmt}" $vhost_variant {
    30% a.example.com;
    70% b.example.com;
}
```

Example: multiple variants

```nginx
split_clients "cache${remote_addr}${http_user_agent}${date_gmt}" $vhost_variant {
    20% a.example.com;
    20% b.example.com;
    20% c.example.com;
    20% d.example.com;
    20% e.example.com;
}
```

## Important Notes

* The split is deterministic. The same user will consistently hit the same variant.
* Changes to the split logic may reassign users.
* You must ensure all variant domains are reachable and correctly configured.
* DNS resolution is required for proxying, hence the resolver directive.

## How the Split is Determined

The input string:

```
"cache${remote_addr}${http_user_agent}${date_gmt}"
```

is hashed using MurmurHash2.

This hash determines which percentage bucket a user falls into.

Example mapping:

* First 0.5% → variant A
* Next 2% → variant B
* Remaining → default

## Troubleshooting

If routing behaves unexpectedly:

* Run:

```bash
hypernode-manage-vhosts --all
```

* Verify all variant vhosts exist
* Check DNS resolution
* Validate nginx configuration:

```bash
nginx -t
```

## When to Use This Setup

Use this approach when:

* You need infrastructure-level A/B testing
* You run separate codebases per variant
* You want full control without external tools

Avoid this setup if:

* You only need frontend experiments
* You rely on analytics tools like Google Optimize