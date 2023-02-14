---
myst:
  html_meta:
    description: Learn how to check the DNS settings of your Hypernode with our DNS
      Check. This guide shows how to use the DNS Check in our Control Panel.
    title: How to use the DNS Check? | Control Panel | Hypernode
redirect_from:
  - /en/services/control-panel/how-to-use-the-dns-check/
---

<!-- source: https://support.hypernode.com/en/services/control-panel/how-to-use-the-dns-check/ -->

# How to Use the DNS Check

Use the DNS check in the Control Panel to ensure your externally hosted domain is properly configured to send email via Hypernode. The DNS check also verifies whether the domain is correctly pointed to the Hypernode by checking the CNAME- and A-records.

**Please note that if you are using Cloudflare or another CDN type product, we cannot check all your DNS records.**

## Email Records

If your domain is hosted externally and you want to send email via your Hypernode, there are some DNS records that need to be added to the external DNS. This is needed to authenticate the Hypernode to send email from your domain.

### CNAME Record

This record should be as follows:

|                                   |          |         |                                              |
| --------------------------------- | -------- | ------- | -------------------------------------------- |
| **Label**                         | **Type** | **TTL** | **Content**                                  |
| hypernode.\_domainkey.example.com | CNAME    | 3600    | hypernode.\_domainkey.*example*.hypernode.io |

### Domain Key

This record should be as follows:

|                         |          |         |             |
| ----------------------- | -------- | ------- | ----------- |
| **Label**               | **Type** | **TTL** | **Content** |
| \_domainkey.example.com | TXT      | 3600    | o=~         |

### Mail Auth Record

This record is required by our email delivery partner, and indicates they are authorized to accept outgoing mail for your domain.

|                                 |          |         |                                                                  |
| ------------------------------- | -------- | ------- | ---------------------------------------------------------------- |
| **Label**                       | **Type** | **TTL** | **Content**                                                      |
| x-transip-mail-auth.example.com | TXT      | 3600    | f491ddb3e61d1c92ab6de9f81257b1c0b95986d6550517f005c8e5e895da6fd2 |

### SPF Record

This is the TransIP SPF record. If you already have an SPF record, you need to add Hypernode specific "include:spf.example.hypernode.io" to your existing record.

|           |          |         |                                              |
| --------- | -------- | ------- | -------------------------------------------- |
| **Label** | **Type** | **TTL** | **Content**                                  |
| @         | TXT      | 3600    | v=spf1 include:spf.example.hypernode.io ~all |

Please see [this article for how to set up your SPF records for Hypernode](../../hypernode-platform/dns/how-to-set-up-your-spf-records-for-hypernode.md).

## Web Records

The DNS Check verifies whether the domain is correctly pointed to the Hypernode by checking the CNAME- and A-records.

### CNAME Record

The recommended way to configure your DNS is to create a CNAME record in your DNS configuration, pointing to Hypernode:

|                                           |          |         |                      |
| ----------------------------------------- | -------- | ------- | -------------------- |
| **Label**                                 | **Type** | **TTL** | **Content**          |
| [www.example.com](http://www.example.com) | CNAME    | 600     | example.hypernode.io |

This means that [www.example.com](http://www.example.com) will point to wherever example.hypernode.io points, and we will make sure that that always points to the correct IP address.

### A Record

One way to redirect your apex (or naked) domain, when the domain is not hosted on the Byte name servers, is to use the www-izers:

|                                       |          |         |               |
| ------------------------------------- | -------- | ------- | ------------- |
| **Label**                             | **Type** | **TTL** | **Content**   |
| [example.com](http://www.example.com) | A        | 600     | 46.21.232.141 |
| [example.com](http://www.example.com) | A        | 600     | 46.21.233.172 |

Add both for redundancy!

This is the preferred way for the DNS Check because if for whatever reason the IP of your Hypernode changes, your shop will still be reachable.

**NB:** Note that if you make use of the www-izer redirect servers, users that visit <https://example.com> directly will get an error message, either indicating that there is no HTTPS available or a plain connection refused error. The www-izers actually work as a forwarding service to the direct IP address of the Hypernode. This way we can manage any IP changes for you. That is the advantage, the disadvantage is that these records do not cooperate with SSL and that therefore the certificate does not work properly on the domain name without the [www.](http://www.%C2%A0)

It's also an option to use the direct IP address of your Hypernode. You can find your IP with the “ping example.hypernode.io” command.

|                                       |          |         |                      |
| ------------------------------------- | -------- | ------- | -------------------- |
| **Label**                             | **Type** | **TTL** | **Content**          |
| [example.com](http://www.example.com) | A        | 600     | IP of your Hypernode |

Please note that if you use the direct IP, the DNS Check will show a warning, as you will encounter DNS downtime if the IP-address of your Hypernode changes.

### Hypernode Reachable

The DNS Check verifies whether the Hypernode is reachable via the URL you entered.

## Using Cloudflare or Other CDN

If you are using Cloudflare or another CDN type product, we cannot check your records with our DNS Check. Use our [Support Documentation](../../hypernode-platform/dns/how-to-manage-your-dns-settings-for-hypernode.md#option-2-manage-an-external-dns-by-pointing-your-domain-to-hypernode-by-using-cname-and-not-an-a-record)for managing your DNS settings for your Hypernode to make sure you have your DNS settings set up correctly.
