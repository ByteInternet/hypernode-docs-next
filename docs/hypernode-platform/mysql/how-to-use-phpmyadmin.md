---
myst:
  html_meta:
    description: This article will explain how you can use PHPMyAdmin and how to create
      a database dump.
    title: How to use PHPMyAdmin? | Hypernode
redirect_from:
  - /en/hypernode/mysql/how-to-use-phpmyadmin/
  - /knowledgebase/use-phpmyadmin/
---

<!-- source: https://support.hypernode.com/en/hypernode/mysql/how-to-use-phpmyadmin/ -->

# How to Use PHPMyAdmin

This article will explain how you can use PHPMyAdmin and how to create a database dump.

*For your protection, phpMyAdmin by default is only accessible through the `example.hypernode.io/phpmyadmin/` URL, on Vagrant via the `*`example`*.hypernode.local/phpmyadmin/` url and on Docker through `YourBaseURL/dbadmin/` after you followed [these](#configure-phpmyadmin) instructions. You can adjust this behaviour to your own preference.*

## Accessing PHPMyAdmin

PHPMyAdmin comes preinstalled on your Hypernode at <http://example.hypernode.io/phpmyadmin/>. In order to reduce brute force attacks, it is not accessible via any other domains names linked to your Hypernode.

### Credentials

PHPMyAdmin uses the same user and password your database uses. You can find them safely stored on your hypernode in `/data/web/.my.cnf`.

### Enabling HTTPS

By default PHPMyAdmin is installed at <http://example.hypernode.io/phpmyadmin/>. We highly advise you to enable HTTPS before logging in, to keep your credentials safe. You can do so using the following command:

```
hypernode-manage-vhosts --https --force-https example.hypernode.io
```

## Using phpMyAdmin on Hypernode

### Create a database dump using phpMyAdmin

- Go to `https://example.hypernode.io/phpmyadmin/`
- Log in with your credentials
- Click on “Databases” and select the database.
- Click on “Export”.
- Click on “Go” and the export/backup will be available.

**If you have a large database, making a database dump through phpMyAdmin is not very reliable. Before importing it, make sure the integrity of your database dump is sane!**

## Configure PHPMyAdmin

When you want to use phpMyAdmin via another domain, via another URL, or you want to add an allowlist with IP's that are allowed to access phpMyAdmin, you will need to create a custom nginx configuration

- Create an nginx snippet in /data/web/nginx called `server.phpmyadmin` with the following content:

```nginx
location /dbadmin/ {
  # Only allow IP addresses defined in /data/web/include.whitelist
  include /etc/nginx/app/include.whitelist;

  # Uncomment to secure phpMyAdmin with additional basic_auth
  # include /etc/nginx/app/include.basic_auth;

  # For static files, alias this location to PMA files on disk
   alias /usr/share/phpmyadmin/;

try_files $uri $uri/ /dbadmin/index.php last;

location ~ \.php$ {
echo_exec @phpfpm;
}
}
```

- Next, create the include.whitelist in /data/web/nginx and add your IP(s) to the snippet

```nginx
allow XXX.XXX.XXX.XXX;
deny all;
```

Now make sure to set a symlink from within your webroot: `ln -s /usr/share/phpmyadmin/ dbadmin`

And finally visit phpMyAdmin on <https://yourdomain.nl/dbadmin>

**This will only add another URL where phpMyAdmin is accessible. If you only want to use this endpoint, block all access to `/phpmyadmin` too**

### Blocking All Access to PHPMyAdmin

If you want to fully disable phpMyAdmin, create the following snippet as `/data/web/nginx/server.phpmyadmin`:

```nginx
## Block PHPMyAdmin
if ($request_uri ~ ^/phpmyadmin ) {
        return 403;
}

```

## Troubleshooting PHPMyAdmin

- **The phpMyAdmin button in the control panel redirects to `https://` and gives a 404 in Nginx**

This is probably because you redirect ALL traffic over HTTPS. Try using PHPMyAdmin over ssl as explained above.

- **I'm receiving an error while dumping the database**

Most of the time this happens when a database is large and you exceed the `max_execution_time` or `memory_limit` in php. If this happens try [dumping your database on the command line](how-to-use-mysql-on-hypernode.md#creating-a-mysql-back-up)

- **My phpMyAdmin does not show any images**

This happens when you redirect all traffic to HTTPS, causing mixed content errors in your browser. To solve this, use phpMyAdmin over SSL.

- **Static content doesn't (fully) display**

This happens if you define a regex location block in your nginx config that matches phpmyadmin's static files; This will override the existing config for static files under /phpmyadmin/. To solve this, you will have to change your custom location block to not match files in the /phpmyadmin/ location.
