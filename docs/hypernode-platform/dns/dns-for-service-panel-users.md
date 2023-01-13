---
myst:
  html_meta:
    description: You can edit the DNS setting for your domain names in the Service
      Panel (Instellingen => DNS). It takes 24 hours for a DNS change to be implemented.
    title: How to manage your DNS as a Service Panel user?
redirect_from:
  - /en/support/solutions/articles/48001153093-dns-for-service-panel-users/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001153093-dns-for-service-panel-users/ -->

# DNS for Service Panel Users

DNS stands for "Domain Name System" and is a protocol that translates domain names to IP addresses on the internet. A DNS server is simply a table that contains IP addresses and hostnames (the name of a computer). The internet also uses DNS. When you go to a website, the IP address of the server behind the domain name is checked.

You can edit the DNS setting for your domain names in the Service Panel (Instellingen => DNS).

It takes 24 hours for a DNS change to be implemented everywhere. Take this into account.

More information about DNS settings for your Magento webshop on Hypernode technology, for example how to manage your DNS settings for a Hypernode can be found [here](how-to-manage-your-dns-settings-for-hypernode.md).

## Manage DNS With a Third Party

Please note that Hypernode cannot provide uptime guarantees for external DNS. Your SLA does not apply in this case. When a domain name is registered externally, please keep in mind that Hypernode has no influence on the functioning of the DNS. If you don't want to transfer your domain name to Hypernode, changing the name servers to the Byte name servers is a good second option. You will need a Presence plan to be able to manage your DNS from the Service Panel. When you have the DNS set up correctly you can ask your domain name provider to change the name servers to the Byte name servers:

nsa.byte.nl

nsb.byte.nl

nsc.byte.nl

