---
myst:
  html_meta:
    description: Changing the Redis eviction policy on Hypernode with hypernode-systemctl. Learn which policies are available and how to verify the active Redis maxmemory-policy.
    title: Changing the Redis eviction policy on Hypernode
---

# Changing the Redis eviction policy

You can change the Redis `maxmemory-policy` with `hypernode-systemctl settings redis_eviction_policy`. This policy determines which keys Redis can evict when memory is full.


## Available policies

The following values are supported for `redis_eviction_policy`:

- `noeviction`
- `allkeys-lru`
- `allkeys-lfu`
- `allkeys-random`
- `volatile-lru`
- `volatile-lfu`
- `volatile-ttl`
- `volatile-random`

```{infomation}
By default, Redis on Hypernode uses the `volatile-lru` eviction policy.
```

## Check the current policy

To view the current Redis eviction policy:

```bash
hypernode-systemctl settings redis_eviction_policy
```

## Change the policy

Use the following command to change the Redis eviction policy:

```bash
hypernode-systemctl settings redis_eviction_policy <policy>
```

For example:

```bash
hypernode-systemctl settings redis_eviction_policy allkeys-lru
```

## Policy explanation

### `noeviction`
Redis will not evict any keys when memory is full. New write operations
that require memory will fail.

### `allkeys-lru`
Redis can evict any key and removes the least recently used keys first.

### `allkeys-lfu`
Redis can evict any key and removes the least frequently used keys first.

### `allkeys-random`
Redis can evict any key and removes keys at random.

### `volatile-lru`
Redis only evicts keys with an expiration time and removes the least
recently used keys first.

This is the default policy on Hypernode.

### `volatile-lfu`
Redis only evicts keys with an expiration time and removes the least
frequently used keys first.

### `volatile-ttl`
Redis only evicts keys with an expiration time and prefers keys that will
expire soonest.

### `volatile-random`
Redis only evicts keys with an expiration time and removes those keys at
random.

## Important considerations

- Eviction only takes place when Redis reaches its memory limit.
- Policies starting with `allkeys-` can evict any key, including keys without a TTL.
- Even with an `allkeys-` policy, Redis can still run into memory pressure if keys cannot be evicted fast enough to keep up with writes.
- Setting a TTL on cache keys is still recommended, even when using an `allkeys-` policy.
- Policies starting with `volatile-` only apply to keys with a TTL.
- If not enough keys have a TTL, Redis may not be able to evict enough data with a `volatile-` policy, and write operations may fail.
- Changing the policy does not remove existing keys immediately.