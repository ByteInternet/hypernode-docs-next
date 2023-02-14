---
myst:
  html_meta:
    description: If your domain is hosted externally and you want to send email from
      your Hypernode, there are some DNS records that need to be added to the external
      DNS.
    title: How to set up your DNS for outgoing email? | Hypernode
redirect_from:
  - /en/hypernode/email/how-to-set-up-your-dns-for-outgoing-email/
---

<!-- source: https://support.hypernode.com/en/hypernode/email/how-to-set-up-your-dns-for-outgoing-email/ -->

# How to Set Up Your DNS for Outgoing Email

If your domain is hosted externally and you want to send email from your Hypernode, there are some DNS records that need to be added to the external DNS.

In order to stop spam, and ensure reliable delivery of your webshop’s emails, you must first authenticate your domain, and set up SPF, DKIM, and DMARC, DNS records.

## Adding DNS Records

Please add the following DNS records to your nameservers, to authenticate your domain. If you already have an SPF record (the fourth record in the table) in place please check out our documentation on [SPF](../dns/how-to-set-up-your-spf-records-for-hypernode.md), or contact our support for assistance on how to merge the SPF content into your existing values.

| Name                                    | Type  | TTL | Content                                                          |
| --------------------------------------- | ----- | --- | ---------------------------------------------------------------- |
| x-transip-mail-auth.***example.com***   | TXT   | 600 | f491ddb3e61d1c92ab6de9f81257b1c0b95986d6550517f005c8e5e895da6fd2 |
| \_domainkey.***example.com***           | TXT   | 600 | o=~                                                              |
| hypernode.\_domainkey.***example.com*** | CNAME | 600 | hypernode.\_domainkey.***example***.hypernode.io                 |
| ***example.com***                       | TXT   | 600 | v=spf1 include:spf.***example***.hypernode.io ~all               |

## Validating your DNS records

To check if your DNS records have been configured correctly, please check our online [DNS validator.](https://my.hypernode.com/dns/check/)

- The first record is the mail auth record required by the TransIP mailplatform, used at Hypernode.
- The second and third records are needed for automatic DKIM signing and DMARC
- The fourth record is the SPF record. Please make sure you include spf.***example***.hypernode.io in your DNS's SPF record.

Please check our [DNS validato](https://my.hypernode.com/dns/check/)r to confirm email can be sent successfully.

## Additional audit options

If you're sending email from your Hypernode with multiple domains you can perform an additional audit from the Command Line Interface. The following command can be used and performs a check based on the **mail.logs** from a week earlier.

```console
app@yqc2sw-example-magweb-cmbl:~$ hypernode-mail-status domains --check
example.com - mail_auth: ok, dkim_hypernode: ok, spf_record: ok
example.nl - mail_auth: error, dkim_hypernode: ok, spf_record: ok
```

In this instance the audit gives a green light for **example.com**. From this domain you will be able to send email through your Hypernode and application. For the domain **example.nl** there is one mandatory DNS record missing, namely the **x-transip-mail-auth** This will lead to email from the domain **example.nl** to be **not send** and being held in your email queue. How to manage your email queue can be found in this [article](how-to-manage-your-email-queue.md).
