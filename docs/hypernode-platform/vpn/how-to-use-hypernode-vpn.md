---
myst:
  html_meta:
    description: 'Hypernode-vpn offers a secure way of directly connecting to your
      database from any location. See intstructions that guide you through the process. '
    title: How to use hypernode-vpn?
redirect_from:
  - /en/hypernode/vpn/how-to-use-hypernode-vpn/
---

# Hypernode-vpn documentation

Hypernode-vpn offers a secure way of directly connecting to your database from any location.
Using [OpenVPN](https://openvpn.net/).

## How it works

Our Hypernode-vpn solution implements a standard OpenVPN TLS tunnel to the Hypernode.
Which can be used to talk to the MySQL database securely.
You simply enable OpenVPN on your Hypernode and all the required packages and configuration are installed automatically.
The automation will generate a default user configuration which you can use to connect to the Hypernode.

### Using OpenVPN

To be able to connect to your Hypernode you will need to install the latest version of the
[OpenVPN client](https://openvpn.net/index.php/open-source/downloads.html).

### Enable / Disable

This can simply be done on the Hypernode itself.

```
hypernode-systemctl settings openvpn_enabled --value <True/False>
```

This command will trigger the Hypernode automation to start installing OpenVPN and generate the configuration.
Or delete all the configuration when disabling.

### Client configuration

After the installation process is complete the client configuration can be found in `/data/openvpn/client-configs`.
Normally the standard configuration will be called something like `openvpnclient.<appname>.<domain>.ovpn`.
Place this file in your OpenVPN config directory on your PC/device.
This file contains the OpenVPN private key for you Hypernode, so keep it secure!

### Connecting

When you have downloaded your client configuration use it to connect to your Hypernode.

Linux example

```
$ sudo openvpn --config /etc/openvpn/openvpnclient.erikhyperdev.hypernode.io
```

Windows example

```
# Make sure the client config is placed in the correct directory
# Normally this is C:/ProgramFiles/OpenVPN/config
Start OpenVPN-GUI
SystemTray -> OpenVPN-GUI -> openvpnclient.erikhyperdev.hypernode.io -> Connect
```

### Using OpenVPN

Once connected the standard configuration will make a new tunnel interface on your local device.
The `192.168.255.0/24` subnet will be used for VPN communication.
So when talking to the Hypernode by default use `192.168.255.1` as the IP address.

MySQL example:

```
$ mysql -u app -p -h 192.168.255.1
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 540
Server version: 5.6.37-82.2-log Percona Server (GPL), Release 82.2, Revision d1eb51005df

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```
