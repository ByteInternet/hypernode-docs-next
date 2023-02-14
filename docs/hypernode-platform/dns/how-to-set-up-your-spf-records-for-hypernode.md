---
myst:
  html_meta:
    description: SPF or Sender Policy Framework is a technique used to fight spam.
      You can define which mail servers are allowed to send email for that particular
      domain.
    title: How to set up your SPF records? | Hypernode
redirect_from:
  - /en/hypernode/dns/how-to-set-up-your-spf-records-for-hypernode/
  - /knowledgebase/using-spf-hypernode/
---

<!-- source: https://support.hypernode.com/en/hypernode/dns/how-to-set-up-your-spf-records-for-hypernode/ -->

# How to Set Up your SPF Records for Hypernode

SPF or Sender Policy Framework is a technique used to fight spam.

By adding a TXT record in a specific syntax to the DNS zone of your domain, you can define which mail servers are allowed to send email for that particular domain.

This mechanism helps fighting spam as third party mail servers used by spammers cannot send mail for your domain from IP addresses that are not listed in the SPF record.

In other words: Sender Policy Framework (SPF) is a security mechanism created to prevent the bad guys from sending emails on your behalf by defining which IP addresses can be used to send emails from your domain.

## Composing an SPF record on Hypernode

### Implementing SPF records for the domains that you use on your Hypernode

For all domains that you send email for, create an SPF record.

For every Hypernode, we created a TXT record containing the IP of the Hypernode itself and the IP ranges we use for our outgoing mail platform.
This record is updated when you do an up or downgrade, so it’s always up to date with the IP address used for your Hypernode.

If you include this record in your existing SPF record, all IP addresses that are used for sending email from your Hypernode are covered.
To use this record, prefix ‘spf.’ to your Hypernode app name and include it in your SPF record.

IE: If your node’s app name is ‘example’, your SPF include record is `spf.example.hypernode.io`.

You can add this record to your SPF record using an include mechanism:

```
include:spf.example.hypernode.io
```

When you know which services and IP addresses are allowed to send email from your domain, glue it all together in a single SPF record.

## Determine your mail behaviour

When you start to setup SPF, first determine which mail servers are allowed to send email. This can be your office mail server, additional third parties for transactional email like Mailchimp, MailJet and Elastic Mail etc.

If you use hosted mail services like Microsoft’s Office 365 or Google’s Gmail Suite have a look at their documentation prior to implementing your SPF record.

Many specialised services that offer email functionality provide a custom TXT record. Have a look at the documentation of the hosting company to find out which record to include for the service you are using.

### Adding an SPF record to the DNS of your domain

Add an include for each third party service (IE: for Mailchimp add `include:servers.mcsv.net` to your SPF record), and combine all IP’s and records from all your email sending parties.
When this is done, your record should look something like:

```
 v=spf1 mx include:servers.mcsv.net include:spf.example.hypernode.io include:_spf.google.com -all"
```

Now open the DNS editor of your DNS provider, and create a TXT record that contains the record. Sometimes you need to add double quotes around the statement, sometimes you don’t.
After adding the record, make sure your changes are saved in case there is a “Save your changes”-button, and use `dig` to verify whether the record is visible when doing a lookup.

Never create multiple SPF records for the same domain, but instead include all mechanisms in a single record!

## How the sender policy framework (SPF) works

To determine where the email of a certain domain is delivered we use MX records. These records point to the IP address (or addresses) of the mail server.

SPF records function as reversed MX records and tell the world which ip addresses are allowed to send email for a specific domain. This is done by using a specific syntax in a DNS TXT record. Receiving mail servers check this SPF record to validate whether the mail server sending the email is allowed to do so for this domain. If the IP of the mail server is listed in the SPF record, the email is accepted as valid email, if the IP address does not match the addresses defined in the SPF record, the email will be discarded or moved to a spam folder.

This mechanism prevents unauthorised email senders from “email spoofing”. Email spoofing is when the weakness in the email protocol that allows anyone in the world to send email using a non-existing email address or someone else's email address is abused by deliberately creating emails with a forged sender address.

Due to the way email works, it’s almost impossible to prevent others from sending email on your behalf. SPF is a mechanism to prevent this from happening.

## What do SPF records look like

SPF records in general consist of 2 parts:

- A version indicator: `v=spf1`.
- The record body: In general a set of IP addresses or hostnames that are allowed to send email (mechanisms).

