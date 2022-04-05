# How to Configure Redis for Shopware 6

Redis is a caching method which can increase the speed of the backend and frontend of your shop. On Hypernode every customer has access to Redis cache, starting from 64 MB, depending on the plan. This article will explain how to configure Redis on your shop on Hypernode and how to work with redis-cli.

## Table of Contents
```{contents}
:depth: 3
:backlinks: none
```

## Step One: Configure Redis For Shopware 6 by editing the .env File

Add the following line to the .env file:

```
REDIS_URL=redis://localhost/<database ID>
```
## Step Two: Create the framework.yml File

Create the file "**config/packages/framework.yml**" with the following content:

```
framework:
    cache:
        app: cache.adapter.redis
        system: cache.adapter.redis
        default_redis_provider: '%env(string:REDIS_URL)%'
```
Now flush the Shopware cache, either via the backend or via the CLI by running: 

```
bin/console cache:clear
```
