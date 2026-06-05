---
myst:
  html_meta:
    description: Learn how to view Botstopper logs.
    title: How to view Botstopper logs on Hypernode | Hypernode
---

# How to View Botstopper Logs on Hypernode

Once you have enabled the Botstopper and it's up-and-running, it's important to monitor its activity and performance. Botstopper logs provide valuable insights into the traffic patterns, blocked requests, and overall effectiveness of the bot mitigation. Here's how you can view the Botstopper logs on your Hypernode.

Use the `hypernode-parse-botstopper-log` CLI tool to view and analyze Botstopper logs in a readable format.

## Log Location

Botstopper writes its logs to:

```text
/var/log/botstopper/botstopper.log
```

The raw log file uses [JSON Lines](https://jsonlines.org/). Each line is a separate JSON object. This is useful for automation, but it is not the easiest format to inspect manually.

## View Today's Logs

Run the parser with `--today` to inspect today's Botstopper log entries:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --today
```

The output shows the timestamp, log level, message, and request metadata:

```console
2026-06-05 01:40:05.717877576Z [INF] new challenge issued > host=example.com method=GET path=/ user_agent="Mozilla/5.0 (compatible; CensysInspect/1.1; +https://about.censys.io/)" client_ip=66.132.172.211 accept_language="" priority="" challenge=019e956f-ffd3-735d-9dce-5fe1aa40d534
2026-06-05 02:07:11.959647899Z [INF] new challenge issued > host=example.com method=GET path=/ user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0" client_ip=134.209.40.161 accept_language=en-US,en;q=0.5 priority="u=0, i" challenge=019e9588-d054-7c99-8684-61bbcb099b2f
2026-06-05 02:38:01.225327165Z [INF] new challenge issued > host=example.com method=GET path=/compete-track-tote.html user_agent="Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; TikTokSpider; ttspider-feedback@tiktok.com)" client_ip=47.128.111.110 accept_language=en-US,en;q=0.5 priority="u=0, i" challenge=019e95a5-0807-759a-80d7-f450d68a1923
```

Common messages include `new challenge issued` for visitors or bots that received a browser challenge.

## Filter Logs

Use `--filter` to narrow the output to entries matching a specific field.

For example, only show entries for one host:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --today --filter host=example.com
```

Filters support these operators:

| Operator | Meaning                                      |
| -------- | -------------------------------------------- |
| `=`      | Field exactly equals the value.              |
| `!=`     | Field does not equal the value.              |
| `~`      | Field matches the regular expression.        |
| `!~`     | Field does not match the regular expression. |

Filter by exact text with `=`:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --today --filter client_ip=134.185.85.99
```

Exclude a specific value with `!=`:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --today --filter host!=staging.example.com
```

Filter with a regular expression by using `~`:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --today --filter path~'^/wp-'
```

Exclude values that match a regular expression with `!~`:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --today --filter user_agent!~'(?i)googlebot'
```

Use `--list-fields` to see the available fields:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --list-fields
```

## Select a Date

The parser can read logs for different dates:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --today
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --yesterday
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --days-ago 3
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --date 2026-06-05
```

Use `--filename` when you want to parse a specific log file:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --filename /var/log/botstopper/botstopper.log
```

## Customize Output

By default, the parser prints a useful set of request fields. Use `--fields` to choose which metadata fields are shown after the message:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --today --fields host,path,client_ip,user_agent
```

Use `--format` when you want full control over the output format:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --today --format '%(time)s [%(level)s] %(msg)s > client_ip=%(client_ip)s host=%(host)s method=%(method)s path=%(path)s'
```

Add `--all` if you also want to include non-request service, startup, and configuration events:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --today --all
```

## Command Help

Use `--help` to view all parser options:

```console
app@example-magweb-cmbl ~ $ hypernode-parse-botstopper-log --help
usage: Parse, filter, and inspect botstopper log files. [-h] [--fields FIELDS] [--format FORMAT] [--list-fields] [--filter FILTER] [--verbose] [--all]
                                                        [--filename FILENAME | --today | --yesterday | --days-ago DAYS_AGO | --date DATE]

options:
  -h, --help           show this help message and exit
  --fields FIELDS      Comma separated list of metadata fields to display after the message. Try: --fields ip,host,req,rule,bot,ua. Use --list-fields to display all available fields.
  --format FORMAT      Format string to display fields. Example: --format '%(time)s [%(level)s] %(msg)s > client_ip=%(client_ip)s host=%(host)s method=%(method)s path=%(path)s'
  --list-fields        Display a list of available fields
  --filter FILTER      Filter to apply. Format: <field>=<str>, <field>!=<str>, <field>~<regex>, or <field>!~<regex>
  --verbose, -v        Display debug output
  --all                Include non-request service, startup and config events
  --filename FILENAME  Path of botstopper logfile to parse
  --today              Analyze today's log lines
  --yesterday          Analyze yesterday's log lines
  --days-ago DAYS_AGO  Analyze logs from a number of days ago
  --date DATE          Analyze logs from a specific date
```
