---
myst:
  html_meta:
    description: Developers use the Qualys SSL labs server test to validate the SSL
      settings on their node. Learn how to get an A+ rating for your Hypernode SSL
      configuration.
    title: How to Upgrade Your SSL Settings to an A+? | Hypernode
redirect_from:
  - /en/hypernode/ssl/how-to-upgrade-your-ssl-settings-to-an-a-plus/
---

<!-- source: https://support.hypernode.com/en/hypernode/ssl/how-to-upgrade-your-ssl-settings-to-an-a-plus/ -->

# How to Upgrade Your SSL Settings to an A+

Many developers use the [Qualys SSL labs server test](https://www.ssllabs.com/ssltest/) to validate the SSL settings on their Hypernode. This article explains how to get an A+ rating for your Hypernode SSL configuration.

## SSL on Hypernode Background

There are multiple ways of configuring SSL on Hypernode, you can use [Let’s Encrypt](../ssl/how-to-use-lets-encrypt-on-hypernode.md) or [order an SSL certificate](../ssl/how-to-use-ssl-certificates-on-your-hypernode-when-ordered-via-hypernode-com.md).

All these methods of enabling SSL on your Hypernode, share the same configuration templates that we use for creating an Nginx configuration.

This way, we can ensure you always use the recommended and secure settings for SSL on your node. This template is based on the [Mozilla recommended configuration](https://wiki.mozilla.org/Security/Server_Side_TLS#Recommended_configurations), of which we use the [Intermediate Compatibility Settings](https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility). This configuration is up to date, but not too restricted, leaving the Hypernode accessible to all legacy clients that are protected against the most critical vulnerabilities found in OpenSSL in the last period of time. These critical issues have been fixed in newer versions of the software used to establish a secure connection.

This does imply however, that some browsers which are not protected against these serious issues found in older SSL versions, will not be able to connect to the Hypernode.

Clients that cannot connect over HTTPS to a website running on Hypernode, are recommended to upgrade to newer, more secure versions of their browser or operating system. This includes many browsers running on Windows XP and some very old Android browsers.

Using the [Qualys SSL Labs server test](https://www.ssllabs.com/ssltest/), in the *Handshake Simulation* table, you can check which clients are supported and which are not. This is mostly determined by the browser supporting [SNI (Server name Indication)](https://en.wikipedia.org/wiki/Server_Name_Indication) and being able to use the recommended modern TLS versions and ciphers.

### Switch to Modern Compatibility Settings

It is possible to switch to the [Modern Compatibility Settings](https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility) on your Hypernode. The Mozilla Modern configuration is useful for sites that don’t need backward compatibility, and provides a higher level of security. It is also required by various payment providers, and for accepting credit card payments. If you wish to switch between Intermediate and Modern settings, you can do so using the `hypernode-systemctl settings modern_ssl_config_enabled` command, using the `--value True` or `--value False` arguments.

#### Mozilla Modern Configuration and Hypernode Managed Vhosts

The Hypernode Managed Vhosts (HMV) system is currently enabled by default on all new booted Hypernodes (booted after 01-05-2020). Read more about HMV [here](../nginx/hypernode-managed-vhosts.md).

When you have different vhosts configured, you also need to enable the SSL config **per vhost**. You do this by running this command:

```nginx
hypernode-manage-vhosts example.com --ssl-config modern
```

## Get an A+ Rating

Most of the settings to get a high rating are already in place. We choose and maintain the available ciphers, diffie hellman params and the settings for your Nginx instance to get an **A** rating in the test. By adding some additional configuration, you can easily upgrade this rating to an **A+**.

Adding security headers

One of the recommended settings in your SSL setup, is adding an `HSTS` header. This header instructs browsers to only use HTTPS instead of HTTP on your website. This way your cookies are more secure and your browser is protected against downgrade attacks.

Add a header by creating a `server.hsts` configuration file in /data/web/nginx with the following content:

```nginx
add_header Strict-Transport-Security "max-age=31536000;" always;
```

If all subdomains use SSL too, this is even better:

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

This will make sure all subdomains will redirect to SSL when a HTTP connection is made.

Verifying SSL settings and headers is easily done using curl:

```nginx
curl -v https://example.com/ 2>&1 > /dev/null
```

This will redirect all html output to `/dev/null` and only shows the headers and SSL connection information of the request.

Fix Mixed Content Warnings

Fixed content warnings appear when static content (Javascript, CSS, images etc) are loaded over both HTTP and HTTPS.
If the site is served over HTTPS and static content is requested over HTTP, an error or warning will appear in your browser console.

Google has written some incredible instructions on [how to fix and prevent mixed content warnings](https://developers.google.com/web/fundamentals/security/prevent-mixed-content/fixing-mixed-content) that can help you circumvent issues regarding mixed content.

If you experience many mixed content warnings after [changing your base-URLs in Magento](../../ecommerce-applications/magento-2/how-to-change-your-magento-2-base-urls.md), clear your cache to ensure all cached URLs are replaced with the changed URL settings.

For more experienced CLI users, searching with grep is the easiest way to solve these warnings:

```bash
grep -RE '<code>http://(www\.)?example\.com</code>' /data/web/public
```

Or when you are on Magento 2:

```bash
grep -RE '<code>http://(www\.)?example\.com</code>' /data/web/public /data/web/magento2
```

## Redirect all traffic from HTTP to HTTPS

To redirect all traffic to HTTPS, you can easily add some configuration in Nginx.
To do so, use [the instructions in our article about redirecting all traffic to HTTPS](../nginx/how-to-configure-your-shop-to-only-use-https.md).

If not all of your domains are HTTPS enabled (which is recommended), you can [selectively redirect specific domains to HTTPS, using a mapping](../nginx/how-to-redirect-from-or-to-www.md).

## Additional Information and Troubleshooting

Additional resources

For more information, you can check the following resources:

- [Qualys SSL Labs SSL tester documentation](https://www.ssllabs.com/projects/documentation/index.html)
- [Mozilla recommended SSL settings](https://wiki.mozilla.org/Security/Server_Side_TLS)
- [Google Mixed Content](https://developers.google.com/web/fundamentals/security/prevent-mixed-content/what-is-mixed-content)

Troubleshooting

If the Qualys SSL labs server test is not working on your Hypernode, check the following possibilities:

- Make sure you have ordered or implemented an SSL certificate on your Hypernode
- Check the [known issues page at Qualys](https://community.qualys.com/docs/DOC-4865)
- Check if the Qualys [user agent](../nginx/how-to-block-user-agents-and-referrer-sites.md) or [IP address](../nginx/how-to-block-allow-ip-addresses-in-nginx.md) is blocked
- Check if [the Qualys user agent or IP address is rate limited](../nginx/how-to-resolve-rate-limited-requests-429-too-many-requests.md)
- Check if basic auth is enabled on your node. If this is the case, add a temporary user name and password to the password file and adjust the URL to scan to https://:@example.com (Do not forget to remove the user after the test)
