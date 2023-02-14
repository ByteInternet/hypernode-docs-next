---
myst:
  html_meta:
    description: Learn how to find and read email headers in common email clients
      such as Outlook, Thunderbird, Mac Mail and Gmail.
    title: How to find Mail Headers? | Hypernode
redirect_from:
  - /en/best-practices/email/how-to-find-the-mail-headers/
---

<!-- source: https://support.hypernode.com/en/best-practices/email/how-to-find-the-mail-headers/ -->

# How to Find the Mail Headers

Mail headers describe the route of an email. If you have an issue with sending or receiving email, you can use the mail header to see where the email went and discover what might be going wrong. Do you contact us about email issues? Then we usually ask you for an email header. This article explains how an email header is built and where you can find it.

## Mail Header Example

An email header looks something like this:

`Received: from mx.c1.byte.nl ([[127.0.0.1]])`

`by localhost (mail3.c1.internal [[127.0.0.1]]) (amavisd-new, port 10024)`

`with ESMTP id WQiKV-r4rtRP; Wed, 16 May 2007 12:17:13 +0200 (CEST)`

`Received: from smtp.byte.nl (misc2.c1.internal [[10.1.1.14]])`

`by mx.c1.byte.nl (Postfix) with ESMTP id 769577E47;`

`Wed, 16 May 2007 12:15:13 +0200 (CEST)`

`Received: from pc (a82-92-232-77.adsl.xs4all.nl [[82.92.252.77]])`

`by smtp.byte.nl (Postfix) with ESMTP id 33FE76217A;`

`Wed, 16 May 2007 12:13:13 +0200 (CEST)`

### How to Read Mail Headers

- You read mail headers from the bottom to the top.
- It will show you how the email was sent.
- For example, in the snippet above:
  - The PC sent the message to smtp.byte.nl at 12:13
  - Our outgoing mail server searched for the receiver and forwarded it.
  - It was then delivered to the mailbox at 12:17.

### Delayed Email

In most cases, the delay is not caused by our mail servers. Hypernode directly monitors and handles mail delays. All mail is handled through one mail cluster, if there are problems here, we will notice this immediately in our own work. If there are mail delays, we will put this on our [Hypernode status page](https://www.hypernode-status.com/). If you do not see an incident there, the cause is in almost all cases not Hypernode.

Usually it is the outgoing mail server of the ISP / provider (which receives huge amounts of mail and spam) that ensures delayed delivery.

## How to Find the Mail Header

Finding the mail header differs per email client. Below we explain how to find a mail header in some popular email programs.

### Mail Header in Outlook

1. Click in the Inbox on the right on the email that bounced.
1. Select Options.
1. A Message Options popup window will appear. The email headers are in the Internet headers box.
1. Click in this box and select the text with the mouse or CTRL-A. Copy with the right mouse button or with CTRL-C.
1. Send an email to support@hypernode.com and paste the text with the right mouse button (paste) or CTRL-V.

### Mail Header in Thunderbird

1. Click on the email.
1. Type CTRL-U
1. Copy the entire text and send it to [support@hypernode.com](mailto:support@hypernode.com).

### Mail Header in Mac Mail

1. Select the email that bouced in the Inbox.
1. Go to "View" in the menu bar.
1. Go to "Message".
1. Select "Source version" (Raw Source).
1. A window will open with the source code of the email with the header at the top.
1. Copy the header and send it to [support@hypernode.com](mailto:support@hypernode.com).

### Mail Header in Gmail

1. Open the email you want to check the headers for.
1. Next to Reply, click More and then Show original.
1. The headers will show in a new window, including fields like authentication results. To get the full message header, click Download original.
1. Copy the header and send it to [support@hypernode.com](mailto:support@hypernode.com).
