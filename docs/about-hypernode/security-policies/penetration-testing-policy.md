---
myst:
  html_meta:
    description: Hypernode's policy for customers that wish to run a pentest on their
      website
    title: Penetration Testing Policy | Security | Hypernode
---

# Customer Pentest Policy

```{important}
This policy is for customers that wish to perform an external penetration test on their own hosting environment. For Unaffiliated third-parties that wish to test the Hypernode platform itself, we have a separate [Responsible Disclosure Policy](responsible-disclosure-policy.md).
```

At Hypernode, we support responsible security testing practices that help customers improve the safety and resilience of their hosted application, and our platform. Customers may conduct penetration tests on their own hosting environments under the following conditions and guidelines.

## Scope of Testing

Penetration testing is only permitted on the customer's *own* hosting space. Testing must not extend to, or affect, any other part of the platform or infrastructure managed by either Hypernode, or other Hypernode customers..

## Requirements

Penetration testing is allowed under the following conditions:

- All pentests must be performed by a reputable, experienced, party.
- You will [inform us](https://www.hypernode.com/en/support/) at least 72 hours ahead of time, and let us know the time, source IP(s) and target of the pentest.
- If the pentest causes, or discovers, any server side issues, you will share the full report of the pentest with us afterwards. You will keep these findings confidential, untill we've had the opportunity to assess and address the issue.

We do not allow pentests that:

- Rely on Social Engineering.
- Perform Brute Force testing.
- Test (D)DoS protection or -resilience.
- Test Physical Security of Datacenters, Offices, etc.
- May cause permanent damage to hardware or equipment.

You may wish to add the source IP's of the pentest to the [Hypernode WAF allowlist](./../../best-practices/firewall/ftp-waf-database-allowlist.md), to prevent our automated systems from affecting the test.

## Security Waivers

Hypernode explicitly gives its customers permission to test their own Hypernode hosting environment. If your penetration testing partner still requires a signed waiver, please [contact us](https://www.hypernode.com/en/support/).

# Hypernode's Own Pentest Policy

Hypernode performs regular penetration tests of both the Hypernode hosting platform, and its internal applications like the Hypernode Control Panel. Details about these penetration tests are available for customers [upon request](https://www.hypernode.com/en/support/).
