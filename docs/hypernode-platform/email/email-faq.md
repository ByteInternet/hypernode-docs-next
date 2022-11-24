<!-- source: https://support.hypernode.com/en/hypernode/email/email-faq/ -->

# Email FAQ

If you purchase a Presence Plus plan via Hypernode, you can also create email boxes in the Service Panel. Because a Hypernode plan itself is hosting only, you always need a Presence Plus plan if you want to create mailboxes. With this plan you can both receive and send mail via the Hypernode mail servers. You can use the following protocols: POP, IMAP, and SMTP.

In this article, we explain how you can use email with Hypernode and share tips on how to avoid problems.

## How Can I Manage My Email Addresses via the Service Panel?

If you have chosen the Hypernode mail servers, you can create email addresses and boxes and change passwords via the Service Panel.

*Please note that you cannot create mailboxes with a Presence plan. If you want to create an email address with a Presence plan and want to forward this to an external address, then choose an existing mailbox or external email address such as your gmail or Hotmail address. If you need email hosting (incl. Mailboxes) but not web hosting, choose the Presence Plus plan.*

## How Can I Create a New Email Address?

1. Log in to the Service Panel with your customer number and password
1. Select your domain name
1. Go to the 'Instellingen' tab and click on the Email option
1. Click on the blue envelope under 'E-mail door Byte'
1. Enter a name in the input box under the heading 'Nieuw E-mailadres'
1. Choose  'nieuwe' in the box underneath 'Bezorg e-mail naar dit adres in een' op and press OK
1. Congratulations! You have created an email address
1. In the new screen you will see the details of your mailbox. You can still email this to one of your other mailboxes

More information can be found in the article How can I create a new email address

## Can I Forward Email to an Existing Address

When you have a Presence Plan (and not a Presence Plus) you cannot set up an email box, but you can set up an alias or forward to another address. So for example you can setup an info@ address for your domain and let emails that are addressed to that address be forwarder to for example your Gmail our Microsoft account.

1. Log in to the Service Panel with your customer number and password
1. Select your domain name
1. Go to the 'Instellingen' tab and click on the Email option
1. Click on the blue envelope under 'E-mail door Byte'
1. Enter a name in the input box under the heading 'Nieuw E-mailadres'
1. Then click 'Opslaan'
1. Check the email box (s) where the email should be sent and / or enter the email address where the email should be forwarded under 'Externe E-mail adressen'
1. Then click on the 'Opslaan' button

## Where Can I Find my Email Boxes and Addresses?

On the Service Panel, click the Domain Name for which you want to see this> Settings> Email. At the top you will find an overview of the number of mailboxes and email addresses you use and the maximum number that you can use.

## How Can I Change the Password for my Email Address?

### Log In to Your Account

To log in to your mail box, via your email client (for example Outlook or Thunderbird, etc.) or Hypernode's webmail, you need:

- Your mailbox name (in the form abcde000)
- Your email password

