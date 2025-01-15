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

To protect your Hypernode from all kinds of attacks, bots, brute forces, and scriptkiddies causing downtime, we've implemented several layers of rate limiting.

Most of these rate-limit methods only apply to bots. Still, to avoid FPM worker depletion, we [implemented a rate-limiting mechanism per IP](https://changelog.hypernode.com/release-4735-upper-limit-active-php-requests-per-ip/) to prevent one single IP from exhausting the available FPM workers.

This article will explain the differences between the different rate-limiting methods and show you how to find which rate-limiting method applies and, if needed, how to override them.

## Rate Limiting Methods

On Hypernode we currently differentiate between two rate limiting methods and thus so-called `zones:`

- Rate limiting based on User Agents and requests per second (zone `bots`)
- Rate limiting based on requests per IP address (zone `zoneperip`)

Both methods are implemented using [NginX's limit_req module](http://nginx.org/en/docs/http/ngx_http_limit_req_module.html)

### Determining the Applied Rate Limiting Method

You can quickly determine which method of Rate Limiting was the cause of the request being 429'd since each time any of the rate-limiting methods are hit, a message with be logged in the Nginx error log.

To look for rate limiting messages in the error log, you can run the following command:

```console
$ grep limiting.requests /var/log/nginx/error.log
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

**Note: Per IP rate limiting only applies to requests handled by PHP and not to the static content.**

## Rate Limiting for Bots and Crawlers

Every day, your webshop is visited by many different bots and crawlers. While some, like Google, are important, many only have [a negative impact](../../best-practices/performance/how-to-fix-performance-issues-caused-by-bots-and-crawlers.md) on your site, especially if they don’t follow your robots.txt. To protect your Hypernode against negative performance impacts by misbehaving bots, it utilizes an advanced rate-limiting mechanism. This slows down the hit rate for unimportant bots, leaving more performance for the bots you do care about and, more importantly, your actual visitors.

### Rejecting 429 Too Many Requests

Since our goal is not to block bots but to rate limit them nicely, we must be careful with how we reject them. As such, the best way to reject them is with the ***429 Too Many Requests*** message. This tells the visiting bot that the site is currently unavailable, but the server is there. This is a temporary state so that they can retry at a later time. This does not negatively influence the ranking in any search engine, as the site is there when the bot connects at a later time.

### How to Configure the Bot Rate Limiter

Some bots are default exempt from rate limitings, like Google, Bing, and several monitoring systems. These bots never get rate limited since they usually abide by the robots.txt. However, some bots don't follow the instructions given in robots.txt or are used by abusive crawlers. These bots will be rate limited at one request per second. Any requests over this limit will then return a 429 error. If you want, you can override the system-wide configuration on who gets blocked and who does not. To get started, place the following in a config file called `/data/web/nginx/http.ratelimit`:

```nginx
map $http_user_agent $limit_bots {
    default '';
    ~*(google|bing|heartbeat|uptimerobot|shoppimon|facebookexternal|monitis.com|Zend_Http_Client|magereport.com|SendCloud/|Adyen|ForusP|contentkingapp|node-fetch|Hipex|xCore|Mollie) '';
    ~*(http|crawler|spider|bot|search|Wget|Python-urllib|PHPCrawl|bGenius|MauiBot|aspiegel) 'bot';
}
```

**Note: do not remove the heartbeat entry! As this will break the monitoring of your Hypernode**

As you can see, this sorts all visitors into two groups:

- On the first line, the allowlist, you find the keywords that are exempt from the rate liming, like: `google`, `bing`, `heartbeat`, or `magereport.com`.
- The second line, contains keywords for generic and abusive bots and crawlers, which can trigger the ratelimiter, like `crawler`, `spider`, or `bot`

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
    ~*(specialsnowflakecrawler|google|bing|heartbeat|uptimerobot|shoppimon|facebookexternal|monitis.com|Zend_Http_Client|magereport.com|SendCloud/|Adyen|ForusP|contentkingapp|node-fetch|Hipex) '';
    ~*(http|crawler|spider|bot|search|Wget|Python-urllib|PHPCrawl|bGenius|MauiBot|aspiegel) 'bot';
}
```

Instead of adding the complete User Agent to the regex, it’s often better to limit it to just an identifying keyword, as shown above. The reason behind this is that the string is evaluated as a Regular Expression, which means that extra care needs to be taken when adding anything other than alphanumeric characters. Also as user agents might change slightly over time, this may this bot will no longer be allowlisted over time.

### Known Rate Limited Plugins and Service Provider

There are a couple of plugins and service providers that tend to hit the blacklisted keyword in the `http.ratelimit` snippet and, therefore, may need to be excluded individually. Below we have listed them and their User Agents for your convenience

- Adyen - `Jakarta Commons-HttpClient/3.0.1`
- Adyen - `Apache-HttpClient/4.4.1 (Java/1.8.0_74)`
- Adyen - `Adyen HttpClient 1.0`
- MailPlus - `Jersey/2.23.1`
- Mollie - `Mollie.nl HTTP client/1.0`
- Screaming - `Screaming Frog SEO Spider`

Besides the above-known plugins that will hit the blacklisted keyword, `http.ratelimit` we know that Picqer will also hit the rate limiter because of being blocked by "**zoneperip**". Please find [here](https://picqer.com/files/ip-addresses.txt) the IP addresses of Picqer. You can exclude those IP addressess from hitting the rate limiter if you follow the [instructions](#known-rate-limited-plugins-and-service-provider).

## Rate Limiting per IP Address

To prevent a single IP from using all the FPM workers available simultaneously, leaving no workers available for other visitors, we implemented a per IP rate limit mechanism. This mechanism sets a maximum amount of PHP-FPM workers that can be used by one IP to 20. This way, one single IP address cannot deplete all the available FPM workers, leaving other visitors with an error page or a non-responding site.

**Please note:** if [Hypernode Managed Vhosts](hypernode-managed-vhosts.md) is enabled, only add the `http.ratelimit` file in the Nginx root. Don't add it to the specific vhost as well, as this may cause conflicts.

### Exclude IP Addresses from the per IP Rate Limiting

In some cases, it might be necessary to exclude specific IP addresses from the per IP rate limiting. If you wish to exclude an IP address, you can do so by creating a config file called `/data/web/nginx/http.ratelimit` with the following content:

```nginx
geo $limit_conn_per_ip {
    default $remote_addr;
    198.51.100.69 '';
}
```

In this example, we have excluded the IP address **198.51.100.69** by setting an empty value in the form of `''`.

In addition to excluding a single IP address, it is also possible to allow a whole range of IP addresses. You can do this by using the so-called CIDR notation (e.g., 198.51.100.0/24 to whitelist all IP addresses within the range 198.51.100.0 to 198.51.100.255). In that case, you can use the following snippet in `/data/web/nginx/http.ratelimit` instead:

```nginx
geo $limit_conn_per_ip {
    default $remote_addr;
    198.51.100.0/24 '';
}
```

### Disable per IP Rate Limiting

When your shop performance is very poor, it’s possible all your FPM workers are busy just serving regular traffic. Handling a request takes so much time that all workers are continuously depleted by a small number of visitors. We highly recommend optimizing your shop for speed and a temporary upgrade to a bigger plan if this situation arises. Disabling the rate limit will not fix this problem but only change the error message from a `Too many requests` error to a timeout error.

For debugging purposes, however, it could be helpful to disable the per-IP connection limit for all IP’s. With the following snippet in `/data/web/nginx/http.ratelimit` , it is possible to altogether disable IP based rate limiting:

```nginx
geo $limit_conn_per_ip {
    default '';
}
```

**Warning: Only use this setting for debugging purposed! Using this setting on production Hypernodes is highly discouraged, as your shop can be easily taken offline by a single IP using slow and/or flood attacks.**

### Exclude Specific URLs from the per IP Rate Limiting Mechanism

To exclude specific URLs from being rate-limited you can create a file `/data/web/nginx/server.ratelimit` with the following content:

```nginx
set $ratelimit_request_url "$remote_addr";
if ($request_uri ~ ^\/(.*)\/rest\/V1\/example-call\/(.*) ) {
    set $ratelimit_request_url '';
}

if ($request_uri ~ ^\/elasticsearch.php$ ) {
    set $ratelimit_request_url '';
}
```

In the example above, the URLs `*/rest/V1/example-call/*` and `/elasticsearch.php` are the ones that have to be excluded. You now have to use the `$ratelimit_request` variable as a default value in the file `/data/web/nginx/http.ratelimit` (see below) to exclude these URLs from the rate limiter and make sure that bots and crawlers will still be rate limited based on their User Agent.

```nginx
geo $limit_conn_per_ip {
    default $ratelimit_request_url;
}
```

You can also combine this with a regular allowlist, and exclude IP Addresses as described above.

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
