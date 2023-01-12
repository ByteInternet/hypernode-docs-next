---
myst:
  html_meta:
    description: It is increasingly common for spammers to crawl your site and it
      can be hard to trace them down. Here are some strategies for finding and blocking
      them.
    title: How to block spammers and scanners? | Hypernode
redirect_from:
  - /en/support/solutions/articles/48001165533-how-to-block-spammers-and-scanners/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001165533-how-to-block-spammers-and-scanners/ -->

# How to Block Spammers and Scanners

It is increasingly common for spammers to crawl your site. This often results in high load on your Hypernode and a slow site for real visitors.

It can be hard to trace down these abusers. Here are some strategies for finding and blocking them.

## Step 1: Identify Culprits

A common use case is that spammers or scanners fill up all your PHPFPM slots when they scan or brute-force your site. We’ve developed the tool, `hypernode-fpm-status`, to grant you more insight into what is going on in your PHPFPM workers. Try this:

```nginx
root@pup0t4-example-magweb-xls ~ # hypernode-fpm-status

04983 GONE 90.3266 108.61.122.72 POST my.hypernode.io/downloader/index.php?A=loggedin (Mozilla/5.0 (Windows; U; Windows NT 6.0) Gecko/20091201 Firefox/3.5.6 GTB5)
04984 GONE 92.5596 108.61.122.72 POST my.hypernode.io/downloader/index.php?A=loggedin (Mozilla/5.0 (Windows; U; Windows NT 6.0) Gecko/20091201 Firefox/3.5.6 GTB5)
12305 GONE 74.7021+8 46.28.203.130 POST my.hypernode.io/downloader/index.php?A=loggedin (Mozilla/5.0 (Windows; U; Windows NT 6.0) Gecko/20091201 Firefox/3.5.6 GTB5)
12306 GONE 86.3169+2 108.61.122.72 POST my.hypernode.io/downloader/index.php?A=loggedin (Mozilla/5.0 (Windows; U; Windows NT 6.0) Gecko/20091201 Firefox/3.5.6 GTB5)
12307 GONE 74.7289+8 46.28.203.130 POST my.hypernode.io/downloader/index.php?A=loggedin (Mozilla/5.0 (Windows; U; Windows NT 6.0) Gecko/20091201 Firefox/3.5.6 GTB5)
12327 GONE 84.7464+2 46.28.203.130 POST my.hypernode.io/downloader/index.php?A=loggedin (Mozilla/5.0 (Windows; U; Windows NT 6.0) Gecko/20091201 Firefox/3.5.6 GTB5)
12350 GONE 83.9709+2 108.61.122.72 POST my.hypernode.io/downloader/index.php?A=loggedin (Mozilla/5.0 (Windows; U; Windows NT 6.0) Gecko/20091201 Firefox/3.5.6 GTB5)
12351 GONE 77.5164+6 46.28.203.130 POST my.hypernode.io/downloader/index.php?A=loggedin (Mozilla/5.0 (Windows; U; Windows NT 6.0) Gecko/20091201 Firefox/3.5.6 GTB5)
12352 GONE 84.0770+2 46.28.203.130 POST my.hypernode.io/downloader/index.php?A=loggedin (Mozilla/5.0 (Windows; U; Windows NT 6.0) Gecko/20091201 Firefox/3.5.6 GTB5)
12353 GONE 82.5902+3 46.28.203.130 POST my.hypernode.io/downloader/index.php?A=loggedin (Mozilla/5.0 (Windows; U; Windows NT 6.0) Gecko/20091201 Firefox/3.5.6 GTB5)
root@pup0t4-example-magweb-xls ~ #
```

## Step 2: Add IPs to Blacklist

You’ll immediately notice two IPs that are trying to download files from your server. You’ve found your scanners!

Now log in to your Hypernode using SSH and edit `/data/web/nginx/server.blacklist`

```nginx
editor /data/web/nginx/server.blacklist
```

Add the IPs to the file:

```nginx
## Block these IP's from using your site. They should have proper CIDR notation.
## It is not possible to include host/domainnames here.

# deny 62.195.123.45;
# deny 87.211.184.188;
# deny 213.186.119.0/24;
# deny 213.186.120.0/24;

deny 108.61.122.72; # look out! always close with semi-colon ;
deny 46.28.203.130;
```

If you make a mistake, the shell will warn you:

```nginx
>app@pup0t4-mynode-magweb-xls

Your Nginx configuration contains errors, please check
/data/web/nginx/nginx_error_output to see them.

~ $
```

## Step 3: Check to See That All Is Well

Now you’ll see that the client is banned from the server:

```json
{
    "time":"2014-11-21T09:39:31+00:00",
    "remote_addr":"108.61.122.72",
    "remote_user":"-",
    "host":"my.hypernode.io",
    "request":"POST /downloader/index.php?A=loggedin HTTP/1.1",
    "status":"403",
    "body_bytes_sent":"162",
    "referer":"-",
    "user_agent":"Mozilla/5.0 (Windows; U; Windows NT 6.0) Gecko/20091201 Firefox/3.5.6 GTB5",
    "request_time":"0.000",
    "handler":"",
    "country":"US",
    "android_dupe_bug":"",
    "ssl_cipher":"-",
    "ssl_protocol":"-"
}
```
