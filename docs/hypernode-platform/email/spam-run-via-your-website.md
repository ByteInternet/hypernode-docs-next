---
myst:
  html_meta:
    description: 'All plans have the option to send emails from the website. Abusers
      use this to advertise products, we call this a spam run. Read tje most common
      reasons here. '
    title: Policy for sending emails on Hypernode
redirect_from:
  - /en/hypernode/email/spam-run-via-your-website/
---

<!-- source: https://support.hypernode.com/en/hypernode/email/spam-run-via-your-website/ -->

# Spam Run via Your Website

All plans have the option to send emails from the website. Abusers are only too happy to use this to advertise products that you as a person or company do not want to be associated with. We call this a spam run. In most cases this is done in a way that does not comply with our email policy.

We also detect a spam run in the queue in the outgoing mail server. As soon as the outgoing spam filter sees more than a maximum number of sent messages set by us, which are marked as spam and therefore contain a high spam score, a website will be automatically disabled. We do this to prevent disruptions, to give our techies a good night's rest and to ensure that our mail servers do not end up on blacklists. If the website is turned off, we will send the spam messages that are still waiting in the queue back to the sender's address (the bounce address). In these bounces, we refer to this article to explain what's going on.

It is often difficult for us to say what the exact cause of this was. Therefore, some research is necessary. Below are the most common reasons for spam runs.

## A Refer-A-Friend Module or Guestbook Is Being Abused

Some sites have modules installed with which a page can be recommended to another person using email. When no or insufficiently secured captcha is used, there is a risk that these forms will be misused with the help of scripts to send spam. If you have such a form on the site, we recommend that you take a good look at the security (and possibly the usefulness).

If you have a guestbook or other page on your website where people can leave a message anonymously, you run the risk of it being misused by so-called spam bots. These send automated messages hoping to attract more visitors to their pages. This often involves advertising for erection pills and other dubious products. Sometimes a lot of gibberish is posted with a link to the spammer's website.

There are two solutions:

- Protecting the form with a password
- Using a [Captcha](http://nl.wikipedia.org/wiki/Captcha)

## The Site Has Been Hacked

When a site is hacked in such a way that someone was able to add their own code, there is a chance that it was used to upload a mail script. The best way to check if this is the case is to compare the code as it is on the site at the time of shutdown with its own backup. If you do not have your own backup, we recommend that you attach the oldest snapshot to your Hypernode and compare the code in it with the current situation.
