---
myst:
  html_meta:
    description: 'Sometimes you want to use multiple PHP versions to test a Magento update as Example. 
      Find out how to enable and use alternative PHP versions.'
    title: How to use Alternative PHP versions? | Hypernode
---

# Enable alternative PHP versions

Alternative PHP versions are disabled by default. Please contact our support department if you want to make use of this feature.
We will enable it for your Hypernode and you can start using it using the CLI.

# How to use alternative PHP versions

Please make sure the alternative PHP version feature is enabled for your Hypernode as described above.
You can list, enable and disable the alternative PHP versions on your Hypernode using the `hypernode-systemctl` command.

## List alternative PHP versions

To list the enabled alternative PHP versions, you can use the following command:

```bash
hypernode-systemctl alternative_php_versions list
```

The output will tell you the enabled PHP versions, please note that this does not contain your main system PHP version.

```bash
Currently enabled PHP versions are ['8.3', '7.1', '8.0'].
```

## Enable alternative PHP version

To enable an alternative PHP version on your Hypernode, you can make use of the `enable` command:

```bash
hypernode-systemctl alternative_php_versions enable 8.2
```

The specified PHP version will be enabled and may take some time to complete. You can follow the progress by using `livelog`:

```bash
ACTION                          START                   END                     STATE           TASKS   RUNNING
update_node                     2024-06-03T10:21:28Z    2024-06-03T10:21:32Z    running         7/9     php_update_node_to_update_flow
```

## Disable alternative PHP version

If you dont use a specific alternative PHP version anymore you may want to disable the alternative PHP version:

```bash
hypernode-systemctl alternative_php_versions disable 8.2
```

# Configure vhost to adapt alternative php version

Once you have the desired alternative PHP versions enabled, you can associate them with the desired Vhost.
You can do this by using Hypernode managed vhosts (hmv).

You can specify an alternative PHP handler for the desired vhost:

```bash
hmv <my_vhost> --handler phpfpm83alt
```

You can list the available PHP handlers on your Hypernode:

```bash
hmv <my_vhost> --help
```

You see as example

```bash
--handler {phpfpm,phpfpm83alt,phpfpm71alt,phpfpm80alt}
```

*Please note that you can only specify the handlers for the enabled alternative PHP versions.*
