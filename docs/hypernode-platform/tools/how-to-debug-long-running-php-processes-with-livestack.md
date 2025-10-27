---
myst:
  html_meta:
    description: 'If you have a PHP process that has been running for a long while, it can be difficult to find out what it’s currently doing.
      With livestack.py you can see a point-in-time stack trace of a running process, and have a place to start debugging further.'
    title: How to debug long running PHP processes with livestack on Hypernode?
---

# How to debug long running PHP processes with livestack.py

[livestack.py](https://github.com/bigbridge-nl/livestack) is a debugging tool built by [Bigbridge](https://bigbridge.nl).
It can be used on Hypernode to inspect the current stack frame of a running PHP process.
It requires some setup to get running, but it is very powerful when investigating long running cron commands, or hanging web requests.

Note that livestack.py is not a Hypernode project, and as such Hypernode does not give support for the usage or with any issues of livestack.py.
You can [create a GitHub issue](https://github.com/bigbridge-nl/livestack/issues) on the livestack GitHub page when you encounter problems.

## Setup

First, contact [hypernode support](mailto:support@hypernode.io?subject=PHP%20debug%20symbols) to ask them to enable the php-dbg (PHP debug symbols) package for your Hypernode.
For now this is a manual step that needs to be done by support on any Hypernode you want to use livestack.py on.

Then, you can copy the script to your hypernode:

```bash
# On your hypernode:
git clone https://github.com/bigbridge-nl/livestack.git
```

## General usage

Let's say you're investigating an index process that is taking a lot of time to complete:

```shell
app@webshop-magweb-aws:~$ ps aux | grep cron:run
app      1614969  0.0  0.0   2584   932 ?        S    10:39   23:51 /usr/bin/php /data/web/webshop.nl/deployments/releases/current/bin/magento cron:run --group index
```

The ps output shows this process has been running for a long time.
It may be in a loop, or waiting on something, or just processing way too many things---but you don't know yet.

If you knew where to look you could use XDebug locally or on your [staging server](/hypernode-platform/php/remote-debugging.md), but the first step is knowing where to look.
Using livestack.py you can pause the program momentarily and print out a stacktrace.
Now you have an idea what the program is currently running.
By running livestack.py a few times, you can see in which area of the code PHP is spending the most time.

Let's see how it works with an example:

```shell
app@webshop-magweb-aws:~$ ~/livestack/livestack.py 'cron:run --group index'
Printing stack for '/usr/bin/php /data/web/webshop.nl/deployments/releases/current/bin/magento cron:run --group index' (PID: 1614969)

#0 (internal) - curl_exec
#1 vendor/ezimuel/ringphp/src/Client/CurlHandler.php:89 - GuzzleHttp\Ring\Client\CurlHandler::_invokeAsArray
#2 vendor/ezimuel/ringphp/src/Client/CurlHandler.php:68 - GuzzleHttp\Ring\Client\CurlHandler::__invoke
#3 vendor/ezimuel/ringphp/src/Client/Middleware.php:30 - GuzzleHttp\Ring\Client\Middleware::GuzzleHttp\Ring\Client\{closure}
#4 vendor/elasticsearch/elasticsearch/src/Elasticsearch/Connections/Connection.php:265 - Elasticsearch\Connections\Connection::Elasticsearch\Connections\{closure}
#5 vendor/elasticsearch/elasticsearch/src/Elasticsearch/Connections/Connection.php:241 - Elasticsearch\Connections\Connection::performRequest
#6 vendor/elasticsearch/elasticsearch/src/Elasticsearch/Transport.php:110 - Elasticsearch\Transport::performRequest
#7 vendor/elasticsearch/elasticsearch/src/Elasticsearch/Client.php:1929 - Elasticsearch\Client::performRequest
#8 vendor/elasticsearch/elasticsearch/src/Elasticsearch/Client.php:347 - Elasticsearch\Client::bulk
#9 vendor/magento/module-elasticsearch-7/Model/Client/Elasticsearch.php:173 - Magento\Elasticsearch7\Model\Client\Elasticsearch::bulkQuery
#10 vendor/magento/module-elasticsearch/Model/Adapter/Elasticsearch.php:237 - Magento\Elasticsearch\Model\Adapter\Elasticsearch::addDocs
#11 vendor/magento/module-elasticsearch/Model/Indexer/IndexerHandler.php:140 - Magento\Elasticsearch\Model\Indexer\IndexerHandler::saveIndex
#12 vendor/magento/module-catalog-search/Model/Indexer/Fulltext.php:176 - Magento\CatalogSearch\Model\Indexer\Fulltext::executeByDimensions
#13 vendor/magento/module-catalog-search/Model/Indexer/Fulltext.php:236 - Magento\CatalogSearch\Model\Indexer\Fulltext::Magento\CatalogSearch\Model\Indexer\{closure}
...
#52 vendor/symfony/console/Application.php:1040 - Symfony\Component\Console\Application::doRunCommand
#53 vendor/symfony/console/Application.php:301 - Symfony\Component\Console\Application::doRun
#54 vendor/magento/framework/Console/Cli.php:116 - Magento\Framework\Console\Cli::doRun
#55 vendor/symfony/console/Application.php:171 - Symfony\Component\Console\Application::run
#56 bin/magento:23 - (unknown function)
```

In this example the grep mode is used.
The first argument is a regex which searches through the running PHP processes.
The equivalent shell command would be (roughly) `ps aux | grep php | grep 'cron:run --group index'`, as livestack.py only filters through php processes.

Another way to use livestack.py is to supply the process ID (PID) directly.
For this, use the `--pid` option.
The two modes work equivalently.

```shell
app@webshop-magweb-aws:~$ ~/livestack/livestack.py --pid=1614969
```

So in this example you can see something happening in the fulltext indexer that's causing problems!
If you run livestack.py a couple of times in short succession, and every time you see the same curl_exec call by this indexer you know where the problem is.
You may not yet know what exactly is causing the problem, but you can start your debugging session somewhere.

## Examining long running web requests

You may already know how to use livefpm and hypernode-fpm-status to see [what kinds of requests your Hypernode is currently serving](/hypernode-platform/tools/what-kind-of-request-is-my-hypernode-serving.md).
You can investigate any long running requests further using livestack.py.


As `hypernode-fpm-status | grep '/some/url'` would give you current PHP process generating some url, you can also run `livestack.py --fpm '/some/url'` to find the current stack trace of that PHP process.

When using the `--fpm` flag, you are basically grepping through the output of `hypernode-fpm-status`, so you can search for a url, ip or user-agent.

An example (this only works if you have a single BUSY request):

```shell
app@webshop-magweb-aws:~$ ./livestack.py --fpm BUSY
Printing stack for 'BUSY 498.7s NL phpfpm    95.97.37.190    GET  webshop.hypernode.io/men/tops-men.html?color=58&x=8123111111   (Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36)' (PID: 825564)

#0 (internal) - sleep
#1 /data/web/deployments/releases/3/pub/index.php:11 - (unknown function)
```

Once again, you can also use the `--pid` option instead of grepping using livestack.py.
You don't need to use the `--fpm` option when you have the PID directly.

## Considerations with production usage

Livestack.py works in production, where you normally would not have XDebug enabled.
However, do note that livestack.py does pause your PHP script or request for one to two seconds.
In cases where the script or request seems to be hanging anyway this may not matter but it's an important consideration.

Also, although livestack.py has not managed to crash the PHP process with simple stack trace dumping during testing at Bigbridge, it is certainly possible (and not hard) to crash the PHP process in interactive usage.
Care should be taken to not prod at the PHP internals too much when using GDB or livestack.py in interactive mode.

## Advanced (interactive) usage

Internally, livestack.py uses GDB to attach to the running process and inspect it's memory.
After commanding GDB, it unattaches and the PHP process is free to continue running.
However, in interactive mode you can stay in GDB and issue more commands.
This keeps the PHP process paused while you are interacting with GDB.
Of course, this hangs the PHP script or request for as long as you stay attached.

Interactive mode allows you to jump into GDB giving you full power to see every byte of process memory and execution flow.
Besides the regular GDB commands, two extra PHP specific commands are added by livestack.py:

- `php-print-stack` This is the same as a regular incantation of livestack.py, and prints the stack trace PHP was currently executing.

- `php-frame-info <frame-number>` Using the frame number from `php-print-stack`, get some more information about this function call.
Currently this only shows the contents of "simple" function arguments.
As internally this uses json_encode, object arguments are not supported.
However, you can see the sql insert command or the bindings of the `Magento\Framework\DB\Adapter\Pdo\Mysql::query` function for example.

Using interactive mode requires a bit more GDB knowledge, and ideally knowledge of the PHP/Zend C code internals.
One interesting command to get started may be the `bt full` command, which shows you a stack trace of the PHP internals.

When you want to exit the interactive mode, you can type `Ctrl+D` or use the `quit` command.
After detaching, the process continues on like normal.
