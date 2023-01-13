---
myst:
  html_meta:
    description: Some Magento sections are interesting targets for hackers. This article
      explains how to protect your shop from malicious attacks.
    title: How to protect your Magento shop against brute force attacks?
redirect_from:
  - /en/best-practices/security/how-to-protect-magento-against-brute-force-attacks/
  - /knowledgebase/how-to-protect-your-magento-store-against-brute-force/
---

<!-- source: https://support.hypernode.com/en/best-practices/security/how-to-protect-magento-against-brute-force-attacks/ -->

# How to Protect Magento Against Brute Force Attacks

Magento comes standard with sections for administrative purposes, like `/admin` and `/downloader`. These sections are interesting targets for hackers. This article explains how to protect your shop from malicious attacks.

## Available check on MageReport.com

MageReport gives insight in the vulnerability of your shop by checking these URL’s:

```nginx
/index.phprss/catalog/notifystock/ (yes, without the slash)
/admin
/downloader
```

An error is raised, when an admin/downloader login screen is found, or a basic auth dialogue (on RSS).

## What is the problem?

Each Magento shop comes standard with several sections for administrative purposes (also called “back-end” or “admin panel”). These are by default located at `/admin`, `/downloader` and various `/rss` endpoints (such as `/rss/catalog/notifystock/`) and can be abused in several ways.

First, if these sections are at their default locations, hackers can easily find them and launch a brute-force attack. In such an attack, random passwords are tried automatically, until one succeeds. While it appears to be a cumbersome method, simple passwords like “admin123” or “qwerty” can be guessed within minutes.

On our platform, we see about **one million brute-force probes** per week.

Second, even if you have strong passwords (like “\*ks\$Sf@#571”) that cannot be guessed easily, these brute-force attacks might impose a problem. Valuable server capacity is wasted in handling these failed login attempts. In other words, your site may be slower while under attack.

Third, to exploit several known Magento vulnerabilities, a hacker would require the name of the admin panel. So it is best to make this secret.

## What do I do?

On Hypernode we have implemented adaptive filtering.

While this will block the majority of malicious probes, you are still recommended to implement the following best practices.

### 1. Change the name of the back-end panel

Magento 1: The default “admin” is defined in the file `app/etc/local.xml` under `admin → routers → adminhml → args → frontName`. Change it into something you can easily remember, but that is difficult to guess by others. So do not use “control” or “admin123” or “manage”.

Flush your cache in the back end through: System → Cache Management. Or run in SSH: `magerun cache:flush`

Magento 2: This step is not required, as Magento generates an obfuscated back-end name for you during installation.

### 2. Secure /downloader and /rss

Magento 1 uses the /downloader as a way to install programs via the Magento Connect Manager. This link is a standard Magento URL, making it an easy target for brute-force attacks. Although you will likely never use this folder, its presence is essential for installing (future) patches. So instead of renaming, we recommend to install IP access control (an “IP whitelist”).

NB. The /rss endpoints can be reached in various ways, also (for example) via `/index.phprss/catalog/notifystock`.

**Are you using Hypernode (or Nginx)?**

Create a file called `nginx/server.downloader` that contains:

```nginx
location /downloader/ {
  allow x.x.x.x;
  deny all;

  location ~ \.php$ {
    echo_exec @phpfpm;
  }
}
```

Replace x.x.x.x with the IP addresses you want to allow.

And do the same for `nginx/server.rss`:

```nginx
location ~ rss/(catalog|order)/(new|review|notifystock) {
    allow x.x.x.x;
    deny all;

    location ~ \.php$ {
        echo_exec @phpfpm;
    }
}
```

**N.B.** The above snippet doesn’t work for Magento 1 shops due to the counter measures we have taken for SUPEE 6285. In case you want to restrict access to the rss endpoints for a Magento 1 shop, then you need to explicitly define each endpoint as follows.

```nginx
# Endpoint '/rss/order/new' without trailing slash
location = /rss/order/new {
    allow x.x.x.x;
    deny all;

    echo_exec @phpfpm;
}

# Endpoint '/rss/order/new/' with trailing slash
location = /rss/order/new/ {
    allow x.x.x.x;
    deny all;

    echo_exec @phpfpm;
}

# Endpoint '/rss/order/review' without trailing slash
location = /rss/order/review {
    allow x.x.x.x;
    deny all;

    echo_exec @phpfpm;
}

etc...
```

**Do you use Apache?**

Modify the existing`downloader/.htaccess` file and add these lines to end:

```nginx
order deny,allow
deny from all
allow from x.x.x.x
```

Because the RSS endpoint is reachable under various locations, it is generally not possible to filter RSS when using Apache (without using mod_rewrite). It is recommended to upgrade to at least version 1.9.3 and disable RSS in the backend.

### 3. Install adaptive filtering

Hackers launching brute-force attacks against your shop are likely to use other malicious tactics as well. Therefore, it is recommended to block hack sources as soon as they are identified. This is called adaptive filtering or an Intrusion Prevention System (IPS). This step requires platform/server access so is generally done by your hosting provider. On Hypernode, we have got you covered: if we detect robot-like, repeated login attempts, the source will be blocked. Profit!

If you are on your own, you could use these measures (a subset of our own IPS).

First, install fail2ban. Add this snippet to `/etc/fail2ban/jail.local`:

```nginx
[hn-nginx-retry-ban]
# Only ban after multiple retries.
# Use this for "soft" bad behaviour.
port = http,https
filter = hn-nginx-retry-ban
logpath = /var/log/nginx/access.log
bantime = 7200
maxretry = 10
```

And this in `/etc/fail2ban/filter.d/hn-nginx-retry-ban.conf`:

```nginx
[Definition]
# Use this for "soft" bad behaviour, as the source will only be banned after multiple retries.
failregex = ^&lt;HOST&gt; .+"POST \S+wp-login.php
            ^&lt;HOST&gt; .+"(POST|GET) \S+/etc/passwd
            ^&lt;HOST&gt; .+"POST \S+(/downloader/|/downloader/index.php\?A=loggedin|/admin/index/|/admin/)\s
ignoreregex =
```

Disclaimer: these configuration snippets are provided “as is” and we do not guarantee that they will work for you.

### Amasty Improved Layered Navigation (Magento 1)

Do you have a Magento 1 shop and do you use the Amasty extension? You may be open to bruteforce attacks if you have a vulnerable version of the Improved Layered Navigation plugin installed. Try visiting the path `/amshopby/adminhtml_filter` (e.g. [www.example.com/amshopby/adminhtml_filter](http://www.example.com/amshopby/adminhtml_filter)) and check if you are redirected to your admin login page. If so, follow the instructions above to restrict access to this path.

## Need help?

We do not provide Magento consultancy ourselves, however we partnered with professional agencies that will be able to help you. Don’t hesitate to [contact one of these agencies](https://www.magereport.com/page/support).
