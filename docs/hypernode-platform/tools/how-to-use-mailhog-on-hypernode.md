---
myst:
  html_meta:
    description: 'MailHog is an email testing tool for developers to catch all these
      emails in a single mailbox. Learn how to use MailHog on Hypernode. '
    title: How to use Mailhog on Hypernode?
redirect_from:
  - /en/hypernode/tools/how-to-use-mailhog-on-hypernode/
  - /knowledgebase/how-to-use-mailhog-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-use-mailhog-on-hypernode/ -->

# How to Use MailHog on Hypernode

Debugging outgoing mail issues could require you to inspect all outgoing mail from a webshop. With MailHog you can send out as many test emails as you’d like, none will reach your customers. MailHog is an email testing tool for developers to catch all these emails in a single mailbox.

**Please note: any mail sent out while MailHog is activated will be consumed by MailHog. The emails caught by MailHog will not reach your customers. After MailHog is deactivated only the emails sent after deactivation will reach the customers.**

## How to Activate MailHog

To install MailHog on a Hypernode, MailHog first needs to be enabled. This can be done using the following command through the CLI.

```nginx
hypernode-systemctl settings mailhog_enabled True
```

This will install and activate MailHog (might take a couple minutes).

## How to Use MailHog

After the setting is changed and the node is updated, all mail sent from the Hypernode will be caught in the MailHog mailbox. Mail will not reach customers anymore.

To access MailHog we need to link the `8025` port on the Hypernode to our own `8025` port. This can be done using a SSH connection. Enter the following command on the CLI on your local computer.

```nginx
ssh app@appname.hypernode.io -L 8025:localhost:8025
```

This will forward `localhost:8025` (where MailHog is running) to our local `8025` port. Now going to `localhost:8025` in a browser will show the MailHog mailbox with all the mails it catches from the Hypernode.

## Access MailHog with HMV and Basic Authentication

If HMV ([Hypernode Managed Vhosts](../nginx/hypernode-managed-vhosts.md)) is enabled on your Hypernode, you can easily create a vhost for MailHog by using the command below which also enables Basic Authentication.

```nginx
hypernode-manage-vhosts mailhog.example.hypernode.io --https --force-https --type mailhog
```

After you've whitelisted your IP-address in ~/nginx/mailhog.example.hypernode.io/server.basicauth.conf, MailHog will be accessible through <https://mailhog.example.hypernode.io>

## How to Deactivate Mailhog

If you are using a development node, MailHog can keep running. If you used MailHog to test something on the production node, it needs to be turned off after use. Luckily this is as easy as turning MailHog on. Using the following command.

```nginx
hypernode-systemctl settings mailhog_enabled False
```

Wait for the Hypernode to uninstall MailHog and restore all the normal mail settings (might take a couple minutes).
