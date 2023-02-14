---
myst:
  html_meta:
    description: In this article we explain how to configure your Hypernode to serve
      a robots.txt for one or multiple storefronts in Magento 2.
    title: How to create robots.txt for Magento 2? | Hypernode
redirect_from:
  - /en/ecommerce/magento-2/how-to-create-a-robots-txt-for-magento-2-x/
  - /knowledgebase/create-robots-txt-magento-2/
---

<!-- source: https://support.hypernode.com/en/ecommerce/magento-2/how-to-create-a-robots-txt-for-magento-2-x/ -->

# How to Create a Robots.txt for Magento 2.x

As Magento 2 provides a mechanism for creating a robots.txt file, there is no need to manually create one. All you need to do is add some configuration in Nginx and Magento itself and a robots.txt will be generated periodically using cron.

## Generate a Robot.txt in Magento

To generate a `robots.txt` file, use the following steps:

- Log into your Magento admin backend
- Select `Store` -> `Configuration`
- Select `General` -> `Design`
- Select the dropdown `Search Engine Robots`.
- Select the default storefront or one you want to create a `robots.txt` for.
- For `Default Robots`, use one of the available options:
  - `INDEX, FOLLOW`: Tell crawlers to index the site and to keep doing this periodically.
  - `NOINDEX, FOLLOW`: Tell crawlers not to index the site but to check for changes of this policy periodically.
  - `INDEX, NOFOLLOW`: Tell crawlers to index the shop just once and don’t check for changes periodically.
  - `NOINDEX, NOFOLLOW`: Tell crawlers not to index the shop and don’t check for changes periodically.

After this is done, click the `Reset to Default` button to add the default `robots.txt` instructions to the custom instructions field. You can now add your custom instructions to the default. After editing, click the `Save Config` button to save your `robots.txt` file to disk.

## Configure Nginx to Serve One Robots.txt for All Storefronts

When you use a single `robots.txt` file for all your storefronts, configuring your `robots.txt` within nginx is fairly simple.

Create a symlink in `/data/web/public` that points to the `robots.txt` file in `/data/web/magento:`

```bash
ln -s /data/web/magento2/robots.txt /data/web/public/robots.txt
```

## Configure Nginx to Serve a Different Robots.txt for Each Storefront

Magento 2 currently does not support multiple `robots.txt` files for each storefront of website, which is surprising as the rest of the suite is fully designed for use with multiple storefronts. Therefore we should use a little workaround and move the `robots.txt` file to another location after each time we save the changes in our robots.txt files.

*Unfortunately the Magento2 robots.txt implementation is not the best. If you use multiple storefronts, Magento 2 will save each robots.txt over the previous one, erasing all changes made for other storefronts.*

Follow the following instructions to work around this:

- First create a new location for our `robots.txt`files:

```bash
mkdir -p /data/web/magento2/robots
```

- Then move the default (global) `robots.txt` to this directory.
  We will use the current `robots.txt`as the fallback when the robots.txt for the corresponding storefront is missing:

```bash
cp /data/web/magento2/robots.txt /data/web/magento2/robots/robots.txt
```

- Now adjust the robots.txt settings in the backend for the first individual storefront. For each storefront, adjust the default settings to your needs and save your robots.txt using the big `Save Config` button.
- After you clicked save, copy or move the generated storefront to it’s definitive location. We use the naming convention `robots_$storecode.txt`. EG: If your storecode is shop_nl, then use the filename robots_shop_nl.txt:

```bash
cp /data/web/magento2/robots.txt /data/web/magento2/robots/robots_shop_nl.txt
```

- Alternatively you can manually create a working robots.txt for each storefront and save those in `/data/web/magento2/robots`and edit those afterwards:

```bash
for storefront in $( n98-magerun2 sys:store:list --format=csv | sed 1d | cut -d, -f2 ); do
  cp /data/web/magento2/robots.txt /data/web/magento2/robots/robots_${storefront}.txt
done
```

- When this is done we need to add some Nginx configuration to make sure the correct storefront is served with each storefront. Save a snippet as `/data/web/nginx/server.robots`with the following content:

```nginx
location @robots_fallback {
  root /data/web/magento2/robots;
}

location = /robots.txt {
  alias /data/web/magento2/robots/robots_$storecode.txt;
  error_page 404 = @robots_fallback;
}
```

Now test your `robots.txt` by requesting and verify whether the correct sitemap is served:

```bash
curl -v https://www.example.com/robots.txt
```

## Examples of Frequently Used Robots.txt

- Allow full access to all directories and pages:

```bash
User-agent:*
Disallow:
```

- Deny access for any User Agent to any directory and page:

```bash
User-agent:*
Disallow: /
```

- The recommended default settings for Magento 2 can be found [here](https://gist.githubusercontent.com/hn-support/65aa2a12a7c47456cb695e366ee3fea5/raw/a735eff63c11c8f7e79b60e7299cdd68b8238860/robots.txt)

## Additional resources

- <https://developers.google.com/s/results?q=control-crawl>
- <https://support.google.com/webmasters/answer/6062596?hl=en>
- <http://www.robotstxt.org/>
