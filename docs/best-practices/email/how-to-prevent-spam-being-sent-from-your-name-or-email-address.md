---
myst:
  html_meta:
    description: Minimize the chance of someone sending spam using your name and email
      address and learn what Hypernode can and cannot do to help you.
    title: Prevent spam being sent from your name or email address
redirect_from:
  - /en/best-practices/email/how-to-prevent-spam-being-sent-from-your-name-or-email-address/
---

<!-- source: https://support.hypernode.com/en/best-practices/email/how-to-prevent-spam-being-sent-from-your-name-or-email-address/ -->

# How to Prevent Spam Being Sent From Your Name or Email Address

Anyone can send email from any name and email address. When sending the mail, you simply change the email address and sender. Malicious parties like to use this when sending spam. In this article we explain what you can do to prevent this.

## Send Email Under a Different Name

**"Someone is sending spam email with my email address as the sender!"**

It may happen that others send mail in your name. These could be viruses that have taken your name from the address book of an infected computer. But it could also be spammers, who have randomly chosen your name or email address from a large list as sender for their spam messages (a so-called “Joe-Job”). Everyone can set random email addresses in the mail program and spammers are already very skilled at this. The responses to those spam messages will then logically be sent to your email address.

**Annoying, but unfortunately nothing can be done to prevent this 100%.**

The email system does not provide for sender verification, so it is possible to specify anything. However, there a few things you could try to minimise the chances of this happening:

- If you get a lot of responses from a single person, you can have this sender blocked by your mail program.
- If the responses are sent to an address that falls under your Catch All, but that you don't actually use, you can disable this specific address via the Service Panel. For this you create an extra address (the address to which the messages will be sent) and have the mail forwarded to “nobody”. The messages will then be discarded.
- Tighten your SPF record with -all at the end, so that anything that is not formulated in your SPF record will not be accepted by the receiving mail server.
- Make sure you have SAV enabled in all your mailboxes.
  \*\*Please note:\*\*This construction only works if no mailboxes have been selected, and no other external addresses have been specified.

## Can Such an Email Include My Email Address in the Spam Filter of Others?

That is indeed possible, but most spam filters are smart enough not to block based on properties that can easily be copied (such as the sending address).

## What Can Hypernode Do?

Nothing. Anyone can set what they want as the sender. So your email address, but also our email address (which happens a lot). So unfortunately we can't do anything for you in this case.

## What Should I Do?

All you can do is wait. Finding the channel is of no use, this is 99% definitely a hacked PC in any country, used by hackers to spam. With a bit of luck, it will stop after a few messages.

## Do All My Connections Receive Spam E-Mail Messages From Me Now?

No, you're probably the only one receiving these messages.
