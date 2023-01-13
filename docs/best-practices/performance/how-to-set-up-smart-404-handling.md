---
myst:
  html_meta:
    description: Servers are configured so requests for non-existing files are routed
      through the Magento index. We explain how to reduce load by discarding expensive
      404s.
    title: How to set up smart 404 handling for Magento 2? | Hypernode
redirect_from:
  - /en/best-practices/performance/how-to-set-up-smart-404-handling/
---

<!-- source: https://support.hypernode.com/en/best-practices/performance/how-to-set-up-smart-404-handling/ -->

# How to Set Up Smart 404 Handling

*This article explains how to reduce load by discarding expensive 404s.*

Most Magento servers are configured so that requests for non-existing files are routed through the Magento index.php. This enables search engine friendly URLs, which most people want. However, it might pose a problem when there is loads of traffic for (old) URLs for which Magento does not have a configured page. For example, other sites embed a non existing picture on your site ==> every hit will load the whole Magento framework. Oops!

## Are You Affected?

Check the amount of 404s on your site that are processed by PHP. On Hypernode, you can run this command:

```nginx
 parse-nginx-log --yesterday --php --filter status=404 --fields duration,request,referer
```

This will give you a list of requests for non-existing objects and their referrers. Plus the time (in seconds) spent on handling these useless requests.

In the wild, we have seen 10-30% of capacity spent on these misconfigured 404s.

## How to Fix It

If you control the referring page, obviously you should fix the source. If you do not, you have two options: redirect the traffic to a more appropriate location, or discard it altogether. It is smart to redirect **pages** to your frontpage (or a deep link product page), since this is most likely a human clicking on an old link. On the other hand, you could simply discard requests for URLs which indicate **assets** such as images, CSS and JavaScript. They are embedded, and the container object (a foreign page) will not benefit from embedding HTML instead of an image.

So the trick is: have the server send a static 404 instead of starting Magento to produce a 404 page. The webserver Nginx can do this a whole lot faster than PHP! Order of magnitudes faster. Perhaps even 500 times faster. That’s a lot faster, right?

### Solution 1: Whitelist URLs

Use this, if you know the exact URLs that give 404s.

On Hypernode, create these configuration files:

```nginx

touch ~/nginx/force404.txt
cat > ~/nginx/http.force404 << \EOM
map $uri $force404 {
default 0;
include app/force404.txt;
}
EOM

```

And now the real magic: generate a list of all static 404 assets, based on yesterday’s traffic.

```nginx
 parse-nginx-log --php --yesterday --filter status=404 --fields request |\
    egrep '^(GET|POST)' | cut -f2 -d' ' | cut -d'?' -f1 | sort | uniq |\
    egrep -i '.(jpg|png|css|js)$' | while read uri; do echo "$uri 1;";
    done > ~/nginx/force404.txt
```

Have a look at this file. Are you happy? Then activate the static 404:

```nginx
 cat > ~/nginx/server.force404 << \EOM
if ($force404) {
    return 404;
}
EOM

```

### Solution 2: Discard 404s Under Specific Folder

If you do not know the specific URLs but want to disable PHP processing for a specific part of your URL namespace (say /mymedia), you can use this snippet:

```nginx

cat > ~/nginx/server.disable-php-processing-for-mymedia << \EOM
location ^~ /mymedia {
try_files $uri =404;
}
EOM

```

You should make sure there are indeed no .php files under this folder, otherwise the webserver will happily serve them as plaintext (along with your precious code).

## Verification

Monitor your access logs for the desired behaviour:

```nginx
 tail -f /var/log/nginx/access.log | parse-nginx-log --filter status=404 --fields request_time,handler,request
```

It should show you no PHP handler, and a near-zero request time. Celebrate another bunch of saved CPU cycles and a performance gain of your shop!
