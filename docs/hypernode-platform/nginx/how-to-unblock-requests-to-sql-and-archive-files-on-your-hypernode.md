---
myst:
  html_meta:
    description: 'Read in this article how to ublock requests to sql and archive files
      on your Hypernode. '
    title: How to unblock requests to SQL and archive files? | Hypernode
redirect_from:
  - /en/hypernode/nginx/how-to-unblock-requests-to-sql-and-archive-files/
---

<!-- source: https://support.hypernode.com/en/hypernode/nginx/how-to-unblock-requests-to-sql-and-archive-files/ -->

# How to Unblock Requests to sql and Archive Files on Your Hypernode

By default we block `.sql` files and archive files in Nginx. We do this to prevent accidental exposure.

This is done by placing the following line in the Nginx configuration:

`location ~ \.(sql|zip|tar|tar.gz|tgz)$ { deny all; }`

Any requests to files with the extenstion `sql`, `zip`, `tar`, `tar.gz` or `tgz` will return with a HTTP 403 response.

## How to Unblock Specific Files

If you want to host files with one of these extensions and make them downloadable, you can undo this block by placing the following line in your Nginx configuration (in a file called `server.zip` in `/data/web/nginx/`):

`location = /some_directory/some_file.zip {}`

Or if you want to unblock an entire directory, you can place the following Nginx configuration:

`location ^~ /some_directory/ {}`

\*\*\*\*\*Do note that you have to use the URL path in this situation and **not** the disk path.

Other variants of this Nginx configuration work as long as it’s more specific than the Nginx configuration that blocks these files (which can be found at the top of this article).
