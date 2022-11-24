<!-- source: https://support.hypernode.com/en/best-practices/email/how-to-use-dkim-domainkeys-identified-mail/ -->

# How to Use DKIM (DomainKeys Identified Mail)

**Please note that this only applies to Service Panel users who log in via service.byte.nl. This functionality isn't available in the Control Panel yet.**

Hypernode gives you the option to use DKIM (DomainKeys Identified Mail). DKIM is an email authentication technique that allows the receiver to check that an email was indeed sent and authorised by the owner of that domain. Are you using Hypernode mail? You can easily configure DKIM via the Service Panel.

## What is DKIM?

With DKIM, emails are more secure. This is necessary because the SMTP email protocol is quite old and poorly secured. It is very easy for malicious parties to fake a sender address. Anyone can send emails from any address without actually having access to an account. For example, it seems as if an email came from a reliable party, but it was actually sent by spammers or scammers who try to retrieve personal information (phishing emails).

By activating DKIM, the recipient of your email can check whether the email actually comes from you (the owner of the domain) and whether the content of the email has not been modified. For this you need: a public key (this is a TXT record in the DNS) and a private key (this is on the sending mail server). The sending mail server adds a the private containing a DKIM header to every email sent, think of it as a digital signature. The receiving mail server must check this header (signature) using the public key.

If the digital signature is correct, the recipient knows that the sender domain has been established and that the e-mail has not been modified in transit. After all, a malicious person does not have the private key. DKIM reduces the chance that emails you send are marked as SPAM (because of that digital signature).

If the digital signature is correct, the recipient knows that the sender domain has been established and that the email has not been modified in transit. After all, a spammer or hacker does not have the private key. DKIM reduces the chance that emails you send are marked as SPAM (because of that digital signature).

## How to Activate DKIM

### Option 1: Your Domain Is Hosted at Hypernode

If your domain is hosted at Hypernode, you can activate DKIM with the push of a button. Follow these steps to do so:

1. Log in to the [Service Panel](https://auth.byte.nl/login/?).
1. Select the domain for which you want to activate DKIM.
1. Go to the tab **Instellingen**and click **E-mail**.
1. Scroll down until you see the option to configure DKIM.
1. On the DKIM page, you can activate DKIM by clicking the **Activeer**button.

When you have activated DKIM, a TXT record will be added to your DNS. A public and private key will also be generated. You don't have to take any further steps.

Please note that due to DNS caching it can take up to 24 hours for a DNS change to be visible worldwide. This means it can take up to 24 hours before your emails are fully secure. This does not influence the functionality of your emails, you can still receive and send emails while the DNS is being updated.

### Option 2: Your Domain Is Hosted Elsewhere

When your domain is hosted elsewhere, Hypernode does not have access to the DNS records. This means you have to add the TXT record yourself. **Please note: this requires a Presence plan**. Follow the steps below:

1. Log in to the [Service Panel](https://auth.byte.nl/login/?).
1. Select the domain for which you want to activate DKIM.
1. Go to the tab **Instellingen**and click **E-mail**.
1. Scroll down until you see the option to configure DKIM.
1. On the DKIM page, you can activate DKIM by clicking the **Activeer**button.
1. A TXT record will be generated. Copy and paste this into the DNS of your domain.

A public and private key will be generated for your domain. Only after adding the TXT record to your external DNS will DKIM be activated. Please note that due to DNS caching it can take up to 24 hours for a DNS change to be visible worldwide. This means it can take up to 24 hours before your emails are fully secure. This does not influence the functionality of your emails, you can still receive and send emails while the DNS is being updated.

## How to Deactivate DKIM

You can deactivate DKIM by following these steps:

1. Log in to the [Service Panel](https://auth.byte.nl/login/?).
1. Select the domain for which you want to deactivate DKIM.
1. Go to the tab **Instellingen**and click **E-mail**.
1. Scroll down until you see the option to configure DKIM.
1. On the DKIM page, you can deactivate DKIM by clicking the **Deactiveer**button.

If your domain is hosted in Hypernode, the private and public key are immediately revoked and the TXT record is deleted from the DNS. If your domain is external, only the private and public key will be revoked and you have to delete the TXT record from the external DNS yourself. No worries if you forget to do this. Your email will function normally; the record no longer has a function.

## What Happens if You Activate DKIM After Deactivating?

If you decide to reactivate DKIM, the above process will be repeated. If your DNS is external and you have not yet deleted the old TXT record, you can leave it. If you have removed the TXT record after deactivating DKIM, do not forget to add this TXT record again to use DKIM.

Is your domain hosted at Hypernode and do we manage the DNS? Then you don't have to do anything. Our automation will take care of everything.