If it is not possible to change the name servers at your domain provider you can find how to direct your domain to your Hypernode [here](how-to-manage-your-dns-settings-for-hypernode.md#option-2-manage-an-external-dns-by-pointing-your-domain-to-hypernode-by-using-cname-and-not-an-a-record).

## How Does DNS Work at Hypernode?

You can find the DNS settings in our Service Panel. To do this, go to the 'Instellingen' tab and choose the DNS option. For each Presence plan we have a list of standard DNS set up:

3 NS records (name servers) from Hypernode. These cannot be removed or changed. If you need to change the name servers (to for example Cloudflare) you can request this by sending an email to [support@hypernode.com](mailto:support@hypernode.com) (from the email address that is linked to the account)

3 MX records referring to Byte mail servers

4 A records to link the domain name to the web hosting

3 CNAME records to link certain services at the domain level

1 TXT record (SPF record) to ensure that Byte's mail servers are authorised to email with email addresses ending in this domain.

There are also four buttons with which you can perform the following actions:

### Reset DNS

When this button is pressed, any DNS changes will be reset to the DNS settings to the default settings for the plan.

### Add Record

When this button is pressed you will see a new screen. Here you can add a new record. Here you indicate in the field for **Name** for which subdomain you are creating a record. At **Type** you choose between A, AAAA, CNAME, MX, TXT and SRV. With **conten**t you indicate to which hostname or to which IP address should be referred. You specify which **priority** the record gets and how long the TTL should be.

### X Icon

This will delete the DNS record.

### Notepad Icon

This changes a current record. You will see the same screen as you click on **Add Record,** but you can edit a current record here.

## The Fields in a DNS Table

You can add a number of values to the different DNS records. These values are explained below:

### Name

Here you enter the domain name, which can be a fixed address such as example.nl or [www.example.nl](http://www.example.nl), but you can also add a so called wildcard record. A wildcard record is for example * .example.nl and means that all subdomains that do not have a separate DNS record fall under this, an example:

|                                           |          |              |                 |                  |
| ----------------------------------------- | -------- | ------------ | --------------- | ---------------- |
| **Name**                                  | **Type** | **Priority** | **Content**     | **Time to live** |
| example.com                               | A        | -            | 125.125.125.125 | 600              |
| [www.example.com](http://www.example.com) | A        | -            | 124.124.124.124 | 600              |
| \*.example.com                            | A        | -            | 123.123.123.123 | 600              |

### Type

The type of record will be shown here, more about the type of DNS records is explained in the next paragraph.

### Content

The value of the DNS record is entered here, which differs per record type. Information about which values you can enter per type can be found in the next paragraph about types of records.

### Prio

The priority of a DNS record is only used for MX records (mail records), with this you can assign a priority to different mail servers and thus ensure that, for example, our (fallback) mailserver is called on when your own mail servers are offline.

### TTL

TTL stands for “Time To Live”, which is the time in seconds that a server remembers the data in a DNS record. At hypernode the TTL for the A records is set to 600 by default. This means that if you go to a domain, the data for that record is stored for ten minutes. So if you surf on a Hypernode domain for fifteen minutes, your provider's DNS server should have made two requests to request the A record of that domain. Providers sometimes want to store this data for longer, they will then force a longer TTL than actually indicated in the DNS server. This is called DNS caching and it is described in detail further on this page.

Hypernode recommends using a short TTL for the A records. Suppose you want to change an IP address of a record with a TTL of an hour or more, it will take an hour for people who have already visited the site to be notified of the change. A short TTL ensures that you can switch quickly if necessary.

## Types of Records

Different DNS records have been created for the different types of internet traffic. Here it is described which types of DNS records are most common and what purpose they have;

### NS Records

The NS records contain the "authoritative name servers" or prevailing name servers. When your domain name is listed with Hypernode, these will always be on Byte's name servers by default. This determines that we are the party that manages the DNS records. You can also find them in the WHOIS. The Byte name servers are:

nsa.byte.nl

nsb.byte.nl

nsc.byte.nl

If you have set up other name servers, the DNS data will be downloaded from that server. Hypernode always recommends using the Byte name servers so that in the event of IP changes (if you switch from datacenter) we can switch quickly, without having to make changes to the DNS configuration. You can NOT change the name servers from the Service Panel. If you need to change the name servers (to for example Cloudflare) you can request this by sending an email to [support@hypernode.com](mailto:support@hypernode.com) (from the email address that is linked to the account).

### A Records

The A record is used to link a domain name to an IP address. Usually there are multiple A records per domain name. In the example mentioned earlier under “The fields in a DNS table” there are three A records. One ensures that all visitors of domainname.nl are forwarded to the correct server and the other ensures that the domain name starting with www is also redirected to the server. A domain name always needs at least one A record to identify the web server. The third A record in the example is a wildcard record (`*.example.com`)

If no A (or CNAME) record exists for * .example.nl, subdomains will not be accessible and (provided no separate address has been created for it) [www.example.nl](http://www.domainname.nl) neither. Www.example.com is seen as a subdomain by DNS.

### AAAA Records

This is the A record for IPv6 addresses.

### MX Records

The MX records contain the host names of the mail server(s). In addition to the hostname, you can assign a priority to each MX record. For example, you can give your own mail servers a higher priority (a lower number) than our smtp2.byte.nl server. This means that smtp2.byte.nl is only used as a mail server when your own servers are not available. We also call this "fallback server". Also make sure that you do not give every MX record a priority of 10, otherwise our server will not be able to determine which record is about the primary mail server. These are the MX records of the Hypernode mail servers:

|             |          |               |          |
| ----------- | -------- | ------------- | -------- |
| **Name**    | **Type** | **Value**     | **Prio** |
| example.com | MX       | smtp1.byte.nl | 10       |
| example.com | MX       | smtp2.byte.nl | 20       |

Always use your primary domain for your MX records. An MX record with the Name on “mail.example.nl” will only work for …@mail.example.nl addresses.

### CNAME Records

With a CNAME record you can make a reference for a hostname to another hostname.

|                                           |          |                      |          |
| ----------------------------------------- | -------- | -------------------- | -------- |
| **Name**                                  | **Type** | **Value**            | **Prio** |
| [www.example.com](http://www.example.com) | CNAME    | example.hypernode.io | -        |

An advantage of using a CNAME is that if the IP address of the web server changes you won't need to change the record for the www domain.

### TXT Records

TXT records are flexible in use, you can store all kinds of information in a TXT record. For example, Google uses it for identification if you want to link a Google Apps account to your domain name. Google will then ask you to create a TXT record with a code in it that verifies your identity.

### SRV records

SRV (Service) records are used by some programs or devices to provide automatic settings. Certain IP telephones, for example, can easily be connected or reached with this. An SRV record has a specific format: <service>. <protocol> .example.org, and a specific value: “<priority> <weight> <port> <destination address>”. If you want to create an SRV record, you will receive the name of the service and the protocol of the program or device that can use SRV records. You can find this in the manual or on the website of your product. For example: Your domain name is example.com and you must create “\_sip.\_tcp.example.com” with the following value: “10 60 5060 bigbox.example.com”. You enter “\_sip.\_tcp” as the name, “60 5060 bigbox.example.com” as the value and “10” as the Priority.

### SOA Records

An SOA record is mainly used for the internal communication of different DNS servers and never needs to be changed.

### SPF Records

With an SPF record you can define which mail servers are allowed to send email for that particular domain (and prevent spam from being sent from your domain). You can find more information about SPF records and how to use them for Hypernode [here](how-to-set-up-your-spf-records-for-hypernode.md).

## DNS Caching

DNS Caching means that the content of a DNS record is stored on a server between your computer and the authoritative name server. Some providers store this data longer than specified in the TTL, so it can take up to a day for the changes to your DNS record to take effect everywhere. This is something to keep in mind when changing DNS settings. There is very little you can do about it that the whole world does not immediately see your new site (most of it), but as a developer it is of course annoying. Fortunately, there is a (local) solution, namely the hosts file. This is a file where you can enter hostnames and IP addresses yourself. This way you can link a domain name to an IP address so that when you visit this domain name, the DNS server is no longer consulted and you are always referred to the same IP address.Please see[this article](../../best-practices/testing/how-to-test-your-website-by-changing-your-hosts-file.md) for more information about the host file.

### DKIM and DMARC

DKIM and DMARC are techniques that use a combination of private and public keys to indicate who the sender is. The public keys can be added via the Service Panel as a TXT record in the DNS editor. The private key that is injected into the header of an email can be added using your own PHP code. This is a very complex technique that requires a lot of knowledge. Unfortunately, we cannot help with generating the keys and / or adding the private key in the code of your website / webshop / email client. If you experience problems with setting the TXT record, it is best to send us an email. Please include the full public key so that we can determine what is going wrong.
