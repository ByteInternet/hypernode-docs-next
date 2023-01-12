---
myst:
  html_meta:
    description: Magento log cleaning helps you keep your Magento shop fast by cleaning
      and optimizing your database(s). Learn how to enable Log Cleaning in Magento.
    title: How to clean Magento 1 logs? | Hypernode
redirect_from:
  - /en/ecommerce/magento-1/how-to-clean-the-magento-1-x-logs/
  - /knowledgebase/magento-log-cleaning/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-1/how-to-clean-the-magento-1-x-logs/ -->

# How to Clean the Magento 1.x Logs

Magento log cleaning helps you keep your Magento shop fast by cleaning and optimizing your database(s).

Magento saves your web statistics by logging these in your database. This data is useful, but it takes up a lot of disk space and unfortunately Magento’s database is not very efficient. To keep your Magento shop optimized and thus fast, you’ll need to clean these logs. An easy way of cleaning up your database is by enabling Log Cleaning in the backend of Magento. This method is called ‘Automatic log cleaning’. More advanced Magento users can manually clean their logs.

## Enable Automatic Log Cleaning

Magento offers an easy tool to clean your logs. When you’re not familiar with Magento’s database system, we recommend you to use this tool. Simply follow the steps written below:

1. Log into your Magento backend `System` -> `Configurations`
1. In the left menu under `Advanced` click on `System`
1. Under `Log Cleaning`, change `Enable Log Cleaning` to `YES` and configure the `Save Log for 7 days`
1. Click `Save Config`

*The most important setting is Save log for .. days. We recommend you to pick a number between 1 and 30 days.*

## Manually Clean the Magento Logs

*It is not recommended to manually clean your logs if you don't have prior knowledge of MySQL databases.*

Cleaning your Magento logs manually is the most effective way of cleaning your logs. You can use either SSH or phpMyAdmin to manually clean the logs.

### Manually Clean the Logs via SSH

Log on to your Hypernode via SSH, navigate to the root of your Magento shop (usually `/data/web/public/` and use the following command:

```bash
php -f shell/log.php clean
```

### Manually Clean the Logs via phpMyAdmin

Open your database in PHPMyAdmin and select the following tables:

1. dataflow_batch_export
1. dataflow_batch_import
1. log_customer
1. log_quote
1. log_summary
1. log_summary_type
1. log_url
1. log_url_info
1. log_visitor
1. log_visitor_info
1. log_visitor_online
1. report_viewed_product_index
1. report_compared_product_index
1. report_event

Scroll down to select ‘Empty’ from the dropdown ‘With selected’ and click yes.

## Turn Off Database Logging

If you don’t need any database logging it can be worthwhile to disable all logging. To do so, install the [`disablelog extension by Yireo`](https://www.yireo.com/software/magento-extensions). For shops that are heavy on the database, this can help reduce the amount of update/insert queries and therefore reducing load times.
