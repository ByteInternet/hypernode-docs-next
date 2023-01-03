---
myst:
  html_meta:
    description: 'Your trial gives you 14 days of free testing on our Hypernode platform.
      Find out how to get started and test all features on the platform in this article. '
redirect_from:
- /en/getting-started/how-to-order/how-to-get-started-with-your-hypernode-trial/
---

<!-- source: https://support.hypernode.com/en/getting-started/how-to-order/how-to-get-started-with-your-hypernode-trial/ -->

# How to Get Started With Your Hypernode Trial

You have reached this page because you ordered a trial or paid plan on our Hypernode platform. Welcome!

Enthusiastic about Hypernode? Convert your trial into a paid hosting plan. You can choose from [a wide range of Hypernode plans](https://www.hypernode.com/magento-cloud-hosting/#plans). We offer both development plans and production plans. All plans have a 30 days contract term which gives you full flexibility to only pay for what you use.

## About Your Trial

With your free trial you have 14 days to test your shops’ performance on Hypernode. After 2 weeks your trial will expire automatically, unless you decide to convert your trial into a paid hosting plan.

The specs of your trial are: 62GB storage, 3 CPU, 8GB RAM, 1024MB Redis cache, PHP 7.4.

## Your Control Panel

Improving our Hypernode platform is [a continuous process](https://support.hypernode.com/category/changelog/) and the sole focus of our development team. You can log into your Control Panel via [this page](https://my.hypernode.com/).

- Your Control Panel allows you to manage contact and billing information.
- You can also change the PHP version of your Hypernode from the Control Panel.
- Furthermore you can add SSH users, enable Varnish and configure an external SSL certificate to use on your Hypernode.

## Get Started With Your Hypernode

We recommend taking the following steps:

### Step 1 – Log in to your Hypernode via SSH

Get started by [creating SSH keys and logging in to your Hypernode via SSH](https://support.hypernode.com/knowledgebase/use-ssh-keys-on-hypernode/).

### Step 2 – Configure Hypernode settings

You are in control and can change some Hypernode settings yourself via [the Hypernode-systemctl CLI tool](https://support.hypernode.com/knowledgebase/hypernode-systemctl-cli-tool/), like:

- PHP version: easily change the PHP version of your Hypernode
- Enable Ioncube: only enable this if you really have to, as Ioncube is a performance killer
- Enable Blackfire: a great tool to find performance bottlenecks in Magento
- Enable [OpenVPN](https://community.hypernode.io/#/Documentation/hypernode-vpn/README) for secure database connections
- Password authentication: indicates whether password authentication for the Hypernode is allowed instead of only SSH keys.
- Firewall block: indicates whether FTP (which is unsafe) is completely blocked or not
- Safer SSL and SSH configuration: you can configure Mozilla Modern SSL and enable stricter SSH encryption

### Step 3a – Import an existing shop via the Hypernode Importer tool

We have developed an awesome time saving tool, the Hypernode Importer tool. With 1 simple command you import a copy of an existing shop onto your Hypernode. This will not have a negative impact on your live shop. Instructions can be found in the [Hypernode support documentation](https://support.hypernode.com/en/hypernode/tools/how-to-migrate-your-shop-to-hypernode#Option-2-for-all-customers%3A-Migrate-your-shop-via-Shell-using-hypernode-importer).

### Step 3b – Install a new application on your Hypernode

In our support documentation you will find detailed information about installing the different applications on a Hypernode:

- [Akeneo 3](https://support.hypernode.com/en/ecommerce/akeneo/how-to-install-akeneo-3-on-hypernode)
- [Akeneo 4](https://support.hypernode.com/knowledgebase/installing-akeneo-4/)
- [Magento 1](https://support.hypernode.com/knowledgebase/installing-magento-on-hypernode/)
- [Magento 2](https://support.hypernode.com/knowledgebase/installing-magento-2-on-hypernode/)
- [Shopware 5](https://support.hypernode.com/knowledgebase/how-to-install-shopware-5-on-hypernode/)
- [Shopware 6](https://support.hypernode.com/knowledgebase/how-to-install-shopware-6-on-hypernode/)

### Step 4 – Set up Hypernode Managed Vhosts

The Hypernode Managed Vhosts (HMV) system is currently enabled by default on all new booted Hypernodes (all Hypernodes created after 01-05-2020).

Check if you have HMV enabled by running this command:

`hypernode-systemctl settings managed_vhosts_enabled`

If so, it will give the following output:

`managed_vhosts_enabled is set to value True`

If this is not enabled, skip the part below.

Due to this configuration it is required to add a new vhost for every domain you want to link to your Hypernode. So you need to configure your DNS correctly and add a new vhost for the domain.

To add a new vhost, for example the domainname [www.example.com](http://www.example.com), to your configuration, you can simply run the command `hypernode-manage-vhosts www.example.com`. This will create a new vhost configuration in `/data/web/nginx/www.example.com/`, using the Magento 2 template.

Please note that defining the vhosts '[www.example.com](http://www.example.com)', does not automatically add 'example.com' as a vhost. You will have to manually define a vhost for this. Since most people simply want their 'example.com' to redirect to '[www.example.com](http://www.example.com)', you can simply use the `--type wwwizer` argument to set this up. This will configure the vhost to redirect all traffic to the www-version of the domain.

Read more about Hypernode Managed Vhosts in [this article](https://support.hypernode.com/en/hypernode/nginx/hypernode-managed-vhosts).

### Step 5 – Configure Base URLs

You can find how to change your base URLs for Magento 1 [here](https://support.hypernode.com/en/ecommerce/magento-1/how-to-change-the-base-url-in-magento-1-x).

You can find how to change your base URLs for Magento 2 [here](https://support.hypernode.com/en/ecommerce/magento-2/how-to-change-your-magento-2-base-urls).

Please note: when you have an SSL certificate and use the secure base URL you should change the unsecure base URLs to HTTPS as well. This could result in conflicts when you leave this on HTTP.

### Step 6 – Configure DNS

There are 2 ways to handle your DNS. Only customers who have access to the Service Panel can choose option 2.

1. Point the DNS of your externally hosted domain to the Hypernode by adding two records:
   1. An A-record to the direct IP of your Hypernode for your apex or naked domain.
   1. A CNAME-record to example.hypernode.io for your www-domain, with example replaced by your appname of course.
1. Move your domain(s) to Hypernode and let us manage the DNS (Service Panel users only).

### Step 7 – Configure Nginx

One of the biggest differences between Hypernode and more traditional platforms is the use of Nginx (pronunciation: ‘Engine X’) over Apache. Nginx has much better performance than Apache, and allows us to serve your webshop to many more visitors than Apache would.

See [this category from our Support Documentation](https://support.hypernode.com/en/hypernode/nginx/) for more information about configuring Nginx.

### Step 8 – Start testing

**Tools for shop development and optimization**

Try our handy [CLI tools](https://support.hypernode.com/knowledgebase/hypernode-cli-tools-magerun-plugins/), like:

- Save disk space by using the Magento Image Optimizer
- Find out which Magento extensions slow down your shop using the php-slow-log
- Debug issues by parsing the Nginx access logs

Also we have useful [Magerun plugins](https://support.hypernode.com/knowledgebase/hypernode-cli-tools-magerun-plugins/) to retrieve information super fast, like:

- Analyze all pages in sitemap.xml and get a performance report
- Check if all security patches have been installed for your Magento version
- Find out if there are any outdated Magento extensions you need to update
- Test the vulnerability of the admin passwords of your users

Of course there is so much more to test, just decide for yourself what is important to you.

## If You Started on a Trial, Upgrade Your Trial into a Paid Hosting Plan

Convinced about Hypernode? [Convert your trial into a paid hosting plan](https://support.hypernode.com/knowledgebase/order-a-hypernode-plan/). We are happy to help you with choosing the right plan for your shop. Should your shop need more or less resources in the future, you can up or downgrade your plan any time. You only pay for what you use.

## In Need of Support?

We encourage you to have a look at our extensive Hypernode support documentation on [support.hypernode.com](https://support.hypernode.com/). Here you will find useful information and tips and tricks on e.g. how to import a shop to Hypernode, recommended tools for developers, etc.

Do you have questions about our Hypernode platform or would you like to give us some feedback? We would love to hear from you! Please send an email to [support@hypernode.com](mailto:support@hypernode.com) and we will get back to you. Our sales team and support team are available on weekdays from 8:00 AM until 18:00 PM CET/CEST (UTC+1/UTC+2).
