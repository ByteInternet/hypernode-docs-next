---
myst:
  html_meta:
    description: Learn how to replace the default WordPress cron with a cron job on Hypernode to improve performance, schedule tasks precisely, and mitigate DDoS attacks.
    title: How to Set Up a Real Cron Job for WordPress/WooCommerce on Hypernode
redirect_from:
  - /en/ecommerce/woocommerce/how-to-set-up-a-cron-job-for-wordpress-woocommerce-on-hypernode/
---

<!-- source: https://support.hypernode.com/en/ecommerce/woocommerce/how-to-set-up-a-cron-job-for-wordpress-woocommerce-on-hypernode/ -->

# How to set up a cron job for WordPress/WooCommerce on Hypernode

In this guide, we'll explain how to replace the default WordPress cron job with a cron job on your Hypernode server. This can be useful for low traffic sites, important tasks that need to be run at specific times, mitigating excessive DDoS attacks, or improving high page load times.

## Disable WordPress cron

To begin, disable the default WordPress cron by editing the wp-config.php file.

Connect to your server using an FTP client like FileZilla or an SSH client such as PuTTY. Navigate to the root directory of your WordPress installation and locate the `wp-config.php` file. Open the file for editing and add the following line of code before `/* That’s all. Stop editing! Happy blogging. */`:

```php
define('DISABLE_WP_CRON', true);
```

This code disables the default WordPress cron functionality, allowing you to set up a cron job.

## Adding a new cron job to your server

Next, set up a cron job on your Hypernode server. Log in to your server via SSH and open your crontab file with the following command:

```bash
crontab -e
```

Add the following line to your crontab file to set up a cron job that runs every minute:
```console
* * * * * wget -q -O - 'https://yourdomain.hypernode.io/wp-cron.php?doing_wp_cron' >/dev/null 2>&1
```
Replace `https://yourdomain.hypernode.io` with the actual URL of your WordPress site.

Explanation of the Cron Job Command
- `* * * * *`: Specifies the interval for the cron job. In this case, it is set to run every minute. You can adjust this based on your needs.
- `wget -q -O - 'https://yourdomain.hypernode.io/wp-cron.php?doing_wp_cron'`: Uses wget to make a web request to the WordPress cron URL, triggering any scheduled tasks.
- `>/dev/null 2>&1`: Discards any output from the command, preventing it from filling up your server logs.

After setting up your cron job, monitor your WordPress site to ensure that scheduled tasks are being executed as expected. This setup ensures that your WordPress or WooCommerce site on Hypernode handles scheduled tasks more reliably, especially under conditions where the default cron system may not suffice.