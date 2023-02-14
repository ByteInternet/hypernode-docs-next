---
myst:
  html_meta:
    description: Our tool Magereport will tell you if there are any known security
      issues with your shop. This article explains how to recover a hacked Magento
      shop.
    title: How to recover a hacked Magento shop? | Security | Hypernode
redirect_from:
  - /en/best-practices/security/how-to-recover-a-hacked-magento-shop/
  - /knowledgebase/recover-a-hacked-magento-shop/
---

<!-- source: https://support.hypernode.com/en/best-practices/security/how-to-recover-a-hacked-magento-shop/ -->

# How to Recover a Hacked Magento Shop

Unfortunately webshops get hacked. Most of the times because of an outdated CMS version or buggy plugin(s) and/or extension(s). Regularly check your shop with [Magereport.com](https://www.magereport.com/) to make sure your Magento shop’s security is up-to-date. Magereport will tell you if there are any known security issues with your shop and if so, how to fix them. This article explains how to recover a hacked Magento shop.

## Is My Shop Hacked?

In many cases, Magereport.com would tell you if your shop has been hacked! Magereport checks for known backdoors and encrypted files that should not be encrypted. For example: `/skin/error.php` (not an official Magento core file) or `.README_FOR_DECRYPT.txt` (ransomware payment instructions) and so on.

You may also get alerted some other way, perhaps via a central agency such as the NCSC, or your local equivalent.

On Hypernode we also provide a [Malware scanner](../../best-practices/security/how-to-scan-your-hypernode-for-malware.md), based on [Yara](http://yara.readthedocs.io/) with an [extra set of signatures to detect magento directed malware](https://github.com/gwillem/magento-malware-scanner). Every night an audit on new or changed files will be performed and when the scanner hits a possible infected file, it will notify Hypernode's abuse department. We will check if it is a false-positive and if not; we'll send you a warning message by email.

## What to do When your Shop is Hacked

This is a good priority list to start cleaning up your shop:

### Collect Evidence

To find out what happened and how, it’s extremely important to collect evidence. We do this, among other things, by collecting the logs in /var/log and in the Magento content directory.

This needs to be done asap, as the intruder might eliminate traces if he finds out you are on to him. Make sure to make a copy of all the relevant logs (notably, system logging located in/var/log/syslog and /var/log/auth.log, Nginx access and errors logging located in /var/log/nginx/. Also make a copy of Magento’s log files (var/log/\*).

### Analyse Root Cause

It is 99% likely that the intruder got in through an old security flaw in Magento or its plugins, or by using either a weak, or leaked, user/password combination. Check if your shop is fully patched using Magereport.com.

If you are fully patched, the intruder likely got in through a flaw in one of your used plugins.
Try to find the method the hackers used to break into your Magento shop. Use this tutorial about breach analysis on Magento.

### Tips to Find and Fix the Issue

Fixing a site has no use if the intruder can just as easily get back in afterwards. Determine what you should change in order to prevent repeated abuse.

In most cases this will be:

- Remove unknown, unused, and old admin accounts.
- Change passwords for admin accounts to strong passwords (and activate 2-factor authentication using Authy or Google Authenticator) for stronger security.
- Install all the relevant patches, for both Magento and any plugins.
- Upgrade your Magento to the latest version.
- Configure brute force protection.
- Run a scan using the [Magento corediff scanner](../../hypernode-platform/tools/how-to-use-magento-corediff-on-hypernode.md). If any clearly suspicious files are found, move them to a non reachable directory (like `/data/web/hacked/`) for later analysis, remove them from your website, and restore a trusted copy of the affected files.

### Throw the Hacker Out

An intruder most likely has left one or more backdoors. These could be separate files (`/skin/error.php`) or mixed in with regular Magento code (`Mage.php` or `include/config.php`)

To avoid recurring hacking incidents, your code and database should be thoroughly clean. The only trustworthy way to accomplish this, is to remove everything and recover from a (known clean) backup or git checkout. Establish which files were changed and go back to the latest clean version. For example, do a `git diff origin/<old-release`>. Do not trust any git checkout on the server, as that could have been compromised as well.

If you do not have a backup or version control, success is not guaranteed. But you could try to find
suspicious and/or recently modified files. And you could compare with a new Magento installation to see if core files have been modified. You may also use [a historical back-up](../../hypernode-platform/backups/how-to-restore-your-hypernode-from-a-snapshot.md) to restore (parts) of your Hypernode to a trusted copy.

## Need help?

Magento is no easy open source CMS. Although we’re very skilled in hosting Magento shops, making them fast and keeping conversion high, we’re no Magento developers. Luckily, we know a lot of agencies that do know a lot about how Magento works. If you need help, we advise you to contact an expert in recovering hacked Magento shops, such as [Sansec](https://www.sansec.io/), or find [a local technical partner](https://www.magereport.com/page/support) to assist you.
