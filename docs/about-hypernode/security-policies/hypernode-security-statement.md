---
myst:
  html_meta:
    description: At Hypernode, we prioritize the security of our servers and hosting
      platform. Our security policies and procedures are based on ISO 27001:2013 certification.
    title: Security Statement - Protecting Your Data | Hypernode
redirect_from:
  - /en/about/security/hypernode-security-statement/
---

<!-- source: https://support.hypernode.com/en/about/security/hypernode-security-statement/ -->

# Hypernode Security Statement

At Hypernode we take the security of our servers, and our hosting platform, very seriously. We understand that many of our customers entrust their most important data to us, and we strive to keep this data as secure as possible. A good security standard leans on certifications, best practices, and industry standards, to set policies, and implement procedures. Combining all this allows us to defend both your, and our own data, against an ever-changing landscape of both online and offline threats.
Below we have listed some of our most important policies to help ensure the safety of your data.

## ISO Certification

One of the main pillars of our security policy is our ISO 27001:2013 certification. ISO 27001 is a highly respected internationally standard for information security management. To obtain this certificate, we had to set up an information security management system, which allowed us to identify what policies, guidelines, and procedures were needed to safeguard both our own, and our customer's data. This system receives yearly, external, audits, to help us identify missing, or insufficient, policies and procedures.

## Cloud Hosting Supplier Certification

Because we work with cloud hosting suppliers around the world, we also need to make sure that your data is safely stored at these suppliers. To ensure this, we only work with ISO 27001:2013 certified hosting companies.

We currently run Hypernodes at 3 different cloud suppliers:

- Combell OpenStack (COS)
  - Both [ISO 27001](https://www.combell.com/en/about-combell/iso-27001-quality-label) and [ISO 9001](https://www.combell.com/en/about-combell/iso-9001-quality-label) certified.
  - Datacenter certified with ISO 14001, ISO 27001, ISO 23301, and PCI-DSS
- Amazon Web Services (AWS)
  - [ISO 9001](https://aws.amazon.com/compliance/iso-9001-faqs/), [ISO 27001](https://aws.amazon.com/compliance/iso-27001-faqs/), [ISO 27017](https://aws.amazon.com/compliance/iso-27017-faqs/), [ISO 27018](https://aws.amazon.com/compliance/iso-27018-faqs/), certified.
  - Datacenter certified with ISO 9001 and ISO 27001.
- DigitalOcean (DO)
  - [ISO 27001:2013](https://www.digitalocean.com/trust/certification-reports/) certified.
  - Datacenter certified with either ISO 27001:2013, or SOC 2 Type II, dependent on physical location.

## Infrastructure Hardening

As your security is only as strong as the weakest link, the safety of our systems is built-in from the ground up, starting with our own infrastructure used to manage, monitor, and deploy Hypernodes. We employ various technical and non-technical measures to ensure both the stability and safety of these systems.

- All our servers run on proven secure and stable Operating Systems, using either Debian, Ubuntu LTS, or similar software for dedicated systems.

- All servers are centrally managed and updated periodically. Security updates to critical software are installed automatically.

- All servers are hardened against attacks.

  - Only the necessary software and services are installed on servers.
  - Default passwords are changed.
  - Security software is installed on all machines to prevent virus/malware infection.

- Administrative access to servers is only possible through secure, encrypted, connections. Authentication is performed through the use of cryptographic authentication keys.

  - TLS connections are configured to only use modern, secure, encryption.
  - Cryptographic keys are tied to a single person. The use of shared cryptographic keys, or sharing of personal keys, for accessing our infrastructure, is prohibited.
  - Administrative access is only granted to employees as required to perform their duties.
  - All employees receive training before being given administrative access.

- All services are configured following best practices, published by software suppliers, and organizations such as NCSC, IETF, and Mozilla.

- Our entire infrastructure is secured by both a dedicated hardware perimeter firewall and host-based software firewalls.

## Hypernode Hardening

E-commerce sites are a prime target for cybercriminals, something we realize like no other. Your Hypernode is designed from the ground up with security in mind. Every precaution has been taken to ensure that your shop’s data stays secure on your Hypernode.

- All Hypernodes run on Debian Buster, a proven secure and stable Operating System.

- All Hypernodes are centrally managed and updated automatically several times a week.

- All Hypernodes are hardened against attacks.

  - Only the necessary software and services are installed on servers.
  - Default passwords are changed.
  - Security software is installed to protect the Operating System against virus/malware infection.

- Administrative access to Hypernodes is only possible through secure, encrypted, connections. Authentication is performed through the use of cryptographic authentication keys.

  - Cryptographic keys are either tied to a single person or loaded through a Bastion Host accessed with a personal cryptographic key.
  - Administrative access to servers is only granted to employees as required to perform their duties.
  - All employees receive training before being given administrative access.

- All services are configured following best practices, published by software suppliers and organizations such as NCSC, IETF, and Mozilla.

## Webserver Hardening

With the rise of automation, botnets, and downloadable exploits, websites are now under attack almost 24/7. We have taken every precaution to make sure your shop is as secure as possible against web-based attacks. By aggregating anonymized logs from many Hypernodes at a time, we can identify bad actors and new attack vectors and defend your shop before it gets attacked.

- Known “bad actor” IP ranges that perform brute force attacks are blocked.

- We block access to many specific files used by Magento, Shopware, and other often used software, to prevent information leakage.

- We block popular techniques, such as null-bytes, (blind) sql injection, path traversal, and php code insertion.

- Logs are monitored and brute force attacks against both Magento, and other software, are blocked automatically.

- Default rules protect your shop against misconfiguration of oft used Magento modules and external software.

- When a Magento patch is released that fixes dangerous security issues, we may update your Hypernode with a temporary patch to block this new attack.

  - Even with these patches in place, we still advise customers to install these Magento updates.

- We scan all Hypernodes daily for known (Magento) malware.

## People Hardening

With enough monitoring, alerting, and automation, it is possible to create a fully secure system. But if the weakest link, the human operator, is not factored in, mistakes can still happen. Mistakes that, either intentionally, or accidentally, bypass security measures. As such we have taken utmost care to educate our employees and ensure they are part of the security solution.

- Employees receive an in-depth security training when they are employed, as well as yearly refresher courses.

  - Select personnel also receives periodic training about newly identified security threats.

- Employee access to any system is based on the principle of least privilege, and only as required to perform their duties.

  - Root access is only granted to specially trained sysadmin, and technical support.
  - Access to customer’s data is granted only to trained support specialists.

- All employees are vetted before being granted access to customer’s data.
