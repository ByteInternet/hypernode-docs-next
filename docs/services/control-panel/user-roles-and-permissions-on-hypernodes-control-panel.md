---
myst:
  html_meta:
    description: 'Hypernode offers a comprehensive user control panel that allows
      you to easily manage user roles and permissions. Learn all about user roles
      and permissions. '
    title: User roles and permissions | Control Panel | Hypernode
redirect_from:
  - /en/services/control-panel/user-roles-and-permissions-on-hypernodes-control-panel/
---

<!-- source: https://support.hypernode.com/en/services/control-panel/user-roles-and-permissions-on-hypernodes-control-panel/ -->

# User Roles and Permissions on Hypernode’s Control Panel

For security and usability, the Hypernode Control Panel's features are available to users based on the role assigned to the individual user. Each user invited to a team is assigned a role within the team.

## The Different Control Panel Roles

A user can have different roles between teams. Each role is defined by a set of permissions. The permissions, based on the specific role, apply to all Hypernodes in a team. This also includes the SSL certificates that have been linked to the Hypernodes in the team.

- **Owner:** Can access and use every feature. This is the most powerful role and cannot be assigned. The Owner is the only one who can transfer the ownership of the Hypernode you can read more about this [here](how-to-transfer-ownership-of-a-hypernode-in-the-control-panel.md). The user creating the Team is automatically the Owner. The Owner is the person in charge of billing.
- **Admin:** Can use all features and change Hypernode plans. Please see [this article for](../../about-hypernode/billing/how-to-up-or-downgrade-your-hypernode-plan.md#up--and-downgrading-your-hosting-plan-for-control-panel-users) an explanation on how to change your Hypernode plan. They can invite other team members and set or change roles of team members.
- **Developer:** Can manage all technical features on a Hypernode level.
- **Merchant:** Can access the Control Panel on a view-only basis.

## Permissions

|                                       |                          |               |           |           |
| ------------------------------------- | ------------------------ | ------------- | --------- | --------- |
| **Permissions**                       | **Merchant (view-only)** | **Developer** | **Admin** | **Owner** |
| See the team                          | ✅                        | ✅             | ✅         | ✅         |
| See the Hypernodes in the team        | ✅                        | ✅             | ✅         | ✅         |
| See the logs                          | ✅                        | ✅             | ✅         | ✅         |
| See the SSH keys that have been added | ✅                        | ✅             | ✅         | ✅         |
| See the linked SSL certificate        | ✅                        | ✅             | ✅         | ✅         |
| See the allowlist                     | ✅                        | ✅             | ✅         | ✅         |
| Manage the allowlist                  |                          | ✅             | ✅         | ✅         |
| Manage SSL certificates               |                          | ✅             | ✅         | ✅         |
| Add SSH keys                          |                          | ✅             | ✅         | ✅         |
| Request to restore backups            |                          | ✅             | ✅         | ✅         |
| Attach backups                        |                          | ✅             | ✅         | ✅         |
| Create backups                        |                          | ✅             | ✅         | ✅         |
| Can enable Varnish                    |                          | ✅             | ✅         | ✅         |
| Can change the PHP version            |                          | ✅             | ✅         | ✅         |
| Can manage the monitoring             |                          | ✅             | ✅         | ✅         |
| Can manage bots                       |                          | ✅             | ✅         | ✅         |
| Can add and remove team members       |                          |               | ✅         | ✅         |
| Can change roles within the team      |                          |               | ✅         | ✅         |
| Can remove Hypernodes                 |                          |               | ✅         | ✅         |
| Can rename the team                   |                          |               | ✅         | ✅         |
| Can change the plan                   |                          |               | ✅         | ✅         |
| Can delete the team                   |                          |               |           | ✅         |
| Can add Hypernodes to a team          |                          |               |           | ✅         |
| Can transfer ownership                |                          |               |           | ✅         |
| Can change the payment details        |                          |               |           | ✅         |
| Can view the invoices                 |                          |               |           | ✅         |

## How to Assign Roles

Initially, the Owner is the only user that can assign roles to other team members. After assigning a user the Admin role, they will also be able to assign roles. Use the following steps to assign roles:

1. Log in to the Hypernode Control Panel.
1. If your Hypernode is not in a Team yet, create a Team first. [Here's](how-to-use-teams.md) how to do this.
1. Click on **Teams** in the sidebar on the left and then select the applicable team.
1. Click **Invite new member**and follow the steps.

**Please note: when inviting a new member to the team, you are required to assign them a role.**

### How to Change Roles Within an Existing Team

1. Log in to the Hypernode Control Panel.
1. Click on **Teams** in the sidebar on the left and then select the applicable team.
1. Hover over **Teams** in the sidebar and click **Roles**.
1. Change the roles per member here.
