<!-- source: https://support.hypernode.com/en/services/domains/how-to-transfer-your-domain-to-hypernode/ -->

# How to Transfer Your Domain to Hypernode for Service Panel Users

**Please note that this only applies to Service Panel users who log in via service.byte.nl. If you use the Control Panel (my.hypernode.com), you can use [this article](https://support.hypernode.com/en/services/domains/how-to-use-domains-in-the-control-panel#Transfer-an-Existing-Domain-to-Hypernode) to transfer your domain to Hypernode.**

You can transfer your domain name to Hypernode easily and quickly in a few steps. We explain each step in this article.

## Step 1 Order a Presence Package

Only customers who have access to our Service Panel can order a Presence package and transfer their domain to Hypernode. You can find instructions on how to order in this article: [How to order a Domain/Presence plan](https://support.hypernode.com/en/getting-started/how-to-order/how-to-order-a-domain-presence-plan)

## Step 2 Check Your DNS and Email Settings

Before you transfer your domain to Hypernode you should configure your DNS. If you use external mail solutions, it is certainly advisable to set the MX records for example. If you want to use Hypernode's email services, make sure that you have created email addresses and mailboxes.

### Check Your DNS for AAAA-records

We strongly advise you to delete any AAAA-record from your DNS before transferring your domain to Hypernode. At the moment, the Hypernode platform **does not** support the use of IPv6 addresses. Because IPv6 is not supported, the use of an AAAA-record in your DNS will actually prevent [Let's Encrypt](https://support.hypernode.com/en/hypernode/ssl/how-to-use-let-s-encrypt-on-hypernode) from validating your request, which will cause your site to be unreachable over HTTPS.

Another downside is because IPv6 connectivity is not available, the use of an AAAA-record in your DNS will prevent your site from being accessible to certain visitors.

## Step 3 Prepare for the Extension-Specific Procedure

Not every extension has the same procedure, some transfers need an authorization code while others need an email validation or a fax form.

The following extensions are transferred by authorization code:

**.NL | .BE | .DE | .EU | .AT | .SE | .GR | .CH | .FR | .RU | .IT | all gTLD's (generic Top Level Domain), these are domainextension that aren't associated with a country, like .COM, .NET, .ORG en .SHOP.**

The authorization code can be provided by your current provider.

## Step 4 Transfer Your Domain

Depending on the specific procedure you can initiate your domain transfer via the Service Panel. The transfer for a .NL extension is processed immediately but for the other extensions the following situation applicable.

After entering the correct authorization code, the transfer is requested. The registrar where your domain name is registered is then asked to confirm the transfer. The registrar has 5 days to approve or reject the move.

- If the transfer is approved within 5 days, the transfer is processed immediately.
- If the transfer is rejected within 5 days, the transfer will be rejected.
- If the registrar takes no action within 5 days, the transfer will take place automatically after 5 days.

Once your domain name has been moved, all your visitors will be redirected to the Byte nameservers within 24 hours. Browsers cache the IP address of your website for 24 hours. This is called 24 hour DNS cache. After the 24 hours all browsers have flushed their cache and all visitors will be redirected to Hypernode. You can prevent this by adjusting the DNS at the old provider and changing the name servers or A-records to us.

If you want to transfer a different extension than mentioned before, please check our offer: <https://www.byte.nl/domeinnaam/>

## Step 5 Link Your Domain to Your Hypernode

When you link your domain to your Hypernode via the Service Panel, we manage the link between your domain and your Hypernode.

Basically, your Hypernode has a dedicated IP address, but with a Cloud provider change this IP address changes. When we manage your DNS, we change the IP address for you so that you don't have to set your alarm clock at night.

### Link Your Domain to Your Hypernode

By following the steps below you can link your domain to your Hypernode:

- Log in to the Byte [Service Panel](https://service.byte.nl)
- Select your Hypernode plan
- Click on the Hypernode tab
- Click “SSL & DNS”
- Select your domain name and click “Koppel domeinnaam aan deze Hypernode”
- Confirm your action by pressing “OK”

When you link your domain to your Hypernode your DNS records for this domain will be updated.

We store the previous records as a TXT record with the name \___backup__ so when you unlink the domain from your node, we will be able to restore the previous records.

### Unlink Your Domain From Your Hypernode

To unlink your domain from your Hypernode you can use the same menu: Select the domain from the list and choose “Ontkoppel domeinnaam van deze Hypernode”

This will restore the previous records if the TXT record with the name __backup__ is still present.
