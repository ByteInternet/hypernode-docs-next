---
myst:
  html_meta:
    description: Our primary focus is providing a fast and stable hosting platform.
      In case of application related issues, we may ask you to reach out a third-party
      developer.
    title: Scope of Support | Hypernode
redirect_from:
  - /en/about/support/scope-of-support/
---

<!-- source: https://support.hypernode.com/en/about/support/scope-of-support/ -->

# Scope of Support

This document outlines the scope and limitations of support for our Hypernode platform and all related products. We strive to provide great support to attain the highest level of customer satisfaction. We also believe that clearly defining the scope of support provides clarity for our support team, but most importantly for our customers.

We will always try to be helpful, but certain changes can only be made by the customer or their developer.

## Support Availability

1. From Monday to Friday during office hours (from 8:00 AM – 6:00 PM CE(S)T) you can request support regarding technical, financial or sales questions by email (support@hypernode.com) and / or telephone (+31 (0)20 521 6226).
1. Hypernode primarily provides support in Dutch and English. If you contact us in a different language, we’ll do our best to translate your message and will reply in English.

## Server & Application Support

1. Server Support
   1. The Hypernode will come pre-configured with our web server stack, intended for hosting a web application. All pre-installed components, including but not limited to Nginx, Redis, PHP, MySQL, Elasticsearch will be supported by Hypernode. No customizations will be made to the default web server stack.
   1. In case of an issue or error, our Support team will inspect the Hypernode and its logs to debug and resolve the issue if it's related to the server or configuration. However, if the issue turns out to be related to the application, this needs to be resolved by the customer or their developer. Our Support team will share any relevant information and logs if needed.
1. Application Support
   1. Hypernode can, as a courtesy, attempt best-effort support when it comes to issues related to the application. However, as we are hosting specialists, our primary focus is on providing a fast and stable platform and not the inner workings of the web application installed on them. We may recommend reaching out to a third-party developer if necessary.
1. Exclusions
   1. Hypernode cannot assist with the installation of, or issues relating to, third-party software, such as plugins, modules, add-ons, themes or other components or scripts.
   1. Changes to the webshop content, design or appearance are excluded from the scope of support.
   1. The Hypernode Support cannot assist with issues regarding Search Engine Optimization (SEO).
   1. Email configuration and issues specific to e-mail clients such as Outlook, Thunderbird and Gmail are also not within the scope of support.

## Domains and SSL Certificates

1. We guarantee that domain names registered via us are renewed on time. We generally don't offer support on DNS settings, but we can always, as a courtesy, attempt best-effort support.
1. For SSL certificates purchased via Hypernode, we take care of the technical implementation of the certificate. We also renew the certificate on time and provide customer support on SSL issues.

## Performance & Optimization

1. Several tools and tips to improve the load times and stability of the Hypernode, such as the Hypernode-image-optimizer, blocking unwanted bots and crawlers and more, can be found in the Hypernode Support Documentation.
1. While installing Varnish is something we can assist you with (on plans where Varnish is available), the actual configuration for optimal performance of your webshop is not within the scope of support.
1. Hypernode can give customers advice about webshop optimizations, but we cannot implement these optimizations. We may recommend reaching out to a third-party developer if necessary.

## Security

1. Known “bad actor” IP ranges that perform brute force attacks are blocked.
1. We block access to many specific files used by Magento, Shopware, and other often used software, to prevent information leakage.
1. We block popular techniques, such as null-bytes, (blind) sql injection, path traversal, and PHP code insertion.
1. Logs are monitored and brute force attacks are blocked automatically.
1. Default rules protect your shop against misconfiguration of oft used Magento modules and external software.
1. When an OS update is released that fixes dangerous security issues, we may update your Hypernode with a temporary patch to block this new attack.
   1. Even with these patches in place, we still advise customers to install (Magento) updates.
1. We scan all Hypernodes daily for known (Magento) malware.

## Monitoring

1. Our monitoring is focused on the Hypernode hosting software services that come preinstalled on the Hypernode; Nginx, MySQL, and PHP, and the optional extra services; Varnish, and RabbitMQ. Each service is checked to see if it’s still running and responsive. We also monitor the root filesystem, where free space is required for logs and temp files that could otherwise cause any of these services to fail.
1. We do not monitor the application or “Does Magento/Shopware/Akeneo work”. While we do know a lot about hosting software, and we know quite a bit about the hosted applications and Magento, we don’t know the specific implementation. We also don’t know what is ‘normal’ or ‘expected’ behaviour for the application.

## Back-ups

1. Backups are made every day and saved for 7 days. We also save 1 backup per week for 3 weeks. This means there's always 4 weeks worth of backups.
1. Customers can access and restore the required files and database from available backups via the command line.
1. We can also restore the Hypernode from a backup. This means that we restore the appropriate database table, files or directories from the backup. This service costs €125,-. Restoring a backup is never completely without risk, Hypernode is not liable for data loss or other discrepancies.

## Onboarding

The goal of the onboarding process is to assist new customers in migrating their eCommerce platform to Hypernode. The aim is always to not only migrate the webshop for the customer, but also familiarize them with our platform and provide them with the adequate knowledge so that they can migrate any further eCommerce platforms themselves.

1. Basic Migration
   With a basic migration we will assist the customer in migrating their eCommerce platform as is. This means that we will make sure that the webshop is working on our Hypernode platform, but we will not look into any optimizations that can be done.
1. Hyperformance
   With a Hyperformance migration we will not only assist the customer in migrating their eCommerce platform to our Hypernode platform, we will also focus on optimizing the shop to guarantee the best performance on our Hypernode platform. We will be looking at the following things:
   1. Caching
   1. Image optimization
   1. Static file optimization
   1. Recommending any changes to be done within the eCommerce platform itself
1. What is not included in onboarding
   1. Email migration
   1. Custom Varnish configuration
   1. Fixing Application related issues
   1. Transferring Domains (unless it is delivered in a specific format)
   1. Changing DNS records at external domain registrar

## Complaints & Disagreements

1. Complaints
   Hypernode is committed to giving you the best service, but if something goes wrong we want to hear about it. If you want to file a complaint about us, you can do so by email to support@hypernode.com. Please include your account number or email address so we can get back to you as quickly as possible.
1. Disagreements (dispute resolution)Conflicts can arise between the merchant and the developer. Even though Hypernode cannot mediate in these types of situations, we can always give you advice on how to handle a conflict like this. Please shoot us a message on support@hypernode.com.
1. While we will always strive to resolve disagreements in the best way possible, we cannot deviate from certain protocols. These protocols include, but are not limited to, cancellations and customer account roles.

Hypernode reserves the right to determine, at its sole discretion, what falls under the Scope of Support on a case by case basis as necessary.
