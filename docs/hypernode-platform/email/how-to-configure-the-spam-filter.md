---
myst:
  html_meta:
    description: Spam is unsolicited email, usually with a commercial content. If
      you receive a lot of spam in your email box, we recommend you to configure a
      spam filter.
    title: How to configure your email spam filter? | Hypernode
redirect_from:
  - /en/best-practices/email/how-to-configure-the-spam-filter/
---

<!-- source: https://support.hypernode.com/en/best-practices/email/how-to-configure-the-spam-filter/ -->

# How to Configure the Spam Filter

**Please note that this only applies to Service Panel users who log in via service.byte.nl.**

Spam is unsolicited email, usually with a commercial content. If you receive a lot of spam in your email box, we recommend you to configure a spam filter.

## How Does the Spam Filter Work

The spam filter examines whether incoming email is spam, by running many hundreds of tests on the email that arrives in your email box on our server. The test results together provide a spam score. The higher this score, the more likely it is a genuine spam message. You can then choose to have the spam with the highest scores marked and / or blocked by our spam filter.

**Please note! When you create a new mailbox, the spam filters are turned on by default. Both *Blokkeer Spam* and *Markeer Spam* are set to High.**

### Marking as Spam

When you choose the option to mark spam, our spam filter will mark emails with a high spam score by adding the text SPAM in the subject line. With this addition you can easily have the spam delivered to your mail program in a separate folder by setting a filter rule.

### Blocking Spam

When you choose the block option, our spam filter will delete emails with a high spam score from the server before it reaches your mailbox. No bounce will be sent for these messages. Spammers use a fake sender address, so a bounce would end up with the wrong person. There is a small chance of a single false deletion of email when using this method.

The diagram below shows an approximation of what happens when you set up the spam filter. A false positive is an incorrectly rejected email.

|          |                  |                  |                     |
| -------- | ---------------- | ---------------- | ------------------- |
| **Mode** | **SA Threshold** | **Spam blocked** | **False Positives** |
| Disabled | 9999             | 0%               | 0                   |
| Low      | 12               | 70%              | 1 in 57.000         |
| Medium   | 8                | 80%              | 1 in 9.000          |
| High     | 5                | 98%              | 1 in 1.000          |

## Configuring the Spam Filter

If you use Hypernode's mail servers, you can set the spam filter yourself on the Service Panel using this step-by-step plan:

1. Log into the Service Panel.
1. Select the desired domain.
1. Go to the tab *Instellingen*\*.\*\*\*
1. Select *E-mail*.
1. Click the virus- and spam settings icon located next to each mailbox (you can have different settings for each mail box).
1. On the virus and spam filter settings page you can use the dropdown menu to configure the spam settings. We advice you to set the following:
   1. \*\*Marking spam: High.\*\*For example, most of the spam (about 98%) is marked in the subject line and you can have it set aside by your email program
   1. **Blocking spam: Low**. Only obvious spam is blocked and the chance that you will lose a legit email is negligible.

## Tests by Our Spam Filter

Our spam filter contains many hundreds of tests that are performed to determine if an incoming mail looks like spam. These tests are updated regularly (approximately every month) to thwart the latest spam techniques. See below for a summary of some of the most important tests:

- Servers that try to deliver mail to us are checked for a large number of characteristics. Does the server meet all internet standards? Is the server trying to sent messages using a false name?
- Several blacklists are checked. These lists contain servers which have been hacked or have already sent spam in the past 24 hours.
- The sender address of the incoming mail is checked. If this address does not exist, the mail will be rejected.
- The text of the mail is searched. If words such as Viagra and Get Rich Quick appear, there will be penalty points. If it contains URLs of well-known spam sites, there will be penalty points. Above a certain number of penalty points, the mail will be rejected.
- Via a statistical method (so-called Bayesian Spam Filtering) the mail gets a spam score. Above a certain score, the mail will be rejected.

These are only a few examples. Please see [this website](http://www.spamassassin.org/) for more information. We also use [this Sender Verification](http://www.postfix.org/). We also use this blacklist.

## Frequently Asked Questions

**Can I block specific email addresses or domains?**

No, that's not possible. This is called *blacklisting*and will have little to no effect due to constantly changing senders.

**Only one of my accounts is receiving a lot of spam.**

There are major differences per email address. There are email addresses that never receive spam and email addresses that receive more than 2000 spam messages every day. It depends on how often an email address appears on spam lists.

**What can I or you do to prevent spam messages?**

1. Hypernode constantly updates the spam filters. Still receiving spam? Please keep in mind we have probably already blocked 4 or 5 times the amount of spam messages. Set your spam filter to high.
1. Delete all catchall email addresses.

**My spam filter is set to high, but I'm still receiving spam messages.**

As you can see from the list above, about 2% of spam can slip through even if the spam filter is set to high. That translates to thousands of spam messages per day. You do not have to report a spam message to our support desk, we would not be able to process it and updating our spam filters is automatic.

**My mails is being scanned, but no messages are labelled with SPAM.**

If you use your own mail server, we will not label your messages with SPAM. We will only add an X-Spam-Level header.

**Will forward addresses also be filtered for spam?**

For forward addresses we will add a mail header:

```
X-Spam-Level: '''*'''**
```

Use the filters of your mail program to filter out this header.

**Can I disable the spam filter completely?**

You can disable the spam filter via the Service Panel. Your email will still be checked for Sender Address Verification and with a blacklist (only Spamhaus at the moment).
