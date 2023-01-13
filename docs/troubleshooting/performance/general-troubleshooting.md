---
myst:
  html_meta:
    description: 'Hypernode provides the best performance for your Magento webshop.
      Get insights on how to troubleshoot general issues. '
    title: Performance | General Troubleshooting | Hypernode
redirect_from:
  - /en/troubleshooting/performance/general-troubleshooting/
---

<!-- source: https://support.hypernode.com/en/troubleshooting/performance/general-troubleshooting/ -->

# General Troubleshooting

Need to debug a problem? Hypernode has many possibilities to analyse a suspicious or unwanted situation. Learn where to look and reach a conclusion fast.

## Notes on Log Files in General

System and logfile times are in *UTC (GMT) timezone*! Dutch time is UTC+1 in winter and UTC+2 in summer.

Log files are rotated daily. Previous log files are compressed using gzip. They can be viewed with commands such as `zcat` or `zgrep`.

## Webserver

Most issues will result from specific people or external systems interacting with your shop over HTTP. There are several tools to tell you what happened and what is currently going on.

### Live Usage

To see live, ongoing requests on your Hypernode, type `livefpm` and you will see a continuous overview like this:

```nginx
24769 BUSY   0.2s DE 54.93.108.145   POST www.site.nl/index.php/api/soap/index/   (Picqer Magento Integration (picqer.com))
24227 IDLE   0.1s DE 54.93.108.145   GET  www.site.nl/api/soap?wsdl   (Picqer Magento Integration (picqer.com))
24762 BUSY   0.1s NL 37.139.5.130    GET  www.site.nl/index.php/api/soap/index/?wsdl=1   (None)
```

Here, there are 3 PHP slots, of which 2 are busy. You see the duration (keep it below 1 sec for happy visitors!), the country, IP, request and user agent.

### Past Usage

There is a wealth of information on past requests available. Hypernode uses extended request logging using JSON. The live log is in `/var/log/nginx/access.log` and is rotated daily. Because it can be hard to read the raw data, we have made the `hypernode-parse-nginx-log` (or short: `pnl`) tool for you.

See the help for `pnl`:

```nginx
$ pnl --help
usage: hypernode-parse-nginx-log [-h] [--fields FIELDS] [--php] [--bots]
                                 [--format FORMAT] [--list-fields]
                                 [--filter FILTER] [--verbose]
                                 [--filename FILENAME | --today | --yesterday]

Parses, filters and styles Hypernode Nginx logs. Our Nginx logs are JSON
encoded for easy machine parsing. This utility will convert to human-
digestible output.

optional arguments:
  -h, --help           show this help message and exit
  --fields FIELDS      Comma separated list of fields to display
  --php                Short for --filter handler phpfpm
  --bots               Short for --filter
                       user_agent~(http|bot|crawl|spider|search)
  --format FORMAT      Format string to display fields
  --list-fields        Display a list of available fields
  --filter FILTER      Filter to apply. Format: <field>=<str> or
                       <field>~<regex> or <field>!~<regex>
  --verbose, -v        Display debug output
  --filename FILENAME  Path of nginx logfile to parse (default STDIN)
  --today              Short for --filename /var/log/nginx/access.log
  --yesterday          Short for --filename /var/log/nginx/access.log.1.gz
```

You can use the following fields for filtering or output:

- status (http status code)
- ua (user agent)
- req (request)
- ip
- cc (country code)
- referer
- duration
- handler (php-fpm, varnish, empty)

### Examples

See live hits as they happen, but only those who are handled by PHP (`tal` is short for `tail -f /var/log/nginx/access.log`):

```console
$ tal | pnl --php
```

Parse multiple log files, possibly gzipped:

```console
$ zcat -f /var/log/nginx/access.log* | pnl
```

See all bots today with their user agents:

```console
$ pnl --today --bots --fields status,duration,ip,req,ua
```

See all HTTP 500 hits.

```console
$ pnl --today --filter status=500
```

See how many times a particular HTTP status code was returned today (formatted in a nice table).

```console
$ pnl --today --fields status | sort | uniq -c | sort -nk2 | \
    awk 'BEGIN { print "Status Amount";print "------ ------" };{ printf "%-6s %s\n", $2, $1 }'
```

See a distribution of all 502 (bad gateway) hits over all logfiles.

