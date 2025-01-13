---
myst:
  html_meta:
    description: 'Need to upgrade or downgrade your Hypernode plan? Learn how to use
      the Hypernode command line interface (CLI) to easily change your hosting plan. '
    title: How to change your plan via the CLI? | Hypernode
redirect_from:
  - /en/services/control-panel/how-to-change-your-plan-via-the-cli/
---

<!-- source: https://support.hypernode.com/en/services/control-panel/how-to-change-your-plan-via-the-cli/ -->

# How to Change Your Plan via the CLI

**Please note that this article only applies to Control Panel customers that log in via my.hypernode.com.**

## Allowing Plan Changes via the CLI

To allow plan changes for a specific Hypernode plan via the command line, follow the steps below:

- Navigate go the Change plan page.
- Click on the CLI tab, enable plan changes via the CLI.

**Please note:** when enabled, **everyone who has SSH access can change the plan from the CLI**, even if they are not the Owner or Admin.

## Changing Your Plan via the CLI

The command to change your plan is `hypernode-systemctl xgrade` followed by the plan code.

For example if you want to change the plan to a Falcon 2XL plan you can use the following command: `hypernode-systemctl xgrade FALCON_2XL_202203`

You can also schedule a plan change via the CLI, by adding a parameter. Scheduling an upgrade to a Falcon 2XL plan would look like this:

`hypernode-systemctl xgrade FALCON_2XL_202203 --scheduled-at 2021-12-30T13:00:00+03:00`

Important: the timezone in which to schedule plan changes is CET or CEST.

If you want to see the list of scheduled up- or downgrades you can use this command:

`hypernode-systemctl list_xgrades`

Use the command below to see an overview of all products and possible parameters:

`hypernode-systemctl xgrade --help`

All Hypernode plan codes can also be found in the below table. For plan pricing, please visit the [pricing page](https://www.hypernode.com/en/plans-and-prices/).


|                      |                        |          |         |          |                    |
|----------------------|------------------------| -------- |---------| -------- | ------------------ |
| **Product code**     | **Name**               | **CPUs** | **RAM** | **Disk** | **Provider**       |
| FALCON_XS_202203     | Falcon XS              | 2        | 4 GB    | 44 GB    | Combell OpenStack  |
| FALCON_XS_202203DEV  | Falcon XS Development  | 2        | 4 GB    | 44 GB    | Combell OpenStack  |
| FALCON_S_202203      | Falcon S               | 2        | 8 GB    | 44 GB    | Combell OpenStack  |
| FALCON_S_202203DEV   | Faclon S Development   | 2        | 8 GB    | 44 GB    | Combell OpenStack  |
| FALCON_M_202203      | Falcon M               | 3        | 16 GB   | 62 GB    | Combell OpenStack  |
| FALCON_M_202203DEV   | Falcon M Development   | 3        | 16 GB   | 62 GB    | Combell OpenStack  |
| FALCON_L_202203      | Falcon L               | 5        | 24 GB   | 138 GB   | Combell OpenStack  |
| FALCON_L_202203DEV   | Falcon L Development   | 5        | 24 GB   | 138 GB   | Combell OpenStack  |
| FALCON_XL_202203     | Falcon XL              | 8        | 32 GB   | 286 GB   | Combell OpenStack  |
| FALCON_XL_202203DEV  | Falcon XL Development  | 8        | 32 GB   | 286 GB   | Combell OpenStack  |
| FALCON_2XL_202203    | Falcon 2XL             | 12       | 48 GB   | 606 GB   | Combell OpenStack  |
| FALCON_2XL_202203DEV | Falcon 2XL Development | 12       | 48 GB   | 606 GB   | Combell OpenStack  |
| FALCON_3XL_202203    | Falcon 3XL             | 16       | 64 GB   | 901 GB   | Combell OpenStack  |
| FALCON_3XL_202203DEV | Falcon 3XL Development | 16       | 64 GB   | 901 GB   | Combell OpenStack  |
| FALCON_4XL_202203    | Falcon 4XL             | 18       | 80 GB   | 1206 GB  | Combell OpenStack  |
| FALCON_4XL_202203DEV | Falcon 4XL Development | 18       | 80 GB   | 1206 GB  | Combell OpenStack  |
| FALCON_5XL_202203    | Falcon 5XL             | 20       | 96 GB   | 1812 GB  | Combell OpenStack  |
| FALCON_5XL_202203DEV | Falcon 5XL Development | 20       | 96 GB   | 1812GB   | Combell OpenStack  |
| EAGLE_M_202203       | Eagle M                | 4        | 8 GB    | 250 GB   | Amazon (Frankfurt) |
| EAGLE_M_202203DEV    | Eagle M Development    | 4        | 8 GB    | 250 GB   | Amazon (Frankfurt) |
| EAGLE_L_202203       | Eagle L                | 8        | 16 GB   | 500 GB   | Amazon (Frankfurt  |
| EAGLE_L_202203DEV    | Eagle L                | 8        | 16 GB   | 500 GB   | Amazon (Frankfurt) |
| EAGLE_XL_202203      | Eagle XL               | 16       | 32 GB   | 750 GB   | Amazon (Frankfurt) |
| EAGLE_XL_202203DEV   | Eagle XL Development   | 16       | 32 GB   | 750 GB   | Amazon (Frankfurt) |
| EAGLE_2XL_202203     | Eagle 2XL              | 36       | 72 GB   | 1000 GB  | Amazon (Frankfurt) |
| EAGLE_2XL_202203DEV  | Eagle 2XL Development  | 36       | 72 GB   | 1000 GB  | Amazon (Frankfurt) |
| EAGLE_3XL_202203     | Eagle 3XL              | 40       | 160 GB  | 1000 GB  | Amazon (Frankfurt) |
| EAGLE_3XL_202203DEV  | Eagle 3XL Development  | 40       | 160 GB  | 1000 GB  | Amazon (Frankfurt) |
| EAGLE_4XL_202203     | Eagle 4XL              | 64       | 256 GB  | 1000 GB  | Amazon (Frankfurt) |
| EAGLE_4XL_202203DEV  | Eagle 4XL Development  | 64       | 256 GB  | 1000 GB  | Amazon (Frankfurt) |
| EAGLE_5XL_202203     | Eagle 5XL              | 96       | 384 GB  | 1000 GB  | Amazon (Frankfurt) |
| EAGLE_5XL_202203DEV  | Eagle 5XL Development  | 96       | 384 GB  | 1000 GB  | Amazon (Frankfurt) |
| EAGLE_6XL_202203     | Eagle 6XL              | 128      | 512 GB  | 1000 GB  | Amazon (Frankfurt) |
| EAGLE_6XL_202203DEV  | Eagle 6XL Development  | 128      | 512 GB  | 1000 GB  | Amazon (Frankfurt) |
| EAGLE_7XL_202307     | Eagle 7XL              | 192      | 768 GB  | 1000 GB  | Amazon (Frankfurt) |
| EAGLE_7XL_202307DEV  | Eagle 7XL              | 192      | 768 GB  | 1000 GB  | Amazon (Frankfurt) |
