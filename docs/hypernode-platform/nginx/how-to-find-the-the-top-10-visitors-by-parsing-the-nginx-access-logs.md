---
myst:
  html_meta:
    description: 'To find the top 10 visitors of your Magento shop, you can easily
      use the Nginx access logging tot get these statistics. Read all about it in
      this article. '
    title: Find the top 10 visitors by parsing the NGINX access logs
redirect_from:
  - /en/hypernode/nginx/how-to-find-the-the-top-10-visitors-by-parsing-the-nginx-access-logs/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-find-the-the-top-10-visitors-by-parsing-the-nginx-access-logs/ -->

# How to find the the Top 10 Visitors by Parsing the Nginx access.logs

To find the top 10 visitors of your Magento shop, you can easily use the Nginx access logging tot get these statistics. With one command on the CLI, you will be able to get many insights on your access logging.

Our Nginx access logging are generated in the JSON format. This way we can easily parse them from scripts, without having to use a special Nginx logging parser.

To show the Nginx access logging in a more human readable format, we created a little command line tool called `hypernode-parse-nginx-log`

## Parsing Nginx Logs

- To get started: Go to the Nginx log directory

```nginx
cd /var/log/nginx
```

- Get the top 10 of today per domain

```nginx
cat access.log | grep $domain | hypernode-parse-nginx-log | awk '{ print $4}' | sort | uniq -c | sort -n | tail -n 10

```

- Get the top 40 of yesterday

```nginx
zcat access.log.1.gz | hypernode-parse-nginx-log | awk '{ print $4}' | sort | uniq -c | sort -n | tail -n 40
```

- Get the top 100 of all logs present

```nginx
zcat access.log* | hypernode-parse-nginx-log | awk '{ print $4}' | sort | uniq -c | sort -n | tail -n 100
```

- Finding IP’s that do many POST requests

```nginx
cat access.log | hypernode-parse-nginx-log | grep POST | awk '{print $4}' | sort | uniq -c | sort -n
```

## Write the Output to a File

To redirect the output of your one-liners to a file as well to your screen, you can use this command:

```nginx
cat access.log | hypernode-parse-nginx-log | grep POST | tee /tmp/some_file.txt
```