```console
$ for log in `ls -t /var/log/nginx/access.log*`; \
    do echo -n "$log: "; \
    zcat -f $log | pnl --filter status=502 | wc -l; \
    done
```

See whether bot traffic has increased over the last few days

```console
$ for log in `ls -t /var/log/nginx/access.log*`; \
    do echo -n "$log: "; \
    zcat -f $log | pnl --php --bots | wc -l; \
    done
```

See all 404 hits that were handled by Magento in yesterday’s log (so you can make static placeholders)

```console
$ pnl --yesterday --php \
    --filter status=404 --fields request | egrep ^GET | cut -f2 -d' ' |\
     cut -d'?' -f1 | sort | uniq -c | sort -n
```

See all pageviews from China

```console
$ pnl --php --yesterday --filter country=CN
```

Or all pageviews not from the Netherlands:

```console
$ pnl --php --today --filter 'country!=NL'
```

Check all bot pageviews (and user agents) and sort on frequency

```console
$ pnl --yesterday --bots --php --fields ua | sort | uniq -c | sort -n
```

See all Android hits

```console
$ pnl --yesterday --filter ua~Android \
    --fields status,country,ua
```

How many PHP requests were there yesterday?

```console
$ pnl --yesterday --php | wc -l
```

How many unique IPs were served yesterday?

```console
$ pnl --yesterday --fields remote_addr | sort | uniq | wc -l
```

Find all IPs that used multiple user agents today

```console
$ pnl --today --fields remote_addr,user_agent | sort | uniq |\
    cut -d' ' -f1 | sort | uniq -c | sort -n | grep -v ' 1 '
```

Calculate total outbound traffic for yesterday (in this case, 20GB):

```console
$ pnl --yesterday --fields body_bytes_sent | awk '{s+=$1} END {printf "%.0f\n", s}'
20726556545
```

See `hypernode-parse-nginx-log --help` for more options on filtering and output.

### Errors

Basic operational webserver errors (about blocked requests) are logged to `/var/log/nginx/error.log`.

If you have modified your Nginx configuration (by updating files in `/data/web/nginx`) and it contains an error, it will put the error message in `/data/web/nginx/nginx_error_output`. After you resolve the issue, the file will disappear. If no such file exist, it means that your configuration is ok!

## PHP

### Debugging PHP Issues

For debugging PHP issues, these files are useful:

- /var/log/php-fpm/php-fpm.log (for PHP-FPM)
- /var/log/php-fpm/php-slow.log (for FPM that took longer than 10 seconds)

You can check whether PHP failed, because the webserver will give a HTTP 502 Bad Gateway error. Check whether these errors have occurred:

```console
$ pnl --yesterday --php --filter status=502
```

### Headers Already Sent

The error `Warning: Cannot modify header information - headers already sent (output started at script:line)` basically tells you that the actual output of your PHP script was returned before the complete HTTP headers could be sent. This error can be caused by a number of reasons, most commonly:

- Whitespace before `<?php` for “script.php line 1” warnings
- Whitespace after `?>`
- `Print` or `echo` statements that prematurely terminate the opportunity to send HTTP headers.

