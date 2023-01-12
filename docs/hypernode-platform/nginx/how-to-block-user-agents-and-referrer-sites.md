---
myst:
  html_meta:
    description: "Read in this article how you can both block user agents, as referrer\
      \ sites. We've got you. "
    title: How to block user agents and referrer sites? | Hypernode
redirect_from:
  - /en/hypernode/nginx/how-to-block-user-agents-and-referrer-sites/
  - /knowledgebase/blocking-user-agents-referrers/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-block-user-agents-and-referrer-sites/ -->

# How to Block User Agents and Referrer Sites

**Blocking IP addresses, User Agents or Referres may cause unforseen issues, since it's easy to block more then expected.**

## How to Block User Agents

First you need to know what User Agent you wish to block. You can retrieve such information from the access logs (`/var/log/nginx/access.log`)

```json
{"time":"2020-01-27T13:08:05+00:00", "remote_addr":"80.113.31.106", "remote_user":"", "host":"yourappname.hypernode.io", "request":"GET / HTTP/1.1", "status":"200", "body_bytes_sent":"87", "referer":"", "user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36", "request_time":"0.000", "handler":"", "country":"NL", "port":"80", "ssl_cipher":"", "ssl_protocol":""}
```

Once you know which User Agent you wish to blacklist you can follow the instructions below:

- Create or update the `server.blacklist` file in `/data/web/nginx/`with:

```bash
sensible-editor /data/web/nginx/server.blacklist
```

- Add the following snippet and include the User Agent you wish to block in the first line after `$http_user_agent ~ "`:

```nginx
if ($http_user_agent ~ "Windows 95|Windows 98|biz360.com|xpymep|TurnitinBot|sindice|Purebot|libwww-perl") {
    return 403;
    break;
}
```

## How to Block Referrer Sites

Blocking a referrer site is not much different from blocking a User Agent. Simply create or update the `server.blacklist` file again in `/data/web/nginx/`with:

```bash
sensible-editor /data/web/nginx/server.blacklist
```

and paste the following snippet:

```nginx
if ($http_referer ~* (seo|referrer|redirect|babes|click|girl|jewelry|love|organic|poker|porn|sex|teen|video|webcam) ) {
    return 405;
}
```
