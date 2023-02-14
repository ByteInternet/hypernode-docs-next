---
myst:
  html_meta:
    description: There are several ways to change the Base URL of your Magento 1.x
      storefronts. In this article we provide you with instructions for each of these
      ways.
    title: How to change the base url in Magento 1? | Hypernode
redirect_from:
  - /en/ecommerce/magento-1/how-to-change-the-base-url-in-magento-1-x/
  - /knowledgebase/change-baseurl-magento1/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-change-the-base-url-in-magento-1-x/ -->

# How to Change the Base URL in Magento 1.x

*Information about how to change the Base URL in Magento 2.x can be found [here](../../ecommerce-applications/magento-2/how-to-change-your-magento-2-base-urls.md)*

There are several ways to change the Base URL of your Magento 1.x storefronts. Below we will provide you with instructions for each of these ways.

## Change the Base URL via the Web

### Change the Base URL via the Magento Backend

- Login to your Magento Backend
- In the top navigation bar, select `System` > `Configuration`
- In the menu on the left, select `General` > `Web`
- Open the `Secure` and `Unsecure` sections from the dropdown
- Now set the Base URL you wish to use for your shop and click on `Save Config`
- After setting your Base URL you have to flush your Magento caches by going to `System` > `Cache Management` and click `Flush Cache Storage`

### Change the Base URL via phpMyAdmin

- Login to [phpMyAdmin](../../hypernode-platform/mysql/how-to-use-phpmyadmin.md)
- Select the database you're using for Magento and open the table `core_config_data`
- Click in the top navigation bar on `SQL`
- Change the command to `SELECT * FROM `core_config_data` WHERE path like '%web%secure%'` and click on `Go`
- Now double-click the value you wish to change
- After this clear your cache from the Magento admin or run `magerun clear:cache` on the command line of the Hypernode.

**Make sure to always start your Base URL with `http://` or `https://` and end it with a slash `/`**

## Changing the Base URLs Using SSH

### Change the Base URLs Directly in MySQL from the Commandline

Log into your MySQL database, by connecting and typing your password:

```bash
mysql -u app -p

```

Below are the SQL commands to change your base_url values. Replace unsecure url `http://www.hypernode.com/` and secure url `https://www.hypernode.com/` with the domain name of your webshop. (don’t forget the trailing slash)

```mysql
UPDATE core_config_data SET value = 'http://www.hypernode.com/' WHERE path LIKE 'web/unsecure/base_url';
UPDATE core_config_data SET value = 'https://www.hypernode.com/' WHERE path LIKE 'web/secure/base_url';

```

Verify the correctness of your base_url settings with the following statement:

```mysql
SELECT path,value FROM core_config_data WHERE path LIKE 'web/unsecure/base%';
SELECT path,value FROM core_config_data WHERE path LIKE 'web/secure/base%';

```

Now clear your cache from the Magento admin or run `magerun clear:cache` on the command line of the Hypernode.

### Change the Base URLs Using Magerun

Changing your base url using Magerun is quite easy thanks to the [awesome addons created by Peter Jaap Blaakmeer](http://magerun.net/magerun-addons-by-peter-jaap-blaakmeer/)

Login on your Hypernode using SSH and navigate to your Magento directory:

```bash
cd ~/public/

```

Then use the following command to get an overview of the current Base URLs:

```bash
magerun sys:store:config:base-url:list
```

This will print a list of your storefronts and their Base URLs:

```bash
Magento Stores - Base URLs

+----+---------+------------------------------+------------------------------+
| id | code | unsecure_baseurl | secure_baseurl |
+----+---------+------------------------------+------------------------------+
| 1 | default | http://support.hypernode.io/ | http://support.hypernode.io/ |
+----+---------+------------------------------+------------------------------+
```

Next run the following Magerun command and answer the questions asked by the script:

```bash
magerun sys:store:config:base-url:set
```

Now you can change the default Base URL by selecting `Main shop` or change the base URL’s of your storefronts by selecting `Storeview` and fill in all the answers to the questions the script is asking you. (Don’t forget the trailing slash at the end of the URL)

### Change the Base URLS Using a Script

If you want to change your Base URLs to `https://` (for the use of an SSL certificate), we created [a handy Python script](https://gist.github.com/hn-support/0c76ebb5615a5be789997db2ae40bcdd) that you can use to quickly adjust your Base URL’s. To make use of this script, setting the unsecure base URL first is required.

To use it, download the script, make it executable and run it, run the following commands:

```bash
cd /data/web/public
wget https://gist.githubusercontent.com/hn-support/0c76ebb5615a5be789997db2ae40bcdd/raw -O change-baseurls.py
chmod +x change-baseurls.py
./change-baseurls.py
```

Now check your Base URLs using Magerun:

```bash
magerun sys:store:config:base-url:list
```