An in-depth explanation on how to determine what is causing the issue and how to fix it can be found [here](https://stackoverflow.com/questions/8028957/how-to-fix-headers-already-sent-error-in-php).

## MySQL

Debugging MySQL issues starts with running `mytop`. It will give you an overview of the active queries. Use the `o` and `f` keys to sort on duration and to see the full query.

To check on past queries, see the slow log at `/var/log/mysql/mysql-slow.log`. It contains all the queries that took longer than 2 seconds.

If your queries are stopped before completion, check in `/var/log/mysql/error.log` whether MySQL has crashed and is restarted (happens seldomly).

## FTP Usage

Logs of logins and transfer can be found at `/var/log/proftpd/proftpd.log`.

## Email

Check on the status of outgoing mail in `/var/log/mail.log`. Also, check if any outgoing mail is still in the queue, by running `mailq`. As an `app` user you have a tool available to remove emails from the mailqueue. On Hypernode we have email policies. If the volume of emails to send is higher than the number of emails being processed for delivery, the queue grows larger and this may consume considerable disk space.

With `hypernode-postsuper` you can clear items from the mail queue. Details can be found in our [changelog about the hypernode-postsuper tool](https://changelog.hypernode.com/changelog/release-5678-new-hypernode-postsuper-utility-to-clear-mail-queue/).

## Cron Tasks

Verify starting of your cron tasks:

```nginx
$ grep CRON /var/log/syslog | tail
```

If you have installed the excellent [Aoe_Scheduler](https://github.com/AOEpeople/Aoe_Scheduler) module, it will also keep a Magento specific cron log in `public/var/log/cron.log`.

## Magento Errors

Magento is generally abundant in logging issues. It will write these to `public/var/report` and `public/var/log`.

## Generic Solutions

### Flush Your Caches

Most of the times when something goes wrong in Magento, it can be solved by simply flushing your cache. There are a couple of ways of flushing your cache:

1. Use the Cache Management in Magento. Log in to the backend of your Magento shop. Go to System –> Cache Management and use the flush buttons.
1. Use Magerun on the commandline: `magerun cache:flush`
1. Flush Redis-specific cache on the commandline: `redis-cli flushall`

### Restart PHP-FPM

If you want to reload PHP-FPM or kill all currently running processes that you would like to abort, you can run the SSH shell: `pkill -9 -u app php5-fpm`

This will kill all workers (which will be restarted) but keeps the master process alive, leaving PHP-FPM in a state it can easily start new threads to continue.

### Restart Services (MySQL, Nginx, php7.1-fpm, Varnish, Redis) as an `app` User

As an the `app` user you have the capability of restarting or reloading a select number of services like MySQL, Nginx, php7.1-fpm and Varnish. The command is `hypernode-servicectl` and it takes as arguments an action (restart or reload) and a service (Nginx, php7.1-fpm, etc). This can be useful to resolve some user space issues.

The command can be executed as `hypernode-servicectl` or `/usr/bin/hypernode-servicectl`. The `help` menu displays the available options.

```console
$ hypernode-servicectl --help
usage: hypernode-servicectl [-h] [--version] [action] [service [service ...]]

Control Hypernode services

positional arguments:
  action      desired action on services (restart|reload)
  service     target service, (mysql|nginx|php7.1-fpm)

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
```

More information on this handy command can be found in this [Hypernode Changelog](https://changelog.hypernode.com/changelog/release-5070-new-hypernode-servicectl-utility-restart-services-app-user/) and the one dedicated to [restarting Redis](https://changelog.hypernode.com/changelog/release-5840-hypernode-servicectl-can-also-restart-redis/).

### Troubleshooting Slow MySQL Queries

First, check whether any slow queries are running right now by running `mytop`. If there are many queries, type ‘o’ to reverse the order and show longest running queries on top. If there’s a particular long running query, type ‘f’ and then the id to view the full query. If you want to abort it, type ‘k’ and then the query id to kill it. Warning: generally only do this for SELECT queries. Killing other queries might corrupt your data. Second, examine recent slow queries by running`less /var/log/mysql/mysql-slow.log`. Once you have find a suspect (for example, a query that takes longer than 2 seconds), you can prefix your querie with the `EXPLAIN` keyword to find where the bottleneck is. For example:

```console
mysql> explain SELECT `main_table`.* FROM `catalogsearch_query` AS `main_table` ORDER BY updated_at DESC LIMIT 5;

+----+-------------+------------+------+---------------+------+---------+------+------+----------------+
| id | select_type | table | type | possible_keys | key | key_len | ref | rows | Extra |
+----+-------------+------------+------+---------------+------+---------+------+------+----------------+
| 1 | SIMPLE | main_table | ALL | NULL | NULL | NULL | NULL | 2159 | Using filesort |
+----+-------------+------------+------+---------------+------+---------+------+------+----------------+
1 row in set (0.00 sec)
```

This will **not** run your query, but tell you how many rows were examined, whether an index was used, and what kinds of sorting algorithms were used. In this case, there was a relatively low number of rows involved (2159). However, the filesort algorithm is extremely slow and should be avoided. See more information about avoiding filesort [here](http://dba.stackexchange.com/questions/44614/is-it-possible-to-avoid-filesort) and [here](http://venublog.com/2007/11/29/mysql-how-to-avoid-filesort/). The solution in this case is to add a proper index on the updated_at column.
