<!-- source: https://support.hypernode.com/en/services/control-panel/how-to-change-your-plan-via-the-cli/ -->
# How to Change Your Plan via the CLI

**Please note that this article only applies to Control Panel customers that log in via my.hypernode.com.**


Allowing Plan Changes via the CLI
---------------------------------

To allow plan changes for a specific Hypernode plan via the command line, follow the steps below:

* Navigate go the Change plan page.
* Click on the CLI tab, enable plan changes via the CLI.

**Please note:** when enabled, **everyone who has SSH access can change the plan from the CLI**, even if they are not the Owner or Admin. 

Changing Your Plan via the CLI
------------------------------

The command to change your plan is `hypernode-systemctl xgrade` followed by the plan code. 

For example if you want to change the plan to a Professional 2XL plan you can use the following command: `hypernode-systemctl xgrade MAGP32`

You can also schedule a plan change via the CLI, by adding a parameter. Scheduling an upgrade to a Professional 2XL plan would look like this:  

`hypernode-systemctl xgrade MAGP32 --scheduled-at 2021-12-30T13:00:00+03:00`

Important: the timezone in which to schedule plan changes is CET or CEST.

If you want to see the list of scheduled up- or downgrades you can use this command:

`hypernode-systemctl list_xgrades`

Use the command below to see an overview of all products and possible parameters:

`hypernode-systemctl xgrade --help`

All Hypernode plan codes can also be found in the below table.

| **Product code** | **Name** | **Price** | **CPUs** | **RAM** | **Disk** | **Provider** |
| MAGG201908 | Grow | €99 | 2 | 4 GB | 44 GB | Combell OpenStack |
| MAGG201908DEV | Grow Development | €69 | 2 | 4 GB | 44 GB | Combell OpenStack |
| MAGPS202006 | Professional S | €135 | 2 | 6 GB | 44 GB | Combell OpenStack |
| MAGPS202006DEV | Professional S Development | €95 | 2 | 6 GB | 44 GB | Combell OpenStack |
| MAGP4201908 | Professional M | €175 | 3 | 8 GB | 62 GB | Combell OpenStack |
| MAGP4201908DEV | Professional M Development | €115 | 3 | 8 GB | 62 GB | Combell OpenStack |
| MAGP8201908 | Professional L | €295 | 4 | 16 GB | 138 GB | Combell OpenStack |
| MAGP8201908DEV | Professional L Development | €195 | 4 | 16 GB | 138 GB | Combell OpenStack |
| MAGP162021 | Professional XL | €535 | 6 | 24 GB | 286 GB | Combell OpenStack |
| MAGP162021DEV | Professional XL Development | €375 | 6 | 24 GB | 286 GB | Combell OpenStack |
| MAGP32 | Professional 2XL | €825 | 8 | 32 GB | 606 GB | Combell OpenStack |
| MAGP32DEV | Professional 2XL Development | €615 | 8 | 32 GB | 606 GB | Combell OpenStack |
| MAGP48 | Professional 3XL | €1205 | 12 | 48 GB | 901 GB | Combell OpenStack |
| MAGP48DEV | Professional 3XL Development | €865 | 12 | 48 GB | 901 GB | Combell OpenStack |
| MAGP64 | Professional 4XL | €1745 | 16 | 64 GB | 1206 GB | Combell OpenStack |
| MAGP64DEV | Professional 4XL Development | €1395 | 16 | 64 GB | 1206 GB | Combell OpenStack |
| MAGP96 | Professional 5XL | €2675 | 20 | 96 GB | 1812 GB | Combell OpenStack |
| MAGP96DEV | Professional 5XL Development | €2055 | 20 | 96GB | 1812GB | Combell OpenStack |
| MAGXCL4 | Excellence M | €510 | 4 | 8 GB | 250 GB | Amazon (Frankfurt) |
| MAGXCL4DEV | Excellence M Development | €415 | 4 | 8 GB | 250 GB | Amazon (Frankfurt) |
| MAGXCL8 | Excellence L | €920 | 8 | 16 GB | 500 GB | Amazon (Frankfurt |
| MAGXCL8DEV | Excellence L | €775 | 8 | 16 GB | 500 GB | Amazon (Frankfurt) |
| MAGXCL16 | Excellence XL | €1630 | 16 | 32 GB | 750 GB | Amazon (Frankfurt) |
| MAGXCL16DEV | Excellence XL Development | €1335 | 16 | 32 GB | 750 GB | Amazon (Frankfurt) |
| MAGXCL32 | Excellence 2XL | €2960 | 36 | 72 GB | 1000 GB | Amazon (Frankfurt) |
| MAGXCL32DEV | Excellence 2XL Development | €2525 | 36 | 72 GB | 1000 GB | Amazon (Frankfurt) |
| MAGXCL40 | Excellence 3XL | €4490 | 40 | 160 GB | 1000 GB | Amazon (Frankfurt) |
| MAGXCL40DEV | Excellence 3XL Development | €3915 | 40 | 160 GB | 1000 GB | Amazon (Frankfurt) |
| MAGXCL64 | Excellence 4XL | €7140 | 64 | 256 GB | 1000 GB | Amazon (Frankfurt) |
| MAGXCL64DEV | Excellence 4XL Development | €6075 | 64 | 256 GB | 1000 GB | Amazon (Frankfurt) |
| MAGXCL96 | Excellence 5XL | €9999 | 96 | 384 GB | 1000 GB | Amazon (Frankfurt) |
| MAGXCL96DEV | Excellence 5XL Development | €8755 | 96 | 384 GB | 1000 GB | Amazon (Frankfurt) |
| MAGXCL128 | Excellence 6XL | €25499 | 128 | 1952 GB | 1000 GB | Amazon (Frankfurt) |
| MAGXCL128DEV | Excellence 6XL Development | €20595 | 128 | 1952 GB | 1000 GB | Amazon (Frankfurt) |
