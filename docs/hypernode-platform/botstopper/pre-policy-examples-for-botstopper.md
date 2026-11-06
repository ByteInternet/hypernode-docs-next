---
myst:
  html_meta:
    description: Ready-to-use Botstopper pre-policy examples for Hypernode, to allow
      trusted bots, monitoring tools, and integrations before the standard rules run.
    title: Pre-Policy Examples for Botstopper | Hypernode
---

# Pre-Policy Examples for Botstopper

This page contains ready-to-use pre-policy rules for Botstopper. Pre-policy rules run before most of the standard Hypernode deny and challenge rules. Use them to allow trusted traffic, such as monitoring tools, SEO tools, and integrations, or to block very specific traffic early.

For an explanation of how Botstopper works and how policies are evaluated, see [How to Use Botstopper on Hypernode](./how-to-use-botstopper.md).

## How to Add a Pre-Policy

Pre-policy rules go in `/data/web/botstopper/pre.policy.yml`. This file contains a YAML list of policy rules.

1. Open the file as the `app` user:

   ```bash
   sensible-editor /data/web/botstopper/pre.policy.yml
   ```

1. Copy the rule you want to use from the examples below and add it to the list. If the file only contains `[]`, replace it with the rule.

1. Save the file and restart Botstopper:

   ```bash
   hypernode-servicectl restart techaro-botstopper@default
   ```

1. Test the result to confirm the rule behaves as expected.

When you combine multiple rules, make sure the file stays a single valid YAML list. Each rule starts with `- name:`.

```{warning}
Pre-policy rules run before the standard Hypernode rules. A broad `DENY` rule in `pre.policy.yml` can block good crawlers or integrations that the standard policy would otherwise allow. Keep your rules as specific as possible and always test them before using them in production.
```

## Examples

