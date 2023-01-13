---
myst:
  html_meta:
    description: Get a clear overview of pagespeed, transactions, error rates, slow
      queries and more. Easily customizable, and set alerts for performance thresholds.
    title: How to find performance bottlenecks with New Relic?
redirect_from:
  - /en/best-practices/performance/how-to-find-your-performance-bottleneck-with-new-relic/
  - /knowledgebase/new-relic-performance-management/
---

<!-- source: https://support.hypernode.com/en/best-practices/performance/how-to-find-your-performance-bottleneck-with-new-relic/ -->

# How to Find Your Performance Bottleneck with New Relic

[New Relic](https://newrelic.com/) is a profiling tool that will explain what is happening "behind the scenes". You can use it to determine the performance bottleneck of your shop.

## Why Use New Relic?

New Relic gives you real-time and historical information about the performance of your shop. Some important features:

- Easy to use; one click install.
- Gives you a clear overview of possible bottlenecks: pagespeed, transactions, error rates, slow queries and many more.
- You can add alerts for when the performance or error rate reaches a specific threshold.
- You can customize and filter the output so it only gives you information you need.
- Use it to measure performance before and after you make adjustments, so you will have scientific data on which scenario performs better!

## New Relic Is A Third Party Tool

New Relic is a third party tool and therefore, we cannot offer any in-depth support on [how New Relic works](https://docs.newrelic.com/docs/using-new-relic/). Of course you can always share your findings with us and we can see whether we can sort out any issues together.

Before you can activate New Relic at Hypernode you need to [create an account](https://newrelic.com/signup) at New Relic. You get a Free (Forever) plan or a Standard plan with add-ons. If you require more advanced profiling, such as application trace details, you can upgrade your account at New Relic to a paid Pro or Enterprise plan.

## How to Activate New Relic

### Activation Via the CLI

SSH to your Hypernode and use these commands to enable New Relic:

```nginx
Enable New Relic: ~$ hypernode-systemctl settings new_relic_enabled --value 'True'
Enter New Relic licence key: ~$ hypernode-systemctl settings new_relic_secret --value 'licence key'
Enter New Relic 'app name'~$ hypernode-systemctl settings new_relic_app_name --value 'app name'
```

### Activation Via the Service Panel

First create a New Relic account via the Byte Service Panel. Then activate New Relic at Hypernode. Follow the next steps:

1. Log in on the [Service Panel](https://service.byte.nl/protected/)
1. Select your Hypernode.
1. Click on the *Instellingen* tab.
1. Click on the *New Relic* option.
1. Click on the link, you will be forwarded to New Relic
1. Create an account, you will set an app name and receive a license key.
1. Enter the license key and the app name set at New Relic in your Service Panel to activate New Relic
1. Login to the New Relic dashboard to see statistics

**Please take into account that it takes a most 10 minutes for our system to actually create the account. Grab a cup of coffee and relax!**

### Activation Via the Control Panel

1. Log in on the [Control Panel](https://auth.hypernode.com)
1. Select your Hypernode (name.hypernode.io) under *My Hypernodes* and click on the Details button
1. Hover over the *Hypernodes* button and go to *Monitoring* in the side menu
1. Click on the *New Relic* option.
1. Click on the *New Relic* link, you will be forwarded to New Relic.
1. Create an account, you will set an app name and receive a license key.
1. Enter the license key and the app name set at New Relic in your Control Panel and select *Enable New Relic* to activate New Relic. Click on *save.*
1. Login to the New Relic dashboard to see statistics

**Please take into account that it takes a most 10 minutes for our system to actually create the account. Grab a cup of coffee and relax!**

## Troubleshooting

### I’m Getting The `New Relic integration requires the New Relic-PHP 5 agent` While My PHP Version Is Set to PHP 7

This error appears when the native Magento New Relic extension is installed in your webshop while the New Relic extension is disabled. To solve this, **enable** New Relic.

### Turn Off New Relic Transaction Tracer

In some very rare cases, when you have enabled a huge amount of extensions, or use code with an extraordinary amount of recursion, the detailed tracing might add some overhead to your sites performance. In that case, you should disable trace details by putting these lines in `/data/web/public/.user.ini`:

```nginx
[newrelic]
newrelic.transaction_tracer.detail = 0
```

### Fatal error: Aborting! The New Relic imposed maximum PHP function nesting level of ‘5000’ has been reached

This error is created by the New Relic PHP extension and is caused by an infinite recursive loop within Magento. The New Relic PHP extension detects this loop and exits the PHP process before PHP runs out of cstack frames and crashes with a segfault.

We already changed the maximum nesting level for this extension from 500 to 5000, which should be more then enough for Magento, so if you run into this error, check your New Relic traces to find the recursive loop.

As a quickfix it is possible temporary change the value from 5000 to something bigger. This will not fix the issue as the cause is still there, but it will remove the error message. To do this create a `.user.ini` file in `/data/web/public` with the following setting:

```nginx
[newrelic]
newrelic.special.max_nesting_level=10000
```

And restart PHP-FPM with the following command (where X.X is the version of PHP you are using) for the changes to take effect immediately

```bash
hypernode-servicectl restart phpX.X-fpm
```

### Disable All Apdex Notifications for New Relic

To disable all `apdex` notification mails:

- Select `APM` and scroll all the way down to the bottom to the section `ALERTS`.
- Select `ALERTS` > `Application Policies`
- Click `Default application alert policy`
- Now set both the red and the orange apdex warning to `Disable`.
- Unselect the “Alert when any ping URL is unresponsive for 1 minutes”