## Breaking up an SPF record

Let’s use this SPF record as an example:

```
v=spf1 a mx include:spf.example.hypernode.io ip4:82.94.214.5 ~all
```

The use of the version indicator is fairly easy: As creating multiple TXT records is possible, this is used to indicate that the specific TXT record is an SPF record. This indicator currently is `v=spf1`, as we are still using version one of the SPF implementation.
The record body consists of a set of mechanisms available to instruct mail servers which IP’s are allowed to send email for this domain.

## Mechanisms

The mechanisms used in this example are:

- The `a` mechanism for hostnames. When the sender's IP address matches the IP address (a record) of the domain, the email is allowed.
- The ip4 mechanism for regular IPv4 addresses. Add the IP address after "IP4" to whitelist the IP address. If email is sent from this IP and the domain name resolves to this IP, the email is accepted.
- The `mx` mechanism. If the email is sent from this MX record, the e-mail is allowed.
- The include mechanism. If the conditions in the record (that is included) are met, then the mail is allowed.

## Qualifiers

Mechanisms can be prefixed with a qualifier which describes which action to take when a sending IP address matches the mechanism. The default qualifier is a +, which can also be left out.

This means our example SPF record can as well be written as:

```
v=spf1+a+mx+include:spf.example.hypernode.io~all
```

The following qualifiers are available:

- +(Pass) – An IP that matches the mechanism with this qualifier should pass the SPF check.
- -(Fail) – An IP that matches the mechanism with this qualifier should fail the SPF check.
- ~(SoftFail) – An IP that matches the mechanism with this qualifier should soft-fail. In other words: The SPF check should fail, but the mail should be accepted by the receiving sender.
- ?(Neutral) – An IP that matches the mechanism with this qualifier should neither pass nor fail the SPF check.

The last statement of an SPF record (in our example ~all) is the catchall qualifier: This indicates what the receiving mail server should do with the email if non of the defined mechanisms match.
These qualifiers together enable you to create a fine-grained selection of email senders that should or should not be rejected by the receiving mail server.

## The Return-Path

When working with SPF, it is important to know that the receiving mail server that validates the SPF record, never looks at the email address that is set as the From address.

The From header is part of the message body and is only used for display purposes in mail clients. The receiving mail server does not inspect the message body for checking SPF but instead uses the return-path, which is a separate header, that is send prior to the message body. This is also the email address that is used to return emails to when the message bounces or an error occurs.

### Using an SPF record generator

There are web based tools available that can help you generate an SPF record. As there are always corner cases which the generator does not take into account, blindly generating an SPF record with one of these tools and copy paste it in your DNS zone is never a good idea. If you know what you are doing however, this generators can be of great assistance.

The best generators we’ve found so far are the one on[spfwizard.net](https://www.spfwizard.net), and the one on [unlock the inbox.](https://www.unlocktheinbox.com/spfwizard/) Both tools are free of use for anyone.

### Finding your current SPF record

Although there are multiple online web-based tools to lookup your SPF record, the easiest is on the command line using the `dig` utility:

```nginx
 dig -t TXT +short example.com
```

Which in this case returns 2 TXT records, of which one is the SPF record:

```nginx
"v=spf1 -all"
```

## Troubleshooting

Debugging SPF issues can be hard, as the only way of finding information about whether your SPF is correct, is by digging through the mail headers of your received and sent emails.
Luckily there are several third party services and analysis tools available to assist you in creating and maintaining your SPF record.

We list a few that can help you solving SPF problems:

- [Kittermans SPF validation](https://www.kitterman.com/spf/validate.html) – This is the first SPF checker ever, and still well known for it’s completeness
- [The SPF Check @ MX Toolbox](https://mxtoolbox.com/spf.aspx)– This is the most complete online email utility
- [Mailcleaner Batch SPF Tester](https://www.mailcleaner.net/tools/test_spf.html) – Very useful to verify if all your domains are setup correctly.

## Differences compared to DKIM

SPF is not the same as DKIM. SPF and DKIM are both spam protection mechanism that prevent unauthorised senders from mailing in your behalf.
Where DKIM works with signing messages and validating the signature to determine whether the sender is who he or she says they , SPF uses DNS to determine which IP addresses are allowed to send email for a particular domain.

**SPF is a complex technique and we recommend new users to get a specialised third party to implement your SPF records. On our partner page you will find an extended list of technical partners that can assist you implementing your SPF records.**
