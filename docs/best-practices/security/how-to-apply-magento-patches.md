---
myst:
  html_meta:
    description: Learn how to apply Magento patches for optimal protection. Check
      your shop with MageReport and ensure your webshop is not vulnerable to malicious
      parties.
    title: How to apply Magento patches? | Security | Hypernode
redirect_from:
  - /en/best-practices/security/how-to-deploy-magento-patches/
---

<!-- source: https://support.hypernode.com/en/best-practices/security/how-to-deploy-magento-patches/ -->

# How to Apply Magento Patches

Every now and then Magento releases a patch that ensures that your webshop can perform optimally and is protected as much as possible. By ensuring that you always install the latest patches, you can not only take advantage of the latest features, but above all prevent your site from being vulnerable to malicious parties. It is therefore important to always install all patches from Magento on your webshop.

## Different Magento Patches

Every once in a while Magento issues a new patch for Magento Community and Magento Enterprise to increase the security of their software. These patches are basically security releases, and new Magento versions mostly contain all prior patches. Whenever a new patch comes out, make sure to download and install it as soon as possible. A complete overview of Magento patches can be found on [Magento.com](https://magento.com/security/patches).

## Check Your Shop With MageReport.com

Not sure whether your shop is vulnerable and needs to be patched? Check [MageReport](https://www.magereport.com/)!

**The SUPEE-10888, -10752 and -10570 checks result in ‘unknown’?**

MageReport is not able to check from ‘the outside’ whether these patches are installed. Checking your shop will likely result in ‘unknown’, unless we see your shop has been updated to a security version in which the patch has been incorporated. If this is the case, the check will be green.

## Seven Steps to Apply the Patch and Increase Your Magento Security

You need SSH (shell) access to download and apply the patch. You need only three commands, CD, WGET and BASH, to navigate, download and apply the patch.

### Step 1: Make a Backup

There’s a chance that certain plugins or elements in your webshop aren’t compatible with the Magento patch. That’s why we always recommend you to make a backup first, in case something goes wrong.

### Step 2: Log on to SSH (Shell)

Log on to the shell server. If you don’t how to log on, contact your hosting provider or technical contact. Hypernode customers can follow the steps in the article [How to Log in to the Hypernode With SSH](../../hypernode-platform/ssh/how-to-log-in-to-the-hypernode-with-ssh.md).

### Step 3: Download and Upload the Patch

To download the correct patch for your webshop you need to know what version of Magento you’re using. Don’t know what version you use? Find out using [this tutorial](https://www.euperia.com/development/how-to-find-the-magento-version/844).

Download the patch(es) you need via the [Magento downloads page](http://magento.com/security/patches). Upload the patch with SSH to your Magento folder.

### Step 4: Apply the Patch

Navigate to your Magento folder:

```nginx
cd example.nl
```

After this, the command BASH will apply the patch you just downloaded:

```nginx
 bash NAME_PATCH
```

Let’s assume here that the patch name is: `patch_supee-5994.sh` . Your actual command would look like this:

```nginx
 bash patch_supee-5994.sh
```

### Step 5: Clear Your Cache

It’s important to flush the Magento cache after applying the patch. Flushing your caches can be done in the back-end of your Magento shop under Cache management. More info about flushing your cache in the back-end of Magento can be found in the [Magentocommerce Knowledgebase](http://www.magentocommerce.com/knowledge-base/entry/cache-storage-management/%09200). Don’t forget to flush your OPcode or APC cache as well!

### Step 6: Check Your Shop

Don’t forget to check your shop for vulnerabilities after patching and flushing your caches. Magento’s [Security Patch Page](http://magento.com/security-patch) provides a list of signs to look out for to determine whether your site is comprised or not.

### Step 7: Clean up the Patch

After testing your shop, it’s highly advised to remove the patch file. This will help keep the webfolder nice and tidy (no unnecessary files)

```nginx
 rm NAME_PATCH
```

## FAQ

**I keep getting a Hunk failed error. What should I do?**

When you get the Hunk failed error it means you downloaded the patch for the wrong version. Please check what version of Magento you’re running and download the correct patch. If you still receive this error, please check the [Magento forum](http://community.magento.com/) for more information on these patches or discuss your problem on one of their boards.

**How long will downloading and applying the patch take?**

Downloading and applying the patch doesn’t take much time. We do however recommend that you check your shop thoroughly after applying the patch, which can take up quite some time.

**I’ve patched my shop, but I keep getting an notification in the back end of Magento**

Magento doesn’t check whether you’ve applied the patch or not, so that notification will always be visible, patched or not. If you already applied the patch, you can ignore the notification or indicate you’ve read the message.

**Can I check if a patch is installed?**

Yes you can. You can scan your site with [MageReport.com](http://www.magereport.com/) to see if a patch is installed or not. If a check comes up grey it’s possible the files that are needed for the check are relocated. Therefore it can’t see whether your shop is patched or not. No worries. Simply use SSH to check if your shop is patched.

Every check that’s been installed can easily be found in the content of your shop. More specifically it’s logged in `app/etc/applied.patches.list` . So you use the command ‘grep’ to access the list:

```nginx
  grep '|' app/etc/applied.patches.list
```

The output will look like this:

```nginx
-e 2015-04-14 08:34:22 UTC | SUPEE-5344 | EE_1.14.1.0 | v1 | a5c9abcb6a387aabd6b33ebcb79f6b7a97bbde77 | Thu Feb 5 19:14:49 2015 +0200 | v1.14.1.0..HEAD
```

In this example only SUPEE-5344 has been applied. When you uninstalled a patch, you’ll see this:

```nginx
 -e 2015-04-14 15:21:48 UTC | SUPEE-5344 | EE_1.14.1.0 | v1 | a5c9abcb6a387aabd6b33ebcb79f6b7a97bbde77 | Thu Feb 5 19:14:49 2015 +0200 | v1.14.1.0..HEAD | REVERTED
```

**Magereport keeps saying security patch 6482 isn’t installed**

We found out that there are several reasons why Patch 6788 comes out as uninstalled on [MageReport.com.](https://www.magereport.com/page/support), so we recommend you to check the following:

- When compilation is enabled in the backend of your Magento, SUPEE-6482 doesn’t work properly. Disable compilation (navigate to System > Tools > Compilation page and click on Disable button) to make sure the patch works. After disabling compilation, check your site with [MageReport.com.](https://www.magereport.com/page/support) again. If the check still comes out as not installed, try re-compiling.
- Check if the patch is installed in the correct directory;
- Reload your opcode cache, webserver, php-fpm process and possible other caches. The old code might be still be active;
- Check your shops’ .htaccess. If you’ve made any adjustements in your .htaccess, it’s possible the patch is only partially installed;
- Using a Magento version older than Magento 1.6.1.0? Update to a more recent version. When patching Magento versions older than Magento 1.6.1.0, certain redirects aren’t added.

We hope one of the causes mentioned above can fix your problem. If not, we recommend you to hire a Magento specialist. Unfortunately we can’t help fixing these problems. We’re a hosting company that specializes in Magento hosting. Magento development however is a completely different specialty. A list of Magento developers per country can be found on [MageReport.com.](https://www.magereport.com/page/support)
