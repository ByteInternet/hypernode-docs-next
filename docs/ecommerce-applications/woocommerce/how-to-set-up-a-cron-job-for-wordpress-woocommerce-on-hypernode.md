---
myst:
  html_meta:
    description: Learn how to replace the default WordPress cron with a cron job on
      Hypernode to improve performance, schedule tasks precisely, and mitigate DDoS
      attacks.
    title: How to Set Up a Real Cron Job for WordPress/WooCommerce on Hypernode
---

# How to set up a cron job for WordPress/WooCommerce on Hypernode

In this guide, we'll explain how to replace the default WordPress cron job with a cron job on your Hypernode server. This can be useful for low traffic sites, important tasks that need to be run at specific times, mitigating excessive DDoS attacks, or improving high page load times.

**Important note:** Access to wp-cron.php is blocked by default on Hypernode for security reasons. This is done to protect your server from potential DDoS attacks and unauthorized execution of scheduled tasks through the wp-cron.php endpoint. Setting up a proper server-side cron job as described in this guide allows you to safely run your WordPress scheduled tasks while maintaining the security benefits.

## Disable WordPress cron

To begin, disable the default WordPress cron by editing the wp-config.php file.

Connect to your server using an FTP client like FileZilla or an SSH client such as PuTTY. Navigate to the root directory of your WordPress installation and locate the `wp-config.php` file. Open the file for editing and add the following line of code before `/* That's all. Stop editing! Happy blogging. */`:

```php
define('DISABLE_WP_CRON', true);
```

This code disables the default WordPress cron functionality, allowing you to set up a cron job.

## Adding a new cron job to your server

Next, set up a cron job on your Hypernode server. Log in to your server via SSH and open your crontab file with the following command:

```bash
app@abcdef-example-magweb-cmbl ~ $ crontab -e
```

Add the following line to your crontab file to set up a cron job that runs every minute:

```console
* * * * * /usr/bin/chronic php /data/web/public/wp-cron.php > /dev/null 2>&1
```

**Note:** Make sure to replace `/data/web/public/wp-cron.php` with the actual path to your WordPress installation if it's different from the default path. The default WordPress installation path on Hypernode is typically `/data/web/public/`.

### Explanation of the Cron Job Command

- `* * * * *`: Specifies the interval for the cron job. In this case, it is set to run every minute. You can adjust this based on your needs.
- `php /data/web/public/wp-cron.php`: Directly executes the WordPress cron script using PHP, eliminating the need for an HTTP request.
- `> /dev/null 2>&1`: Discards any output from the command, preventing it from filling up your server logs.

After setting up your cron job, monitor your WordPress site to ensure that scheduled tasks are being executed as expected. This setup ensures that your WordPress or WooCommerce site on Hypernode handles scheduled tasks more reliably, especially under conditions where the default cron system may not suffice.
