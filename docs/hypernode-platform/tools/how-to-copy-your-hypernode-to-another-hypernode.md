---
myst:
  html_meta:
    description: 'If you want to make a copy of your Hypernode to another Hypernode,
      whether it’s a development node or not, here’s a guide on how to do it. '
    title: How to copy your Hypernode to another Hypernode?
redirect_from:
  - /en/hypernode/tools/how-to-copy-your-hypernode-to-another-hypernode/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-copy-your-hypernode-to-another-hypernode/ -->

# How to copy your Hypernode to another Hypernode

If you wish to make a copy of your Hypernode to another Hypernode, whether it's a development node or not, here's how you do it:

## [1. Buy a new Hypernode via your Control Panel](https://my.hypernode.com/)

## 2. SSH Access

To receive SSH access from <new-appname>.hypernode.io to <old-appname>.hypernode.io make a SSH keypair on <new-appname>.hypernode.io and place this public key in the **authorized_keys** on <old-appname>.hypernode.io

You can make an SSH keypair like this:

```bash
ssh app@<new-appname>.hypernode.io
ssh-keygen
```

Press "Enter" several times and you have your keypair. Copy your public key from id_rsa.pub and place they key in <old-appname>.hypernode.io `/data/web/.ssh/authorized_keys`.

## 3. Import

Login <new-appname>.hypernode.io. Now you're able to run the **hypernode-importer** with only one command:

```bash
hypernode-importer --user app --host <old-appname>.hypernode.io --path /data/web/magento2  # (please check the right path to the Magento 2 folder)
```

## 4. Base-URLS

One last step is to change the Base-URLS into the right URL for example: [https://newappname.hypernode.io/](https://appname%28new%29.hypernode.io/)
You're able to request Let's Encrypt for this vhost:

```bash
hypernode-manage-vhosts newappname.hypernode.io --https --force-https
```

Please do remember that Let's Encrypt is a free service and it's possible that it isn't working correct 100%. We do offer single, EV or Wildcard SSL certificates as well, maybe it isn't necessary for a development plan but keep it in mind for your production Hypernode with your live webshop.

## Troubleshooting

These are the only steps you need to do to make a copy of one Hypernode to another Hypernode. If you want us to do this, that's possible and no problem at all. The cost will be **125 euro** per Hypernode.
