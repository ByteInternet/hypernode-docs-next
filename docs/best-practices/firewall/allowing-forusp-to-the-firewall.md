---
myst:
  html_meta:
    description: Learn how to allow FocusP on the Hypernode Allowlists
    title: Allowing FocusP to the Firewall | Hypernode
---

# How to add ForusP to the whitelist

To ensure that ForusP can perform their scan on your Hypernode without anyissues, the IP addresses associated with ForusP must be added to the Hypernode Web Application Firewall (WAF). The WAF acts as a layer of protection by filtering incoming traffic and blocking potential threats. Adding the necessary IP addresses to the allowlist ensures that the scanning process runs smoothly without interruptions. You can achieve this by either using the Hypernode Control Panel or by executing commands directly on the server using the command-line interface (CLI).

## Adding IP Addresses in the allowlist via the Control Panel

Follow these steps to add ForusP's IP addresses using the Hypernode Control Panel:

- Go to to my.hypernode.com
- Log in with your credentials
- Once logged in, select the Hypernode you wish to configure
- Click on **Allowlist** from the menu
- Select **Rule type** and choose **WAF** from the dropdown
- Enter the IP address you want to allow
  IP addresses ForusP: **154.16.73.227** | **132.226.222.205** | **144.24.249.196**
- Provide a descriptive name for the entry for example ForusP. Use descriptive names when adding entries to help identify their purpose in the future.
- Click on **Save** to apply the changes

Repeat the steps above to add the others. The IP addresses you add will become active within a few minutes, allowing ForusP to access your Hypernode environment without being blocked by the firewall.

## Adding IP Addresses by using CLI

For users comfortable with the command-line interface, you can add the IP addresses directly on the server. This requires logging into the server using SSH. Follow these steps:

```bash
hypernode-systemctl whitelist add waf 154.16.73.227 --description "ForusP"
hypernode-systemctl whitelist add waf 132.226.222.205 --description "ForusP"
hypernode-systemctl whitelist add waf 144.24.249.196 --description "ForusP"
```

By following the steps outlined above, you can ensure that ForusP has the necessary access to perform scans on your Hypernode environment without encountering any firewall-related issues. Proper configuration of the WAF helps maintain a secure and efficient system while allowing trusted services to operate seamlessly.
