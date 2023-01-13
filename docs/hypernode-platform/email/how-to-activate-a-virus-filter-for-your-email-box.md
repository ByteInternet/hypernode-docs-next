---
myst:
  html_meta:
    description: In this article we explain how Hypernodes virus filter works, how
      to deactivate it and what type of file extensions are blocked by the virus filter.
    title: How to activate a virus filter for your email box? | Hypernode
redirect_from:
  - /en/best-practices/email/how-to-activate-a-virus-filter-for-your-email-box/
---

<!-- source: https://support.hypernode.com/en/best-practices/email/how-to-activate-a-virus-filter-for-your-email-box/ -->

# How to Activate a Virus Filter for Your Email Box

A virus filter checks all incoming (and outgoing) email for viruses. In this article we explain how Hypernodes virus filter works, how to deactivate it and what type of file extensions are blocked by the virus filter.

## Hypernode Virus Filter

The Hypernode virus filter is on by default to protect your mailbox, but it does not block incoming and outgoing email that doesn't contain a virus. This way you don't have to worry about losing important email.

Hypernode uses a virus scanner based on heuristics and 3-hour updated virus descriptions. This minimises the chance that a new virus will slip through the scanner.

When a virus is detected, it is possible that only the infected attachment is deleted. The email is then forwarded with the message that an infected attachment has been deleted. Or the entire email is deleted and the sender receives a notification.

## Disable Virus Filter

We do not recommend deactivating the virus filter, but if you want to do this, you can do so via the Service Panel:

- Log in to the [Service Panel](https://service.byte.nl/protected/overzicht/).
- Select your domain name.
- Click the 'Instellingen' tab.
- Click on the 'Email' option.
- Click on the 'virus- en spamfilterinstellingen' icon
- Deselect the box after Virus Filter.
- Click Save.

## Blocked Files

The chance that a malicious file slips through the filter is very small, but it's possible. After all, sometimes malicious files are not yet known. For this reason our anti-virus filter blocks all files with the following file extensions unconditionally:

**.exe | .scr | .vbs | .bat | .pif | .com**

These files are executable on the Windows platform and are almost never sent by users. These files are also blocked if the virus filter is switched off.

## How to Send Blocked Files

If you still want to send (or have sent) a file with such an extension, you have two options:

- Change the file extension.
- Put the file on your webspace. You then send a link with the location of the file on the website. This way the file surely arrives!
