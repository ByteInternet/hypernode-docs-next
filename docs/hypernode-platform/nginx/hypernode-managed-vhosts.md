---
myst:
  html_meta:
    description: Learn all about The Hypernode Managed Vhosts (HMV). The system is
      an easy to use, yet powerful, system of configuring Nginx on Hypernode.
    title: How to enable and manage Hypernode Vhosts?
redirect_from:
  - /en/hypernode/nginx/hypernode-managed-vhosts/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/hypernode-managed-vhosts/ -->

# Hypernode Managed Vhosts

The Hypernode Managed Vhosts (HMV) system is an easy to use, yet powerful, system of configuring Nginx on Hypernode. A vhost is a configuration that allows you to setup multiple domainnames, each with it's own, independent, configuration. With it, you can easily host a Wordpress blog on a subdomain, and a Magento on your main domain, set up HTTPS for both automatically, and efficiently redirect visitors to your www-domain.

The main advantage of HMV is that it separates your Nginx config into a global folder, containing configuration for all server blocks, and domain specific configs, giving you more control and reducing unexpected side-effects of domain specific configurations.

## Enabling Managed Vhosts

The Hypernode Managed Vhosts (HMV) system is currently enabled by default on all new booted Hypernodes.

However if you have a Hypernode created before 01-05-2020 your Hypernode may still be running in 'legacy' mode. To enable the HMV you can run the command:

`hypernode-systemctl settings managed_vhosts_enabled True`.

This will convert your current legacy config into the HMV config. It will also convert all currently active vhosts into managed vhosts.

Please note that while switching to HMV is very easy, there are a few things to check after switching to make sure everything works, as not every setting is automatically transferred.

Run `hypernode-manage-vhosts --list` to get an overview of your current configuration and use the list below to check if it's correct. Not everything will apply to your Hypernode.

- Make sure your domain is the default server instead of the Hypernode. You can do this by running the following command:

`hypernode-manage-vhosts www.example.com --default-server`

- Configure the vhosts to only use HTTPS. If you already have an SSL certificate configured and you don't want to use Let's Encrypt, use this command:

`hypernode-manage-vhosts www.example.com --https --force-https --ssl-noclobber`

This will make sure you won't overwrite the existing SSL certificate.

If you do want to configure Let's Encrypt for the vhost you can use this command:

`hypernode-manage-vhosts www.example.com --https --force-https`

- If you make use of Varnish, make sure to enable Varnish for the specific vhosts:

`hypernode-manage-vhosts www.example.com --varnish`

- Want to redirect all traffic over www? Set up your naked domains to be wwwizers, with this command:

`hypernode-manage-vhosts --type wwwizer [example.com](//example.com)`

Please make sure to also double check your custom Nginx configurations, as these might not be converted automatically.

You can always use `hypernode-manage-vhosts --help` to get more information on the different configurations.

## Managing Vhosts

Once the Hypernode Managed Vhosts (HMV) system is enabled, you can start defining and configuring your vhosts. On new booted Hypernodes there will be one vhosts by default: example.hypernode.io.

### Adding Vhosts

