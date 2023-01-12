---
myst:
  html_meta:
    description: If you are sending email through the Hypernode and your application
      you will want to know how you can manage your email queue.
    title: How to manage your email queue? | Hypernode
redirect_from:
  - /en/hypernode/email/how-to-manage-your-email-queue/
---

<!-- source: https://support.hypernode.com/en/hypernode/email/how-to-manage-your-email-queue/ -->

# How to Manage Your Email Queue

If you are sending email through the Hypernode and your application you will want to know how you can manage your email queue. In this article we will explain how you can do this on the Hypernode platform. This will give you insights when emails are not being send and how you can push them or remove them completely.

## Insight into your mail queue

On your Hypernode you are able to get insight what emails are in your mail queue. The common software systems providing email services queue messages as part of their operations. Hypernodes are configured to process a capped amount of emails enforced by the email policies. On the Command Line Interface you can use the following command to open your mail queue.

```
app@yqc2sw-example-magweb-cmbl:~$ mailq
-Queue ID- --Size-- ----Arrival Time---- -Sender/Recipient-------

8E71A60796 1671918 Fri May 20 18:44:23 info@example.nl
(host vps.transip.email[83.217.90.250] said: 421 4.7.0 No valid 'x-transip-mail-auth' DNS record found for 'example.nl'.
	Please see https://www.transip.eu/knowledgebase/entry/349 for more information. (8D9WKA15KCh21) (in reply to end of DATA command))
 info@example.nl
 support@hypernode.com

5D769432C0* 320 Fri May 5 11:45:31 test@example.nl
 support@hypernode.com

5F30C432C1* 320 Fri May 5 11:45:31 test@example.nl
 support@hypernode.com
--- 3 Kbytes in 3 Requests.
```

In this use case there are three emails in the queue and one of them will not be send because the the DNS is not setup correctly. How to set up your DNS for outgoing email can be found in this [article](how-to-set-up-your-dns-for-outgoing-email.md). When the required DNS record is added to the domain DNS you are able to force a retry to send this email. This can be done from the Command Line Interface as the **app** user with:

```
app@yqc2sw-example-magweb-cmbl:~$ **/usr/sbin/sendmail -q**
```

## Remove email from your mail queue

If the volume of emails to send is higher than the number of emails being processed for delivery, the queue grows larger, and depending on the volume this may consume considerable disk space. Then it may be desired for the app user to clear items from the mail queue of emails that can be sent again later, or simply drop unnecessary email. This can be done using the hypernode-postsuper command. The help menu displays the available options.

```
app@yqc2sw-example-magweb-cmbl:~$hypernode-postsuper --help
usage: hypernode-postsuper [-h] [-v] -d DELETE

Hypernode wrapper for postfix postsuper command

optional arguments:
 -h, --help show this help message and exit
 -v, --verbose Enable verbose logging
 -d DELETE, --delete DELETE
 Delete a message with the named queue ID, or ALL to
 clear queues, set - to specify queue id from stdin
```

For example, given we have a few emails in the queue, removing one item from the queue would look like:

```
app@yqc2sw-example-magweb-cmbl:~$ mailq
-Queue ID- --Size-- ----Arrival Time---- -Sender/Recipient-------

8E71A60796 1671918 Fri May 20 18:44:23 info@example.nl
(host vps.transip.email[83.217.90.250] said: 421 4.7.0 No valid 'x-transip-mail-auth' DNS record found for 'example.nl'.
Please see https://www.transip.eu/knowledgebase/entry/349 for more information. (8D9WKA15KCh21) (in reply to end of DATA command))
 info@example.nl
 support@hypernode.com

5D769432C0* 320 Fri May 5 11:45:31 test@example.nl
 support@hypernode.com

5F30C432C1* 320 Fri May 5 11:45:31 test@example.nl
 support@hypernode.com
--- 3 Kbytes in 3 Requests.

app@yqc2sw-example-magweb-cmbl:~$ hypernode-postsuper -d 5D769432C0
postsuper: 5D769432C0: removed
postsuper: Deleted: 1 message
```

Clearing out the mail queue would look like:

```
app@yqc2sw-example-magweb-cmbl:~$ hypernode-postsuper -d ALL
WARNING: Clearing out postfix mail queues
postsuper: Deleted: 3 messages
```

For more information about this setting see this [changelog](https://changelog.hypernode.com/release-5678-new-hypernode-postsuper-utility-to-clear-mail-queue/).
