---
myst:
  html_meta:
    description: Learn how to enable Botstopper, choose an AI policy, and write custom
      Botstopper policies on Hypernode.
    title: How to use Botstopper on Hypernode | Hypernode
---

# How to Use Botstopper on Hypernode

Bot traffic has changed. Some bots still identify themselves with clear user agents, but many scrapers now use large sets of user agents or pretend to be a normal Chrome browser. That makes simple user-agent blocking less reliable.

Botstopper gives you control over this traffic before it reaches Magento, Shopware, or another application. It checks incoming requests and decides whether they should be allowed, blocked, or challenged. Botstopper is the commercial derivative of the open source project [Anubis](https://anubis.techaro.lol/).

Use Botstopper when bots cause high load, scrape content, crawl expensive layered navigation URLs, or ignore your `robots.txt` file. Botstopper also lets each merchant choose how strict they want to be with AI crawlers and AI clients.

```{tip}
For more background on bot traffic and Magento performance, see [How to Fix Performance Issues Caused by Bots and Crawlers](../../best-practices/performance/how-to-fix-performance-issues-caused-by-bots-and-crawlers.md).
```

## Enable Botstopper

Botstopper is disabled by default on a Hypernode. Enable it with:

```bash
hypernode-systemctl settings botstopper_enabled True
```

Disable it again with:

```bash
hypernode-systemctl settings botstopper_enabled False
```

## Configure Botstopper Per Vhost

Botstopper is enabled per vhost by default. This means that when you enable Botstopper on Hypernode level, Botstopper becomes active for all managed vhosts unless you disabled it for a specific vhost. See [Hypernode Managed Vhosts](../nginx/hypernode-managed-vhosts.md) for more information about vhost configuration.

Disable Botstopper for one vhost with:

```bash
hypernode-manage-vhosts example.com --disable-botstopper
```

Enable it again for that vhost with:

```bash
hypernode-manage-vhosts example.com --botstopper
```

## Choose an AI Policy

Botstopper has three AI policies. The default policy is `aggressive`.

```bash
hypernode-systemctl settings botstopper_ai_policy aggressive
hypernode-systemctl settings botstopper_ai_policy moderate
hypernode-systemctl settings botstopper_ai_policy permissive
```

| Policy       | Behavior                                                                                                         |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| `aggressive` | Blocks AI training crawlers, AI search crawlers, and AI clients as much as possible.                             |
| `moderate`   | Blocks AI training crawlers and unknown AI bots. Allows documented AI search bots and user-triggered AI clients. |
| `permissive` | Allows documented AI bots. Blocks unknown AI-style bots.                                                         |

Use `aggressive` if you want the strictest AI blocking. Use `moderate` if you want to block AI training while keeping documented AI search and user tools working. Use `permissive` if you only want to block unclear or undocumented AI crawlers.

Some AI crawlers also require `robots.txt` rules before they respect your opt-out. Botstopper blocks requests at the webserver layer, but `robots.txt` is still useful for crawlers that require policy signals there. See the [Magento 1 robots.txt](../../ecommerce-applications/magento-1/how-to-create-a-robots-txt-for-your-magento-1-shop.md) or [Magento 2 robots.txt](../../ecommerce-applications/magento-2/how-to-create-a-robots-txt-for-magento-2-x.md) articles if you need to configure one.

## How Botstopper Handles Requests

Botstopper evaluates policy rules from top to bottom. A rule can allow, deny, challenge, or weigh a request.

| Action      | What happens                                                 |
| ----------- | ------------------------------------------------------------ |
| `ALLOW`     | The request is sent to your shop immediately.                |
| `DENY`      | The request is blocked with HTTP `403`.                      |
| `CHALLENGE` | The visitor receives a browser challenge.                    |
| `WEIGH`     | Suspicion points are added or removed. Evaluation continues. |

`ALLOW`, `DENY`, and `CHALLENGE` stop evaluation immediately. The first matching rule wins.

`WEIGH` does not stop evaluation. Multiple `WEIGH` rules can match the same request. After all rules are checked, Botstopper uses the final weight to decide whether the request should be allowed or challenged.

Challenge responses use HTTP `200`. This is intentional. Many aggressive scraper bots stop retrying once they receive a `200` response.

## Standard Hypernode Policies

Hypernode ships Botstopper with a standard policy that keeps important services working and blocks common abusive traffic.

The standard policy does the following:

1. Allows Hypernode platform services, payment providers, monitoring tools, and common e-commerce integrations.
1. Allows IP addresses on the Hypernode WAF allowlist.
1. Runs your custom pre-policy from `/data/web/botstopper/pre.policy.yml`.
1. Denies sensitive Magento media paths, such as `/media/customer/`, `/media/import/`, and `/media/downloadable/`.
1. Allows storefront assets, such as `/static/`, normal `/media/` files, etc.
1. Denies or weighs known bad bots, headless browsers, abusive cloud ranges, and suspicious HTTP clients.
1. Applies the configured AI policy.
1. Allows known good search engine crawlers when they are verified by IP ranges or reverse DNS.
1. Allows common public files, such as `robots.txt`, `sitemap.xml`, `favicon.ico`, and `.well-known` paths.
1. Adds suspicion weight for some high-risk countries, networks, and browser-like user agents.
1. Runs your custom post-policy from `/data/web/botstopper/post.policy.yml`.
1. Uses the final suspicion weight to allow or challenge the request.

The WAF allowlist is shared with the Hypernode firewall allowlist. Botstopper allows these IPs before your custom `pre.policy.yml` and before the standard deny and challenge rules.

Add a trusted IP to the WAF allowlist with:

```bash
hypernode-systemctl whitelist add waf 1.2.3.4 --description "Office IP"
```

View the WAF allowlist with:

```bash
hypernode-systemctl whitelist get --type waf
```

See [How to allowlist FTP, WAF and database](../../best-practices/firewall/ftp-waf-database-allowlist.md) for more details.

The order matters. For example, a broad `DENY` rule in `pre.policy.yml` can block a good crawler before the standard verified crawler allow rules are reached.

## Write Custom Policies

You can add your own rules in these files:

| File                                   | When it runs                                         | Use it for                                                        |
| -------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------- |
| `/data/web/botstopper/pre.policy.yml`  | Before most standard deny and challenge rules        | Allowing trusted traffic or blocking very specific traffic early. |
| `/data/web/botstopper/post.policy.yml` | After standard rules, before final weight thresholds | Adding suspicion weight or handling fallback cases.               |

Both files contain a YAML list of policy rules. An empty file looks like this:

```yaml
[]
```

Edit the files as the `app` user. For example:

```bash
sensible-editor /data/web/botstopper/pre.policy.yml
```

After changing a policy file, restart Botstopper:

```bash
hypernode-servicectl restart techaro-botstopper@default.service
```

## Policy Conditions

A policy rule can match on request details, such as the client IP, user agent, path, or headers.

Common fields are:

| Field              | Checks                                                |
| ------------------ | ----------------------------------------------------- |
| `remote_addresses` | Client IP address against CIDR ranges.                |
| `user_agent_regex` | The `User-Agent` header against a regular expression. |
| `path_regex`       | The request path against a regular expression.        |
| `headers_regex`    | Request headers against regular expressions.          |
| `expression`       | A custom expression for advanced matching.            |

When a rule has multiple conditions, all conditions must match. This is useful for trusted allow rules. For example, you can allow a monitoring tool only when both its user agent and source IP match.

## Examples

Allow a trusted monitoring service:

```yaml
- name: allow-my-monitor
  action: ALLOW
  user_agent_regex: MyMonitor
  remote_addresses:
    - 203.0.113.10/32
```

Block a specific bot:

```yaml
- name: block-bad-bot
  action: DENY
  user_agent_regex: BadBot
```

Challenge traffic to an expensive search page:

```yaml
- name: challenge-suspicious-search
  action: CHALLENGE
  path_regex: ^/catalogsearch/result/.*
```

Add suspicion weight for bots crawling layered navigation URLs:

```yaml
- name: weigh-layered-navigation-bots
  action: WEIGH
  path_regex: ^/.*(color|size|brand)=.*
  user_agent_regex: (?i:bot|crawler|spider)
  weight:
    adjust: 20
```

Protect a trusted integration from a broader custom rule:

```yaml
- name: allow-partner-feed
  action: ALLOW
  path_regex: ^/partner/feed/.*
  user_agent_regex: PartnerFeedClient
  remote_addresses:
    - 198.51.100.0/24
```

Allow JSON API requests, using [CEL expressions](https://anubis.techaro.lol/docs/admin/configuration/expressions):

```yaml
- name: allow-api-requests
  action: ALLOW
  expression:
    all:
      - '"Accept" in headers'
      - 'headers["Accept"] == "application/json"'
      - 'path.startsWith("/api/")'
```

You usually do not need allow rules for API or webhook traffic. Botstopper allows traffic by default. Use an `ALLOW` rule when you already have, or plan to add, a broader custom rule that could otherwise challenge or block this trusted traffic.

## Logging

The botstopper service logs to `/var/log/botstopper/botstopper.log`. The log file consists [JSON Lines](https://jsonlines.org/), meaning that each line in the log file is a JSON-parseable line.

You can render the entire log file:

```bash
cat /var/log/botstopper/botstopper.log | jq .
```

Or follow the log file

```bash
tail -f /var/log/botstopper/botstopper.log | jq .
```

## Safe Policy Changes

Use specific rules whenever possible. Broad user-agent rules can block legitimate crawlers or integrations.

Prefer `WEIGH` when you are not fully sure traffic should be blocked. A `WEIGH` rule lets Botstopper combine multiple signals before it challenges the request.

Use `ALLOW` with both a user agent and IP range for trusted services when possible. User agents can be spoofed, IP ranges are harder to fake.

Use the WAF allowlist for trusted source IPs that should always bypass Botstopper checks. This is often better than maintaining your own IP allow rule in `pre.policy.yml`.

Keep custom `DENY` rules narrow. A broad `DENY` rule in `pre.policy.yml` can override the standard Hypernode allow rules that run later.

Do not add allow rules for every API endpoint or webhook. Add them when a specific Botstopper rule would otherwise match that traffic.

## Anubis Documentation

Because Botstopper is the commercial derivative of Anubis, the Anubis documentation is a useful reference when you want to understand the underlying concepts or write advanced custom policies:

- [How Anubis works](https://anubis.techaro.lol/docs/design/how-anubis-works)
- [Anubis policies](https://anubis.techaro.lol/docs/admin/policies/)
- [Anubis policy thresholds](https://anubis.techaro.lol/docs/admin/configuration/thresholds)
