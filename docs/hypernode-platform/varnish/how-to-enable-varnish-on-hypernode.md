---
myst:
  html_meta:
    description: 'After enabling Varnish, you need to configure both Varnish and your
      application. Per application we have a guide to walk you through the process. '
    title: How to enable Varnish on Hypernode?
redirect_from:
  - /en/hypernode/varnish/how-to-enable-varnish-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/hypernode/varnish/how-to-enable-varnish-on-hypernode/ -->

# How to enable Varnish on Hypernode

Customers with a Trial, Pelican M (or up), Falcon S (or up) or Eagle plan can use Varnish to boost the performance of their application. After enabling Varnish, you still need to configure both Varnish and your application. We have [support documentation per application](../varnish/how-to-enable-varnish-on-hypernode.md#configure-varnish-on-your-application) available to guide you through the process:

## Enable Varnish 4.0 or 6.0

At Hypernode it’s possible to enable Varnish 4.0 or 6.0 via the Control Panel, Service Panel or CLI. The Varnish version needed depends on the application version you’re running.

**Enable Varnish via the[Control Panel](https://auth.hypernode.com/)**

- Click on "Hypernodes"
- Click on "Caching"
- Select the Hypernode
- Click on "Enable Varnish"

**Enable Varnish via the [Service Panel](https://service.byte.nl/)**

- Log in on the Service Panel
- Go to the tab "Instellingen"
- Click on "Varnish"
- Use the switch to enable Varnish

**Configure Varnish 6.0 via the [hypernode-systemctl tool](../tools/how-to-use-the-hypernode-systemctl-cli-tool.md)**

`hypernode-systemctl settings varnish_version 6.0`

**Or if you want to switch to Varnish 4.0**
`hypernode-systemctl settings varnish_version 4.0`

**Enable Varnish via the [hypernode-systemctl tool](../tools/how-to-use-the-hypernode-systemctl-cli-tool.md)**

`hypernode-systemctl settings varnish_enabled true`

## Configure Varnish on the Vhost

Since the introduction of \*\*[hypernode-manage-vhosts](https://changelog.hypernode.com/changelog/release-7166-hypernode-manage-vhosts-enabled-by-default/)\*\*Hypernode may work somewhat different than you might be used to. With HMV enabled, it requires one more step to configure Varnish for your shop/vhost. Remember, for each domain, there should be a vhost created. You can list an overview of all configured vhosts with `hypernode-manage-vhosts --list`. While you do that, note that there is a column, "varnish". By default this is set to "False". Which means that Varnish isn't configured for this vhost. You can configure Varnish for the vhost by running the following command:

`hypernode-manage-vhosts EXAMPLE.COM --varnish`

## Configure Varnish on your application

The last step will be configuring Varnish on your application. Below you can find our available documentation for configuring Varnish on the application you’re using:

- [How to configure Varnish for Magento 1](../../ecommerce-applications/magento-1/how-to-configure-varnish-for-magento-1-x.md)
- [How to configure Varnish for Magento 2](../../ecommerce-applications/magento-2/how-to-configure-varnish-for-magento-2-x.md)
- [How to configure Varnish for Shopware 5](../../ecommerce-applications/shopware-5/how-to-configure-varnish-for-shopware-5.md)
- [How to configure Varnish for Shopware 6](../../ecommerce-applications/shopware-6/how-to-configure-varnish-for-shopware-6.md)
