---
myst:
  html_meta:
    description: Learn how to solve this Redis Error that appears if Magento is trying
      to store more data in the Redis cache then possible.
    title: How to Solve Redis Out-of-Memory Error? | Hypernode
redirect_from:
  - /en/hypernode/tools/how-to-solve-redis-error-oom-command-not-allowed-when-used-memory-maxmemory-/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-solve-redis-error-oom-command-not-allowed-when-used-memory-maxmemory-/ -->

# How to Solve Redis Error "OOM command not allowed when used memory > ‘maxmemory’"

This error appears if Magento is trying to store more data in the Redis cache then possible.

## Verifying Memory Usage of Your Redis Instance

You can get more insights of the Redis memory on your Hypernode by running the command below.

```nginx
redis-cli info | grep memory_human

# Memory
used_memory_human:331.51M
total_system_memory_human:5.83G
maxmemory_human:896.00M
```

## Fix It

The quick fix will be to flush the Redis cache so there is plenty of Redis memory available again. You can do this by running `redis-cli flushall`

To prevent this you can try using compression on the Redis data, but most of the time this will only temporary ban out the problem. After a while, when the Redis cache is completely filled up again, the errors will re-appear.

### Check if Your Keys Have an Expire Set

You can inspect your keys with the command below

```nginx
redis-cli info keyspace

# Keyspace
db0:keys=59253,expires=1117,avg_ttl=81268890
db1:keys=13608,expires=904,avg_ttl=82515590
db2:keys=144,expires=144,avg_ttl=199414742
```

This will give you some insights in the Redis databases you've configured, the keys and whether they have an expire or not. In the above example a huge amount of the Redis keys don't have an expire set. This means that those keys won't ever expire and be removed from the Redis cache to make place for new keys. As a result the cache will be at greater risk to reach its maximum.

Once these keys and expires are greatly out of balance like the above example you could force an expire to your keys by adding the following snippet to your Redis config in your `env.php`.

```nginx
'auto_expire_lifetime' => '84600',
'auto_expire_pattern' => '/^[a-zA-Z0-9._-]/',
'lifetimelimit' => '57600'
```

This should give most of the keys an expire which should either prevent or at least delay the Redis memory from reaching its limits.

If you store both the Magento caches (FPC and cache) and the sessions in Redis, moving the sessions from memory to files or the database could be a solution, but this can cause an increase in load times.

Another fix could be disabling Redis cache for your staging environment on the Hypernode (if enabled), leaving the staging memory for the production website. (Don’t forget to clear it’s caches too!)

However, to solve this issue there is only one real fix: **Upgrade to a bigger node that has more memory.**
