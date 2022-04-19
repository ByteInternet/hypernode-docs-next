<!-- source: https://support.hypernode.com/en/services/domains/how-to-use-domains-in-the-control-panel/ -->
# How to Use Domains in the Control Panel

**Please note that this article only applies to Control Panel customers that log in via my.hypernode.com.**

There are three different ways to use domains in the Control Panel.


Registering a New Domain
------------------------

To register a new domain, follow these steps:

1. Log in to the Hypernode Control Panel.
2. Select domains from the sidebar on the left.
3. Click on the orange **Order domain** button on the right.
![](_res/RF4b1aQPQipsvKWQ5Jyi7YiC7nhGWKQHyg.png)
4. Enter the domain you want to add to your account and click **Check domain**.
5. If the domain is available, you'll see an **Order domain** button.
6. Choose a Hypernode to link the domain to.
We will create an A record for example.com and a CNAME record for [www.example.com](http://www.example.com). If a domain is linked to a Hypernode, it’s no longer possible to manually change the apex records that point to your Hypernode.
**Please note:** the owner of the Hypernode is also the owner of the domain plan, which means they pay for the domain and can cancel the plan.
7. Next choose a domain holder. You can either pick an existing domain holder or add a new one. The domain holder is the legal owner of the domain name. Only they can initiate a transfer or reinstate a quarantined domain, so please make sure you pick the right holder.
8. Fill in the TLD information.
9. Check if everything is correct and place your order.

Transfer an Existing Domain to Hypernode
----------------------------------------

To transfer an existing domain, follow these steps:

1. Log in to the Hypernode Control Panel.
2. Select domains from the sidebar on the left.
3. Click on the orange **Order domain** button on the right.
4. Enter the domain you want to add to your account and click **Check domain**.
![](_res/FlDmwwbqiRXdz5gltG0ewBcoxc-NMLr35g.png)
5. To transfer the domain, click on the **Transfer to Hypernode** button.
6. Choose a Hypernode to link the domain to.
We will create an A record for example.com and a CNAME record for [www.example.com](http://www.example.com). If a domain is linked to a Hypernode, it’s no longer possible to manually change the apex records that point to your Hypernode.
**Please note:**the owner of the Hypernode is also the owner of the domain plan, which means they pay for the domain and can cancel the plan.
7. Next choose a domain holder. You can either pick an existing domain holder or add a new one. The domain holder is the legal owner of the domain name. Only they can initiate a transfer or reinstate a quarantined domain, so please make sure you pick the right holder.
8. Check if everything is correct and place your order.
9. At this point, your domain has not been transferred yet. Before you transfer your domain to Hypernode you should configure your DNS. If you use external mail solutions, it is certainly advisable to set the MX records for example. We also strongly advise you to delete any AAAA-record from your DNS before transferring your domain to Hypernode. At the moment, the Hypernode platform does not support the use of IPv6 addresses.
10. To initiate the transfer, enter your authorization code in the Control Panel. Please note: domain transfers can take a few days to complete, depending on the domain extension.

Using Our DNS Only Service
--------------------------

You can also use our DNS only plan. This means you can host your domain externally and only change the domain's nameservers to our nameservers.
Follow the steps below:

1. Log in to the Hypernode Control Panel.
2. Select domains from the sidebar on the left.
3. Click on the orange **Order domain** button on the right.
4. Enter the domain you want to add to your account and click **Check domain**.
5. Press **DNS only**.
6. Choose a Hypernode to link the domain to.
We will create an A record for example.com and a CNAME record for [www.example.com](http://www.example.com). If a domain is linked to a Hypernode, it’s no longer possible to manually change the apex records that point to your Hypernode. Please note: the owner of the Hypernode is also the owner of the domain, which means they pay for the domain.
7. Check if everything is correct and place your order.
8. Go to the DNS Manager and add, edit or delete records as needed:
![](_res/mHz-v7hbGSLEdArIOUUsYHCp7ASiuO3Fjw.png)
9. Assign our nameservers (**nsa.byte.nl**, **nsb.byte.nl**, **nsc.byte.nl**) to your domain name through your domain registrar. The DNS records set in the Control Panel will not be active until after you've updated your nameservers.
