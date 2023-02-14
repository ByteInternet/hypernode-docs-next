---
myst:
  html_meta:
    description: Our mail platform handles rate limiting and enforces a strict limit
      on your outgoing email flow. If you exceed the limits, your email will be delivered
      at a later time.
    title: Policy for sending emails on Hypernodes
redirect_from:
  - /en/hypernode/email/policy-for-sending-email-on-hypernode/
  - /knowledgebase/hypernode-email-policy/
---

<!-- source: https://support.hypernode.com/en/hypernode/email/policy-for-sending-email-on-hypernode/ -->

# Policy for sending email on Hypernode

All emails send from a Hypernode using the local PHP mail() functionality or sent to port 25 on the local host, is routed through our central outgoing email platform that filters spam emails and emails from infected websites. This mail platform handles rate limiting and enforces a strict limit on your outgoing email flow. If you exceed the limits, your email will be delayed and delivered at a later time.

## Introduction

Sending too much mail in a short amount of time could cause jams and mail delayed deliverance when sending to large email providers like Gmail and Microsoft.

When someone sends a large mailing to e.g. 5000 receipts at once, the email flow for other Hypernodes can delay for hours or even cause bounces or blacklisting problems.

To guarantee a fast and healthy email flow for all Hypernodes, we enforce a strict emails per minute policy and block mail that is tagged as spam or contain malafide attachments. This is necessary to ensure that your emails are delivered in a reasonable amount of time and will not be marked as spam or deleted by receiving mailservers.

Our mailservers make sure only a limited amount of emails can be send per hour from a single Hypernode. If you send too much mail in a short time, mail coming from your Hypernode will be rate limited.

This means effectively that all email coming from your Hypernode will be stored and delivered at a later time.

## Mail Policies

### Confirmed Receiver and Opt-In

Sending commercial or charity emails to companies and individuals that did not explicitly agreed to receiving emails is [prohibited by Dutch law](https://www.acm.nl/nl/onderwerpen/telecommunicatie/internet/spam/).

Use only email addresses of receivers that subscribed to your newsletter or ordered products and gave explicit permission ([confirmed opt-in](https://en.wikipedia.org/wiki/Closed-loop_authentication)) to receive emails.

This applies to new and existing customers. Do not use email lists that you bought or downloaded from third parties without the consent of the receiving party.

### Simple and Accessible Subscription Cancelling

Provide a visible and easy accessible unsubscribe link in each mailing. Recipients must **always** be able to unsubscribe from your mailings, even though they have given consent earlier.

Make sure unsubscribing is possible with one or two clicks, without the need to sign in or re-typing the email address. The chance that your email will be marked as spam will be much smaller.

Having an unsubscribe link in your emails will lower the spam count on the receiving mailservers, making it more likely to be accepted.

### Time Limits

Use a rate limit on your mailings. Do not send 10.000 emails at once, but use a mechanism that sends small chunks of only a few emails every few minutes.

When sending emails through or mail platform, the following restrictions apply:

- Send a maximum of 1 email **per second**
- Limit your emails **per 10 minutes** to a maximum of **200 emails**
- Limit your emails **per hour** to a maximum of **1000 emails**
- Limit your emails **per day** to a maximum of **5000 emails**
- Limit your emails **per destination domain** to a maximum of **60 emails per minute**

The limits might look odd, because in case you send 200 emails per 10 minutes, wouldn’t that mean that you send 1200 emails per hour? Unfortunately it does not exactly work that way. They are hard limits of the maximum amount of emails you can send per second/10 minutes/hour/day/domain, without the risk of being rate limited.

When the rate limiter is active, emails will be stored on the mailserver to be delivered at a later time.

Examples:

- If you want to send 900 emails, you can safely send them in batches of 200 per 10 minutes.
- If you want to send 1200 emails, you can send 1000 spread over the first hour, and then you have 200 left to send the next hour.

## Sending Mail Through Third Parties

If you are sending larger mailings containing 5000 emails and up per day you are recommended to use an external mail provider like [Mailchimp](https://mailchimp.com/) or [Klaviyo](https://www.klaviyo.com/) to send your mail.

These third party email providers are not rate limited, as long as the mail does not pass our mail platform.

There are many [Magento email extensions](https://www.magentocommerce.com/magento-connect/integrations/email-integration.html) to send your mail through your own external mail provider or your own mailserver.

## Check if Emails Were Rate Limited

By looking at mail headers it is possible to verify whether emails were rate limited: all emails include a x-byte-ratelimited header:

```nginx
X-Byte-Mail-Received-Via: smtp-auth
X-Byte-Domain-ID: 1
X-Byte-Mail-Received-Via: mail-in-forward
X-Byte-SASL-User: byte0001
X-Byte-Domain-ID: 1
X-Byte-Ratelimited: NO
```
