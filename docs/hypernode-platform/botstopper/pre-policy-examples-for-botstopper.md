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

```{note}
The rules below don't include IP addresses, because providers change them regularly. Where a rule uses `remote_addresses`, copy the current IP addresses from the page of the provider that we link to. If a provider doesn't publish its IP addresses, contact that provider to ask which IP addresses they use.
```

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

Allows `AhrefsBot` and `AhrefsSiteAudit` from the [IP ranges published by Ahrefs](https://ahrefs.com/robot). Add the current IP addresses from that page under `remote_addresses` before you use the rule.

```yaml
- name: allow-ahrefs-bots
  action: ALLOW
  expression:
    all:
      - userAgent.matches("(?i:(ahrefsbot|ahrefssiteaudit))")
  remote_addresses:
    # Add the current IP addresses from the provider here, for example:
    - 192.0.2.0/24
```

#### Semrush Site Audit

Allows the Semrush `SiteAuditBot` from the [IP range published by Semrush](https://www.semrush.com/kb/681-site-audit-troubleshooting#allowlist-bot). Add the current IP addresses from that page under `remote_addresses` before you use the rule.

```yaml
- name: allow-SiteAuditBot
  action: ALLOW
  user_agent_regex: SiteAuditBot
  remote_addresses:
    # Add the current IP addresses from the provider here, for example:
    - 192.0.2.0/24
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

Allows HetrixTools uptime monitoring from the [IP addresses published by HetrixTools](https://docs.hetrixtools.com/uptime-monitoring-ip-addresses/). Add the current IP addresses from that page under `remote_addresses` before you use the rule.

```yaml
- name: allow-hetrixtools-uptime
  action: ALLOW
  user_agent_regex: HetrixTools
  remote_addresses:
    # Add the current IP addresses from the provider here, for example:
    - 192.0.2.0/24
```

#### Oh Dear

Allows Oh Dear monitoring from the [IP addresses published by Oh Dear](https://ohdear.app/docs/faq/what-ips-does-oh-dear-monitor-from). Add the current IP addresses from that page under `remote_addresses` before you use the rule.

```yaml
- name: allow-ohdear.app
  action: ALLOW
  user_agent_regex: OhDear
  remote_addresses:
    # Add the current IP addresses from the provider here, for example:
    - 192.0.2.0/24
```

#### Pingdom

Allows Pingdom monitoring checks from the [probe server IP addresses published by SolarWinds](https://documentation.solarwinds.com/en/success_center/pingdom/content/topics/pingdom-probe-servers-ip-addresses.htm). Add the current IP addresses from that page under `remote_addresses` before you use the rule.

```yaml
- name: allow-pingdom
  action: ALLOW
  expression:
    all:
      - userAgent.matches("(?i:Pingdom)")
  remote_addresses:
    # Add the current IP addresses from the provider here, for example:
    - 192.0.2.0/24
```

#### UptimeRobot

Allows UptimeRobot monitoring from the [IP addresses published by UptimeRobot](https://uptimerobot.com/help/locations/). Add the current IP addresses from that page under `remote_addresses` before you use the rule.

```yaml
- name: allow-uptimerobot-monitoring
  action: ALLOW
  user_agent_regex: UptimeRobot
  remote_addresses:
    # Add the current IP addresses from the provider here, for example:
    - 192.0.2.0/24
```

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

Allows the Cookiebot scanner from the [IP addresses published by Cookiebot](https://support.cookiebot.com/hc/en-us/articles/360003824153-Whitelisting-the-Cookiebot-scanner). Add the current IP addresses from that page under `remote_addresses` before you use the rule.

```yaml
- name: allow-cookiebot-scanner
  action: ALLOW
  user_agent_regex: Cookiebot
  remote_addresses:
    # Add the current IP addresses from the provider here, for example:
    - 192.0.2.0/24
```

#### CookieYes

Allows the [CookieYes scanner](https://www.cookieyes.com/documentation/cookieyesbot/), `CookieYesbot`.

```yaml
- name: allow-CookieYesbot-scanner
  action: ALLOW
  user_agent_regex: CookieYesbot
```

### WordPress Tools

#### BlogVault

Allows the BlogVault WordPress backup service from the [IP addresses published by BlogVault](https://app.blogvault.net/api/bv_bots). Add the current IP addresses from that page under `remote_addresses` before you use the rule.

```yaml
- name: allow-blogvault
  action: ALLOW
  remote_addresses:
    # Add the current IP addresses from the provider here, for example:
    - 192.0.2.0/24
```

#### InfiniteWP

Allows [InfiniteWP](https://infinitewp.com), a dashboard to manage multiple WordPress sites.

```yaml
- name: allow-infinitewp
  action: ALLOW
  user_agent_regex: InfiniteWP
```

#### WP Rocket

Allows the WP Rocket SaaS service from the [IP ranges published by WP Rocket](https://docs.wp-rocket.me/article/1628-which-ip-do-i-need-to-allow-for-wp-rocket). Add the current IP addresses from that page under `remote_addresses` before you use the rule.

```yaml
- name: allow-wprocket
  action: ALLOW
  user_agent_regex: WP-Rocket-SaaS
  remote_addresses:
    # Add the current IP addresses from the provider here, for example:
    - 192.0.2.0/24
```

### Other Integrations

#### Sendcloud

Allows the Sendcloud shipping platform from the [IP addresses published by Sendcloud](https://cdn.sendcloud.com/global-media/public-ips.txt). Add the current IP addresses from that page under `remote_addresses` before you use the rule.

```yaml
- name: allow-sendcloud
  action: ALLOW
  user_agent_regex: (?i)sendcloud
  remote_addresses:
    # Add the current IP addresses from the provider here, for example:
    - 192.0.2.0/24
```

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
