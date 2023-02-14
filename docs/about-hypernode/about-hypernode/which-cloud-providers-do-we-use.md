---
myst:
  html_meta:
    description: Hypernode uses a range of cloud providers to host its advanced hosting
      platform, including Combell OpenStack, DigitalOcean, and Amazon Cloud Services.
    title: Cloud Providers used by Hypernode | Hypernode
redirect_from:
  - /en/about/about-us/which-cloud-providers-do-we-use/
---

<!-- source: https://support.hypernode.com/en/about/about-us/which-cloud-providers-do-we-use/ -->

# Which Cloud Providers Do We Use

Hypernode is an advanced e-commerce cloud hosting platform for webshops. The Hypernode platform is developed independently from a specific cloud provider, allowing us to choose only the best providers and switch from providers if needed. Price, location, cooperation, and infrastructure are the main aspects we consider when choosing a cloud provider. Outsourcing the hardware part of hosting enables us to focus solely on what we're good at and that is continuously improving the Hypernode technology.

## Which Cloud Providers Do We Use?

Our Hypernode platform is available to webshops worldwide. Our customers can choose from a wide range of data centers around the world.

### Combell OpenStack

After years of preparation, testing, and improvement, we started using the OpenStack platform within the Combell Group in 2018. We both are part of team.blue. Using Combell OpenStack lets us take matters into our own hands because we have direct contact with colleagues instead of a supplier.

If you order a trial or hosting plan (Falcon) your Hypernode will be booted in Ghent, Belgium.

**Advantages Combell OpenStack**

- We influence the roadmap and, therefore, have more flexibility in achieving what we want.
- Combell OpenStack provides the same uptime guarantee as DigitalOcean: 99.9% for the Falcon line.
- Just as good or even better performance than DigitalOcean
- In the case of incidents and issues, we have direct communication lines
- Combell OpenStack uses only the latest hardware. Booting a new node is much faster compared to DigitalOcean
- Combell OpenStack offers Snapshots backups

**Disadvantages Combell OpenStack**

Combell OpenStack has only one data center in Ghent (Belgium).

### DigitalOcean

DigitalOcean is an innovative and relatively young hosting party that focuses purely on the wishes of developers instead of end users. This works very well for us because their focus is entirely on what is essential for good stable hosting. Our Hypernode platform builds the bridge between the developer and the end user.

We use DigitalOcean for shops that want their Hypernode to be located in a data center outside Western Europe.

**Advantages DigitalOcean**

- The innovative and young company
- We have good contact with their engineers to discuss our wishes
- Uptime guarantee: 99.9% for the Pelican line
- Reliable and stable infrastructure
- Unlimited IOPS (Input / Output operations per second)

**Disadvantages DigitalOcean**

- Less influence on roadmap compared to Combell OpenStack. We are one of many customers.
- DigitalOcean uses a mix of older and newer (faster) hardware, meaning we need to search for the best hardware when booting a Hypernode. This takes time.
- Backup creation is done differently. Backups are created on the node and transferred to a different location. Both creation and restoration take more time compared to snapshot backups.
- DigitalOcean does not use shared storage. In case of issues with a hypervisor, an email ticket needs to be submitted before an engineer takes action and reboots a hypervisor. This may cost precious time.

### Amazon Cloud Services (AWS)

All our Hypernode Eagle plans are hosted at AWS.

Cloud provider Amazon is the market leader in web hosting. Amazon offers top quality: a very stable and innovative platform that offers Hypernode a lot of space for developing and offering intelligent and handy features on the Hypernode platform.

**Advantages AWS**

- Most stable platform of all cloud hosters
- Uptime guarantee of 99.95%
- Speedy backup process via snapshots
- Super fast and stable IOPS (Input / Output operations per second)
- Excellent maintenance policy, including good communication
- Shared storage for hypervisors. In case of issues, a reboot only takes 2 minutes

**Disadvantages AWS**

- The IOPS are not unlimited. If your shop is not well-optimized and has a lot of visitors, it may hit the limits of the Hypernode. The good news about Amazon’s policy is that you will never suffer from busy neighbors :-).

## Your Hypernode in a Different Data Center

If you order a trial or hosting plan (Falcon) your Hypernode will be booted in Ghent, **Belgium**.

If you ordered a Hypernode Eagle plan, your Hypernode is booted in Frankfurt (**Germany**).

If your main target group is outside of Western Europe, you can move your shop to a different data center closer to your customers.

This can be arranged.

Email support@hypernode.com and let us know your data center of choice. Your shop will be moved manually to the new data center, depending on your agreed date and time. We only move Hypernodes during [our office hours](https://www.hypernode.com/contact-us/).

### Location of Data Centers

**DigitalOcean:** London, Frankfurt, New York, San Francisco, Toronto, Bangalore, Singapore

[**AWS:**](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) N. Virginia, Ohio, N. California, Oregon, Central Canada, Frankfurt, Ireland, London, Paris, Tokyo, Seoul, Osaka, Singapore, Sidney, Mumbai, São Paulo

### Keep in Mind

Moving your Hypernode to a new data center will lead to a new IP address. You may need to change the DNS settings of your domains or whitelist the new IP address to make sure certain connections with third parties (like payment providers) keep working.