Your mailbox name and password are automatically generated when you create a [new account](#How-Can-I-Create-a-New-Email-Address?).

### Your Mailbox Name

Your username consists of the first five letters of your domain name, followed by a number ranging from 000 to 999. For example: The username banaa000 is created for the domain name banaan.nl.

### Create a New Password

On the Service Panel you can create a new email password for each mailbox in your account in your email settings. The password must contain at least 8 characters, including a number and a capital letter. You can choose a password that you can easily remember. You can change your email password on the Service Panel by following these steps:

1. Log in to the Service Panel.
1. Select the correct domain name from the domain name overview.
1. Go to the 'Instellingen' tab and click on the Email option.
1. You will now see a list of active email addresses and referrals. Here are the options to set up your account. Move the mouse over the icons to see what they stand for. With the key icon you can change your email password.
1. Then choose your own password of at least 8 characters, with at least one capital letter and one number.

Note: Remember your password well. It will not be emailed to you. Hypernode does not store passwords, so we cannot retrieve them for you. If you have lost your password, you must create a new password via the Service Panel.

### Quick New Mail Password Without Service Panel?

Do you remember your password, but would you like to change it? Then set a self-selected password for your mailbox via: <https://service.byte.nl/mail/>. Now take the following steps:

1. Enter the mailbox whose password you want to reset
1. Enter your current password.
1. Choose a new password
1. Repeat the new password
1. Click on create

## Setting Up Your Email Client / Application

If you have created an email address, the next step is how to receive and send the email for your mailbox. You can use the Webmail application (RoundCube) from Hypernode for this, but it is more common to set it up on a phone, tablet or in an email client (such as Outlook or Apple mail). Will you set up the email address on multiple devices or is the address used by several people? Then we recommend that you to set up the address as an IMAP account.

## How Can I Create a Catch-all Account?

You can also create a catch-all email address. A catch-all address is an email address that “receives” and forwards all emails that are sent to your domain name. Regardless of which characters precede the @ and your domain name. This also applies to emails that are sent to a non-existent address. Catch-all should actually be called: catch all that is left. This means that all email is received that does not belong in another email box or redirect.

If you use the Hypernode mailservers you can create a catch-all email address.

1. Go to the 'Instellingen' tab and then to the 'E-mail' button.
1. Create a catch-all email address (@ example.nl) underneath 'Nieuw e-mailadres' (geef een nieuw e-mailadres op)
1. Leave the first text field empty here.
1. Check the email box (s) where the e-mail should be sent and / or enter the email address where the email should be forwarded to under 'Externe E-mail adressen'
1. Then click on the 'Opslaan' button.

## Can I Set up an Autoresponder?

If you are temporarily absent and would like to inform your contacts, you can set up an autoresponder. You can specify for what timeframe you want to set up the autoresponder and which message the autoresponder should send to the recipient. For more information on how to set this up, see the page: [How to Enable an Autoresponder/ Out of Office for Your Email Address](https://support.hypernode.com/en/best-practices/email/how-to-enable-an-autoresponder-out-of-office-for-your-email-address)

## What is the difference between POP and IMAP?

POP (Post Office Protocol) is the most common protocol for retrieving email from a mail server. The difference with IMAP is that the email remains on the mail server. With POP you literally take the email from our mail server.

An advantage of IMAP is that the email remains on the server (until the user explicitly deletes it), making it possible to log in with an IMAP program from any location and view all email. Multiple clients have access to the same mailbox this way.

### Configure Byte IMAP server

Hypernode also offers (in addition to using the POP server) an IMAP server for incoming email. Every mail box at Hypernode can therefore be accessed via IMAP. IMAP is considerably more complex than POP and is therefore only intended for advanced users. In addition, Hypernode does not provide substantive support for the use of IMAP.

The server name of our IMAP mail server is: imap.byte.nl. You use port 143 to retrieve the email via IMAP. You use port 993 if you want to use IMAP over SSL.

### Configure Byte POP Server

The server name of our POP3 mailserver is"pop.byte.nl. You use port 110 to retrieve the email via POP.

## Which Settings Should I Use to Receive Email?

|                   |                    |          |
| ----------------- | ------------------ | -------- |
| **Server type**   | **Server address** | **Port** |
| POP               | pop.byte.nl        | 110      |
| Secure POP (TLS)  | pop.byte.nl        | 995      |
| IMAP              | imap.byte.nl       | 143      |
| Secure IMAP (TLS) | imap.byte.nl       | 993      |

Secure IMAP is the recommended and most secure method for receiving mail. When you use secure IMAP, email is retrieved over an encrypted connection.

## Which Settings Should I Use for Sending Email?

|                 |                    |            |
| --------------- | ------------------ | ---------- |
| **Server type** | **Server address** | **Port**   |
| SMTP Submission | SMTP.byte.nl       | 587        |
| SMTP            | SMTP.byte.nl       | 2525 of 25 |

We recommend that you always use port 587 for sending email. This port should also be automatically detected when setting up most email clients. If this does not work you can alternatively use port 2525. The default port (25) also works, but some ISPs block this port by default.

## Email Problems

When using email, unfortunately sometimes things can go wrong. If you are unable to find a solution, you can always contact us at support@hypernode.com. It is important that you include as much information in your email as possible.

### Mail Attachment Problems

It is possible that you cannot open certain email attachments in your email program. This is often due to the strict security of your email client. This protection blocks potentially harmful files that may contain viruses (for example, .BAT, .EXE, .VBS, .JS, and .PDF files) by default.

You can remove this protection in the settings of your email program or you can only allow a specific type of file to be opened in Windows. More information can also be found on [Wikipedia](http://en.wikipedia.org/wiki/Email_attachment).

### Allow Only Opening a Certain Type of File (in Windows).

A safer way than disabling all security in your email program is to only allow opening certain files, for example PDF. The following explains how to do this, but is recommended for users with a little more experience:

1. Right-click Start and then click Explore (Windows Explorer).
1. Click the Tools menu and choose the Folder Options option.
1. Click the File Types tab.
1. Find the “registered file type” or extension you want to edit and then select it.
1. Click the Advanced button.
1. Select open from the displayed list of actions and deselect the checkbox for “Confirm open after download”.

## Can I Use a Spam Filter via Hypernode?

At Hypernode we have a Virus Filter that we can use to block a lot of spam. Unfortunately it is not possible to block everything. We have therefore also added a spam filter option in our Service Panel that allows you to block some spam yourself. You can read more information about this in the article Spam Filter.

If you want to send a large mailing, keep in mind that you send it in small batches instead of in a large batch. There is a chance that if you do this, your email will be seen as spam. If you want to prevent this, read our support documentation.

## What Are the Limitations for email?

If you use our email service, please take into account the email limits when you send an email. Keep the following values:

**Total maximum email message size**

An email message can be up to 30 megabytes (mb) in size. On the web servers (when you send email from your website), a maximum email size of 10 MB applies to outgoing email.

**Maximum attachment size**

With a large attachment, a lot of data is added to be able to send it in the email. Therefore, sending an attachment that is already 30 MB in size would not work. Attachments larger than 20 MB can already cause problems.

**Maximum Zipfile size**

When sending a zip file as an attachment, the content is also scanned for size. Therefore, the contents of the zip file cannot exceed 30 MB.
