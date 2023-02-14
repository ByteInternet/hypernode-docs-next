---
myst:
  html_meta:
    description: Learn about Hypernode's approach in handling DDoS attacks and the
      steps they take to protect your website from Distributed Denial of Service.
    title: How Hypernode handles DDoS sttacks | Security
redirect_from:
  - /en/best-practices/security/how-does-hypernode-handle-ddos-attacks-/
---

<!-- source: https://support.hypernode.com/en/best-practices/security/how-does-hypernode-handle-ddos-attacks-/ -->

# How Does Hypernode Handle DDoS Attacks?

DDoS stands for **Distributed Denial of Service**. In the news you often hear that the website of a bank has been affected by this, but these attacks also occur with other types of websites. Unfortunately, we sometimes suffer from these attacks at Hypernode.

In this article we explain what a DDoS attack is and what Hypernode does when this occurs.

## How Does a DDoS Attack Work?

A DDoS attack tries to make millions of connections to a website. The server can only process x number of requests at a time. If the server is busy with all other requests, you will have to wait.

During a DDoS attack, special programs (flooders and bots) are used to set up many connections to a target location in quick succession.

When millions of simultaneous connections are made, it is only a matter of time before the server can no longer handle the number of requests. If you visit the website, your connection (request) will be placed in a queue. Since the server still has to process all other requests, you cannot reach the website.

## How Does Hypernode Handle a DDoS Attack?

When we notice irregularities in the traffic of a Hypernode, there are three steps we take:

1. Check if we can block the DDoS on the Hypernode itself, e.g. by blocking specific countries. When our automation detects suspicious requests, we take the precaution of blocking these requests by placing an NGINX configuration. By doing so, we can rule out recurrence of similar future attacks.
1. Check if we can block the DDoS at Combell via the 'NaWas', an industry standard anti DDoS setup in the Netherlands.
1. When the steps above are not enough, we can assist the user in setting up a special anti-DDoS setup, such as Cloudflare.

## What if a Hypernode Is the Source of the Attack?

It might happen that a Hypernode is the source of an attack . When this happens, we will disable this website. The reactivation of the website then falls under Hypernode's abuse policy.
