<!-- source: https://support.hypernode.com/en/best-practices/performance/how-to-use-blackfire-on-hypernode-to-find-performance-issues/ -->
# How to Use Blackfire on Hypernode to Find Performance Issues

All Hypernodes support Blackfire, an amazing tool to find performance bottlenecks in Magento. It is similar to New Relic, but much better suited for troubleshooting.

**Hypernode customers can get a 20% discount on the Premium plan. Contact**[**support@hypernode.com**](mailto:support@hypernode.com)**for a coupon code.**


How to Activate Blackfire
-------------------------

First, signup for an account. Start with the free version, which includes a wealth of information. In your account tab, you will see this:

![](_res/Sv3H3WBgTnIO3PGwgr5RgBCFRpcAvYrOlg.png)

Activate via the hypernode-systemctl tool
-----------------------------------------

You can activate Blackfire via the hypernode-systemctl tool. First you need to enable it, then add your Server ID and Server Token.

* `hypernode-systemctl settings blackfire_enabled`: boolean - Indicates whether Blackfire is enabled on your node.
* `hypernode-systemctl settings blackfire_server_id`: string - The Blackfire Service ID for your Blackfire setup.
* `hypernode-systemctl settings blackfire_server_token`: string - The Blackfire Server Token for your Blackfire setup.

Activate via Your Control Panel
-------------------------------

1. Log in on the [Control Panel](https://auth.hypernode.com)
2. Select your Hypernode (example.hypernode.io) and click **Details**
3. Hover over **Hypernodes**in the sidebar and select **Monitoring**
4. Click the **Blackfire** tab
5. Enter your Blackfire Server ID and Blackfire Server Token and click **Save**.
6. Now select **Enable Blackfire** to enable Blackfire

**Please take into account that it takes a most 10 minutes for our system to actually create the account. Grab a cup of coffee and relax!**

Activate via Your Service Panel
-------------------------------

1. Log in to your [Service Panel](https://auth.byte.nl/login/)
2. Select the Hypernode from the overview
3. Go to **Instellingen**and then **Blackfire**
4. Select **Enable**, enter your Service ID and Server Token
5. Save your input by clicking **Opslaan.**

****Please take into account that it takes a most 10 minutes for our system to actually create the account. Grab a cup of coffee and relax!****

How Is It Different From New Relic?
-----------------------------------

New Relic is an Application Performance Monitoring utility. It is made to track real traffic, and to provide alerts and a first level of insight to business managers and developers. Analyzing the performance of an application’s code requires to instrument the code, which generates an overhead.

The more precise data is gathered, the slowest the app gets.

Therefore, analyzing all of the traffic makes it impossible to get pin-point information on the code’s resources consumption.

Blackfire works in a very different manner, and is therefore very complementary. End users requests are not instrumented; only the requests triggered by the developer or tool requiring performance information are. Blackfire’s profiling technology thereby provides and unequaled code introspection, and enables developers to understand the behavior of their code and identify optimization possibilities very fast. Blackfire is usable in production, just like New Relic, but provides an even better value-add in development in staging, through the use of performance tests, which proactively validate the code, before any go-live.

For more information, check [the Blackfire documentation](https://blackfire.io/docs).

Using Blackfire With Varnish
----------------------------

If you want to use Varnish in combination with Blackfire, some additional configuration in your VCL is required.

This is quite an expert level change and requires enough experience with varnish to manually edit your VCL.

```
acl profile {
   "x.y.z.w";
}

sub vcl_recv {
  if (req.http.X-Blackfire-Query && client.ip ~ profile) {
    if (req.esi_level > 0) {
        # ESI request should not be included in the profile.
        # Instead you should profile them separately, each one
        # in their dedicated profile.
        # Removing the Blackfire header avoids to trigger the profiling.
        # Not returning let it go trough your usual workflow as a regular
        # ESI request without distinction.
        unset req.http.X-Blackfire-Query;
    } else {
        return (pass);
    }
  }
}
```
You can find the extended instructions in [the Blackfire documentation](https://blackfire.io/docs/reference-guide/configuration)
