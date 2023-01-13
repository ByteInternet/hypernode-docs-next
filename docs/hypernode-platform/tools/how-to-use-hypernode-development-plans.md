---
myst:
  html_meta:
    description: 'Development Plans can be used for development and testing. Use this
      guide on how to use Hypernode Development Plans. '
    title: How to use Hypernode Development Plans?
redirect_from:
  - /en/hypernode/tools/how-to-use-hypernode-development-plans/
  - /knowledgebase/development-plans-for-your-magento-shop/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-use-hypernode-development-plans/ -->

# How to Use Hypernode Development Plans

Hypernode offers its customers discounted development plans of all the regular Hypernode plans for development and testing. These plans are meant to develop one webshop at a time, to run all the tests you can think of, and to give your customer (the shop-owner) access during development. Keep in mind though, these development plans cannot be used to go live with a shop.

## What Is a Development Plan?

A development plan is an exact copy of our regular Hypernode plans, with identical specs, features and cloud providers. However, they are completely separate nodes allowing you to perform load tests, try out Varnish or test different PHP-versions, all without affecting your production site.

The development plans come ready-to-go. You don’t have to worry about web stacks, optimisations, libraries or New Relic agents. In addition, it’s easy to share the acceptance environment with customers. This allows the shop-owner to get a better idea of the store’s performance on the production environment.

## Converting a Development Plan to a Production Plan

When you’re done developing you can convert to a regular production node at the click of a button in your Service Panel (service.byte.nl) or Control Panel (my.hypernode.com).

### Upgrading Your Development Plan for Service Panel Users

When you log in via [service.byte.nl](https://auth.byte.nl/)please follow the steps below to upgrade your development plan:

- Log in to the Service Panel. After logging in, you'll see a list of all your Hypernode plans.
- Click on the domain or Hypernode you want to upgrade.
- Click on **Pakketbeheer**in the tab **Administratief**.
- Click on **Wijzigen**next to **Pakkettype**.
- You'll now see an overview of your current plan. Next to your current plan, you'll see the specs of the new plan in the column Pakket.
- After selecting the right plan in the right column (don't forget to select **Production**at Uitvoering), scroll down to agree with terms and conditions and click **Pakket aanpassen**. Your plan will be changed immediately.

Please note only the Contracting party or Technical Party (when they're a Hypernode partner) can change the plan

### Upgrading Your Development Plan for Control Panel Users

If you log in via [my.hypernode.com](https://auth.hypernode.com/), please use the steps below to change your plan via the Control Panel:

- Log into your Control Panel via [my.hypernode.com](http://my.hypernode.com)
- There are two ways to go the **Change plan**page:
  - Go to the**Change plan** page by selecting it from the sidebar on the left. Move your mouse over **Hypernodes** to make the menu appear:
  - Or click **Change your plan** in the Hypernode overview.
- You'll now see an overview of your current plan on the left and the new plan on the right.
- Select the desired plan and the type of environment, which is Production.
- Select an add-on. Read more about our two SLA levels [here](../../about-hypernode/support/emergency-support-outside-office-hours.md#hypernode-emergency-service-costs).
- Agree with terms and conditions and click Change to this plan. Your plan will be changed immediately.

## Limitations

We offer the development plans with a discount to help our customers set up a good development process. We can offer a discount because there’s no monitoring, no support outside of office hours and no historical back-ups available for development nodes.

Additionally, Google and Bing crawlers are blocked to prevent production usage of the node.

## Using Basic Authentication

By default, development nodes are shielded using basic authentication. This means that any (accidental) visitor needs to enter a separate password before being able to access the site.

The default user credentials for development nodes are:

- Username: dev
- Password: dev

You can of course change these credentials, and add and remove user accounts. It is also possible to whitelist IP addresses to exclude them from the basic authentication. This allows you to whitelist services and third party tools that can’t use basic authentication, or easily allow your merchant access to the development environment.

For information on how to configure this, we have an article on how to use [Basic Authentication on Hypernode Development Plans](../nginx/basic-authentication-on-hypernode-development-plans.md).

To override a single IP from the basic authentication, you can whitelist this IP address by adding it to `/data/web/nginx/whitelist-development-exception.conf`.

This way you can easily test API connectivity, do load tests or run MageReport on your development node.

Alternatively, you can whitelist user agents as well by using the following snippet in `/data/web/nginx/whitelist-development-exception.conf`:

```
map $http_user_agent $development_exceptions {
default "Development restricted area";
~*(useragent1|useragent2|useragent3|etc) "off";
}
```

## How To Use MageReport on a Development Plan

Do you want to check a webshop on a development plan using MageReport? Add the username, the password and the domain name to the URL like this:

<https://www.magereport.com/scan/?s=username:password@dev.example.com>

Alternatively you can whitelist add the IP’s MageReport uses to scan your Hypernode.

## The Difference Between a Development Plan and a Staging Environment

A staging environment shares resources (disk, cpu, memory) and services with your production site. This means that it’s not possible to test different PHP-versions and when you do things such as automated load tests, your production site could be affected.

## The Difference Between a Development Plan and the Hypernode Docker

The Hypernode Docker is a tool that allows you to set up a virtual Hypernode for local development on your computer. In contrast to the development plans it’s not possible the share the acceptance environment with customers.

## How To Start?

Order a development plan and start developing in no time! Do you already have a shop and do you wish to import it onto a Development node? Learn more about migrating it in [this article](../tools/how-to-migrate-your-shop-to-hypernode.md).
