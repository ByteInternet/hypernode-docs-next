---
myst:
  html_meta:
    description: Because Hypernode is hosted in the Cloud, the system timezone is
      set to UTC. Magento 2 should operate on the same timezone as the server. Learn
      how!
    title: How to set Magento 2 to the UTC timezone? | Hypernode
redirect_from:
  - /en/ecommerce/magento-2/how-to-set-magento-2-x-to-the-utc-timezone/
  - /knowledgebase/magento-utc-hypernode/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-set-magento-2-x-to-the-utc-timezone/ -->

# How to Set Magento 2.x to the UTC Timezone

As you probably know, the world is divided in a bunch of time zones. Because Hypernode is hosted in the cloud, the system timezone is set to UTC. This is because we cannot always know in what timezone the server will be hosted, but we want to deliver a consistent system timezone for our customers.

You will probably want to work in a different timezone OR show a different timezone to your customers. So this is an issue not only when dealing with a Hypernode, but also when operating an intercontinental shop.

In short:

1. You should set the global timezone for Magento to the UTC-equivalent GMT Standard Time.
1. Then, set the timezone for all websites to your local timezone.
1. If you are in The Netherlands, choose “Europe/Berlin” if “Europe/Amsterdam” is not in the list.

## Why Do I Need to Change the Timezone?

Unfortunately Magento has some internals that lose the sense of time zones by converting to and from an ancient time format called the Unix Time. This time format does not have a sense of time zones.

This problem crops up when calculating stuff involving dates and shows up as weird problems like:

- Catalog price rules will disappear after a few hours.
- Magento cronjobs email you with the error “Too late for schedule”.

All of this is because MySQL and Magento do not agree on the timezone to use and also do not communicate correctly. To solve this problem, Magento should operate on the same timezone as the server. Then, to display all dates and times on your websites and stores as you like them, set the timezone for all websites to your preferred timezone.

## Set the Correct Timezone for Magento 2.x

### Set the Global Timezone to GMT or UTC

If Magento does not support the UTC timezone, then select its equivalent GMT Standard Time.

1. Go to `Stores` -> `Configuration`
1. Make sure the `Store View` is set to: `Default Config`
1. Go to `General` -> `General`
1. Scroll down to `Locale Options`
1. Select `GMT (UTC)` next to `Timezone`

### Set the Default Website Scopes to Your Preferred Timezones

Next are your storeviews. These will ensure that your websites displays Dutch, Chinese or American order and shipping times, or some other time according to your settings.

1. Go to `Stores` -> `Configuration`
1. Select the website for which you wish to change the time zone under `Store View` (Don’t select the storeview itself)
1. Go to `General` -> `General`
1. Scroll down to `Locale Options`
1. Select the timezone where the shops is located next to `Time zone`. *For example: `Central European Standard Time (Europe/Amsterdam)` for a Dutch shop*
