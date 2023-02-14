---
myst:
  html_meta:
    description: When you want to use Office365 and your domain is registered with
      Hypernode or hosted on our name servers, you will need to set up your DNS correctly
      to do so.
    title: How to set up your DNS for Office 365? | Hypernode
redirect_from:
  - /en/best-practices/email/how-to-set-up-your-dns-for-using-office365/
---

<!-- source: https://support.hypernode.com/en/best-practices/email/how-to-set-up-your-dns-for-using-office365/ -->

# How to Set Up Your DNS for Using Office365

When you want to use Office365 and your domain is registered with Hypernode or hosted on our name servers, you will need to set up your DNS correctly to do so.

## Validation Record

When you add your domain to Office365 they wil provide you with a verification string that you need to add to the DNS for your domain, the string will look something like this \*MS=ms#########.\*You need to add this at a TXT record. To do so login to your [Service Panel](https://auth.byte.nl/)and follow the next steps:

1. Log in to the Service Panel (service.byte.nl).
1. Select the domain from the domain overview.
1. Click the tab **Instellingen**.
1. Then select **DNS**.
1. Click **Voeg Record Toe**
1. Switch the record type to TXT and for the content add the string Office365 generated for you. Then click **Save Record**

## DNS Records for Office365

When you want to keep using the Hypernode name servers while using Office365 you need to change your DNS Set Up at Hypernode with the following records.

|                                    |          |                                                                                 |          |         |
| ---------------------------------- | -------- | ------------------------------------------------------------------------------- | -------- | ------- |
| **Name**                           | **Type** | **Content**                                                                     | **Prio** | **TTL** |
| domain.nl                          | MX       | domain-nl.mail.protection.outlook.com **(replace smtp1.byte.nl)**               | 10       | 3600    |
| autodiscover.domain.nl             | CNAME    | autodiscover.outlook.com                                                        | –        | 3600    |
| enterpriseregistration             | CNAME    | enterpriseregistration.windows.net                                              |          | 3600    |
| enterpriseenrollment               | CNAME    | enterpriseenrollment.manage.microsoft.com                                       |          | 3600    |
| lyncdiscover.domain.nl             | CNAME    | webdir.online.lync.com                                                          | –        | 3600    |
| msoid.domain.nl                    | CNAME    | clientconfig.microsoftonline-p.net                                              | –        | 3600    |
| sip.domain.nl                      | CNAME    | sipdir.online.lync.com                                                          | –        | 3600    |
| \_sipfederationtls.\_tcp.domain.nl | SRV      | 1 5061 sipfed.online.lync.com                                                   | 100      | 3600    |
| \_sip.\_tls.domain.nl              | SRV      | 1 443 sipdir.online.lync.com                                                    | 100      | 3600    |
| domain.nl                          | TXT      | v=spf1 include spf.example.hypernode.io include:spf.protection.outlook.com -all | –        | 3600    |

You don't need to add a new SPF record if you already have one (for example for your Hypernode) you can just edit the current one (with the pencil icon) and add the Outlook value to the current record

Please note that if you had created email boxes and email addresses at Hypernode, you must delete them. You can do this under **Instellingen > Email**in the Service Panel. Make sure to [export the emails](../../best-practices/email/how-to-export-your-emails.md) in the inbox if you want to save them to your new Office365 account before deleting the accounts at Hypernode.

Do you have any questions about how Office 365 works? Then it is best to visit the [Office 365 Community](https://techcommunity.microsoft.com/t5/office-365/bd-p/Office365General).
