---
myst:
  html_meta:
    description: 'We recommend all Hypernode users to use Redis for caching. Learn
      how Flush the Redis Cache here. '
    title: How to flush the Redic cache? | Hypernode
redirect_from:
  - /en/hypernode/tools/how-to-flush-the-redis-cache/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-flush-the-redis-cache/ -->

# How to Flush the Redis Cache

We recommend all Hypernode users to use Redis for caching.
As the file cache on cloud nodes is often shared with other nodes on the same hardware, writing lots of files can vary a bit in speed and duration.

The memory for the node however, which Redis uses for storing key/value pairs, is reserved for a single Hypernode and is never shared with other servers running on the same hardware. This makes using Redis much faster than using the file caching mechanism that is enabled by default.

## Flush All Redis Caches at Once

If you want to flush all Redis caches at once, you can easily flush all Redis databases using the flushall command:

```bash
redis-cli flushall
```

This will flush out **all** available Redis databases.

**NB:** If the sessions are stored in Redis too, don’t flush out all databases, but selectively use the ones that are used for caching. Read the next section to learn how.

## Flush All Redis Caches when Storing the Sessions in Redis

If you use Redis for the sessions too, flushing all Redis databases at once will flush the sessions database as well, forcing all your visitors to ogin again.

To flush only the databases that are used for caching and not for sessions, use the flushdb command for Redis rather then using `flushall`.
e.g.: If database 0 and 1 are used for caching and database 2 is used for sessions, only flush database 0 and 1:

```bash
redis-cli -n 0 flushdb
redis-cli -n 1 flushdb
```

Or using a `for` loop:

```bash
for i in 1 2; do
  redis-cli -n "${i}" flushdb
done
```