The examples below come from the [Botstopper policy snippets repository](https://github.com/TimVNL/hypernode-botstopper-policies). Each rule is a list item that you can copy into `pre.policy.yml`.

### Search Engines and SEO Tools

The standard Hypernode policy already allows known search engine crawlers when they are verified by IP ranges or reverse DNS. Use these rules when you want to make sure a crawler or SEO tool is never challenged.

#### Google crawlers

Allows requests with common Google crawler user agents, such as `Googlebot`, `AdsBot-Google`, `Storebot-Google`, `Google-InspectionTool`, and `Google-Site-Verification`.

```{note}
This rule only checks the user agent, which can be spoofed. Bots that pretend to be Googlebot are also allowed. The standard policy already allows Google crawlers that are verified by IP range or reverse DNS, so only use this rule if you notice that a Google service is being challenged.
```

```yaml
- name: allow-all-google-temp
  action: ALLOW
  expression:
    all:
      - userAgent.matches("(?i:(googlebot|adsbot-google|mediapartners-google|apis-google|googleother|feedfetcher-google|storebot-google|google-inspectiontool|google-extended|Google-Apps-Script|Google-Site-Verification))")
```

#### Ahrefs

Allows `AhrefsBot` and `AhrefsSiteAudit` from the [IP ranges published by Ahrefs](https://ahrefs.com/robot).

<details>
<summary>Show the full rule (81 IP addresses)</summary>

```yaml
- name: allow-ahrefs-bots
  action: ALLOW
  expression:
    all:
      - userAgent.matches("(?i:(ahrefsbot|ahrefssiteaudit))")
  remote_addresses:
    - 5.39.1.224/27
    - 5.39.109.160/27
    - 15.235.27.0/24
    - 15.235.96.0/24
    - 15.235.98.0/24
    - 37.59.204.128/27
    - 51.68.247.192/27
    - 51.75.236.128/27
    - 51.81.103.240/28
    - 51.81.104.32/28
    - 51.81.105.16/28
    - 51.81.110.16/28
    - 51.81.110.48/28
    - 51.81.110.80/28
    - 51.81.111.0/28
    - 51.81.111.64/28
    - 51.81.111.112/28
    - 51.81.111.128/28
    - 51.81.163.16/28
    - 51.81.163.48/28
    - 51.81.163.64/28
    - 51.81.164.144/28
    - 51.81.164.192/28
    - 51.81.165.80/28
    - 51.81.165.208/28
    - 51.81.169.112/28
    - 51.81.169.192/28
    - 51.81.170.0/28
    - 51.89.38.128/28
    - 51.89.39.48/28
    - 51.89.59.32/28
    - 51.89.69.32/28
    - 51.89.69.96/28
    - 51.89.71.80/28
    - 51.89.71.144/28
    - 51.89.72.0/28
    - 51.89.74.192/28
    - 51.89.83.48/28
    - 51.89.129.0/24
    - 51.161.37.0/24
    - 51.161.65.0/24
    - 51.195.183.0/24
    - 51.195.215.0/24
    - 51.195.244.0/24
    - 51.222.95.0/24
    - 51.222.168.0/24
    - 51.222.253.0/26
    - 54.36.148.0/23
    - 54.37.118.64/27
    - 54.38.147.0/24
    - 54.39.0.0/24
    - 54.39.6.0/24
    - 54.39.89.0/24
    - 54.39.136.0/24
    - 54.39.203.0/24
    - 54.39.210.0/24
    - 92.222.104.192/27
    - 92.222.108.96/27
    - 94.23.188.192/27
    - 142.44.220.0/24
    - 142.44.225.0/24
    - 142.44.228.0/24
    - 142.44.233.0/24
    - 148.113.128.0/24
    - 148.113.130.0/24
    - 167.114.139.0/24
    - 168.100.149.0/24
    - 176.31.139.0/27
    - 198.244.168.0/24
    - 198.244.183.0/24
    - 198.244.186.193/32
    - 198.244.186.194/31
    - 198.244.186.196/30
    - 198.244.186.200/31
    - 198.244.186.202/32
    - 198.244.226.0/24
    - 198.244.240.0/24
    - 198.244.242.0/24
    - 202.8.40.0/22
    - 202.94.84.110/31
    - 202.94.84.112/31
```

</details>

#### Semrush Site Audit

Allows the Semrush `SiteAuditBot` from the [IP range published by Semrush](https://www.semrush.com/kb/681-site-audit-troubleshooting#allowlist-bot).

```yaml
- name: allow-SiteAuditBot
  action: ALLOW
  user_agent_regex: SiteAuditBot
  remote_addresses:
    - 85.208.98.128/25
```

### AI Retrieval Bots

#### AI retrieval and citation bots

Allows known AI retrieval and citation bots, so answer engines and assistant-triggered fetchers can access your shop. This rule allows `PerplexityBot`, `Perplexity-User`, `OAI-SearchBot`, `ChatGPT-User`, and `ClaudeBot`.

```{note}
This rule runs before the configured AI policy, so these bots are allowed regardless of your `botstopper_ai_policy` setting. The rule only checks the user agent, which can be spoofed.
```

```yaml
- name: allow-retrieval-citation-bots
  action: ALLOW
  expression:
    all:
      - userAgent.matches("(?i:(PerplexityBot|Perplexity-User|OAI-SearchBot|ChatGPT-User|ClaudeBot))")
```

### Uptime Monitoring

Uptime monitoring tools request your shop at short intervals. If Botstopper challenges these requests, the monitoring tool reports your shop as down.

#### HetrixTools

Allows HetrixTools uptime monitoring from the [IP addresses published by HetrixTools](https://docs.hetrixtools.com/uptime-monitoring-ip-addresses/).

<details>
<summary>Show the full rule (103 IP addresses)</summary>

```yaml
- name: allow-hetrixtools-uptime
  action: ALLOW
  user_agent_regex: HetrixTools
  remote_addresses:
    - 52.207.41.187/32
    - 96.126.106.201/32
    - 52.23.120.125/32
    - 138.197.17.201/32
    - 66.165.247.154/32
    - 149.28.50.248/32
    - 172.241.23.225/32
    - 209.222.107.178/32
    - 67.213.120.27/32
    - 94.154.159.133/32
    - 66.206.13.170/32
    - 79.127.243.80/32
    - 23.239.7.4/32
    - 52.52.33.209/32
    - 149.28.212.239/32
    - 159.89.159.134/32
    - 66.165.225.34/32
    - 23.106.180.172/32
    - 69.67.149.243/32
    - 77.247.126.141/32
    - 104.194.8.169/32
    - 172.235.62.113/32
    - 66.42.97.101/32
    - 95.179.139.97/32
    - 51.15.61.222/32
    - 188.166.79.172/32
    - 37.48.96.90/32
    - 194.126.173.238/32
    - 51.158.156.63/32
    - 194.49.53.65/32
    - 217.195.155.50/32
    - 52.56.73.124/32
    - 139.162.228.62/32
    - 95.179.193.59/32
    - 178.62.11.90/32
    - 51.195.149.151/32
    - 23.106.61.94/32
    - 185.174.110.102/32
    - 103.50.32.15/32
    - 94.72.181.90/32
    - 185.38.148.144/32
    - 51.89.144.57/32
    - 52.59.92.96/32
    - 78.46.88.58/32
    - 94.16.112.18/32
    - 51.195.46.219/32
    - 178.162.208.86/32
    - 192.248.181.140/32
    - 91.239.130.97/32
    - 66.206.25.250/32
    - 164.92.161.215/32
    - 172.105.249.219/32
    - 152.53.124.134/32
    - 51.89.47.4/32
    - 52.221.91.160/32
    - 139.162.22.205/32
    - 128.199.187.77/32
    - 45.76.150.238/32
    - 51.79.156.91/32
    - 23.106.120.205/32
    - 107.155.75.66/32
    - 210.16.67.82/32
    - 51.79.212.229/32
    - 104.237.139.48/32
    - 45.32.204.172/32
    - 23.227.169.50/32
    - 172.241.24.83/32
    - 2.56.188.250/32
    - 207.188.6.20/32
    - 121.127.40.34/32
    - 52.65.182.14/32
    - 45.76.120.140/32
    - 139.99.169.250/32
    - 172.105.168.58/32
    - 103.101.130.73/32
    - 203.96.179.194/32
    - 91.242.215.225/32
    - 139.99.233.44/32
    - 52.67.204.189/32
    - 104.41.61.219/32
    - 103.88.233.41/32
    - 216.238.100.86/32
    - 189.1.173.35/32
    - 45.158.39.210/32
    - 52.199.17.123/32
    - 45.76.202.144/32
    - 172.104.99.63/32
    - 23.106.230.203/32
    - 43.230.163.178/32
    - 199.254.199.6/32
    - 35.154.5.38/32
    - 148.113.2.135/32
    - 172.105.37.103/32
    - 181.41.142.138/32
    - 65.20.70.55/32
    - 181.41.142.170/32
    - 148.113.25.248/32
    - 146.59.0.13/32
    - 70.34.249.133/32
    - 84.17.55.195/32
    - 151.115.123.218/32
    - 51.38.143.147/32
    - 70.34.248.245/32
```

</details>

#### Oh Dear

Allows Oh Dear monitoring from the [IP addresses published by Oh Dear](https://ohdear.app/docs/faq/what-ips-does-oh-dear-monitor-from).

<details>
<summary>Show the full rule (74 IP addresses)</summary>

```yaml
- name: allow-ohdear.app
  action: ALLOW
  user_agent_regex: OhDear
  remote_addresses:
    - 45.32.146.84/32
    - 2001:19f0:6801:5f3:5400:1ff:fe38:3572/128
    - 139.59.61.47/32
    - 2400:6180:100:d0::12:e001/128
    - 45.76.59.200/32
    - 2001:19f0:6401:f5a:5400:1ff:fe57:57e9/128
    - 45.32.189.194/32
    - 2001:19f0:5801:1e90:5400:1ff:fecb:f1f2/128
    - 45.76.46.251/32
    - 2001:19f0:6801:15d7:5400:1ff:fef9:8e1d/128
    - 165.22.95.234/32
    - 2a03:b0c0:3:e0::220:2001/128
    - 95.179.211.184/32
    - 2a05:f480:1c00:7dd:5400:2ff:fe68:af7/128
    - 167.71.54.244/32
    - 2a03:b0c0:3:e0::2a8:6001/128
    - 45.76.236.54/32
    - 2001:19f0:6401:19d5:5400:2ff:feb3:6d28/128
    - 167.172.97.55/32
    - 2a03:b0c0:3:e0::386:1/128
    - 164.90.176.102/32
    - 2a03:b0c0:3:f0::173:0/128
    - 199.247.9.185/32
    - 2a05:f480:1c00:c80:5400:2ff:feda:ca89/128
    - 217.69.10.40/32
    - 2001:19f0:6801:9d3:5400:2ff:feda:fb6e/128
    - 159.203.38.39/32
    - 2604:a880:cad:d0::7aa:6001/128
    - 198.13.48.175/32
    - 2001:19f0:7002:3d5:5400:2ff:fedb:8dc0/128
    - 46.101.122.201/32
    - 2a03:b0c0:3:d0::10b8:8001/128
    - 158.247.212.166/32
    - 2401:c080:1c02:b4:5400:3ff:fe1a:56a2/128
    - 45.32.107.252/32
    - 2001:19f0:4400:737b:5400:3ff:fe1a:5634/128
    - 165.227.31.113/32
    - 2604:a880:2:d0::15d9:c001/128
    - 45.63.54.118/32
    - 2001:19f0:6001:5ef0:5400:3ff:fe1a:5666/128
    - 178.62.45.205/32
    - 2a03:b0c0:1:d0::81:e001/128
    - 134.209.122.208/32
    - 2604:a880:400:d0::1a7d:4001/128
    - 13.245.37.23/32
    - 54.94.4.151/32
    - 45.32.147.8/32
    - 2a05:f480:1c00:5f0:5400:3ff:fe50:e0c5/128
    - 134.209.243.63/32
    - 2a03:b0c0:3:d0::4f5:f001/128
    - 138.68.138.12/32
    - 138.68.138.180/32
    - 104.236.192.248/32
    - 165.22.36.80/32
    - 159.203.60.48/32
    - 216.128.128.104/32
    - 2001:19f0:6401:3a:5400:5ff:fe8b:5e4b/128
    - 70.34.203.58/32
    - 2a05:f480:2000:295b:5400:5ff:fe85:e8c9/128
    - 217.19.225.103/32
    - 176.62.160.106/32
    - 23.88.67.24/32
    - 2a01:4f8:272:426a::2/128
    - 167.71.40.86/32
    - 2a03:b0c0:3:d0::e8d:1001/128
    - 167.71.57.77/32
    - 2a03:b0c0:3:f0:0:1:8224:4000/128
    - 137.184.22.216/32
    - 2604:a880:400:d0::1ce6:d001/128
    - 159.65.3.76/32
    - 2400:6180:0:d0::157d:f001/128
    - 142.93.110.196/32
    - 68.183.121.207/32
    - 167.99.69.81/32
```

</details>

#### Pingdom

Allows Pingdom monitoring checks from the [probe server IP addresses published by SolarWinds](https://documentation.solarwinds.com/en/success_center/pingdom/content/topics/pingdom-probe-servers-ip-addresses.htm).

<details>
<summary>Show the full rule (149 IP addresses)</summary>

```yaml
- name: allow-pingdom
  action: ALLOW
  expression:
    all:
      - userAgent.matches("(?i:Pingdom)")
  remote_addresses:
    - 3.10.222.182/32
    - 3.11.131.95/32
    - 3.66.99.59/32
    - 3.120.200.34/32
    - 3.121.108.101/32
    - 3.125.198.20/32
    - 3.127.78.190/32
    - 3.219.128.11/32
    - 3.234.196.132/32
    - 13.41.140.26/32
    - 13.41.156.80/32
    - 13.48.152.99/32
    - 13.49.128.195/32
    - 13.232.220.164/32
    - 13.238.73.96/32
    - 13.238.127.47/32
    - 15.157.158.165/32
    - 15.157.248.148/32
    - 18.133.153.87/32
    - 18.159.29.185/32
    - 18.169.231.220/32
    - 18.176.175.170/32
    - 18.228.82.35/32
    - 18.230.158.101/32
    - 23.22.2.46/32
    - 23.83.129.219/32
    - 23.92.127.2/32
    - 23.106.37.99/32
    - 23.111.152.74/32
    - 23.111.159.174/32
    - 35.75.240.83/32
    - 35.76.210.156/32
    - 35.79.242.196/32
    - 35.85.117.184/32
    - 43.225.198.122/32
    - 43.229.84.12/32
    - 44.194.39.17/32
    - 44.226.213.159/32
    - 44.240.34.6/32
    - 46.20.45.18/32
    - 46.246.122.10/32
    - 50.16.153.186/32
    - 51.20.199.140/32
    - 51.21.185.148/32
    - 52.0.204.16/32
    - 52.5.245.15/32
    - 52.13.171.123/32
    - 52.21.31.140/32
    - 52.24.42.103/32
    - 52.34.250.64/32
    - 52.37.65.41/32
    - 52.48.244.35/32
    - 52.52.34.158/32
    - 52.52.95.213/32
    - 52.52.118.192/32
    - 52.57.132.90/32
    - 52.59.46.112/32
    - 52.59.147.246/32
    - 52.60.62.239/32
    - 52.60.154.13/32
    - 52.62.12.49/32
    - 52.63.142.2/32
    - 52.63.164.147/32
    - 52.63.167.55/32
    - 52.65.247.85/32
    - 52.67.148.55/32
    - 52.73.209.122/32
    - 52.89.43.70/32
    - 52.194.115.181/32
    - 52.197.31.124/32
    - 52.197.224.235/32
    - 52.198.25.184/32
    - 52.201.3.199/32
    - 52.209.34.226/32
    - 52.209.186.226/32
    - 52.210.232.124/32
    - 54.65.106.94/32
    - 54.68.48.199/32
    - 54.70.202.58/32
    - 54.79.157.219/32
    - 54.79.202.123/32
    - 54.94.28.109/32
    - 54.94.182.182/32
    - 54.94.206.111/32
    - 54.94.238.198/32
    - 54.153.170.200/32
    - 64.237.49.203/32
    - 64.237.55.3/32
    - 66.165.229.130/32
    - 66.165.233.234/32
    - 72.46.130.18/32
    - 72.46.131.10/32
    - 75.101.131.114/32
    - 76.164.234.106/32
    - 76.164.234.130/32
    - 82.103.136.16/32
    - 82.103.139.165/32
    - 82.103.145.126/32
    - 85.195.116.134/32
    - 89.163.146.247/32
    - 89.163.242.206/32
    - 94.75.211.73/32
    - 94.75.211.74/32
    - 94.247.174.83/32
    - 103.47.211.210/32
    - 108.181.70.3/32
    - 141.125.89.147/32
    - 148.72.170.233/32
    - 148.72.171.17/32
    - 151.106.52.134/32
    - 158.175.95.9/32
    - 162.218.67.34/32
    - 162.253.128.178/32
    - 167.17.67.101/32
    - 168.1.203.46/32
    - 169.44.155.138/32
    - 169.51.2.18/32
    - 169.54.70.214/32
    - 169.63.150.216/32
    - 172.241.112.86/32
    - 173.248.147.18/32
    - 174.34.156.130/32
    - 175.45.132.20/32
    - 176.34.7.155/32
    - 177.47.99.26/32
    - 177.71.158.135/32
    - 178.162.206.244/32
    - 179.50.12.212/32
    - 184.75.210.90/32
    - 184.75.210.226/32
    - 184.75.214.66/32
    - 184.75.214.98/32
    - 185.39.146.214/32
    - 185.39.146.215/32
    - 185.70.76.23/32
    - 185.93.3.65/32
    - 185.136.156.82/32
    - 185.152.65.167/32
    - 185.180.12.65/32
    - 185.246.208.82/32
    - 190.120.230.7/32
    - 196.240.207.18/32
    - 196.244.191.18/32
    - 196.245.151.42/32
    - 199.87.228.66/32
    - 200.58.101.248/32
    - 207.244.80.239/32
    - 209.58.139.193/32
    - 209.58.139.194/32
```

</details>

#### UptimeRobot

Allows UptimeRobot monitoring from the [IP addresses published by UptimeRobot](https://uptimerobot.com/help/locations/).

<details>
<summary>Show the full rule (103 IP addresses)</summary>

```yaml
- name: allow-uptimerobot-monitoring
  action: ALLOW
  user_agent_regex: UptimeRobot
  remote_addresses:
    - 3.12.251.153/32
    - 3.20.63.178/32
    - 3.77.67.4/32
    - 3.79.134.69/32
    - 3.105.133.239/32
    - 3.105.190.221/32
    - 3.133.226.214/32
    - 3.149.57.90/32
    - 3.212.128.62/32
    - 5.161.61.238/32
    - 5.161.73.160/32
    - 5.161.75.7/32
    - 5.161.113.195/32
    - 5.161.117.52/32
    - 5.161.177.47/32
    - 5.161.194.92/32
    - 5.161.215.244/32
    - 5.223.43.32/32
    - 5.223.53.147/32
    - 5.223.57.22/32
    - 18.116.205.62/32
    - 18.180.208.214/32
    - 18.192.166.72/32
    - 18.193.252.127/32
    - 24.144.78.39/32
    - 24.144.78.185/32
    - 34.198.201.66/32
    - 45.55.123.175/32
    - 45.55.127.146/32
    - 49.13.24.81/32
    - 49.13.130.29/32
    - 49.13.134.145/32
    - 49.13.164.148/32
    - 49.13.167.123/32
    - 52.15.147.27/32
    - 52.22.236.30/32
    - 52.28.162.93/32
    - 52.59.43.236/32
    - 52.87.72.16/32
    - 54.64.67.106/32
    - 54.79.28.129/32
    - 54.87.112.51/32
    - 54.167.223.174/32
    - 54.249.170.27/32
    - 63.178.84.147/32
    - 64.225.81.248/32
    - 64.225.82.147/32
    - 78.46.190.63/32
    - 78.46.215.1/32
    - 78.47.98.55/32
    - 78.47.173.76/32
    - 88.99.80.227/32
    - 91.99.101.207/32
    - 128.140.41.193/32
    - 128.140.106.114/32
    - 129.212.132.140/32
    - 134.199.240.137/32
    - 138.197.53.117/32
    - 138.197.53.138/32
    - 138.197.54.143/32
    - 138.197.54.247/32
    - 138.197.63.92/32
    - 139.59.50.44/32
    - 142.132.180.39/32
    - 143.198.249.237/32
    - 143.198.250.89/32
    - 143.244.196.21/32
    - 143.244.196.211/32
    - 143.244.221.177/32
    - 144.126.251.21/32
    - 146.190.9.187/32
    - 152.42.149.135/32
    - 157.90.155.240/32
    - 157.90.156.63/32
    - 159.69.158.189/32
    - 159.223.243.219/32
    - 161.35.247.201/32
    - 167.99.18.52/32
    - 167.235.143.113/32
    - 168.119.53.160/32
    - 168.119.96.239/32
    - 168.119.123.75/32
    - 170.64.250.64/32
    - 170.64.250.132/32
    - 170.64.250.235/32
    - 178.156.181.172/32
    - 178.156.184.20/32
    - 178.156.185.127/32
    - 178.156.185.231/32
    - 178.156.187.238/32
    - 178.156.189.113/32
    - 178.156.189.249/32
    - 188.166.201.79/32
    - 206.189.241.133/32
    - 209.38.49.1/32
    - 209.38.49.206/32
    - 209.38.49.226/32
    - 209.38.51.43/32
    - 209.38.53.7/32
    - 209.38.124.252/32
    - 216.144.248.27/32
    - 216.144.248.28/32
    - 216.144.248.29/32
```

</details>

#### Uptime Kuma

Allows [Uptime Kuma](https://github.com/louislam/uptime-kuma/wiki), a self-hosted monitoring tool. Because Uptime Kuma runs on your own server, there is no fixed IP range. If you know the IP address of your Uptime Kuma server, add it under `remote_addresses` to make the rule more specific.

```yaml
- name: allow-uptime-kuma
  action: ALLOW
  user_agent_regex: Uptime-Kuma
```

### Cookie Consent Scanners

Cookie consent tools scan your shop to detect which cookies it sets. If Botstopper challenges the scanner, the cookie overview of your consent banner can become incomplete.

#### Cookiebot

Allows the Cookiebot scanner from the [IP addresses published by Cookiebot](https://support.cookiebot.com/hc/en-us/articles/360003824153-Whitelisting-the-Cookiebot-scanner).

<details>
<summary>Show the full rule (11 IP addresses)</summary>

```yaml
- name: allow-cookiebot-scanner
  action: ALLOW
  user_agent_regex: Cookiebot
  remote_addresses:
    - 20.223.9.138/32
    - 34.107.102.47/32
    - 34.141.10.24/32
    - 34.159.86.126/32
    - 34.159.168.195/32
    - 34.159.247.222/32
    - 35.198.78.207/32
    - 35.198.137.6/32
    - 35.198.160.49/32
    - 35.246.143.2/32
    - 35.246.191.14/32
```

</details>

#### CookieYes

Allows the [CookieYes scanner](https://www.cookieyes.com/documentation/cookieyesbot/), `CookieYesbot`.

```yaml
- name: allow-CookieYesbot-scanner
  action: ALLOW
  user_agent_regex: CookieYesbot
```

### WordPress Tools

#### BlogVault

Allows the BlogVault WordPress backup service from the [IP addresses published by BlogVault](https://app.blogvault.net/api/bv_bots).

<details>
<summary>Show the full rule (69 IP addresses)</summary>

```yaml
- name: allow-blogvault
  action: ALLOW
  remote_addresses:
    - 46.101.79.34/32
    - 139.180.180.168/32
    - 136.244.79.211/32
    - 217.69.12.130/32
    - 66.42.61.105/32
    - 95.179.211.0/32
    - 49.13.85.158/32
    - 78.46.201.135/32
    - 188.245.49.234/32
    - 188.245.80.240/32
    - 116.202.106.0/32
    - 5.161.106.94/32
    - 5.161.201.188/32
    - 5.161.52.234/32
    - 5.161.177.123/32
    - 5.161.250.15/32
    - 157.230.220.204/32
    - 82.196.2.12/32
    - 188.245.58.208/32
    - 49.12.219.178/32
    - 138.201.158.24/32
    - 91.107.202.135/32
    - 167.235.254.214/32
    - 5.161.44.164/32
    - 178.156.128.204/32
    - 5.161.69.178/32
    - 5.161.216.238/32
    - 5.161.226.151/32
    - 5.161.53.170/32
    - 178.156.134.136/32
    - 5.161.217.158/32
    - 5.161.202.241/32
    - 5.161.250.122/32
    - 188.245.87.173/32
    - 116.202.110.255/32
    - 49.13.10.198/32
    - 5.75.228.162/32
    - 88.99.13.2/32
    - 137.184.135.216/32
    - 143.198.117.131/32
    - 146.185.155.135/32
    - 5.161.252.168/32
    - 178.156.146.200/32
    - 5.161.114.127/32
    - 5.161.96.135/32
    - 178.156.136.36/32
    - 188.245.90.252/32
    - 188.245.48.218/32
    - 188.245.61.191/32
    - 49.12.66.195/32
    - 49.13.22.245/32
    - 188.226.179.196/32
    - 188.226.158.111/32
    - 161.35.15.229/32
    - 68.183.107.157/32
    - 49.13.61.43/32
    - 49.13.217.108/32
    - 138.199.152.110/32
    - 188.245.53.189/32
    - 104.248.114.9/32
    - 192.81.221.63/32
    - 45.63.10.187/32
    - 45.76.137.73/32
    - 159.223.99.132/32
    - 198.211.127.63/32
    - 37.139.10.11/32
    - 82.196.10.5/32
    - 139.59.75.155/32
    - 165.227.156.122/32
```

</details>

#### InfiniteWP

Allows [InfiniteWP](https://infinitewp.com), a dashboard to manage multiple WordPress sites.

```yaml
- name: allow-infinitewp
  action: ALLOW
  user_agent_regex: InfiniteWP
```

#### WP Rocket

Allows the WP Rocket SaaS service from the [IP ranges published by WP Rocket](https://docs.wp-rocket.me/article/1628-which-ip-do-i-need-to-allow-for-wp-rocket).

<details>
<summary>Show the full rule (29 IP addresses)</summary>

```yaml
- name: allow-wprocket
  action: ALLOW
  user_agent_regex: WP-Rocket-SaaS
  remote_addresses:
    - 172.64.0.0/13
    - 103.22.200.0/22
    - 104.16.0.0/13
    - 5.249.224.0/24
    - 173.245.48.0/20
    - 46.30.214.0/24
    - 197.234.240.0/22
    - 46.30.210.0/24
    - 103.31.4.0/22
    - 131.0.72.0/22
    - 185.10.8.0/22
    - 103.21.244.0/22
    - 198.41.128.0/17
    - 46.30.211.0/24
    - 162.158.0.0/15
    - 188.114.96.0/20
    - 141.101.64.0/18
    - 46.30.212.0/24
    - 190.93.240.0/20
    - 104.24.0.0/14
    - 108.162.192.0/18
    - 2405:8100::/32
    - 2a02:2350:4:200::/55
    - 2c0f:f248::/32
    - 2a06:98c0::/29
    - 2606:4700::/32
    - 2803:f800::/32
    - 2400:cb00::/32
    - 2405:b500::/32
```

</details>

### Other Integrations

#### Sendcloud

Allows the Sendcloud shipping platform from the [IP addresses published by Sendcloud](https://cdn.sendcloud.com/global-media/public-ips.txt).

<details>
<summary>Show the full rule (15 IP addresses)</summary>

```yaml
- name: allow-sendcloud
  action: ALLOW
  user_agent_regex: (?i)sendcloud
  remote_addresses:
    - 3.120.127.184/32
    - 3.121.38.108/32
    - 3.122.58.116/32
    - 35.158.146.12/32
    - 52.57.76.59/32
    - 52.29.84.45/32
    - 52.29.82.100/32
    - 52.58.233.101/32
    - 52.58.235.98/32
    - 18.198.117.128/32
    - 18.158.18.128/32
    - 3.124.13.189/32
    - 3.72.184.234/32
    - 3.70.35.13/32
    - 18.195.37.52/32
```

</details>

#### SleakBot

Allows `SleakBot`, the crawler of the [Sleak](https://sleak.chat) AI chat assistant.

```yaml
- name: allow-sleakbot
  action: ALLOW
  user_agent_regex: SleakBot
```

### Country-Based Rules

These rules use the `X-Country-Code` header, which contains the country of the visitor's IP address.

#### Allow visitors from the Benelux

Allows all traffic from the Netherlands, Belgium, and Luxembourg without a challenge.

```{warning}
This rule allows all traffic from these countries before any other check, including bad bots and scrapers that run from Dutch, Belgian, or Luxembourg IP addresses.
```

```yaml
- name: allow-benelux-without-challenge
  action: ALLOW
  expression:
    all:
      - '"X-Country-Code" in headers'
      - 'headers["X-Country-Code"] in ["NL", "BE", "LU"]'
```

#### Block visitors from outside the EU, UK, and US

Blocks all requests from countries outside the EU/EEA, Switzerland, the United Kingdom and its Crown Dependencies, and the United States. Visitors from other countries receive an HTTP `403` response.

```{warning}
This rule runs before the standard Hypernode allow rules. It also blocks crawlers, payment providers, and integrations that connect from other countries. Add trusted services to the WAF allowlist, or add `ALLOW` rules above this rule in `pre.policy.yml`.
```

```yaml
- name: deny-non-eu-uk-us
  action: DENY
  expression:
    all:
      - '"X-Country-Code" in headers'
      - '!(headers["X-Country-Code"] in ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE", "IS", "LI", "NO", "CH", "GB", "GG", "JE", "IM", "US"])'
```
