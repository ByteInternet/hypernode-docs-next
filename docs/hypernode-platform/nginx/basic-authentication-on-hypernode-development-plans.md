---
myst:
  html_meta:
    description: 'Development Hypernodes are configured to offer a Basic Authentication
      challenge to all visitors. Read everything about this basic Authentication. '
    title: Enable basic authentication on Hypernode development plans
redirect_from:
  - /en/hypernode/nginx/basic-authentication-on-hypernode-development-plans/
  - /knowledgebase/basic-authentication-on-development-plans/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/basic-authentication-on-hypernode-development-plans/ -->

# Basic Authentication on Hypernode Development Plans

Development Hypernodes are configured to offer a Basic Authentication challenge to all visitors. These plans are meant to develop a webshop, to run all the tests you can think of, and to give your customer (the merchant) access during development. Keep in mind though, these development plans cannot be used to go live with a shop.

## Usermanagement

When using Basic Authentication, visitors to the website will have to enter a username and password, before being able to access the site. This is a separate account from any website specific accounts, and in most browsers are displayed as a separate popup.

### Default Username and Password

The default credentials for development nodes are:

- Username: dev
- Password: dev

We advise you to change the default username and password as soon as possible.

### Managing Users and Passwords

Users are stored in a ‘htpasswd’ file, located at `/data/web/nginx/htpasswd-development`. This file must exist and a valid username and password must be defined within this file in order to be able to login. This file can be managed using the `htpasswd` command, through the shell.

To add users, or change an existing users’ password, use the command: `htpasswd /data/web/nginx/htpasswd-development username`.

To remove a users, use the command: `htpasswd -D /data/web/nginx/htpasswd-development username`

## Whitelisting

If you need to connect your development node to external services, API’s, and tooling that do not support basic authentication, it’s possible to whitelist specific IP addresses, user agents, or request paths. Your Hypernode comes preconfigured with a whitelist file that allows you to easily configure your basic auth whitelist, in the file`/data/web/nginx/whitelist-development-exception.conf`

If your Development node lacks this file, or if your whitelist configuration only contains an IP whitelist, you can find a clean version of this file on [our Github](https://gist.github.com/hn-support/3d0ec225e7fd49e6996377e48996f57c#file-whitelist-development-exception-conf). This file also contains examples on how to use the various whitelists. Please note that this snipped was made to work if you use all three options, as they 'chain' on to each other.

### Whitelist an IP or IP range

To whitelist an IP address from basic authentication, you can add it to the geo statement in the whitelist file. You may also use an IP range, in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). Please note you cannot use hostnames in the whitelist.

To find out the IP's that need to be whitelisted, please contact the external service provider, or [check your access logs](../../troubleshooting/performance/general-troubleshooting.md) to see what IP's are accessing the website.

### Whitelist a User Agent

To whitelist a specific user agent you can add it to the User Agent whitelist map in the whitelist file. We suggest whitelisting a specific term, such as the bot name, or the domainname used in the the user agent, using a regex pattern.

### Whitelist an URL

To whitelist a specific URL you can add it to the url whitelist map in the whitelist file. Please note that the whitelist is based on the entire URL, including any arguments. As such, we advise using a regex pattern when whitelisting.

## Disable the basic authentication

To disable the basic authentication on our development plans add the following line in the **Nginx** file **whitelist-development-exception.conf**:

```nginx
# You can make certain IP addresses exempt here from the development
# basic auth. Beware though, that google and bing bots will always
# remain blocked on development nodes!

geo $development_exceptions {
    default "Development restricted area";
    # 1.2.3.4/32 "off"; # disables basic auth for 1.2.3.4/32
    0.0.0.0/0 "off"; # Everything is allowed.
}
```

Please note that Google and Bing are still blocked when everyone else is allowed.

## Troubleshooting

- Google Pagespeed analysis uses the Google bot user agent and can therefore not be used on development nodes.
- In some cases, particularly if you have not yet enabled [Hypernode Managed Vhosts](../../hypernode-platform/nginx/hypernode-managed-vhosts.md), it’s possible the Basic Authentication blocks the Let’s Encrypt validation server. If you wish to make use of Let’s Encrypt on your development Hypernode, you should add the ‘letsencrypt’ user agent to the whitelist file.
