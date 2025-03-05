---
myst:
  html_meta:
    description: Learn how our Xgrade process work and how to make sure your Hypernode
      is ready for the Debian Bookworm upgrade
    title: How does the Xgrade process works
---

# What is the Xgrade process of Hypernode?

An Xgrade is an automated process that allows your server to be upgraded or downgraded without any manual actions. Additionally, an Xgrade enables migration to one of our other providers.

## How does an Xgrade to Debian Bookworm or R405 work, and does it involve downtime?

An Xgrade to Debian Bookworm or R405 (which can be performed together) is carried out by our automation. Below are the relevant steps in the process:

1. Ensure a new Hypernode is created.
1. Configure the new Hypernode (Operating system, MySQL, PHP, Varnish, etc.).
1. Synchronize data (everything within the "/" and "/data" partition).
1. Stop all services on the current Hypernode.
1. Synchronize any new data that has been written.
1. Perform checks to ensure all processes are complete.
1. Send a "Hypernode migrated" event.
1. Destroy the old Hypernode.

As you can see, a completely new Hypernode is created with the correct configurations, whether for a Debian Bookworm or an R405 Xgrade. The first synchronization of data will then take place. The duration of this synchronization depends on the amount and type of data. Typically, we calculate about 1 GB per minute, but this may vary.

At a certain point, all services will be stopped to prevent new orders from being placed and to ensure no data is lost. A second synchronization will then take place to transfer any newly written data. After this, our automation will conduct various checks before finalizing the migration to Debian Bookworm or R405 (or a combination of both).

## What should be checked or adjusted before the Xgrade? (e.g., Node.js and TLS configuration)

### Nodejs

Before scheduling a Xgrade to Debian Bookworm/R405, you must check which Node.js version you are using. This is necessary because Node.js versions 6 and 10 are no longer supported on the new operating system. Standard Magento 2 does not make use of Nodejs, but if you use another CMS or have custom scripts that require them, you may need to update your setup.

You can check your Node.js version in two ways; within the Control Panel, Or through the CLI:
Within the Control Panel: Navigate to Settings → Development.

```
app@uaifqk-hnvandijk-magweb-cmbl:~$ hypernode-systemctl settings nodejs_version
nodejs_version is set to value 16
```

If necessary, you can update Node.js by following these steps:

```
app@uaifqk-hnvandijk-magweb-cmbl:~$ hypernode-systemctl settings nodejs_version 16
Operation was successful and is being processed. Please allow a few minutes for the settings to be applied. Run 'livelog' to see the progress.
```

### TLS configuration

With the upgrade to Debian Bookworm, the TLS configurations will also change. We have chosen to phase out outdated TLS versions 1.0 and 1.1. Additionally, the "modern" TLS configuration will now only support TLS 1.3.

Below are the TLS configurations for Debian Buster:

Intermediate TLS configuration:

```
# intermediate configuration
# nginx 1.16.1 | intermediate profile | OpenSSL 1.1.1d
# Oldest compatible clients: Firefox 27, Android 4.4.2, Chrome 31, Edge 12, IE 11 (Win7), Java 8u31, OpenSSL 1.0.1, Opera 20, Safari 9
# https://wiki.mozilla.org/Security/Server_Side_TLS#Intermediate_compatibility_.28default.29
ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA;
ssl_prefer_server_ciphers on;
# Diffie-Hellman parameter for DHE ciphersuites
ssl_dhparam /etc/nginx/dhparams.pem;

ssl_stapling on;
ssl_stapling_verify on;
```

Modern TLS configuration:

```
# intermediate configuration
# nginx 1.22.1 | intermediate profile | OpenSSL 3.0.11
# Oldest compatible clients: Firefox 27, Android 4.4.2, Chrome 31, Edge, IE 11 on Windows 7, Java 8u31, OpenSSL 1.0.1, Opera 20, and Safari 9
# https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-CHACHA20-POLY1305;
ssl_prefer_server_ciphers off;
# Diffie-Hellman parameter for DHE ciphersuites
ssl_dhparam /etc/nginx/dhparams.pem;

ssl_stapling on;
ssl_stapling_verify on;
```

And here are the new TLS configurations for Debian Bookworm:

Intermediate TLS configuration:

```
# intermediate configuration
# nginx 1.22.1 | intermediate profile | OpenSSL 3.0.11
# Oldest compatible clients: Firefox 27, Android 4.4.2, Chrome 31, Edge, IE 11 on Windows 7, Java 8u31, OpenSSL 1.0.1, Opera 20, and Safari 9
# https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-CHACHA20-POLY1305;
ssl_prefer_server_ciphers off;
# Diffie-Hellman parameter for DHE ciphersuites
ssl_dhparam /etc/nginx/dhparams.pem;

ssl_stapling on;
ssl_stapling_verify on;
```

Modern TLS configuration:

```
# modern configuration
# nginx 1.22.1 | modern profile | OpenSSL 3.0.11
# Oldest compatible clients: Firefox 63, Android 10.0, Chrome 70, Edge 75, Java 11, OpenSSL 1.1.1, Opera 57, and Safari 12.1
# https://wiki.mozilla.org/Security/Server_Side_TLS#Modern_compatibility
ssl_protocols TLSv1.3;
ssl_prefer_server_ciphers off;
ssl_stapling on;
ssl_stapling_verify on;
```

If you need to adjust the TLS configuration, you can do so using the "Hypernode-manage-vhost" command.

```
hmv hnvandijk.nl --ssl-config modern
```

Please see the actual `--ssl-config` flag:

```
  --ssl-config {modern,intermediate}
                        Use the given Mozilla SSL standard config
```

Additionally, you may need to modify the Modern_ssl_config using "hypernode-systemctl".

```
app@uaifqk-hnvandijk-magweb-cmbl:~$ hypernode-systemctl settings modern_ssl_config_enabled
false  true
```

# What needs to be adjusted after the Xgrade? When can it be performed? (IP changes)

If you choose to Xgrade to R405, you will receive a new IP address from our automation system. You must update this IP address in the DNS settings for both the non-www and www records of your domain. This information will be sent to the email address associated with the Hypernode owner.

My domain is at Hypernode, can we automate this? Yes, you can enable the "Synchronize DNS" option in our DNS manager. Our automation will update the DNS settings for you after the Xgrade.

We make use of Cloudflare, would we be able to "automate" this proces? Sure! You can enable CNAME Flattening, which ensures that both the non-www and www records point to the Hypernode hostname. For example:

## Non-www 

```
CNAME hnvandijk.nl ---> hnvandijk.hypernode.io
```

## www

```
CNAME www.hnvandijk.nl ---> hnvandijk.hypernode.io
```

We can schedule the Xgrade at a time that suits you! However, we can only provide the new IP address in advance if the Xgrade is performed during our standard working hours (09:00–18:00).

## I have a dedicated machine instead of a cloud environment. What does this mean?

If you have a dedicated machine and need an OS upgrade, you will be migrated to a different machine. This means you will receive a new IP address. The new machine will be set up at the TBBM data center, and we can only provide the new IP address during our standard working hours.

The OS upgrade process itself is the same as for a cloud environment.

## Additional Questions

- An Xgrade to R405 does not incur additional costs, you will not be charged extra.

- An Xgrade from Hetzner to TBBM also incurs no extra costs, you will not be charged extra.

## More Information

https://changelog.hypernode.com/release-9961-akeneo-7-0-is-now-available-on-the-platform/

https://changelog.hypernode.com/release-9956-hypernode-on-debian-bookworm/

https://changelog.hypernode.com/sunsetting-node-js-versions-6-and-10/
