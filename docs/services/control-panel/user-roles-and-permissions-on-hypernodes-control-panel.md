<!-- source: https://support.hypernode.com/en/services/control-panel/user-roles-and-permissions-on-hypernodes-control-panel/ -->
# User Roles and Permissions on Hypernode’s Control Panel

For security and usability, the Hypernode Control Panel's features are available to users based on the role assigned to the individual user. Each user invited to a team is assigned a role within the team.


The Different Control Panel Roles
---------------------------------

A user can have different roles between teams. Each role is defined by a set of permissions. The permissions, based on the specific role, apply to all Hypernodes in a team. This also includes the SSL certificates that have been linked to the Hypernodes in the team. 

* **Owner:**Can access and use every feature. This is the most powerful role and cannot be assigned. The Owner is the only one who can transfer the ownership of the Hypernode you can read more about this [here](https://support.hypernode.com/en/services/control-panel/transfer-ownership). The user creating the Team is automatically the Owner. The Owner is the person in charge of billing.
* **Admin:** Can use all features and change Hypernode plans. Please see [this article for](https://support.hypernode.com/en/about/billing/how-to-up-or-downgrade-your-hypernode-plan#Up--and-Downgrading-Your-Hosting-Plan-for-Control-Panel-Users) an explanation on how to change your Hypernode plan. They can invite other team members and set or change roles of team members.
* **Developer:** Can manage all technical features on a Hypernode level.
* **Merchant:**Can access the Control Panel on a view-only basis.

Permissions
-----------

| **Permissions** | **Merchant (view-only)** | **Developer** | **Admin** | **Owner** |
| See the team | ✅ | ✅ | ✅ | ✅ |
| See the Hypernodes in the team | ✅ | ✅ | ✅ | ✅ |
| See the logs | ✅ | ✅ | ✅ | ✅ |
| See the SSH keys that have been added | ✅ | ✅ | ✅ | ✅ |
| See the linked SSL certificate | ✅ | ✅ | ✅ | ✅ |
| See the allowlist | ✅ | ✅ | ✅ | ✅ |
| Manage the allowlist |  | ✅ | ✅ | ✅ |
| Manage SSL certificates |  | ✅ | ✅ | ✅ |
| Add SSH keys |  | ✅ | ✅ | ✅ |
| Request to restore backups |  | ✅ | ✅ | ✅ |
| Attach backups |  | ✅ | ✅ | ✅ |
| Create backups |  | ✅ | ✅ | ✅ |
| Can enable Varnish |  | ✅ | ✅ | ✅ |
| Can change the PHP version |  | ✅ | ✅ | ✅ |
| Can manage the monitoring |  | ✅ | ✅ | ✅ |
| Can manage bots |  | ✅ | ✅ | ✅ |
| Can add and remove team members |  |  | ✅ | ✅ |
| Can change roles within the team |  |  | ✅ | ✅ |
| Can remove Hypernodes and change the name of the team |  |  | ✅ | ✅ |
| Can change the plan |  |  | ✅ | ✅ |
| Can delete the team |  |  |  | ✅ |
| Can add Hypernodes to a team |  |  |  | ✅ |
| Can transfer ownership |  |  |  | ✅ |
| Can change the payment details |  |  |  | ✅ |
| Can view the invoices |  |  |  | ✅ |

How to Assign Roles
-------------------

Initially, the Owner is the only user that can assign roles to other team members. After assigning a user the Admin role, they will also be able to assign roles. Use the following steps to assign roles:

1. Log in to the Hypernode Control Panel.
2. If your Hypernode is not in a Team yet, create a Team first. [Here's](https://support.hypernode.com/en/services/control-panel/managing-your-teams) how to do this.
3. Click on **Teams** in the sidebar on the left and then select the applicable team.
4. Click **Invite new member**and follow the steps.

**Please note: when inviting a new member to the team, you are required to assign them a role.**

### How to Change Roles Within an Existing Team

1. Log in to the Hypernode Control Panel.
2. Click on **Teams** in the sidebar on the left and then select the applicable team.
3. Hover over **Teams** in the sidebar and click **Roles**.
4. Change the roles per member here.