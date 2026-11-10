---
myst:
  html_meta:
    description: Learn which alerts and emails Hypernode sends, who receives them,
      which ones you can send to Slack, and which events are only shown in the Control
      Panel logs.
    title: Alerts and Emails You Receive From Hypernode | Hypernode
---

# Alerts and Emails You Receive From Hypernode

Hypernode sends automated emails when something needs your attention on a Hypernode. This page explains which messages you can receive, who gets them, and which ones are not sent by email or Slack at all.

## Who Receives the Emails

Incident and security emails, such as the notice about the StyleSmuggler vulnerability, are sent to the owner and to the team members with the Admin role of each Hypernode that is affected. This makes sure the owner, and usually the agency that manages the shop, can act quickly. You can unsubscribe from these emails, but we advise you not to. If you do, you will not be warned in an emergency.

Other notification emails are sent to the owner of the Hypernode. If someone else, for example your developer, also needs to receive them, invite that person as a team member in the Control Panel and let them set up their own alerts in the Alerts manager. Alerts are set up per account, so each person chooses their own categories, Hypernodes and email address or Slack channel. See our guide on [teams](how-to-use-teams.md) and our guide on [Slack alerts](how-to-configure-slack-alerts-for-hypernodes.md).

## Where to See What Happened

Events on your Hypernode are also shown in the [logs of the Control Panel](using-logs-in-the-control-panel.md), also when no email was sent. Check there first if you want to know what happened on your Hypernode.

## Overview

```{list-table}
---
header-rows: 1
class: wrap-table
widths: 40 15 10 35
---
* - Message
  - Email
  - Slack
  - Action for you
* - Essential system alerts, such as crawler bot traffic, too many MySQL connections, full disk and Redis memory
  - Yes
  - Yes
  - Depends on the alert. The email explains it.
* - Incident or security notice, for example about a vulnerability
  - Yes, to the owner and Admin team members
  - No
  - Yes. Follow the steps in the email.
* - Emergency Rescue
  - Only for out-of-memory (OOM) events
  - No
  - None. See [Emergency Rescue](#emergency-rescue).
* - A domain can't send email, because DNS records are missing
  - Yes
  - No
  - Check your DNS records. See [A Domain Can't Send Email](#a-domain-cant-send-email).
* - An IP address was blocked for malicious activity
  - Yes
  - No
  - None, unless a legitimate visitor is blocked. See [An IP Address Was Blocked](#an-ip-address-was-blocked).
* - Malware detected on your Hypernode
  - No
  - No
  - Yes. See [Malware Detected](#malware-detected).
```

## Alerts You Can Send to Email or Slack

In the Alerts manager of the Control Panel you choose a category of alerts (for example **System**), where to send them (email or a Slack webhook) and for which Hypernodes. The tooltip on each category shows which emails it contains. Currently only the essential system alerts are available. See our guide on [Slack alerts](how-to-configure-slack-alerts-for-hypernodes.md) for how to set it up.

Alerts are set up per Control Panel account, not per Hypernode:

- One Hypernode can be part of the alerts of several accounts. If two accounts send to the same Slack webhook, you get every notification twice.
- An alert can't be edited. To change it, delete it and create a new one. Only the account that owns the alert can delete it.
- An alert for all Hypernodes also covers Hypernodes you forgot about. Deleting it stops the notifications for all of them, so check which Hypernodes it covers first.
- If you receive alerts from an account you can no longer log in to, contact support. We can remove the alert.

## Emergency Rescue

When the monitoring sees too many errors on your Hypernode, an Emergency Rescue is started automatically. You do not have to do anything. The event shows in the Control Panel logs under the name of the account owner, because the platform uses that name for the audit trail. You only receive an email about an Emergency Rescue when it was caused by an out-of-memory (OOM) event. For other rescues no email is sent, but the event is still shown in the Control Panel logs. Emergency Rescue emails are not available as a Slack alert. See our guide on [24/7 monitoring and alerting](../../about-hypernode/support/24-7-monitoring-and-alerting.md) for how this works.

## A Domain Can't Send Email

You may receive a message that your Hypernode can't send email for a domain, for example because the DKIM, SPF or `x-transip-mail-auth` DNS record is missing. Check the domains on your Hypernode:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-mail-status domains --check
```

If all checks are ok and the message was sent before you added the records, the message is outdated. If a check fails, add or correct the DNS record at the party that manages your DNS. See our guide on [setting up DNS for outgoing email](../../hypernode-platform/email/how-to-set-up-your-dns-for-outgoing-email.md).

## An IP Address Was Blocked

Hypernode blocks IP addresses that show malicious behavior, such as brute force attempts and scanning for vulnerabilities. You may receive a notice about this. The block is placed by the platform and does not need anything from you. If a legitimate visitor or service is blocked, contact support.

## Malware Detected

The malware scan runs daily on every Hypernode. When it finds something, this is shown in the Control Panel logs as "Action required: Malware detected on your Hypernode". No email or Slack message is sent for this, because the scan can produce false positives.

A finding means you have to look into it yourself, or ask your developer or a security partner. Hypernode does not investigate or clean up malware on your shop. Details about what was found and where are available with a Sansec license. See our guide on [Sansec eComscan](../../hypernode-platform/tools/how-to-set-up-sansec-ecomscan-on-hypernode.md). If you find a compromise, reset all credentials and secrets as well.
