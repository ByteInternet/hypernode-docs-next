---
myst:
  html_meta:
    description: This article will explain how to configure Redis on your Shopware
      6 shop on Hypernode and how to work with redis-cli.
    title: How to configure Redis for Shopware 6?
redirect_from:
  - /en/support/solutions/articles/48001200521-how-to-configure-redis-for-shopware-6/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001200521-how-to-configure-redis-for-shopware-6/ -->

# How to Configure Redis for Shopware 6

Redis is a caching method which can increase the speed of the backend and frontend of your shop. On Hypernode every customer has access to Redis cache, starting from 64 MB, depending on the plan. This article will explain how to configure Redis on your shop on Hypernode and how to work with redis-cli.

## Step One: Configure Redis For Shopware 6 by editing the .env File

Add the following line to the .env file:

```bash
REDIS_URL=redis://localhost:6379/1
```

## Step Two: Create the framework.yml File

Create the file "**config/packages/framework.yml**" with the following content:

```nginx
framework:
    cache:
        app: cache.adapter.redis
        system: cache.adapter.redis
        default_redis_provider: '%env(string:REDIS_URL)%'
```

Now flush the Shopware cache, either via the backend or via the CLI by running:

```nginx
bin/console cache:clear
```
