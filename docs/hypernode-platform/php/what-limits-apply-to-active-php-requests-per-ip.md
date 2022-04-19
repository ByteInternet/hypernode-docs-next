<!-- source: https://support.hypernode.com/en/support/solutions/articles/48000967652-what-limits-apply-to-active-php-requests-per-ip/ -->
# What Limits Apply To Active PHP Requests Per IP

Hypernodes uses Nginx and PHP-FPM for processing and serving PHP pages. PHP-FPM uses FPM worker threads to process requests from Nginx. The amount of workers that are available on the Hypernode depends on how many available CPU cores the server has. Benchmark tests have concluded that, based on CPU contention and concurrency, the optimal number of workers is defined by the formula `vCPUs * 5`.

When one IP uses up most or all of the available workers, this causes a processing queue and long loading times for PHP generated pages, possibly resulting in error codes being served to visitors. To prevent this from happening, we limit the amount of workers one IP can use. This limit is set at **30 workers per IP**.

### 30 workers per IP

Previously we configured a limit of `vCPUs * 5 - 2`. For our largest Hypernode plans, this could theoretically mean one IP using up to 99% of the available workers. This is undesired behaviour, but it can happen when a lot of people are accessing the admin pages from one office IP. This is why we have chosen to set the limit at 30 workers per IP.

Users that overstep this limit will be served a [429 too many requests status code](https://support.hypernode.com/knowledgebase/resolving-429-many-requests/). You can always circumvent this per IP rate-limiting by [whitelisting IP's in the NGINX config](https://support.hypernode.com/knowledgebase/resolving-429-many-requests/#Exclude_known_IP8217s_from_the_per_IP_rate_limiting_mechanism).
