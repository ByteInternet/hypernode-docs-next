<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-reset-your-magento-1-x-admin-password/ -->

# How to Reset Your Magento 1.x Admin Password

If you are unable to login to your Magento shop, you have several methods to retrieve a new password to log back in.

These methods are:

- Use the 'Reset password' functionality
- Let someone else reset the password for you
- Change the password using `n98-magerun`
- Insert a new password in the database

## Use the Reset Password Functionality

Visit your Magento admin backend in a browser, and click the link **Forgot your password**.

![](_res/itz1Rclya8-kPptdARxQjNkPxSiip9IIgA.png)

Next insert your email address and press the **Retrieve Password** button.

An email will be send to your email address, containing a password reset link.

Click the **RESET PASWORD** link, or paste the link in your browser.

You then will be asked to insert a new password. Insert the password twice and click the **Reset Password** button to save your changes.

![](_res/AIIITmlUbiud6TfSnE1I1Cb1S2I9KLRrkw.png)

Now you should be able to log back in.

## Reset passwords Using the Magento Admin Backend

Using the Magento backend, you can only reset a password if you happen to know your current password, or with a little help from someone else with a valid set of credentials.

If you don't know your current Magento admin credentials, you can either use the **Reset Password** functionality as explained earlier, or change your password with the tools mentioned below.

### Reset your own password in the Magento backend

To reset a password through the Magento backend, access the backend in your browser, and login using the credentials of you user account

Next, select `System` -> `My Account`:

![](_res/nFVHTWs9B4tMtuRENth5h8FSqRFOf0XNlg.png)

From the **My Account** management page, insert your **current password** and second, insert your new password twice.

After that, click the **Save Account** Button in the top-right corner of the page.

### Reset someone elses password using the Magento admin backend

To reset another users credentials, insert the name of the particular user, first, select `System` -> `Permissions` -> `Users`.

![](_res/vJTDfZCCdVd6PszQXOOcYxQF4weBcOC5og.png)

From there, select the user you want to perform a password reset for. You now will be taken to the **User Information** page.

Next, insert your own password in the **Current Admin Password** field, insert a new password for the user and select **Save User**

## Change the Password Using `n98-magerun`

The `n98-magerun` Magento management commandline utility provides a plugin to create, edit and delete users.

With this plugin you can easily change the password for an existing user.

```nginx
cd ~/public
n98-magerun admin:user:change-password
```

This will show a password prompt. Insert the password and test if you can login on the webinterface.

The plugin does not ask for a confirmation, so it might be smart to test the password right after changing it.

## Insert a New Password in the Database Using PHPMyAdmin or the MySQL Client

Additionally you can change the passwords for admin users directly in the database. This is for experts only and not the easiers way.

If you are not familiar with using MySQL, use the `n98-magerun` plugin.

### Insert a new password using PHPMyAdmin

First, login on your PHPMyAdmin:

- Go to PHPMyAdmin on the Hypernode by visitting http://*appname*.hypernode.io/phpmyadmin or by clicking the link in our service panel.
- Login with the username and password in `~/.my.cnf`
- Select the live database in the left side panel.
- In the top bar, select the `SQL` tab.

> Next, follow the instructions below:

- Paste the following query: `UPDATE admin_user SET password = CONCAT(MD5('$SALT$PASSWORD'), ':$SALT') WHERE username = '$USERNAME';`
- Replace `$PASSWORD` with the new admin password and replace `$USERNAME` with the username you want to change the password for.
- Replace `$SALT` with a random string of characters. Use the same random string in both parts of the SQL query. The string should be just 2 characters.
- Click `Go` to execute the query, and login with the given username using the new password.

If your Magento 1 shop uses table prefixes add the prefix to your table name. IE: If your table prefix is `mage_`, use the following query instead:

`UPDATE mage_admin_user SET password = CONCAT(MD5('$SALT$PASSWORD'), ':$SALT') WHERE username = '$USERNAME';`

### Insert a new password using the MySQL client

Changing a password using the MySQL client rather then PHPmyAdmin uses the same queries as mentioned earlier.

> Only use this option if you know what you are doing, as you can easily break stuff in your shop.

First, let's set some variables. Change the values to your preferred values:

```nginx
export USERNAME="exampleuser"
export PASSWORD="Randompassword123"
export DATABASE="magento_live"
export TABLE_PREFIX="mage_"
export SALT="$( < /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32};echo; )" ## Or pick your own random password
```

This uses a random password. Alternatively you can use your own password string as value for `$SALT`.

Now, run the query to change the password for a user:

And for Magento 1 use the following snippet:

```nginx
mysql ${DATABASE} -e "UPDATE ${TABLE_PREFIX}admin_user SET password = CONCAT(MD5('$SALT$PASSWORD'), ':$SALT') WHERE username = '$USERNAME'"
echo "The password for user $USERNAME is changed to $PASSWORD"
```

## Crack the Password

When you lost your credentials for your Magento admin backend, For Magento 1 you can often recover your password from the database, as Magento 1 is still using MD5 as a hashing algoritm.

Using the `n98-magerun hypernode:crack:admin-passwords` plugin, you can recover your password.

There are however easier methods of changing a password for a user.

For the nerds however, if you are looking for more information, have a look at [this article](https://sansec.io/labs/2017/04/12/magento-breach-analysis/)
