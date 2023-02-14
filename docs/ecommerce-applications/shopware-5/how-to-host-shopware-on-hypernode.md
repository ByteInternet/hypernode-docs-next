---
myst:
  html_meta:
    description: All you need to do is add a Shopware specific NGINX configuration
      file to your environment. Shopware requires a Hypernode Falcon S hosting plan
      or larger.
    title: How to host Shopware 5 on Hypernode?
redirect_from:
  - /en/ecommerce/shopware/how-to-host-shopware-on-hypernode/
  - /knowledgebase/how-to-host-shopware-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/ecommerce/shopware/how-to-host-shopware-on-hypernode/ -->

# How to Host Shopware on Hypernode

Shopware CMS is becoming more popular in the E-commerce business each day. Lots of aspects are similar to a Magento environment, so why should you not be able to host Shopware on Hypernode? There are already several shopware shops running successfully on Hypernode! All you need to do is add a Shopware specific Nginx configuration file to your environment. Shopware requires a Hypernode Falcon S hosting plan or larger.

## What is Shopware?

Shopware is an e-commerce system roughly the same as Magento and both have the same basic components. Both systems:

- Make use of the same technology stack (NGINX, PHP, MySQL, RabbitMQ, etc);
- Deal with the same challenges, such as 'light' product images and continuous processes that generate a lot of load;
- Heavily rely on a good performance and a smooth checkout;
- Make use of external systems like PIM's and payment providers;
- And are dealing with the same user behavior;

## Configuring Hypernode for Shopware

All you need to do is create a [vhost](../../hypernode-platform/nginx/hypernode-managed-vhosts.md#managing-vhosts) (or change an existing vhost) with type `shopware5` or `shopware6`.
This will make sure the specific vhost has the right nginx configuration to host your Shopware environment.
So for example, your domain is `www.example.com` and you'd like a vhost with Shopware 6 configuration.
You can create this vhost with the following command: `hypernode-manage-vhosts www.example.com --type shopware6 --https --force-https`.
