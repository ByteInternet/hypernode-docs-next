---
myst:
  html_meta:
    description: This is extremely useful if you want to test your shop without changing
      the DNS settings for your domain. Learn more.
    title: Test your website by changing your Hosts File | Hypernode
redirect_from:
  - /en/best-practices/testing/how-to-test-your-website-by-changing-your-hosts-file/
---

<!-- source: https://support.hypernode.com/en/best-practices/testing/how-to-test-your-website-by-changing-your-hosts-file/ -->

# How to Test Your Website by Changing Your Hosts File

## Introduction

Modifying your hosts file or `/etc/hosts` enables you to test your site without the need of a DNS record.
Using this mechanism, you can change the DNS settings for a domain only on the machine you are working on.
This is extremely useful if you want to test your shop without changing the DNS settings for your domain. You can use this for example, before going live to verify whether a shop is fully functional before pointing the DNS records to that server.

Modifying your local hosts file makes your local machine use the IP addresses specified in the file rather than using DNS lookups. To modify the hosts file, you create an entry for the domain you want to point to the ip address that you want the site to resolve to.

For example, adding the following line, to your hosts file, will point the records `www.domain.com` and `domain.com` to the ip address `1.2.3.4`:

```nginx
1.2.3.4 www.domain.com domain.com
```

In this article, we'll provide instructions for adjusting the hosts file on the following operating systems:

- Windows 10, Windows 8, Windows 7
- Linux
- Mac OS X

After you add the domain information and save the file, your system immediately will resolve the domain name to the specified IP address.

**When you are done testing, remove the entries quickly as it is hard to debug afterwards why your DNS is not behaving as expected on different computers.**

## Windows

Windows 10, Windows 8, Windows 7, and Windows Vista make use of `User Account Control` (UAC), so run Notepad as an Administrator, using the `runas` functionality.

### Windows 8 and Windows 10

- Press the Windows key.
- Type `Notepad` in the search field.
- In the search results, right-click `Notepad` and select `Run as administrator`.
- From Notepad, open the following file: `c:\Windows\System32\Drivers\etc\hosts`
- Make your changes to the file.
- Click `File` > `Save` to save your changes.

## Windows 7

- Click `Start` > `All Programs` > `Accessories`.
- Right-click `Notepad` and select `Run as administrator`.
- Click `Continue` on the Windows needs your permission `UAC` window.
- When `Notepad` opens, click `File` > `Open`.
- In the `File name` field, type `C:\Windows\System32\Drivers\etc\hosts`.
- Click `Open` and make your changes to the file.
- Click `File` > `Save` to save your changes.

## Linux

- Open a terminal window.
- Open the hosts file in your favorite text editor by issuing following command:

`sudo sensible-editor /etc/hosts`

- Enter your sudo password when asked.
- Skip over the present lines and make your edits at the bottom of the file.
- Make your changes to the file.
- Save your edit to te file.

## Mac OS X

- Open a terminal window.
- Open the `/etc/hosts` file by issuing the following command in the terminal prompt:

`sudo nano /etc/hosts`

- Type your sudo password when asked.
- Edit the `/etc/hosts` file.
- Skip over the present lines and make your edits at the bottom of the file.
- Save your edit to the file.
- Make your changes take effect by flushing your computer's DNS cache:

`dscacheutil -flushcache`

The changes should take effect immediately after flushing.
