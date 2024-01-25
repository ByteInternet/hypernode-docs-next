---
myst:
  html_meta:
    description: In the Control Panel, you can configure Slack alerts for your Hypernodes.
    title: How to configure Slack alerts for Hypernodes? | Hypernode
---

# How to configure Slack alerts for Hypernodes?

In the Control Panel, you can configure Slack alerts for your Hypernodes. This allows you to stay up-to-date about your servers without the need to check your email. Currently, you can configure essential system emails.

## Create Slack Webhook (if you don’t have one yet)

For your convenience we recommend starting by generating Slack Webhook. All you need is the Slack Webhook in a format: `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX` and set it up where you want to receive your alerts.

Slack App configuration example:

**Slack App icon:**
![](_res/Hypernode-logo-alerts.jpg)
**Slack App name:** Hypernode Alerts

**Workspace:** MyWorkspace

**channel:** #hypernode-alerts

## How to configure Slack alerts?

1. Log in to the [Control Panel](https://my.hypernode.com/)
1. Navigate to your profile menu in the top right corner and click [Alerts manager](https://my.hypernode.com/alerts-manager/)
1. Choose category of alerts you want to configure.
1. Choose which Hypernodes you want to receive alerts about.
  1. **All Hypernodes** - All Hypernodes you’re linked to, which means you can be the owner, admin or developer to see the Hypernode here. Any new Hypernode you’re linked to will be automatically added to all Hypernodes.
  2. **Include** - You will receive alerts only about Hypernodes included in your filter.
  3. **Exclude** - You will receive alerts about all Hypernodes except the ones that you exclude. For example you have 50 Hypernodes and you exclude yourhypernode, you will get alert about the rest 49.
1. Copy paste Slack Webhook and save your alert.

![](_res/configure-alerts.gif)

## How to change existing Slack alerts?

To remove or overwrite an existing alert filter, delete the current alert and create a new one with the desired configuration.
![](_res/delete-alert.gif)

## Tips

### Examples of emails sent

Check the tooltip in the checkbox card to see what emails are include in each category
![](_res/aagfwegWtrwEavSVfdwfawe.png)

### Use exclude

If you have multiple Hypernodes and don’t want to include all of them, just exclude the ones you don’t want to receive alerts from. Save your time and your mouse :%29
![](_res/feAFawEtGAbvFDdgddsaas.png)
