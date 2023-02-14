---
myst:
  html_meta:
    description: 'Sometimes you want to use software inside your Magento shop, that
      require some other settings for PHP.  Find out how to override PHP settings. '
    title: How to override PHP settings? | Hypernode
redirect_from:
  - /en/hypernode/php/how-to-override-php-settings/
---

<!-- source: https://support.hypernode.com/en/hypernode/php/how-to-override-php-settings/ -->

# How to Override PHP Settings

Sometimes you want to use software inside your Magento shop, that require some other settings for PHP then the defaults supply. For example changing the `max_execution_time` for a PHP script in a certain directory.

## What Settings Can Be Overridden

Some examples of settings you might want to override are:

- upload_max_filesize
- post_max_size
- max_execution_time

[**PHP uses several modes**](http://php.net/manual/en/configuration.changes.modes.php) to adjust settings. These modes determine when and where a PHP setting can be set or changed and by who.

For example, some settings may be set within a PHP script using `ini_set()`, whereas others that may only be changed by server administrators are set in the `php.ini` file in `/etc/php`.

[**Every PHP setting has it's own mode**](http://www.php.net/manual/en/ini.list.php) and thus a place to configure. If a setting can be set in a `.user.ini`, you have the ability to change or adjust this setting yourself manually by adding it to `.user.ini` in a specific directory.

| Mode           | Meaning                                                                        |
| -------------- | ------------------------------------------------------------------------------ |
| PHP_INI_ALL    | This entry can be set anywhere                                                 |
| PHP_INI_USER   | This entry can be set in user scripts (with `ini_set()` or with a `.user.ini`. |
| PHP_INI_PERDIR | This entry can be set in `.user.ini`.                                          |
| PHP_INI_SYSTEM | This entry can only be changed by us. Please contact support.                  |

**The `PHP_INI_SYSTEM` settings can't be changed easily: We chose those values carefully to ensure stability and the most performant settings possible.**

## Entries in `.user.ini` Are Recursive

With a few easy steps, you can override php settings when running in PHP-FPM mode. PHP not only loads the `php.ini` file itself, but it also scans for INI files in each directory; First in the directory the executed script is loaded in, and keeps looking in higher up directories until it reaches the `~/public/` directory.

\*\*Please note:\*\*This would mean, for example, if you were to create the .user.ini within the `~/public/dir1/` directory, the changes are applied to the PHP scripts that are installed in that particular directory only.

Any subsequent PHP installations such as WordPress in a `~/public/blog/` directory, will not be affected by the changes in this `.user.ini` If you wish to change the settings for both directories, you'll have to install two separate `.user.ini` files, or place the `.user.ini` file in your `~/public/` directory. This will affect all PHP scripts running on your Hypernode.

More info can be found on the[PHP documentation page](http://php.net/manual/en/configuration.file.per-user.php).

## Changing your PHP settings

In this example we'll show you how to increase the `max_execution_time` in PHP. If you've created a `.user.ini` file in the right directory, all you need to do is open up your `.user.ini` file and add the following line:

```nginx
max_execution_time = 3600
```

**Keep in mind:**

- PHP Settings in `.user.ini` files are cached by PHP-FPM. When changing settings has no effect, try restarting the PHP-FPM workers: `pkill -u app php-fpm`
- The memory_limit settings are hardcoded and thus cannot be overridden.
