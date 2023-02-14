---
myst:
  html_meta:
    description: On Hypernode, zero downtime deployment is supported. We offer our
      customers full flexibility with their deployment processes.
    title: Zero downtime deployment on Hypernode | Testing
redirect_from:
  - /en/best-practices/testing/zero-downtime-deployment-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/best-practices/testing/zero-downtime-deployment-on-hypernode/ -->

# Zero Downtime Deployment on Hypernode

For e-commerce shops like Magento or Shopware, uptime is key. Customers may perceive downtime as a reason to leave a shop and check out the competition. But shop maintenance and shop development is almost as important as uptime. And shop maintenance leads often leads to downtime. So what is the ideal process of moving new code from a development environment to production?

## Zero Downtime Deployment on Hypernode

On Hypernode, zero downtime deployment is supported. As we host a large number of very different shops, we do not want to interfere with the deployment processes of our customers and partners. We offer our customers full flexibility with their deployment processes.

Zero downtime deployment can be a challenge, but investing time in the set-up may absolutely pay off. Developers around the world exchange ideas and best practices on how to deploy new code without downtime. Not sure where to start? We recommend reading [this article](https://www.hypernode.com/blog/time-saving/how-to-choose-the-best-method-to-deploy-code) on how to deploy code first.

## Magento 2

Magento 2.2 includes [some nice improvements](https://community.magento.com/t5/Magento-DevBlog/Magento-2-2-Deployment-Improvements/ba-p/73119) to make zero downtime deployment possible – if no database changes are needed. Improvements include:

- The removal of static asset generation dependence on the database (so it can be run on a Jenkins or similar server),
- Performance improvements for compilation and static asset generation
- Better per environment vs. shared configuration support.

If there are any database updates zero downtime is difficult to realize. But you can strive for near-zero downtime.

Switch on the Magento maintenance mode just before database updates and immediately turn it off when it is finished. The downtime is approximately 15 seconds or less.

## Interested in Best Practices?

Some of our partners have zero downtime deployment processes in place. Please let us know if you would like to get in touch with them!
