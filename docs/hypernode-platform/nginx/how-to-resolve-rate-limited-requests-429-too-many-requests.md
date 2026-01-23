---
myst:
  html_meta:
    description: This article will explain the differences between the different rate-limiting
      methods, how to find which rate-limiting method applies and how to override
      them.
    title: How to Resolve 429 Too Many Requests | Rate Limited Requests
redirect_from:
  - /en/hypernode/nginx/how-to-resolve-rate-limited-requests-429-too-many-requests/
  - /knowledgebase/resolving-429-many-requests/
---

# How to Resolve Rate Limited Requests (429 Too Many Requests)

To protect your Hypernode from all kinds of attacks, bots, brute forces, and script kiddies causing downtime, we've implemented several layers of rate limiting.

Most of these rate-limit methods only apply to bots. Still, to avoid FPM worker depletion, we [implemented a rate-limiting mechanism per IP](https://changelog.hypernode.com/release-4735-upper-limit-active-php-requests-per-ip/) to prevent one single IP from exhausting the available FPM workers.

This article will explain the differences between the different rate-limiting methods and show you how to find which rate-limiting method applies and, if needed, how to override them.

## Rate Limiting Methods

On Hypernode we currently differentiate between two rate limiting methods and thus so-called `zones:`

- Rate limiting based on User Agents and requests per second (zone `bots`)
- Rate limiting based on requests per IP address (zone `zoneperip`)

Both methods are implemented using [Nginx's limit_req module](https://nginx.org/en/docs/http/ngx_http_limit_req_module.html)

### Determining the Applied Rate Limiting Method

You can quickly determine which method of rate limiting was the cause of the request being 429'd since each time any of the rate-limiting methods are hit, a message will be logged in the Nginx error log.

To look for rate limiting messages in the error log, you can run the following command:

```console
$ grep -E 'limiting (requests|connections)' /var/log/nginx/error.log
2020/06/07 13:33:37 [error] limiting requests, excess: 0.072 by zone "bots", client: 203.0.113.104, server: example.hypernode.io, request: "GET /api/ HTTP/2.0", host: "example.hypernode.io"
2020/06/07 13:33:37 [error] limiting connections by zone "zoneperip", client: 198.51.100.69, server: example.hypernode.io, request: "POST /admin/ HTTP/2.0", host: "example.hypernode.io"
```

A log entry where rate limit is applied to user-agents and requests per second (based on the `bots` zone):

```
2020/06/07 13:33:37 [error] limiting requests, excess: 0.072 by zone "bots", client: 203.0.113.104, server: example.hypernode.io, request: "GET /api/ HTTP/2.0", host: "example.hypernode.io"
```

A log entry where the rate limit is applied per IP address (based on the `zoneperip` zone):

```
2020/06/07 13:33:37 [error] limiting connections by zone "zoneperip", client: 198.51.100.69, server: example.hypernode.io, request: "POST /admin/ HTTP/2.0", host: "example.hypernode.io"
```

**Note: Per‑IP rate limiting only applies to requests handled by PHP and not to static content.**

## Rate Limiting for Bots and Crawlers

Every day, your webshop is visited by many different bots and crawlers. While some, like Google, are important, many only have [a negative impact](../../best-practices/performance/how-to-fix-performance-issues-caused-by-bots-and-crawlers.md) on your site, especially if they don’t follow your robots.txt. To protect your Hypernode against negative performance impacts by misbehaving bots, it utilizes an advanced rate-limiting mechanism. This slows down the hit rate for unimportant bots, leaving more performance for the bots you do care about and, more importantly, your actual visitors.

### Rejecting 429 Too Many Requests

Since our goal is not to block bots but to rate limit them nicely, we must be careful with how we reject them. As such, the best way to reject them is with the ***429 Too Many Requests*** message. This tells the visiting bot that the site is currently unavailable, but the server is there. This is a temporary state so that they can retry at a later time. This does not negatively influence the ranking in any search engine, as the site is there when the bot connects at a later time.

### How to Configure the Bot Rate Limiter

Some bots are exempt from rate limiting by default, like Google, Bing, and several monitoring systems. These bots never get rate limited since they usually abide by the robots.txt. However, some bots don't follow the instructions given in robots.txt or are used by abusive crawlers. These bots will be rate limited at one request per second. Any requests over this limit will then return a 429 error. If you want, you can override the system-wide configuration on who gets blocked and who does not. To get started, place the following in a config file called `/data/web/nginx/http.ratelimit`:

```nginx
map $http_user_agent $limit_bots {
    default '';
    ~*(google|bing|heartbeat|uptimerobot|shoppimon|facebookexternal|monitis.com|Zend_Http_Client|magereport.com|SendCloud/|Adyen|ForusP|contentkingapp|node-fetch|Hipex|xCore|Mollie) '';
    ~*(http|crawler|spider|bot|search|Wget|Python-urllib|PHPCrawl|bGenius|MauiBot|aspiegel) 'bot';
}
```

**Note: do not remove the heartbeat entry! As this will break the monitoring of your Hypernode**

As you can see, this sorts all visitors into two groups:

- On the first line, the allowlist, you find the keywords that are exempt from rate limiting, like: `google`, `bing`, `heartbeat`, or `magereport.com`.
- The second line contains keywords for generic and abusive bots and crawlers, which can trigger the rate limiter, like `crawler`, `spider`, or `bot`.

The keywords are separated by `|` characters since it is a regular expression.

### Allowlisting Additional User Agents

To extend the allowlist, first determine what user agent you wish to add. Use the access log files to see what bots get blocked and which user agent identification it uses. To find the user agent, you can use the following command:

```console
app@abcdef-example-magweb-cmbl:~$ pnl --today --fields time,status,remote_addr,request,user_agent --filter status=429
2020-06-07T13:33:37+00:00       429     203.0.113.104   GET /api/ HTTP/2.0       SpecialSnowflakeCrawler 3.1.4
2020-06-07T13:35:37+00:00       429     203.0.113.104   GET /api/ HTTP/2.0       SpecialSnowflakeCrawler 3.1.4
```

In the example above you can see that a bot with the User Agent `SpecialSnowflakeCrawler 3.1.4` triggered the ratelimiter.  As it contains the word ‘crawler’, it matches the second regular expression and is labeled as a bot. Since the allowlist line overrules the denylist line, the best way to allow this bot is to add their user agent to the allowlist instead of removing ‘crawler’ from the blacklist:

```nginx
map $http_user_agent $limit_bots {
    default '';
    ~*(specialsnowflakecrawler|google|bing|heartbeat|uptimerobot|shoppimon|facebookexternal|monitis.com|Zend_Http_Client|magereport.com|SendCloud/|Adyen|ForusP|contentkingapp|node-fetch|Hipex|xCore|Mollie) '';
    ~*(http|crawler|spider|bot|search|Wget|Python-urllib|PHPCrawl|bGenius|MauiBot|aspiegel) 'bot';
}
```

Instead of adding the complete User Agent to the regex, it’s often better to limit it to just an identifying keyword, as shown above. The reason behind this is that the string is evaluated as a Regular Expression, which means that extra care needs to be taken when adding anything other than alphanumeric characters. Also, as user agents might change slightly over time, an overly specific string may stop matching and the bot will no longer be allowlisted.

### Known Rate Limited Plugins and Service Providers

There are a couple of plugins and service providers that tend to hit the blacklisted keyword in the `http.ratelimit` snippet and, therefore, may need to be excluded individually. Below we have listed them and their User Agents for your convenience

- Adyen - `Jakarta Commons-HttpClient/3.0.1`
- Adyen - `Apache-HttpClient/4.4.1 (Java/1.8.0_74)`
- Adyen - `Adyen HttpClient 1.0`
- MailPlus - `Jersey/2.23.1`
- Mollie - `Mollie.nl HTTP client/1.0`
- Screaming - `Screaming Frog SEO Spider`

Besides the above-known plugins that will hit the blacklisted keyword, `http.ratelimit` we know that Picqer will also hit the rate limiter because of being blocked by "**zoneperip**". Please find [here](https://picqer.com/files/ip-addresses.txt) the IP addresses of Picqer. You can exclude those IP addresses from hitting the rate limiter if you follow the [instructions](#known-rate-limited-plugins-and-service-providers).

## Rate Limiting per IP Address

To prevent a single IP from using all the FPM workers available simultaneously, leaving no workers available for other visitors, we implemented a per IP rate limit mechanism. This mechanism sets a maximum amount of PHP-FPM workers that can be used by one IP to 20. This way, one single IP address cannot deplete all the available FPM workers, leaving other visitors with an error page or a non-responding site.

**Please note:** only add the `http.ratelimit` file in the Nginx root. Don't add it to the specific vhost as well, as this may cause conflicts.

### How per‑IP limiting works (what you can influence)

The platform manages the global per‑IP limiter (zone and limits). You control only the key variable used for counting connections: `$limit_conn_per_ip`. If this variable is an empty string, the per‑IP limiter is effectively disabled for that request; if it contains the client IP, that request is counted towards that IP.

### Exclude IP addresses from the per‑IP rate limiting

In some cases, it might be necessary to exclude specific IP addresses from the per‑IP rate limiting. Define an allowlist and compose the effective key using a geo→map chain in `/data/web/nginx/http.ratelimit`:

```nginx
# 1) Mark IPs/CIDRs that should be exempt from per‑IP limiting
geo $limit_conn_ip_allow {
    default 1;          # 1 = enforce limit
    1.2.3.4 0;          # 0 = exempt
}

# 2) Build the base key used for per‑IP limiting. If exempt → empty key disables per‑IP limiting for this request
map $limit_conn_ip_allow $limit_conn_per_ip_base {
    0 '';
    1 $remote_addr;
}

# 3) Exclude additional URLs from per-IP limiting
map $request_uri $limit_conn_per_ip {
    default $limit_conn_per_ip_base;
    # ~^/rest/V1/example-call/ '';
    # ~^/elasticsearch\.php$ '';
    # ~^/graphql '';
}
```

In this example, we have excluded the IP address **1.2.3.4** by emitting an empty key, no URL whitelists are active in the above example.

In addition to excluding a single IP address, it is also possible to allow a whole range of IP addresses. You can do this by using the so-called CIDR notation (e.g., 198.51.100.0/24 to allowlist all IP addresses within the range 198.51.100.0 to 198.51.100.255). Extend the `geo` block accordingly:

```nginx
geo $limit_conn_ip_allow {
    default 1;
    1.2.3.1 0;
    1.2.3.0/24 0;
}
```

### Disable per‑IP rate limiting

When your shop performance is very poor, it’s possible all your FPM workers are busy just serving regular traffic. Handling a request takes so much time that all workers are continuously depleted by a small number of visitors. We highly recommend optimizing your shop for speed and a temporary upgrade to a bigger plan if this situation arises. Disabling the rate limit will not fix this problem but only change the error message from a `Too many requests` error to a timeout error.

For debugging purposes, however, it could be helpful to disable the per‑IP connection limit for all IPs. With the following snippet in `/data/web/nginx/http.ratelimit`, it is possible to disable per‑IP rate limiting entirely by emitting an empty key for all requests:

```nginx
map $request_uri $limit_conn_per_ip {
    default '';
}
```

**Warning: Only use this setting for debugging purposes! Using this setting on production Hypernodes is highly discouraged, as your shop can be easily taken offline by a single IP using slow and/or flood attacks.**

### Exclude specific URLs from the per‑IP rate limiting mechanism

To exclude specific URLs from being rate‑limited, use the `map $request_uri $limit_conn_per_ip` you added above in `/data/web/nginx/http.ratelimit` and add/uncomment entries like:

```nginx
map $request_uri $limit_conn_per_ip {
    default $limit_conn_per_ip_base;
    ~^/rest/V1/example-call/ '';
    ~^/elasticsearch\.php$ '';
    ~^/graphql$ '';
}
```

With these entries, the URLs `*/rest/V1/example-call/*`, `/elasticsearch.php`, and `/graphql` are excluded from per‑IP limiting. The platform’s global limiter will use `$limit_conn_per_ip` implicitly. You can also combine this with a regular allowlist, as described above.

### Debugging per‑IP rate limiting

Define a custom JSON log format that records the effective per‑IP key and enable it. Add the JSON log format in `/data/web/nginx/http.ratelimit`:

Ensure the log directory exists:

```bash
mkdir -p /data/web/log
```

Then configure the JSON log format and enable the access log:

```text
log_format custom escape=json '{'
                                       '"time":"$time_iso8601", '
                                       '"remote_addr":"$remote_addr", '
                                       '"host":"$http_host", '
                                       '"request":"$request", '
                                       '"status":"$status", '
                                       '"request_time":"$request_time", '
                                       '"user_agent":"$http_user_agent", '
                                       '"limit_conn_per_ip":"$limit_conn_per_ip"'
                                     '}';
access_log /data/web/log/nginx-custom custom;
```

How to read it:

- "limit_conn_per_ip" empty: per‑IP limiter disabled (allowlisted IP/CIDR or URL exclusion)
- Rejections from the per‑IP limiter are logged to the error log, not the access log.

Inspect and correlate recent rejections with keys seen in the access log:

```bash
grep -E 'limiting (requests|connections)' /var/log/nginx/error.log | tail -n 50
tail -n 200 /data/web/log/nginx-custom | jq -r '. | "\(.remote_addr) \(.request) \(.limit_conn_per_ip)"' | tail -n 50
```

### How to Serve a Custom Static Error Page to Rate Limited IP Addresses

If you would like to, you may serve a custom error page to IP addresses that are rate limited. Simply create a static HTML file in `/data/web/public` with any content that you wish to show to these rate-limited IP addresses. Furthermore, you need to create an Nginx configuration file called `/data/web/nginx/server.custom_429` as well. The content of this file should be as follows:

```nginx
error_page 429 /ratelimited.html;
location = /ratelimited.html {
    root /data/web/public;
    internal;
}
```

This snippet will serve a custom static file called `ratelimited.html` to IP addresses that are using too many PHP workers.

**Warning: Only use a static (HTML) page, as creating a PHP script to render an error will be rate-limited as well, causing an endless loop.**
