---
myst:
  html_meta:
    description: Here are a few handy helpers you can use on Hypernode to get a quick
      overview of what kind of requests a Hypernode is currently serving.
    title: What kind of request is my Hypernode serving?
---

# What kind of requests is my Hypernode serving

There are a few handy helpers you can use on Hypernode to get a quick overview of what kind of requests a Hypernode is currently serving.

## mostreqs

Shows you the top requests from the latest `/var/log/nginx/access.log`

```console
app@levkc9-yourappname-magweb-cmbs:~$ mostreqs
     20 "GET / HTTP/1.1"
      6 "GET /wp-login.php HTTP/1.1"
      3 "GET /favicon.ico HTTP/1.1"
alias mostreqs='grep phpfpm /var/log/nginx/access.log | jq .request | sus | tail -n 10 | tac'
```

## livereqs

Shows you a live view of the requests that are currently landing in NGINX

```console
app@levkc9-yourappname-magweb-cmbs:~$ livereqs
1.2.3.4	NL			2021-12-06T14:27:08+00:00	GET / HTTP/1.1	301	Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
alias livereqs='tal|pnl --fields ip,country,handler,remote_user,date,req,status,user_agent'
```

## livefpm

Shows you a real-time overview of what the PHP-FPM workers are processing. This is the same as running `hypernode-fpm-status` in a loop.

```console
$ livefpm
$ alias livefpm='watch -n0.2 '\''hypernode-fpm-status | cut -c1-$(stty size </dev/tty | cut -d" " -f2)'\'''
$ hypernode-fpm-status
21143 IDLE   0.1s US 1.2.3.4  GET  magweb/status.php   (Hypernode heartbeat)
21144 IDLE   0.0s NL 1.2.3.4  GET  magweb/status.php   (Hypernode heartbeat)
21121 IDLE   0.0s SG 1.2.3.4 GET  magweb/status.php   (Hypernode heartbeat)
```
