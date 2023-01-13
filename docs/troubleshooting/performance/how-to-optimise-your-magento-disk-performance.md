---
myst:
  html_meta:
    description: Improve the performance and speed of your Magento store with Hypernode's
      guide on optimising Magento disk performance.
    title: How to optimise your Magento disk performance? | Hypernode
redirect_from:
  - /en/troubleshooting/performance/how-to-optimise-your-magento-disk-performance/
  - /knowledgebase/magento-disk-performance-optimization/
---

<!-- source: https://support.hypernode.com/en/troubleshooting/performance/how-to-optimise-your-magento-disk-performance/ -->

# How to Optimise Your Magento Disk Performance

## Why Care About Disk Performance?

Two reasons:

- If you do not optimize,**your shop might slow down** at an unfortunate moment
- There is a lot of **potential performance profit** here.

Magento is a resource hungry beast. An un-optimized store lays a hefty claim on disk throughput, especially when certain extensions are used. At live shops, we have seen disk access account for more than half of total page generation time. So the potential optimization profit is significant.

The other compelling reason for optimization is that major infrastructure providers, such as Amazon AWS, will start to throttle your disk access once you reach a very high, albeit very real threshold.

## How I/O Throttling Affects You

If you are using the Amazon AWS platform, you may encounter a throughput limit (in rare cases). In general this is not a problem, as the limit is way above average usage. The limit is expressed in I/O operations per second (IOPS), which roughly corresponds to the amount of read and written files. The limit is between 100 (Warning) and 300 (Critical). The average usage of all our Hypernodes is about 50 IOPS.

To accommodate brief peaks in disk throughput, besides the basic IOPS limit, Amazon provides burstable disk performance. Basically you start with a big pool of IOPS credits (5.4M). These credits are used at peak load times, such as reindexing jobs and other batch tasks. Once the burst pool is depleted, the throughput is throttled to the basic level (100/300 IOPS) and the burst pool slowly regenerates (when idle, this takes about 15 hours). Generally this mechanism is a good thing, as it allows very fast throughput for 99% of the sites out there. And it ensures a high and predictable performance to all customers.

On Digital Ocean no IOPS throttling is active, but over usage of disk read and writes can make your overall shop performance and load times take a massive dive.

## How Should I Predict Throttling on Amazon Nodes?

[MageReport](https://www.magereport.com/) provides useful graphs about your current and past I/O performance. If you have peaks beyond 100 (Warning) or 300 (Critical), you are draining your burst pool.

Note: the values from MageReport are per hour, so a heavy peak of 1000 translates to `1000 * 3600 seconds = 3.6M` (burst pool starts with 5.4M). Regeneration happens slowly, at a speed of 3 * GB per second. So if a hypernode has 100GB storage it will regenerate 300 IOPS burst capacity per second.

## How Do I Prevent Throttling on Amazon Nodes?

First you should identify whether you exceed the baseline I/O capacity (100/300), using the MageReport graphs. There are two cases:

- You exceed the baseline during short peaks. This indicates batch jobs, such as reindexing or imports triggered by cron.
- You exceed the baseline continuously. This likely indicates that your main shop code is unusually heavy on I/O (and is triggered by visitors hitting your website), or that an I/O heavy background process is running non-stop.

In both cases, you should examine the relevant code. It is not possible to exactly register the I/O demand per HTTP request or SQL query, but you can find very relevant indications using the following tools:

See live I/O stats: `iostat -x 5` and look for the `r/s` and `w/s` columns.

See the top live MySQL queries: `mytop` or `myprocs`

See the top live PHP-FPM requests: `livefpm`

Find past MySQL queries that incurred heavy I/O: `/var/log/mysql/mysql-slow.log` and search for “Rows_examined” above 50K.

Use [this script](https://gist.github.com/hn-support/66daf5aef6dfae0724c9b69b87d0b170) to correlate I/O peaks (100+) with current SQL and PHP-FPM transactions.

## I Am Being Throttled, Now What?

Apart from the flat I/O usage line in the MageReport graph, you will likely experience a very slow site.

### Short Term Solution

Upgrade your Hypernode through our Service Panel. This will not only increase your base I/O capacity, but also reset the burst pool, so you will start with a clean slate.

Important:

- An up or downgrade will transfer all of your data to a new Hypernode. Usually this takes up to an hour to copy your data (this is invisible to your visitors) and then a few minutes of downtime to transfer the final state. However, if your burst pool is depleted, this might take a bit longer. To be on the safe side, expect a few hours for the complete migration, make sure you don’t run any heavy **background jobs** the meantime and request the transfer in a **quiet period** (night, early morning, Sunday).
- An up or downgrade will incur an **IP change**. If you have configured the DNS using our template, we will handle the DNS for you. If you have online integrations (suppliers) who use a firewall and require your IP, you should update them after the migration finishes.
- You will receive an email once the migration is finalized, with the new IP address.

### Long Term Solution

Analyze your I/O peak usage using the suggestions above, and modify your code or batch jobs to maintain an average usage below the baseline.

## Further Recommendations

- It is strongly recommended to **not run load tests** on a production node, as load tests generally impose non-realistic load and likely incur depletion of your burst pool. Instead, you could boot an identical Hypernode to run load tests, without affecting your production environment.
- Usual suspects of high I/O usage are:
  - Multiple reindex runs
  - Large log files that are being read at every request
  - Import or export batch jobs, such as those required by 3rd party search engines.
  - Large database tables (>50K rows) without index. These are often found in 3rd party extensions of disputable quality. Please refer to the quality ratings on Magento Connect to find high quality extensions.
