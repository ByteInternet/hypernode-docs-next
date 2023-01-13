---
myst:
  html_meta:
    description: A misconfigured webserver can leak Magento cache files containing
      database passwords. This article explains how to prevent this form happening.
    title: How to secure a Magento cacheleak? | Security | Hypernode
redirect_from:
  - /en/best-practices/security/how-to-secure-magento-cacheleak/
---

<!-- source: https://support.hypernode.com/en/best-practices/security/how-to-secure-magento-cacheleak/ -->

# How to Secure Magento Cacheleak

A misconfigured webserver can leak Magento cache files containing database passwords. This is possible, because internal cache files are stored in the public document space of Magento. Default protection is included in the Magento installation, but this is not always activated, especially with modern webservers such as Nginx.

## What Magento Cacheleak?

The vulnerability is a compound of three problems:

**Predicting filenames**

Magento stores its internal data, such as database passwords, in cache files on disk. These file names are seemingly random. Most webservers do not expose file names by default, but the problem is that they can be predicted. The file names consist of [Adler-32](https://en.wikipedia.org/wiki/Adler-32) and [MD5](https://en.wikipedia.org/wiki/MD5); hashes derived from the installation path. Once you know the path, you know the cache file locations.

**Finding out the secret install path**

The secret installation path can be retrieved from various sources, such as `get.php`, `resource_config.json`, the `system.log` or `exception.log`.

**Apache vs. Nginx**

Magento has built-in protection of internal data (`/var`) when the Apache webserver is used (using `.htaccess` files). However, big sites are switching to modern webservers such as Nginx (23% runs Nginx as of August). Default protection doesn’t hold and manual intervention is required by the administrator.

## What Are the Consequences?

When the above conditions are met, a malicious person can anonymously fetch the internal Magento cache and thus obtain secrets such as the database password. This password gives access to customer and payment data.

## How Do I Fix It?

Hypernode customers who run their Magento shop on the Hypernode platform are already protected against this and many other security risks.

If you are hosting elsewhere, it all depends on your webserver.

### Apache

If you are using Apache and MageReport says you are susceptible to Cacheleak, it means that your `.htaccess` files are not activated. Verify that there is at least a `.htaccess` file under `/var`. If there is one, check with your server administrator whether `.htaccess` controls are enabled.

### Nginx

Many people are switching over to Nginx. At the very least, you should make sure your server definition contains a line like this:

```nginx
location ^~ /var/ { return 403; }
```

However, because Nginx [location rules](http://nginx.org/en/docs/http/ngx_http_core_module.html#location) are matched in a non-trivial way, you should verify that there are no other rules that take precedence. For reference, here is (a subset of) the battle tested config that our customers on the Hypernode platform enjoy.

```
# This is an annotated subset of the Nginx configuration from our Magento production platform @ www.hypernode.com
# See https://www.byte.nl/blog/magento-cacheleak-issue

# !!!! If you are a Hypernode customer, do not use this config as it will result in duplicate statements. !!!!!

user app;
worker_processes 4;
pid /var/run/nginx.pid;

events {
    worker_connections 768;
}

http {
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    server_tokens off;
    server_names_hash_bucket_size 64;

    # allows big media uploads
    client_max_body_size 120m;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # GeoIP support is included in the Ubuntu 12.04 Nginx.
    # This enables logging, and the following:
    #    if ($geoip_country_code ~ (CN|ZW) ) {
    #      return 403;
    #    }
    geoip_country         /usr/share/GeoIP/GeoIP.dat;
    gzip on;
    gzip_disable "msie6";

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    gzip_min_length  1000;
    gzip_proxied any;
    gzip_types       text/plain text/html application/json application/xml text/css text/js application/x-javascript;

    # Determine whether a request comes from a human, a search crawler or another bot.
    map $http_user_agent $is_non_search_bot {
        default '';
        ~*(google|bing|pingdom|monitis.com|Zend_Http_Client) '';
        ~*(http|crawler|spider|bot|search|ForusP|Wget/|Python-urllib|PHPCrawl|bGenius) 'bot';
    }

    # Rate limit bots (that are not search spiders) to one PHP request per second.
    # An empty '$limit_bots' would disable rate limiting for this requests
    limit_req_zone $is_non_search_bot zone=bots:1m rate=1r/s;
    limit_req_log_level error;

    index index.html index.php;

    server {
        listen 80 default_server;
        root /var/www;

        # Android dupe request bug, https://www.byte.nl/blog/android-bug-can-kill-site-duplicate-requests
        set $request_url "$scheme://$http_host$request_uri";
        if ($request_url = $http_referer) {
           set $request_is_referer 1;
        }
        if ($http_user_agent ~ 'Android ([23]|4\.[0123])') {
            set $android_buggy_ua 1;
        }
        set $android_dupe_bug "${request_method}${android_buggy_ua}${request_is_referer}";
        if ($android_dupe_bug = 'GET11') {
            # http://en.wikipedia.org/wiki/List_of_HTTP_status_codes
            return 429;
        }

        # Denied locations require a "^~" to prevent regexes (such as the PHP handler below) from matching
        # http://nginx.org/en/docs/http/ngx_http_core_module.html#location
        location ^~ /app/                       { return 403; }
        location ^~ /includes/                  { return 403; }
        location ^~ /media/downloadable/        { return 403; }
        location ^~ /pkginfo/                   { return 403; }
        location ^~ /report/config.xml          { return 403; }
        location ^~ /var/                       { return 403; }
        location ^~ /lib/                       { return 403; }
        location ^~ /dev/                       { return 403; }
        location ^~ /RELEASE_NOTES.txt          { return 403; }
        location ^~ /downloader/pearlib         { return 403; }
        location ^~ /downloader/template        { return 403; }
        location ^~ /downloader/Maged           { return 403; }
        location ~* ^/errors/.+\.xml            { return 403; }

        # CVE-2015-3428 / AW_Blog vulnerability
        # Note the .+ at the start: We want to allow url's like
        # order=create_date, which would otherwise match.
        if ($arg_order ~* .+(select|create|insert|update|drop|delete|concat|alter|load)) {
           return 403;
        }

        # Don't skip .thumbs, this is a default directory where Magento places thumbnails
        # Nginx cannot "not" match something, instead the target is matched with an empty block
        # http://stackoverflow.com/a/16304073
        location ~ /\.thumbs {
        }

        # Skip .git, .htpasswd etc
        location ~ /\. {
            return 404;
        }

        set $fastcgi_root $document_root;

        location / {
            try_files $uri $uri/ @handler;
            expires 30d;
        }

        # SUPEE 6285
        # Only allow the new url case sensitive lowercase, deny case insensitive
        location ^~ /rss/order/new {
            echo_exec @handler;
        }
        location ^~ /rss/catalog/notifystock {
            echo_exec @handler;
        }
        location ^~ /rss/catalog/review {
            echo_exec @handler;
        }
        location ~* /rss/order/new {
            return 403;
        }
        location ~* /rss/catalog/notifystock {
            return 403;
        }
        location ~* /rss/catalog/review {
            return 403;
        }

        ## Order IS important! this is required BEFORE the PHP regex
        ## Allow PHP scripts in skin and JS, but render static 404 pages when skin or js file is missing
        ## Magento has RewriteCond %{REQUEST_URI} !^/(media|skin|js)/ in default htaccess
        location ~ ^/(skin|js)/ {
            location ~ \.php$ {
                echo_exec @phpfpm;
            }
            try_files $uri $uri/ =404;
            expires 30d;
        }
        # Disallow PHP scripts in /media/
        # Also render static 404 pages for missing media
        location ~ ^/media/ {
            location ~ \.php$ {
                return 403;
            }
            try_files $uri $uri/ =404;
            expires 30d;
        }

        location @handler {
            rewrite / /index.php;
        }

        location @fastcgi_backend {

            # Bot rate limit, https://gist.github.com/supairish/2951524
            # Burst=0 (default) --WdG
            limit_req zone=bots;

            # server_name is read-only, so we need a temp var
            set $my_server_name $server_name;
            if ($my_server_name = "") {
                set $my_server_name $http_host;
            }

            try_files $uri =404;
            expires off;
            root $fastcgi_root;
            fastcgi_read_timeout 900s;
            fastcgi_index index.php;
            fastcgi_pass $fastcgi_pass;

            include /etc/nginx/fastcgi_params;

            fastcgi_param HTTP_AUTHORIZATION $http_authorization;
            fastcgi_param SERVER_NAME $my_server_name;

            fastcgi_param NGINX_REQUEST_TIME $date_gmt;

            # If these variables are unset, set them to an empty value here
            # so they are al least defined when fastcgi_param directives are called
            if ($storecode = "") {
                set $storecode "";
            }

            if ($storetype = "") {
                set $storetype "";
            }

            # These are set in http.magerunmaps
            fastcgi_param MAGE_RUN_CODE $storecode if_not_empty;
            fastcgi_param MAGE_RUN_TYPE $storetype if_not_empty;

        }

        location @phpfpm {
            set $log_handler phpfpm;
            set $fastcgi_pass 127.0.0.1:9000;
            echo_exec @fastcgi_backend;
        }

        location @hhvm {
            set $log_handler hhvm;
            set $fastcgi_pass 127.0.0.1:9001;
            echo_exec @fastcgi_backend;
        }

        # Protection against unsecured magmi installs. User-editable
        # so user may set it up as they want. Must be included here
        # to catch and redirect PHP files, if this was loaded in later
        # (after the default php-fpm handler for .php files) then we
        # would not be able to redirect the magmi .php files (which are
        # the ones we really MUST redirect).
        location ~* /magmi($|/) {
            return https://support.hypernode.com/knowledgebase/securing-access-to-magmi/;
        }

        location ~ .php/ {
            rewrite ^(.*.php)/ $1 last;
        }

        # always execute our own handler for php-fpm, to prevent serving raw php code and to have
        # a default when user removes configuration from ~/nginx/
        location ~ \.php$ {
            echo_exec @phpfpm;
        }

        rewrite ^/minify/([0-9]+)(/.*.(js|css))$ /lib/minify/m.php?f=$2&d=$1 last;
        rewrite ^/skin/m/([0-9]+)(/.*.(js|css))$ /lib/minify/m.php?f=$2&d=$1 last;
        location /lib/minify/                   { allow all; }

    }

}
```

## Need Help?

Magento is no easy open source CMS. Although we’re very skilled in hosting Magento shops, making them fast and keeping conversion high, we’re no Magento developers. Luckily, we know a lot of agencies that do know a lot about how Magento works. If you need help, don’t hesitate to [contact one of these agencies](https://www.magereport.com/page/support).
