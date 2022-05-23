<!-- source: https://support.hypernode.com/en/hypernode/dns/how-to-manage-your-dns-settings-for-hypernode/ -->
# How to Manage your DNS Settings for Hypernode

Hypernode is a cloud-based hosting service. In case of an up- or downgrade, your shop can transparently be moved to other hardware with different specs. When upgrading or downgrading a Hypernode plan, we first create a second node, migrate your shop to this new node and then remove the old one.

Thanks to Hypernode’s very cool **Dedicated IP**feature the IP-address of your Hypernode does not (!) change when you change a Hypernode plan. However, there are 3 exceptions to take into account.

**This article explains 3 ways to handle your DNS. Please decide for yourself what would be the best option for your specific situation.**


Dedicated IP on Hypernode – 3 exceptions
----------------------------------------

There are 3 exceptions in where you cannot benefit from a dedicated IP and which may have impact on how your would like to manage your DNS:

1. A change of cloud provider – also when switching between Falcon (formerly known as Professional), Pelican and Eagle (Formerly known as Excellence) plans – will trigger an IP change
2. If you request your node to be booted in a different region (data centre) the IP address will change as well.
3. In extreme emergency situations (like fire or longtime power outages) we might need to migrate your Hypernode to another data centre. Luckily these chances are very low.

If you're likely to switch between Falcon and Eagle plans in the future, we recommend you to move your domain(s) to Hypernode so we can handle the DNS of your domains to avoid downtime. Or, use the DNS settings as explained below (by using CNAME and not A record).

Three ways to handle your DNS
-----------------------------

There are 3 ways to handle your DNS. Only customers who have access to a Service Panel can choose option 1.

1. Move your domain(s) to Hypernode and let Hypernode manage the DNS (Dutch customers only)
2. Manage an external DNS by pointing your domain(s) to Hypernode by using CNAME and not A record
3. Manage an external DNS by pointing your domain(s) to the IP address of Hypernode via A record

Good to know:

*Option 1 and 2 will prevent DNS downtime.*

*Option 2 has an important disadvantage: your cannot use SSL in combination with your naked domain. People that directly visit <https://yourdomain.com/>, will get a certificate warning from the browser.*

*Option 3 is the best option in case of an external DNS and you want to make use of <https://yourdomain.com/>, but you will encounter DNS downtime if the IP address of your Hypernode changes.*

As there are situations you cannot benefit from a dedicated IP on Hypernode, please decide for yourself what is the best way to handle DNS. Our recommendation is always to move your domains to Hypernode if possible.

Below you will find a detailed explanation of option 1 and 2.

Service Panel users only: let us manage your DNS
------------------------------------------------

If you have your domain at Hypernode, we can manage your DNS. We will update the DNS records when the IP of your Hypernode changes. The steps:

