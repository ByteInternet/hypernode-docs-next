<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-update-magento-2/ -->
# How to Update Magento 2

Does your Magento 2 version need an upgrade? This article explains how to upgrade to the latest Magento 2 version. Do you have a Magento 1 shop? Then follow these instructions.

**N.B. You can’t update from Magento 1 to Magento 2. If you wish to use Magento 2, you’ll need a fresh install and start from the beginning. Read more about [How to install Magento 2 on Hypernode](https://support.hypernode.com/en/ecommerce/magento-2/how-to-install-magento-2-on-hypernode).**


Why You Should Update Your Magento Webshop
------------------------------------------

Regularly updating your Magento webshop brings you not only the newest features, but also security fixes, which is highly important for your Magento store’s safety.

Not updating your Magento can result in not only a bad performance, but it makes your shop an easy target for hackers.

Before You Start Updating Magento
---------------------------------

Whatever version you’re updating, we always recommend you to follow these steps first:

* Make sure you have a recent and clean backup. Both a file- and database backup. In case anything goes wrong while updating, you can restore your data easily. More information about making backups can be found in the article [Historical backups](https://support.hypernode.com/en/hypernode/backups/hypernode-backup-policy).
* Check the versions release notes to see what changes have been made.
* Choose a quiet moment to update your Magento. Preferably when there’s hardly any traffic on your site.
* Test an update on a staging environment, development Hypernode or the [Hypernode Docker](https://support.hypernode.com/en/best-practices/testing/hypernode-docker) to make sure all aspects of your shop are compatible with the newest version.

### Updating Magento 2

Make sure you have a Magento account before you update your Magento 2 shop and have created a keypair in your account. If you haven’t added the keypair while installing Magento 2, add them to your Magento via ‘System Config’ (next to System Upgrade).

* Log on to your Magento backend.
* Navigate to ‘System’.
* Click ‘Web Setup wizard’.
	+ *If you can’t access the setup page, it’s possible the symlink wasn’t created when installing magento 2.**[To fix check this how to](https://support.hypernode.com/knowledgebase/using-magento-2-web-setup-wizard/).*
* Select the Magento version you wish to upgrade to and click ‘Next’.
* Start the ‘Readiness check’.
* Click ‘Next’ if possible, otherwise resolve the issues that need fixing before continuing.
* Create a backup by checking all the boxes (Code, Media, Database) and click ‘ Create backup’ (this can take some time).
* Once the database is created, click ‘Upgrade’ to finish upgrading.
* After updating your Magento we recommend you to remove the setup file because it’s publicly accessible. use the following command to remove the public file: rm /data/web/magento2/setup

Still not able to update Magento? Perhaps you haven’t connected your Magento shop with your Magento account yet:

* First get your secure keys by [following the steps in this article](http://devdocs.magento.com/guides/v2.0/install-gde/prereq/connect-auth.html).
* Add the public and private key to your shop via ‘System’ ->’Web Setup Wizard’ -> ‘System config’
* Fill in the keys and click ‘Save config’.
* Go back to ‘System upgrade’ to update your Magento version.

Updating Magento 2 via Composer
-------------------------------

To update through composer, use the following commands:

```nginx
export VERSION="2.0.2"
cd ~/magento2

composer require magento/product-community-edition $VERSION --no-update
composer update<

rm -rf var/di var/generation
php bin/magento cache:clean
php bin/magento cache:flush
php bin/magento setup:upgrade
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
php bin/magento indexer:reindex
```
After upgrade, check your Magento version with the following command:

```nginx
php bin/magento --version
```
Need Help?
----------

Magento is no easy open source CMS. Although we’re very skilled in hosting Magento shops, making them fast and keeping conversion high, we’re no Magento developers. Luckily, we know a lot of agencies that do know a lot about how Magento works. If you need help, don’t hesitate to [contact one of these agencies](https://www.magereport.com/page/support).
