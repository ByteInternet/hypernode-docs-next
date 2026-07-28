---
myst:
  html_meta:
    description: eComscan by Sansec is a malware and vulnerability scanner for webshops,
      preinstalled on every Hypernode. Learn how to run scans and set up monitoring.
    title: How to Set Up Sansec eComscan on Hypernode?
---

# How to Set Up Sansec eComscan on Hypernode

[eComscan](https://sansec.io/) is a malware and vulnerability scanner for eCommerce applications, built by [Sansec](https://sansec.io/), specialists in eCommerce security and digital forensics since 2010. It scans your webshop's files, database, processes and cronjobs for malware, backdoors and vulnerable software, and supports Magento, Shopware, WooCommerce and many other platforms.

eComscan comes preinstalled on every Hypernode, so you can start scanning right away. This article explains how to run your first scan and how to set up continuous monitoring with a cronjob.

## Running Your First Scan

eComscan is already available on your Hypernode and is kept up to date by the platform, so there is nothing to install. Log in to your Hypernode over SSH and point eComscan at your webshop's installation folder:

```bash
ecomscan /data/web/magento2
```

If your shop lives in a different folder, change the path accordingly. For example, use `/data/web/public` for Magento 1 or Shopware.

A scan takes anywhere from a few minutes to half an hour, depending on the size of your shop. eComscan reads your database credentials from your store's configuration files, so it scans your database for malware as well. The output looks like this:

```console
app@example-magweb-cmbl:~$ ecomscan /data/web/magento2
[ eCommerce Security Scanner v1.8.26 (https://sansec.io), build 2026-07-03 ]

   Downloading latest malware signatures...

>> Check: Searching for vulnerabilities and hidden malware in files ...
   Finished scanning 90049 files.

>> Check: Magento 2 - scanning database 'example_magento' for malware ...
   Finished scanning 162 rows in 9 tables.

>> Check: Magento 2 - scanning for vulnerable 3rd party modules ...
   Found 0 vulnerable modules.

...

>> Found: 1x vulnerability on example-magweb-cmbl.nodes.hypernode.io
```

## Adding a License Key

Without a license key, eComscan runs in trial mode: it tells you *whether* something was found, but not the details of every detection. To unlock full reporting, purchase a license key from [Sansec](https://sansec.io/pricing) and pass it along with the `--key` flag:

```bash
ecomscan --key=YOUR_KEY --report=security@example.com /data/web/magento2
```

The `--report` flag sends the full scan report to the given email address, so you have a record of every scan.

## Setting Up Continuous Monitoring

A single scan only tells you about today. To catch infections early, Sansec recommends running eComscan every hour in monitoring mode. In this mode eComscan only sends an email when it finds new suspicious changes since the previous scan.

Run `crontab -e` and add the following line:

```text
# Scan the shop for malware every hour and alert on new findings
10 * * * * flock -n ~/.ecomscan.lock -c 'ecomscan --key=YOUR_KEY --monitor=security@example.com /data/web/magento2'
```

After adding the cronjob, press **CTRL+X**, **Y** and then **ENTER** to save it into your crontab. The `flock` command prevents a new scan from starting while the previous one is still running. For more information about cronjobs on Hypernode, check out [our article about periodic tasks](how-to-use-periodic-tasks-cronjobs-on-hypernode.md).

Please note that monitoring mode requires a valid license key.

## Running a Deep Scan

If you suspect your shop has been compromised, you can run a deep scan. This scans all files instead of just code, and also shows detections with a lower confidence score:

```bash
ecomscan --key=YOUR_KEY --min-confidence=0 --deep /data/web/magento2
```

A deep scan is significantly slower and produces more false positives, so use it for incident response only. Do not add a deep scan to your crontab.

## What to Do When Malware Is Found

If eComscan finds malware in your shop, follow our guide on [how to recover a hacked Magento shop](../../best-practices/security/how-to-recover-a-hacked-magento-shop.md). You can also use [Magento Corediff](how-to-use-magento-corediff-on-hypernode.md), another tool by Sansec, to find unauthorized modifications in your Magento core files.

If you need professional help cleaning up your shop, Sansec also offers incident response services.
