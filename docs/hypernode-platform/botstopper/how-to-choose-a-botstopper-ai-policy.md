---
myst:
  html_meta:
    description: Learn what Botstopper AI policies block and how aggressive, moderate,
      and permissive differ. Choose the right AI policy for your webshop on Hypernode.
    title: How to Choose a Botstopper AI Policy | Hypernode
---

# How to Choose a Botstopper AI Policy

AI crawlers and AI tools fetch your webshop in different ways: some train AI models on your content, others feed AI search results, and some retrieve a page because a person asked an AI tool to open it. This article explains how the Botstopper AI policy decides which of these are allowed and helps you choose one.

```{tip}
Start with [How to Use Botstopper on Hypernode](./how-to-use-botstopper.md) if you want to learn how Botstopper works and how to enable it.
```

## Set the AI Policy

The default AI policy is `aggressive`. Change it with:

```bash
hypernode-systemctl settings botstopper_ai_policy aggressive
hypernode-systemctl settings botstopper_ai_policy moderate
hypernode-systemctl settings botstopper_ai_policy permissive
```

## What Each Policy Blocks

Botstopper sorts AI traffic into categories and treats them differently per policy:

| AI traffic type                                                                 | `aggressive` | `moderate`            | `permissive`          |
| ------------------------------------------------------------------------------- | ------------ | --------------------- | --------------------- |
| Unknown or undocumented AI bots                                                 | Blocked      | Blocked               | Blocked               |
| AI training crawlers (`GPTBot`, `ClaudeBot`)                                    | Blocked      | Blocked               | Allowed when verified |
| AI search crawlers (`OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`)       | Blocked      | Allowed when verified | Allowed when verified |
| AI clients (`ChatGPT-User`, `Claude-User`, `MistralAI-User`, `Perplexity-User`) | Blocked      | Allowed when verified | Allowed when verified |
| Google AI fetchers (`Google-GeminiNotebook`, `Google-Agent`)                    | Blocked      | Blocked               | Allowed when verified |

Unknown AI bots are blocked in every policy. These are bots that use an AI-style user agent but are not documented by a legitimate vendor.

## What "Verified" Means

A documented AI bot is only allowed when its request matches both the user agent the vendor documents **and** the IP ranges the vendor publishes. This is called **verification**.

A bot that sends a real `Claude-User` user agent from a random IP is not verified. It does not receive the allow rule and continues through the normal Botstopper rules instead. Verification prevents attackers from bypassing Botstopper by copying a bot's user agent.

## Which Policy Should You Choose

Choose `aggressive` if you want no AI bots fetching your webshop at all. This is the default. Choose `moderate` if you want to stop AI training crawlers while keeping AI search results and AI tools that people use to open or summarize your pages working. Choose `permissive` if AI traffic is welcome, including training crawlers, as long as the bot is documented and verified.

## What Stays the Same in Every Policy

The AI policy only changes how AI bots are treated. Verified search engine crawlers, such as Googlebot and Bingbot, are allowed in every policy, and only crawlers verified by IP or reverse DNS get this allow rule. Requests that submit forms or place orders (`POST` requests) are never challenged. Headless browsers, abusive bots, and hostile cloud ranges are always blocked, while platform traffic, payment providers, monitoring tools, and the WAF allowlist are always allowed. Regular visitor traffic is weighed and challenged the same way in every policy.

## Create Exceptions for AI Bots

Your custom pre-policy runs before the AI policy rules. Use it to allow or block specific AI traffic for your webshop, regardless of the AI policy. For example, allow one AI search crawler while `aggressive` blocks the rest.

1. Edit the file as the `app` user:

```bash
sensible-editor /data/web/botstopper/pre.policy.yml
```

1. Restart Botstopper after changing a policy file:

```bash
hypernode-servicectl restart techaro-botstopper@default
```

```{warning}
A rule in your pre-policy can block traffic that the standard rules would otherwise allow. Keep custom `DENY` rules narrow, and combine a user agent with an IP range in `ALLOW` rules. See [Write Custom Policies](./how-to-use-botstopper.md#write-custom-policies) for details.
```

Your post-policy runs after the AI rules. It cannot override an AI block: once a `DENY` rule matches, evaluation stops.

## Verify the Result

Check which requests Botstopper allows, blocks, or challenges with:

```bash
hypernode-parse-botstopper-log --today
```

See [How to View Botstopper Logs on Hypernode](./how-to-view-botstopper-logs.md) for filtering options, for example by user agent or client IP.

## Keep `robots.txt` in Order

Some AI vendors only respect an opt-out through `robots.txt`, not through blocked requests. Botstopper blocks requests at the webserver layer, but a `robots.txt` is still useful for crawlers that require a policy signal there. See the [Magento 1 robots.txt](../../ecommerce-applications/magento-1/how-to-create-a-robots-txt-for-your-magento-1-shop.md) or [Magento 2 robots.txt](../../ecommerce-applications/magento-2/how-to-create-a-robots-txt-for-magento-2-x.md) articles if you need to configure one.
