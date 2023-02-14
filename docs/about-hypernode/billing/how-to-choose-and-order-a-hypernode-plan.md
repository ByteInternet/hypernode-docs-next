---
myst:
  html_meta:
    description: Find the perfect hosting plan for your online store with Hypernode.
      Learn how to choose and order a Hypernode plan.
    title: Choose and Order a Hypernode Plan | Hypernode
redirect_from:
  - /en/about/billing/how-to-choose-and-order-a-hypernode-plan/
  - /knowledgebase/order-a-hypernode-plan/
---

<!-- source: https://support.hypernode.com/en/about/billing/how-to-choose-and-order-a-hypernode-plan/ -->

# How to Choose and Order a Hypernode Plan

Need a (new) hosting plan for your Magento, Shopware or Akeneo shop? You’ve come to the right place. Hypernode has been developed in close consultation with e-commerce developers, with the objective of having e-commerce web shops perform to best advantage and to make its development several times easier.

You’re only a few steps away from improving your e-commerce hosting solution. This article wil help you choose the best fit for your shop.

An overview of all hosting plans can be found on [our website](https://www.hypernode.com/magento-hosting-plans/).

## What Hypernode Plans Are There?

Depending on your shop’s wants and needs, we offer different Hypernode hosting plans:

- Pelican (and up)
- Falcon (and up) formerly known as Professional
- Eagle (and up) formerly known as Excellence

Each production plan has a development equivalent. A development plan is cheaper and therefore recommended when developing and testing shops before going live. A development plan can easily be upgraded to a production plan.

Small shops with few products or start-ups will do nicely with a Falcon XS or Falcon S plan. Bigger shops with 4000 to 30.000 visitors a day will need at least a Hypernode Falcon M plan. Big, high end shops with a lot of (unique) visitors a day and products need a lot of CPU and data storage, so an Eagle plan is just what they need.

A complete overview can be found on [our website](https://www.hypernode.com/magento-hosting-plans/).

## Can I Test Hypernode Before I Commit Myself?

Absolutely. When choosing a free non-binding trial you can test our platform and all its features before making a decision. You trial will expire automatically unless you choose to upgrade it to a paid hosting plan. You can order a trial via [hypernode.nl](https://www.hypernode.nl/) or [hypernode.com](https://www.hypernode.com/).

## Which Hypernode Plan Do I Need?

Depending on your needs. Naturally you’ll need enough disk space for your shop, as well as enough CPU to make sure your shops stays fast during peak hours.

If your shop generates a lot of traffic but is small in size, it’s better to choose a Hypernode plan that can handle said traffic easily. Bigger hosting plans like Hypernode Falcon and Eagle also offer a lot more features, such as; historical back-ups, Varnish cache and PCI compliancy (only with Eagle plans).

Not sure what to order? Do not worry about ordering the wrong plan. The contract term of Hypernode plans is only 30 days and you can up- or downgrade your plan any time you want. You only pay for what you use.

## Booting Your Hypernode In a Different Data Center

We make use of cloud providers:

- Combell OpenStack: Hypernode Falcon plans, booted in Gent (Belgium)
- DigitalOcean: Hypernode Pelican plans, booted in other data centers around the world
- Amazon Web Services: Hypernode Eagle plans.

When you order a Hypernode, your node is by default booted in Gent (Combell OpenStack) or Frankfurt (Amazon).

However, it is possible to boot a Hypernode in a different region on request. This can be desirable if you do most of your business in (for example) the USA. Simply send an email to support@hypernode.com and let us know which data center you prefer. We will then boot a Hypernode in your preferred data center and arrange the switch.

Please keep into account that a switch of datacenter triggers an IP change of your Hypernode.

DigitalOcean and Amazon both have data centers all over the world.

- DigitalOcean has data centers in: Londen, Frankfurt, New York, San Fransisco, Toronto, Bangalore, Singapore
- The location of the Amazon (AWS) data centers can be found on [their website](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions).

## How To Order a Hypernode?

You can order a Hypernode plan via our [order page](https://www.hypernode.com/magento-cloud-hosting/#plans). The Control Panel is our default panel, which means all new Hypernode plans and trials will be booted in the Control Panel.

**Please note:** if you are a Service Panel user (i.e. you use the Dutch panel), please order your new plans directly via [this page in the Service Panel](https://service.byte.nl/planinfo/order-selection/). This is to prevent plans from being booted in the wrong system.

## Tips For Ordering a Hypernode

- Choose a logical name. IE: If your site is example.com, order example.hypernode.com
- Make sure you pick a node with enough disk space for both your shop and your database.
- Don’t use environment indicators like staging test, testing, dev or development:
  Without these indicators, you can easily change this node from a live to a test node without confusion or having to migrate to a server with another name.
- Still developing a shop? Then select [a development environment first](../../hypernode-platform/tools/how-to-use-hypernode-development-plans.md). When your Hypernode is [ready to go live](../../best-practices/testing/how-to-go-live-with-your-hypernode.md) you can easily switch to a production node.
- Use [this article to remove a Magento installation](../../ecommerce-applications/magento-2/how-to-remove-your-magento-2-x-installation.md) in case you want to reuse an existing Hypernode or accidentally ordered a Hypernode with a preinstalled Magento on it.