1. [Log in to your Service Panel](https://auth.byte.nl/)with your customer number and password and select your Hypernode.
2. Navigate to ‘SSL & DNS instellingen’ under tab ‘Instellingen’. Here, you will see an overview of all available domains.
3. Search for the domain you would like to link to your Hypernode
4. Go to the column ‘DNS Beheren’, click on “Beschikbaar” and select ‘Koppel domeinnaam aan deze Hypernode’.

Whenever you want to unlink a domain, simply choose ‘Ontkoppel domeinnaam van deze Hypernode’.

When linking a domain to your Hypernode, we will immediately change the DNS records of the domain. Plan this moment carefully when migrating to Hypernode, and make sure content on the original location is no longer used.

### What happens at the background?

We will create an A record for domain.com and a CNAME record for [www.domain.com](http://www.domain.com). Other A- and CNAME records for both domain.com and [www.domain.com](http://www.domain.com) will be removed. Records for subdomains are not touched, so it’s still possible (and perfectly reasonable) to have a subdomain for your blog on blog.domain.com.

If a domain is linked to a Hypernode, it’s no longer possible to manually change the apex records that points to your Hypernode. We will make a backup of the record we adjust. These show up in the DNS admin as TXT records for __backup__.domain.com. If you unlink your Hypernode, we will put the backup records back in place. You can delete or change them if you choose to do so.

****Please note**:**

* By letting us manage your DNS, you will also be able to use your apex domain
* Preferably the TTL for the DNS records is reasonably low to make the transition to Hypernode quick. Check this beforehand.

Manage your own DNS: CNAME for the www record
---------------------------------------------

Configuration:

* Have a CNAME for your www-domain + an A Record that directs to the dedicated IP address of your Hypernode
* Have a CNAME for your www-domain + an A record for your apex (also called naked) domain pointing to a redirector that redirects to the www-domain (our wwwizers)

These examples assume you have a site called yourdomain.com and a Hypernode called yourd01.hypernode.io.

The recommended way to configure your DNS is to create a CNAME record in your DNS configuration, pointing to Hypernode:

```
www.yourdomain.com      CNAME       yourd01.hypernode.io
```
This means that [www.yourdomain.com](http://www.yourdomain.com) will point to wherever yourd01.hypernode.io points, and we will make sure that that always points to the correct IP address.

****Please note**:** You can also configure your wildcard (*) domain name to Hypernode.

```
*.yourdomain.com      CNAME       yourd01.hypernode.io
```
Managing your own DNS: A record for your naked (or apex) domain
---------------------------------------------------------------

Problems arise when people visit your naked (also called apex) domain name: yourdomain.com, without the ‘www.’-prefix. It is not possible to create a CNAME record for your apex domain.

The preferred way to redirect your apex (or naked) domain, when the domain is not hosted on the Byte name servers, is to use the direct IP address of your Hypernode. You can find your IP with the “ping yourname.hypernode.io” command.

Some DNS providers, like [DNSimple](https://dnsimple.com/) or [DNS Made Easy](http://www.dnsmadeeasy.com/) have the possibility to create ALIAS or ANAME pseudo-records. These behave like CNAME records for apex domains. Unfortunately they are not wide-spread yet, so the chances are your provider doesn’t support it.

Another solution is to redirect traffic for the apex domain yourdomain.com to its www-counterpart [www.yourdomain.com](http://www.yourdomain.com). You can use our free wwwizer service for this. Just configure the following A-records for your apex domain and they will redirect all traffic for you.

```
# Add both for redundancy!
yourdomain.com A 46.21.232.141
yourdomain.com A 46.21.233.172
```
**Please note**: Note that if you make use of the wwwizer redirect servers, people that visit <https://yourdomain.com> directly will get an error message, either indicating that there is no https available or a plain connection refused error. The wwwizers actually work as a forwarding service to the direct IP address of the Hypernode. This way we can manage any IP changes for you. That is the advantage, the disadvantage is that these records do not cooperate with SSL and that therefore the certificate does not work properly on the domain name without the [www](http://www).

### Let's Encrypt and Wwwizers

Also important to note is that [Let's Encrypt](https://support.hypernode.com/en/hypernode/ssl/how-to-use-let-s-encrypt-on-hypernode) does not work when you make use of the wwwizers, as the Let's Encrypt validation cannot be completed and will return an error. The solution is to purchase a paid SSL certificate via us or to use the direct IP of your Hypernode instead.

Don’t fancy these solutions? Migrate your domain to Hypernode and let us manage your DNS.

DNS and Hypernode Managed Vhosts
--------------------------------

The Hypernode Managed Vhosts (HMV) system is currently enabled by default on all new booted Hypernodes (all Hypernodes created after 01-05-2020).

Check if you have HMV enabled by running this command: 

`hypernode-systemctl settings managed_vhosts_enabled`

If so, it will give the following output:

`managed_vhosts_enabled is set to value True`

If this is not enabled, skip the part below.

Due to this configuration it is required to add a new vhost for every domain you want to link to your Hypernode. So you need to configure your DNS correctly and add a new vhost for the domain.

To add a new vhost, for example the domain name `www.example.com`, to your configuration, you can simply run the command `hypernode-manage-vhosts www.example.com`. This will create a new vhost configuration in `/data/web/nginx/www.example.com/`, using the Magento 2 template.

Please note that defining the vhosts '[www.example.com](http://www.example.com)', does not automatically add 'example.com' as a vhost. You will have to manually define a vhost for this. Since most people simply want their 'example.com' to redirect to '[www.example.com](http://www.example.com)', you can simply use the `--type wwwizer` argument to set this up. This will configure the vhost to redirect all traffic to the www-version of the domain.

Read more about Hypernode Managed Vhosts in [this article](https://support.hypernode.com/en/hypernode/nginx/hypernode-managed-vhosts).

Redirects in Nginx
------------------

If you want to force a redirect to either the [www](http://www). or the non-[www](http://www). domain, you can use a redirect.

You can read how this works [in this article](https://support.hypernode.com/knowledgebase/redirect-from-or-to-www/).

Shop on a subdomain?
--------------------

If you host your shop on a subdomain (for example shop.yourdomain.com), and you don’t want to be available on [www.shop.yourdomain.com](http://www.shop.yourdomain.com), you can forget all about the wwwizer service, and there’s no need to add the two IP addresses in your A records as explained above. Simply create a CNAME-record pointing to your Hypernode, and it will work:

```
shop.yourdomain.com      CNAME       yourd01.hypernode.io
```
Use the Store Front Status check in Magereport Premium
------------------------------------------------------

If you visit [Magereport Premium](https://www.magereport.com/) with your Hypernode plan, you can verify whether your domains are redirected to your Hypernode.

It will tell you if they’re live (DNS is redirected to Hypernode) and if it’s configured correctly. In case, the storefront tool tells you that the DNS is misconfigured it will present an example of how you should configure the DNS correctly.
