---
myst:
  html_meta:
    description: A lot of spam and abuse comes from specific countries. If you don’t
      do business there, you could block these countries. This article explains how
      to.
    title: How to block your webshop for specific countries? | Hypernode
redirect_from:
  - /en/hypernode/nginx/how-to-block-your-webshop-for-specific-countries/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-block-your-webshop-for-specific-countries/ -->

# How to Block Your Webshop for Specific Countries

A lot of spam and abuse comes from specific countries. If you don't do business there, you could block these countries altogether. This article explains how to block them. First some considerations:

- Country detection is 99,8% accurate (according to MaxMind, the supplier of the geo database).
- It is generally better to servce a static page, than to enforce a hard block. Static pages consume almost no resources and can be used to explain alternative ways to contact your organisation.

If you want to block, say, Russia and China, create the files `http.countries_map` and `server.countries_block` in the `/nginx` folder on your Hypernode. In these files you can use the following configuration:

In `http.countries_map`:

```nginx
map $geoip_country_code $block_country {
    default no;
    CN yes;
    RU yes;
}
```

In `server.countries_block`:

```nginx
if ($block_country = yes) {
    return 403;
}
```

Alternatively you can rewrite the request inside `http.countries_map` and upload a static `access_denied_for_country.html` page.

```nginx
if ($block_country = yes) {
    rewrite ^ /access_denied_for_country.html break;
}
```

## Using The hypernode-systemctl command-line Tool

We have implemented a `block_attack` functionality in the hypernode-systemctl CLI tool as well. To list the possible values you can run this on your Hypernode:

```nginx
app@pup1l6-vdloo-magweb-cmbl:~$ hypernode-systemctl block_attack --help
usage: hypernode-systemctl block_attack BlockChinaBruteForce

The possible values are:

BlockUkraineBruteForce      Attempts to deploy NGINX rules to block all IPs originating from Ukraine if not already configured. Also see https://changelog.hypernode.com/knowledgebase/block-your-site-for-specific-countries/
BlockRussiaBruteForce       Attempts to deploy NGINX rules to block all IPs originating from Russia if not already configured. Also see https://changelog.hypernode.com/knowledgebase/block-your-site-for-specific-countries/
BlockAhrefsBot              Attempts to deploy NGINX rules to block the AhrefsBot Web Crawler if not already configured. See https://changelog.hypernode.com/knowledgebase/fixing-bad-performance-caused-by-search-engines/
BlockSemrushBot             Attempts to deploy NGINX rules to block the SEMrush Web Crawler if not already configured. See https://changelog.hypernode.com/knowledgebase/fixing-bad-performance-caused-by-search-engines/
BlockPhilippinesBruteForce  Attempts to deploy NGINX rules to block all IPs originating from the Philippines if not already configured. Also see https://changelog.hypernode.com/knowledgebase/block-your-site-for-specific-countries/
BlockPageSpeedBruteForce    Attempts to deploy NGINX rules to block known brute-force probes against URLs related to PageSpeed if not already configured
BlockGrapeshotBot           Attempts to deploy NGINX rules to block the Grapeshot Web Crawler if not already configured. See https://changelog.hypernode.com/knowledgebase/fixing-bad-performance-caused-by-search-engines/
BlockMJ12Bot                Attempts to deploy NGINX rules to block the MJ12Bot Web Crawler if not already configured. See https://changelog.hypernode.com/knowledgebase/fixing-bad-performance-caused-by-search-engines/
BlockDotBot                 Attempts to deploy NGINX rules to block the DotBot Web Crawler if not already configured. See https://changelog.hypernode.com/knowledgebase/fixing-bad-performance-caused-by-search-engines/
BlockChinaBruteForce        Attempts to deploy NGINX rules to block all IPs originating from China if not already configured. Also see https://changelog.hypernode.com/knowledgebase/block-your-site-for-specific-countries/
BlockDownloaderBruteForce   Attempts to deploy NGINX rules to block the Magento 1 /downloader endpoint. See https://changelog.hypernode.com/knowledgebase/how-to-protect-your-magento-store-against-brute-force/#2_Secure_downloader_and_rss
BlockRSSBruteForce          Attempts to deploy NGINX rules to block known attacks against the RSS endpoint in Magento 1 if not already configured. See https://changelog.hypernode.com/changelog/release-5946-configurable-memory-management-policy-and-rss-bruteforce-detection/
BlockHongkongBruteForce     Attempts to deploy NGINX rules to block all IPs originating from Hong Kong if not already configured. Also see https://changelog.hypernode.com/knowledgebase/block-your-site-for-specific-countries/
BlockRogerBot               Attempts to deploy NGINX rules to block the Rogerbot Web Crawler if not already configured. See https://changelog.hypernode.com/knowledgebase/fixing-bad-performance-caused-by-search-engines/

positional arguments:
  {BlockUkraineBruteForce,BlockRussiaBruteForce,BlockAhrefsBot,BlockSemrushBot,BlockPhilippinesBruteForce,BlockPageSpeedBruteForce,BlockGrapeshotBot,BlockMJ12Bot,BlockDotBot,BlockChinaBruteForce,BlockDownloaderBruteForce,BlockRSSBruteForce,BlockHongkongBruteForce,BlockRogerBot}

optional arguments:
  -h, --help            show this help message and exit
```

If for example you would then want to block all requests from China because you noticed some suspicious traffic from `CN` IPs in `hypernode-fpm-status`, then you can run:

```nginx
app@pup1l6-vdloo-magweb-cmbl:~$ hypernode-systemctl block_attack BlockChinaBruteForce
Block attack job posted, see hypernode-log (or livelog) for job progress
```

After `hypernode-log` or `livelog` reports the newly posted `block_attack` job as finished the new rule should be deployed.

```nginx
app@pup1l6-vdloo-magweb-cmbl:~$ hypernode-log  | grep block_attack | tail -n 1
block_attack                    2019-01-10T15:34:29Z    2019-01-10T15:34:31Z    success     4/4     finished
```

The newly deployed Nginx rule will then be in the `/data/web/nginx` directory:

```nginx
app@pup1l6-vdloo-magweb-cmbl:~$ cat nginx/server.block_cn
#Placed by Hypernode automation on 2019-01-11 12:18
if ($geoip_country_code = CN) { return 403; }
```
