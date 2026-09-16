---
myst:
  html_meta:
    description: Add a custom SSL certificate to your Hypernode account and link it
      to one or more Hypernodes. Includes Cloudflare Origin CA certificates.
    title: How to use a custom SSL certificate on Hypernode?
---

# How to Use a Custom SSL Certificate on Hypernode

You can add an SSL certificate from another certificate authority to your Hypernode account via the Control Panel. This is useful when you already have a certificate that was not ordered through Hypernode.

The Control Panel requires the certificate files in PEM format:

- Private Key
- Certificate
- Certificate Authority

## Add a Custom SSL Certificate to Your Account

1. Log into your [Control Panel](https://my.hypernode.com/).
1. Select SSL in the sidebar on the left.
1. To add a new SSL certificate, click the **Add SSL** button on the right.
1. Click **Add third party SSL certificate**.
1. Fill in the Private Key, Certificate and Certificate Authority. Use .PEM files only.
1. Click **Apply your SSL certificate**.
1. Click **Details** and then **(Un)link to Hypernodes** to select one or more Hypernodes to link the certificate to.

## Add a Custom SSL Certificate Directly to a Hypernode

You can also add a custom SSL certificate directly to a Hypernode. Follow the steps below to do so:

1. Log into your [Control Panel](https://my.hypernode.com/).
1. Select the specific Hypernode from the overview.
1. Click on your **Hypernode** and select **SSL:** under **Services**.
1. To add a new SSL certificate, click the **Add SSL** button on the right.
1. Click **Add third party SSL certificate**.
1. Fill in the Private Key, Certificate and Certificate Authority. Use .PEM files only.
1. Click **Apply your SSL certificate**.

## Link a Custom SSL Certificate to a Hypernode

If you already have a custom SSL certificate added to your account, you can link it to a specific Hypernode by following these steps:

1. Log into your [Control Panel](https://my.hypernode.com/).
1. Select the specific Hypernode from the overview.
1. Click on your **Hypernode** and select **SSL:** under **Services**.
1. Here you'll see an overview of the available SSL certificates. Click **Details** and then **(Un)link to Hypernodes** to link one or more Hypernodes to link the certificate to.

## Check Which Custom SSL Certificates Are Linked to Your Hypernode

If you want to check which custom SSL certificates are linked to a specific Hypernode, you can do so by following these steps:

1. Log into your [Control Panel](https://my.hypernode.com/).
1. Select the Hypernode from the overview.
1. Click on your **Hypernode** and select **SSL:** under **Services**.
1. You will now see an overview of all linked SSL certificates.
1. Click **Details** to go the detail page. You can unlink the domain or delete the SSL certificate from here.

## Use a Cloudflare Origin CA Certificate

Cloudflare Origin CA certificates encrypt traffic between Cloudflare and your Hypernode. They are useful when your domain uses Cloudflare proxying and you want to use Cloudflare SSL/TLS mode **Full (Strict)**. For more information, see the [official Cloudflare Origin CA documentation](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/).

```{warning}
Cloudflare Origin CA certificates are only trusted by Cloudflare. Site visitors can get certificate warnings if they connect directly to your Hypernode, if you pause Cloudflare, or if you turn off proxying for a hostname that uses this certificate.
```

### Create the Certificate in Cloudflare

1. Log into the [Cloudflare dashboard](https://dash.cloudflare.com/).
1. Select your account and domain.
1. Go to **SSL/TLS** > **Origin Server**.
1. On the **Origin Certificates** tab, click **Create Certificate**.
1. Choose **Generate private key and CSR with Cloudflare**.
1. Choose **ECC** as the private key type. Hypernode's Nginx and OpenSSL versions support ECC certificates, and ECC keeps the certificate and TLS handshake smaller. Use RSA if you specifically need RSA compatibility.
1. Add the hostnames the certificate should cover, such as `example.com`, `www.example.com`, or `*.example.com`.
1. Choose the certificate validity period.
1. Click **Create**.
1. Choose **PEM** as the key format.
1. Copy the **Origin Certificate** and **Private Key** before closing the screen. Cloudflare does not show the private key again later.

### Add the Cloudflare Certificate to Hypernode

Add the certificate as a custom SSL certificate in the Hypernode Control Panel. Use this field mapping:

| Hypernode field       | Cloudflare value                                                            |
| --------------------- | --------------------------------------------------------------------------- |
| Private Key           | The **Private Key** shown when you created the Origin CA certificate        |
| Certificate           | The **Origin Certificate** shown when you created the Origin CA certificate |
| Certificate Authority | The Cloudflare Origin CA root certificate in PEM format                     |

Use the Cloudflare Origin CA root certificate that matches the certificate type you created:

- [Cloudflare Origin ECC PEM](https://developers.cloudflare.com/ssl/static/origin_ca_ecc_root.pem) for ECC certificates.
- [Cloudflare Origin RSA PEM](https://developers.cloudflare.com/ssl/static/origin_ca_rsa_root.pem) for RSA certificates.

After applying the SSL certificate, link it to the correct Hypernode. If the certificate was added directly from the Hypernode SSL page, it is already linked to that Hypernode.

### Set Cloudflare to Full (Strict)

After the certificate is installed and linked in Hypernode, update the SSL/TLS encryption mode in Cloudflare:

```{note}
Only set **Full (Strict)** globally if all Cloudflare-proxied origin hosts in the zone use a valid Origin CA or publicly trusted certificate. If only this Hypernode uses the Origin CA certificate, configure **Full (Strict)** for the relevant hostname in Cloudflare.
```

1. Log into the [Cloudflare dashboard](https://dash.cloudflare.com/).
1. Select your account and domain.
1. Go to **SSL/TLS** > **Overview**.
1. Set **SSL/TLS encryption mode** to **Full (Strict)**.

Test the website through the Cloudflare-proxied hostname after changing this setting.

### Restrict Origin Access With Authenticated Origin Pulls

An origin server certificate lets Cloudflare verify your Hypernode when you use Full (Strict). Authenticated Origin Pulls lets your Hypernode verify the client certificate presented by Cloudflare. Installing an origin server certificate alone does not prevent direct access to your Hypernode. See [Cloudflare Authenticated Origin Pulls](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/).

Hypernode supports [custom Nginx configuration](../nginx/how-to-use-nginx.md). You can use this to configure Authenticated Origin Pulls as described below. The existing Cloudflare integration for visitor IP addresses does not itself enable this certificate check.

#### Before You Start

Ensure your website works through Cloudflare with proxying enabled and SSL/TLS mode set to Full (Strict). Install and link a valid origin server certificate first, following [the custom SSL certificate guide](#add-the-cloudflare-certificate-to-hypernode).

Global Authenticated Origin Pulls uses a certificate shared across Cloudflare accounts. It proves that a request came through the Cloudflare network. It does not prove that the request passed through your specific account or its security rules. For account-specific authentication, use [your own zone-level certificate](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/).

This check protects HTTPS requests handled by the configured Nginx server blocks. It does not block plain HTTP or other services. To prevent an HTTP bypass, configure the origin to redirect HTTP to HTTPS or deny HTTP application access. Cloudflare Always Use HTTPS only affects requests that reach Cloudflare.

#### Download the Cloudflare Certificate

Log into your Hypernode using SSH as the app user. Create the certificate directory and download the [Authenticated Origin Pull CA certificate](https://developers.cloudflare.com/ssl/static/authenticated_origin_pull_ca.pem).

```bash
mkdir -p /data/web/nginx/ssl
cd /data/web/nginx/ssl
wget -O authenticated_origin_pull_ca.pem https://developers.cloudflare.com/ssl/static/authenticated_origin_pull_ca.pem
openssl x509 -in authenticated_origin_pull_ca.pem -noout -subject -issuer -dates
```

Continue only if the download succeeds and OpenSSL can read the certificate. This is a separate certificate from the Origin CA certificate installed through the Hypernode Control Panel. See [Cloudflare global setup](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/).

#### Configure Nginx

Create the global configuration file below.

```bash
vi /data/web/nginx/server.authenticated_origin_pull
```

A global configuration can affect multiple websites. If you use Hypernode Managed Vhosts and only want to protect one website, use the existing vhost directory instead.

```bash
vi /data/web/nginx/example.com/server.authenticated_origin_pull
```

Replace `example.com` with the configured vhost name. Choose one scope. Check all affected hostnames, including staging sites, monitoring endpoints and integrations that connect directly. See [Hypernode Managed Vhosts](../nginx/hypernode-managed-vhosts.md#managing-configuration-files).

Start with optional verification so requests without a client certificate remain accepted during setup.

```nginx
# Cloudflare global Authenticated Origin Pulls
ssl_verify_client optional;
ssl_client_certificate /data/web/nginx/ssl/authenticated_origin_pull_ca.pem;
```

Save the file. Hypernode automatically validates and reloads custom Nginx configuration. Check for errors after each edit.

Resolve any reported errors before continuing. A rejected configuration leaves the previous configuration active. See [the Nginx config reloader](../nginx/how-to-use-nginx.md#nginx-config-reloader).

#### Enable and Enforce Authentication

In the Cloudflare dashboard, select your domain. Open SSL/TLS, then Origin Server, then Authenticated Origin Pulls. Switch Global to On. This setting covers all proxied hostnames in that zone. Follow [Cloudflare global setup](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/).

Check that requests through Cloudflare still work. Then edit the same Nginx file and replace its contents with the enforcing configuration.

```nginx
# Cloudflare global Authenticated Origin Pulls
ssl_verify_client on;
ssl_client_certificate /data/web/nginx/ssl/authenticated_origin_pull_ca.pem;
```

Save and check the reloader error file again. Optional verification does not prevent direct requests without a client certificate. The on setting requires one. See [Nginx client certificate verification](https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_verify_client).

#### Test the Configuration

Test each protected hostname through Cloudflare. Use an uncached page or a temporary cache bypass rule so the test reaches your Hypernode. Check the storefront, admin and checkout.

From your own computer, test direct HTTPS access using the origin IP. Replace example.com and 203.0.113.10 with your hostname and Hypernode IP.

```bash
curl --noproxy '*' --resolve example.com:443:203.0.113.10 -k -i https://example.com/
```

This preserves the hostname and TLS server name while bypassing Cloudflare DNS. The -k option skips server certificate verification for this diagnostic test, which is useful with Cloudflare Origin CA certificates. It does not provide a client certificate.

A direct request without a client certificate should be rejected. Nginx can return the following response.

```text
400 Bad Request
No required SSL certificate was sent
```

A server certificate warning alone does not confirm that Authenticated Origin Pulls works. Confirm that the origin rejects the missing client certificate and that uncached requests through Cloudflare succeed. Repeat for each origin IP and protected hostname.

#### Troubleshooting and Rollback

If requests through Cloudflare fail after enforcement, check that Global Authenticated Origin Pulls is enabled for the correct zone, proxying is active, and the Nginx file uses the Authenticated Origin Pull CA certificate. Check the Nginx reloader output for configuration errors.

To restore access temporarily, change `ssl_verify_client` from `on` to `off` in the same file. Save and confirm that Nginx accepts the change before disabling Authenticated Origin Pulls in Cloudflare. Direct HTTPS access is permitted again while verification is off.

## How to Generate a Certificate Signing Request on Nginx Using OpenSSL

Log into your Hypernode with SSH and run the following command:

```bash
openssl req -new -newkey rsa:2048 -nodes -keyout myserver.key -out myserver.csr
```

```{note}
Replace `myserver` with the domain name you're securing. For example, if your domain name is `mydomain.com`, use `mydomain.key` and `mydomain.csr`.
```

This command creates two files: the private key file for decrypting the SSL certificate and the certificate signing request (CSR) file used to apply for your SSL certificate.

Enter the requested information:

- **Common Name (CN):** The fully-qualified domain name, or URL, you want to secure.
- **Organization (O):** The legally registered name for your business. If you are enrolling as an individual, enter the certificate requestor's name.
- **Organization Unit (OU):** If applicable, enter the DBA (Doing Business As) name.
- **City or Locality (L):** Name of the city where your organization is registered or located. Do not abbreviate.
- **State or Province (S):** Name of the state or province where your organization is located. Do not abbreviate.
- **Country (C):** The two-letter International Organization for Standardization (ISO) country code for where your organization is legally registered.

If you are requesting a wildcard certificate, add an asterisk (`*`) to the left of the common name where you want the wildcard, for example `*.mydomain.com`. Do not use the asterisk in the private key or CSR file names, because `*` is a special character in shells. Use file names like `wildcard.mydomain.com.key` and `wildcard.mydomain.com.csr` instead.

If you do not want to enter a password for this SSL certificate, leave the passphrase field blank.

Your `.csr` file will then be created. Open the CSR file with a text editor and copy and paste it, including the `BEGIN` and `END` tags, into the certificate order form.

Save the generated `.key` file. You will need it when installing your SSL certificate in Nginx.
