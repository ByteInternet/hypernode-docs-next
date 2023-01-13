---
myst:
  html_meta:
    description: Since composer is overall a heavy process it requires quite some
      resources, specifically memory in this case. Here we discuss the causes and
      workarounds.
    title: How to handle composer memory issues? | Hypernode
redirect_from:
  - /en/support/solutions/articles/48001186354-how-to-handle-composer-memory-issues/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001186354-how-to-handle-composer-memory-issues/ -->

# How to Handle Composer Memory Issues

Since composer is overall a heavy process it requires quite some resources, specifically memory in this case. This could result in composer processes which won't be able to finish successfully. In this article we discuss the possible causes and workarounds.

## Composer Crashes on the PHP Memory Limit

You could face two different memory related issues while running composer processes on your Hypernode. First of all, there is a hardcoded PHP memory limit of 2GB for each Hypernode. Usually this should be enough for each PHP process in your shop. But there is one exception for this, which is composer.

Composer is a really heavy process which requires a lot of memory. So it may happen that you're trying to run a composer command which will eventually be canceled due to a lack of PHP memory. The error you'll see will look like this:

```nginx
app@3nljr6-example-magweb-cmbl:~/magento2$ composer require weberinformatics/spreadsheet-product-master
Using version ^1.0 for weberinformatics/spreadsheet-product-master

./composer.json has been updated
Loading composer repositories with package information
Updating dependencies (including require-dev)

mmap() failed: [12] Cannot allocate memory

mmap() failed: [12] Cannot allocate memory
PHP Fatal error:  Out of memory (allocated 1520447488) (tried to allocate 134217736 bytes) in phar:///usr/local/bin/composer/src/Composer/DependencyResolver/RuleSet.php on line 83

Fatal error: Out of memory (allocated 1520447488) (tried to allocate 134217736 bytes) in phar:///usr/local/bin/composer/src/Composer/DependencyResolver/RuleSet.php on line 83)
```

Once you face an error like the above you can work your way around it. All you have to do is run the composer command with `COMPOSER_MEMORY_LIMIT=-1` followed by the rest of your command. So in the above example this will be `COMPOSER_MEMORY_LIMIT=-1 composer require webinformatics/spreadsheet-product-master`

## Composer Crashes on Memory Limit of the Server

If you don't get the PHP memory error, or have already fixed that issue, you could face an overall memory shortage while running composer since composer is just requires a lot of resources. In this case the oom-killer could be triggered and will kill the composer process or your SSH-session which breaks the composer process. For example, this could look like this

```nginx
app@3nljr6-example-magweb-cmbl:~/magento2$ php -d memory_limit=-1 composer require weberinformatics/spreadsheet-product-master
Using version ^1.0 for weberinformatics/spreadsheet-product-master
./composer.json has been updated
Loading composer repositories with package information
Updating dependencies (including require-dev)
Killed
```

Note the "Killed" at the bottom, this indicates that your SSH-session is being killed by the oom-killer due to a lack of memory.

There are several possibilities to still be able to complete the composer command. At first it is important to get some insights in your resources. You can do this by running `htop` ,this will provide you with a live feed of your resources. From here you can click on the "MEM%" column with will sort all the processes on memory usage. Now press "Shift+H" to close the child processes. You'll see from top to bottom which processes is using the most memory.

There are a couple of tricks to get a little bit more memory so you can still successfully run your composer command:

- Restarting MySQL with  hypernode-servicectl restart mysql

MySQL is a service which will often be using quite some memory. That's because MySQL caches the memory in case it may need it again. Restarting MySQL will release all the cached memory so there will be some more memory free.

- Temporary disable the Magento crons

The Magento 2 crons are also quite heavy processes which will acquire their peace of memory while they run every minute. You could comment the Magento crons in the crontab just before you run your composer command and once it is finished you could enable them again.

- Check the proceses which consume the most memory with htop

It is possible you'll see quite some "queue:consumers" processes. These all together could require a lot of memory as well. After disabling the Magento crons you could [track down those processes and kill them](../../troubleshooting/performance/how-to-identify-and-stop-long-running-processes.md#long-running-ssh-process) to free the memory. Do note that those processes will be starting again next minute if the Magento crons are enabled.

Check your list of processes with htop to see if there are any other processes that are unnecessary claiming a lot of memory. This is something you'd have to think of carefully before just killing them, this can differ per server.

If you still haven't enough memory available to complete your composer command after following these steps there is just one single solution. The current Hypernode just doesn't fit your requirements and you'll need to upgrade to a larger plan with more resources.
