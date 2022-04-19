<!-- source: https://support.hypernode.com/en/hypernode/email/how-to-move-your-email-to-hypernode/ -->
# How to Move Your Email to Hypernode

**Please note that this only applies to Service Panel users who log in via service.byte.nl.**

Want to move your email to Hypernode? This guide will explain how to do so without losing messages.


Moving Your Email Addresses to Hypernode
----------------------------------------

Before moving your email address to Hypernode, you need to create the email address in the Service Panel. You can use [this article](https://support.hypernode.com/en/hypernode/email/email-faq#How-Can-I-Create-a-New-Email-Address?) from our Support Documentation to do so.

If you are in the process of transferring your domain to Hypernode and select **verhuis mijn domein**from the Service Panel, the domain is transferred. There's a different procedure per domain extension, please check [this article](https://support.hypernode.com/en/services/domains/how-to-transfer-your-domain-to-hypernode).

After the domain transfer is completed and the MX records point to our mail servers, messages will be delivered to Hypernode. Due to DNS caching, the DNS will not be updated everywhere simultaneously and there will be some overlap in message delivery to your old provider and to Hypernode.

You will therefore have to collect part of your messages from the previous hosting provider. Email that was sent before the domain was moved, but that has not yet been retrieved, must also be collected from the previous hosting provider.

Usually this isn't an issue, but if for example, the owner of the email address is on holiday or otherwise not reachable, you can resolve this by having the email delivered to Hypernode well before you move the domain and cancel the subscription with the old hosting provider. There are two ways to do this:

### Configuring DNS

Add the existing email addresses in the Service Panel and point the MX-records at your current hosting to our mail server.

### Forwarding Email

You can create your email addresses at Hypernode, and have the email for the email addresses forwarded to mailboxnaam@mx.byte.nl from the old hosting provider. Replace *mailboxnaam* with the name of the mailbox that belongs to the email address you want to forward.

For example: create the email address [sales@domein.nl](mailto:sales@domai.nl) => domei001 in the Service Panel. Then, at your old provider, forward the mail for [sales@domein.nl](mailto:sales@domein.nl) to [domei001@mx.byte.nl](mailto:domei001@mx.byte.nl). You can now fetch your email from our POP server in the mailbox domei001.

If you want to forward your all mail, option one (configuring your DNS) is the easier option. If you only want to forward mail sent to certain email address, we recommend option two. Both options require advanced knowledge of DNS and/or email.

Moving Your Own Mail Server to Hypernode
----------------------------------------

If you use your own mail server and want to move your site to Hypernode, you generally have to take the following steps:

* Check which mail server is configured for your domain.
* Log in to the Service Panel and select the desired domain.
* Go to the tab **Instellingen**and select **DNS.**
* If you didn't edit the DNS, you will see the default DNS records. This means there are two MX records:

| **Name** | **Type** | **Value** | **Prio** |
| example.nl | MX | smtp1.byte.nl | 10 |
| example.nl | MX | smtp2.byte.nl | 20 |

* Select the first MX-record and replace 'smtp1.byte.nl' with your own mail server. Click **Save record**.
* If your mail server is 'mail.xs4all.nl', this is all you need to do. If it's called 'mail.example.nl' you also need to create an A-record for 'mail.example.nl'. This is because you're transferring the domain to Hypernode.
* To do this click **new record**.
* Enter 'mail' in the name field. Enter the IP of your email server as **Content** and click **Add**.
* Done!
