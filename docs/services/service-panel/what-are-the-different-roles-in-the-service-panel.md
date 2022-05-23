<!-- source: https://support.hypernode.com/en/hypernode/tools/what-are-the-different-roles-in-the-service-panel-and-what-is-the-difference-between-them/ -->
# What Are the Different Roles in the Service Panel

**Please note that this only applies to Service Panel users who log in via service.byte.nl.**

The Service Panel works with a central login, which enables users to easily manage multiple plans. There are three different roles which you can assign to different accounts. This way you can give your developer technical access to your plan, without them having access to stuff like invoices and billing.


Three Different Roles
---------------------

We work with different roles per plan. This is for legal reasons, but also to make it easier for you to give your developer access if you are not that technical yourself. The three different roles are explained below.

### Registrant (Owner) (R)

The Registrant is the legal owner of the domain name (if the domain is registered via Hypernode). The Registrant can log in to the Service Panel, but only has access to view the mailboxes and can adjust the email settings. As a Registrant you can create your own email addresses and boxes. However, you cannot manage the DNS of the domain name yourself. **This role only applies to Presence (Plus) plans, the Registrant is not the legal owner of a Hypernode.**

### Contractant (Financial Contact) (C)

The Contractant is the person who pays for the plan at Hypernode and therefore the person who receives the invoices. In addition to the same view and change rights in the Service Panel as the Registrant, the Contractant also has access to the settings for the domain name. In addition, the Contractant may determine who the **Technisch Beheerder** is. By default, the Contractant is also the Technisch Beheerder, unless indicated differently when ordering the plan. As a Contractant you can always withdraw the technical rights if necessary.

### Technisch Beheerder (Technical party) (T)

The Technisch Beheerder has access to all technical settings in the Service Panel. The Technisch Beheerder is the only one who can log in via SSH with their customer password. The **Contractant**is the only one who can assign this role to another account.

### Permissions per role

|  |  |  |  |
| --- | --- | --- | --- |
| **Permission** | **Registrant** | **Contractant** | **Technisch Beheerder** |
| Logging in to the Service Panel | ✓ | ✓ | ✓ |
| Configuring email | ✓ | ✓ | ✓ |
| Adjusting PHP version |  |  | ✓ |
| Assigning technical role |  | ✓ |  |
| Linking domains and SSL certificates to  Hypernodes |  |  | ✓ |
| Magereport Premium |  | ✓ | ✓ |
| Blacklisting bots |  |  | ✓ |
| Configuring DNS |  |  | ✓ |
| Transferring domain names |  | ✓ | ✓ |
| Cancelling plans |  | ✓ |  |
| Accessing SSH |  |  | ✓ |
| Up- or downgrading plans |  | ✓ |  |

Please note:

* One account can have multiple roles, e.g. the same account as Registrant and Contractant, but a different account as Technisch Beheerder.
* The Registrant cannot see who is listed as the Contractant and Technisch Beheerder.

How to Assign Roles
-------------------

You can assign roles via the Service Panel. Do you want to make someone else a Contractant and/or Registrant, but this person doesn't have an account yet? Create a new customer account through [this page](https://auth.byte.nl/account/register/?next=) (this is free of charge). You transfer customer roles by customer number. Below we explain how to change the roles:

### Assigning the Contractant and Registrant Role

You can only assign these roles to a user when you have the Contractant role.

1. After logging in to the Service Panel a list of plans will be shown. Click on the relevant plan and select **Administratief**and then **Contractant/Registrant wijzigen**.
2. Fill their account number in at Step 1 and select which roles you want to assign at Step 2. Tick the box for verification at step 3 and fill in your name. Then click **Wijziging starten**.
3. A confirmation email will be sent to the new Contractant or Registrant. They need to confirm this change, only then will this be applied.

**Please note:****if you cancelled your plan, but assign the Contractant role to another account, the cancellation will be undone.****It may be the case you already paid for the plan. For example, when the previous Contractant was the developer. However, upon transfer, a credit is added to the account for the remaining contract term of the old contract. Therefore, there is no question of a double payment or a double paid period.**

### Assigning the Technisch Beheerder Role

The Contractant is the only one who can retract the Technisch Beheer. The Technisch Beheerder can only resign their role back to the Contractant.

1. Log in to the Service Panel and click on the relevant plan. Click **Administratief**and then **Technisch Beheerder wijzigen**.
2. Enter the account number at **Beheerrechten overdragen**.
3. Select the plans this change applies to and click **Geef rechten**.

FAQ
---

### How Can Give My Developer SSH Access to My Hypernode?

You can make your developer Technisch Beheerder for the relevant plan as explained above. 

### I Have Multiple Accounts, Can I Merge These?

If you have plans under different accounts, you can transfer the plans to one account by changing the **Contractant** role. Unfortunately, there is no option to transfer all plans from one customer account to another customer account at once. You have to do this per plan. How to do this is explained above.