To add a new vhost, for example the domainname [www.example.com](http://www.example.com), to your configuration, you can simply run the command `hypernode-manage-vhosts www.example.com`. This will create a new vhost configuration in /data/web/nginx/[www.example.com/](http://www.example.com/), using the Magento 2 template. You can define the configuration template to use, by using the `--type` argument. For example, you can use the Magento 1 config by using the command `hypernode-manage-vhosts --type magento1 www.example.com`. You can choose from 'magento1', 'magento2', 'akeneo', 'vuestorefront', 'generic-php', 'wordpress' and more. For a complete list of available templates you can run the command `hypernode-manage-vhosts --help`.

Important: Simply creating the folder [www.example.com](http://www.example.com) does NOT create a vhost. You will need to use the `hypernode-manage-vhosts` command

Please note that defining the vhosts '[www.example.com](http://www.example.com)', does not automatically add 'example.com' as a vhost. You will have to manually define a vhost for this. Since most people simply want their 'example.com' to redirect to '[www.example.com](http://www.example.com)', you can simply use the --type wwwizer argument to set this up. This will configure the vhost to redirect all traffic to the www-version of the domain.

\***We highly advise against using symlinks in your vhost configuration as this may lead to issues at a later date in in your nginx config.**

### Removing Vhosts

To remove an existing vhost, for example the domainname [www.example.com](http://www.example.com), from your configuration, you can simply run the command `hypernode-manage-vhosts --delete www.example.com`. This will remove the vhost configuration, and remove /data/web/nginx/[www.example.com](http://www.example.com).

Please note that simply deleting the /data/web/nginx/[www.example.com/](http://www.example.com/) folder will NOT remove the vhost, but merely leave it in an unconfigured state.

### Changing Vhosts

Once a vhost is configured, you cannot change the template used to create it. This is because the files from the templates are placed as a user-editable files, and changes may have been made to these. It is, however, possible to manually change the configuration. Alternatively, you can remove and recreate the vhost with the correct type. Please do note that this will remove all the existing configuration made for this specific domain name.

### Listing Vhosts

To list all configured vhosts you can run the command:

`hypernode-manage-vhosts --list`

This will provide a nice overview of all the vhosts with useful information like is it the *default_server*, is *Let's Encrypt* configured, or is *Varnish* enabled.

### Setting a different webroot

Sometimes you have to use a different webroot, for example when you're running multiple applications on one Hypernode. In that case, you can specify the webroot by providing the *--webroot* option:

`hypernode-manage-vhosts example.com --webroot /data/web/my_other_application/public`

Please take not that the webroot option is not used for the built-in staging for your vhost, that will still point to */data/web/staging* by default.

## Let’s Encrypt and Hypernode Managed Vhosts

**Please note: If you want to use Let’s Encrypt and have the Hypernode Managed Vhosts (HMV) system enabled, you need to configure LE during the creation of the vhost. Using the old method with *dehydrated* won't work!**

First, check if HMV is enabled on your Hypernode:

`hypernode-systemctl settings managed_vhosts_enabled`

If so, it will give the following output:

`managed_vhosts_enabled is set to value True`

If you want to request a LE certificate you need to add the `--https` flag with the HMV-command.

`hypernode-manage-vhosts www.example.com --https --force-https`

This command will not only request a LE Certificate but because of the `--force-https`flag it will also redirects all traffic for that specific vhost to HTTPS.

## Varnish and Hypernode Managed Vhosts

Using Varnish in combination with Varnish works slightly different with HMV enabled. Of course Varnish needs to be enables with the **systemctl** tool. `hypernode-systemctl settings varnish_enabled True`

But with HMV you need to configure the vhost for Varnish as well. You can do this by adding the `--varnish`flag to you HMV-command. For example: `hypernode-manage-vhosts example.com --varnish`

Once you the command is processed you could list all the vhost to check if Varnish is enabled for that Vhost. The value in the Varnish column should be set to **True**.

To disable Varnish for a vhost, use the following command: `hypernode-manage-vhosts example.com --disable-varnish`

## Managing Configuration Files

### Vhost-specific configuration

Once you have setup a vhost, say [www.example.com](http://www.example.com), you can place your domain specific configuration in its configuration folder, /data/web/nginx/[www.example.com](http://www.example.com). You can do this the same way you configured your legacy, or global configuration. Simply place a file with a `server.` prefix, and it will be included in the vhost's server {} configuration block. You can also still use the `public.` and `staging.` prefixes, if you wish to have public, or staging, specific configuration.
Please note that any files with the 'HTTP.' prefix will also be loaded in the HTTP context. Nginx, however, only has a single http context. As such, any http configuration placed in a vhost, will also be loaded for all other vhosts.

### Global configuration

Even when using the Hypernode Managed Vhosts (HMV) system, it's still possible to setup configuration on the 'global' level by placing a file in `/data/web/nginx`.

### Multi-domain configuration

If you have multiple vhosts, and want to share configuration between them, without placing this in the global context, you can do so using symlinks. Simply remove a domain specific folder and replace it with a symlink to another domain's folder.

## Troubleshooting

If you are running into issues (e.g. SSL or other configuration errors) with Hypernode Managed Vhosts, we recommend running this command first:

`hypernode-manage-vhosts --all`

This regenerates the HMV configuration based on what is set in `hypernode-manage-vhosts --list` and in our experience resolves most basic issues with Hypernode Managed Vhosts.
