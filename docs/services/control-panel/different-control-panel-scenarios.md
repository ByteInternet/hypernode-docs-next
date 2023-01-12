---
myst:
  html_meta:
    description: Get the best performance out of your Hypernode installation with
      our comprehensive guide to different Control Panel scenarios.
    title: Different Control Panel scenarios | Hypernode
redirect_from:
  - /en/services/control-panel/different-control-panel-scenarios/
---

<!-- source: https://support.hypernode.com/en/services/control-panel/different-control-panel-scenarios/ -->

# Different Control Panel Scenarios

**Please note that this FAQ only applies to Control Panel users that log in via my.hypernode.com. If you use the Service Panel and log in via service.byte.nl please see our [Different Service Panel Scenarios article](../../services/service-panel/different-service-panel-scenarios.md).**

For security and usability, the Hypernode Control Panel's features are available to users based on the role assigned to the individual user. Each user invited to a team is assigned a role within the team.

A user can have different roles between teams. Each role is defined by a set of permissions.

The different roles are as follows:

- **Owner:** Can access and use every feature. This is the most powerful role and cannot be assigned. The user creating the Team is automatically the owner. The owner is the one who receives the invoices.
- **Admin:** Can use all features and change Hypernode plans. Please see this article for an explanation on how to change your Hypernode plan. They can invite other team members and set or change roles of team members.
- **Developer:** Can manage all technical features on a Hypernode level.
- **Merchant:** Can access the Control Panel on a view-only basis.

We have distinguished a few different scenarios below.

## You Are a Merchant and Want to Invite a Developer

In this case you are responsible for billing and you want to invite a developer.

1. Log into the Hypernode Control Panel.
1. From the sidebar on the left, select **Teams**.
1. If you haven't created a Team yet, do so by clicking on the **Create a new Team** button and follow the steps.
1. Select **Details** from the Team overview page and click **Invite new member**.
1. Fill in their email and select the **Developer** role. Add a personal message and click Send invitation.

An invitation will be sent to the invitee's email address. Once they have accepted the invitation, the owner and invited member will be notified of this via email. The developer will have access to all technical features of the Hypernodes in the Team.

## You Are a Developer and You Do Not Want to Be Billed

In this scenario you ordered a trial for your client. After setting up the Hypernode, you want to transfer ownership, because you do not want to be billed for the plan.

1. Log into the Hypernode Control Panel.
1. Select a Hypernode from the overview by clicking **Details**.
1. Move your mouse over **Hypernodes** in the sidebar on the left and select **Transfer ownership**.
1. Enter the email address of the new owner and optionally add a message.
1. Click **Transfer Hypernode**to transfer the Hypernode to the new owner.

The new owner will receive an email to confirm the transfer. Once confirmed, we remove the Hypernode from all teams and remove all SSH keys installed on the Hypernode, so access will be revoked for everyone except the new owner.

The client can then re-add you as a Developer by following the steps listed at **You Are a Merchant and Want to Invite a Developer.**

## Revoking Access

1. Log into the Hypernode Control Panel.
1. From the sidebar on the left, select **Teams**.
1. Select a team by clicking **Details**.
1. Delete a member by clicking the trash can. Confirm the removal.

Once you remove someone from a team, you can always use Invite new member to add them back to the team later on. A notification will be sent to the owner if another team member revoked access for another team member.

## Things to Keep In Mind

- Only **Owners** and **Admins** can invite members to Teams.
- The **Owner** is the only one who can cancel a plan, the **Admin** however can also up- or downgrade a plan.
