---
myst:
  html_meta:
    description: To set an environment for Shopware 6 is the same process as for Magento,
      with the exception that you’ll have to add an additional NGINX configuration
      file.
    title: 'How to install Shopware 6 on Hypernode Docker? '
redirect_from:
  - /en/ecommerce/shopware/how-to-install-shopware-6-on-hypernode-docker/
---

<!-- source: https://support.hypernode.com/en/ecommerce/shopware/how-to-install-shopware-6-on-hypernode-docker/ -->

# How to Install Shopware 6 on Hypernode Docker

The Hypernode Docker Image can be used to set up a local test environment for Magento as well as Shopware. To set such an environment for Shopware is basically the same process as for Magento. This article explains how you can install Shopware 6 on your Docker environment.

## Step One - Start a Docker container

Before you can start a Docker container make sure that Docker is running. Next you need to choose which Docker image you want to run depending on the PHP and MySQL version. You can see all available **[images](https://github.com/byteinternet/hypernode-docker)** here.

After you've chosen the image, you need to pull the image to your local machine. Once the image is pulled, you can start a Docker container from that image. Use the format below and if needed change the name "hypernode-buster-docer-php7.4-mysql57" to your right version.

```bash
docker pull docker.hypernode.com/byteinternet/hypernode-buster-docker-php74-mysql57:latest
docker run -p 222:22 -p 8080:80 -p 8025:8025 docker.hypernode.com/byteinternet/hypernode-buster-docker-php74-mysql57:latest
```

This will expose port 222 on the container and port 8080 on the localhost. In this example you should use the following command to connect to the container:

```bash
# Login as app user
ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -p 222 app@127.0.0.1
```

The password is `insecure_docker_ssh_password`.

## Step Two - Configure Shopware 6 Nginx Config

Create a **/data/web/nginx/server.shopware6**config file with the following content:

```nginx
location /recovery/install {
    index index.php;
    try_files $uri /recovery/install/index.php$is_args$args;
}

location /recovery/update/ {
    location /recovery/update/assets {
    }
    if (!-e $request_filename){
        rewrite . /recovery/update/index.php last;
    }
}
location ~ \.php$ {
    echo_exec @phpfpm;
}
```

## Step Three - Download and install the latest version of Shopware 6

Download the latest Shopware 6 version from the [Shopware](https://www.shopware.com/en/download/#shopware-6%22%3EShopware) website by right clicking on “Download for free” and click on “Copy Link Address”. Now paste the link after the `wget` command like below.

```nginx
mkdir /data/web/shopware
cd /data/web/shopware
wget https://www.shopware.com/en/Download/redirect/file/install_6.1.3_1582123990.zip

# Unzip the downloaded .zip file
unzip install_6.1.3_1582123990.zip

# Enable secure document root
rm -rf /data/web/public
ln -s /data/web/shopware/public/ /data/web/public

```

## Install Shopware 6

Now open your browser and browse to [http://127.0.0.1:8080/recovery/install](http://127.0.0.1:8080/recovery/install/index.php%22%3Ehttp://127.0.0.1:8080/recovery/install/index.php%3C/a). At this point you can follow the install-guide through your browser. Make sure to fill in the right details at **Configure database:**

- Database server: localhost
- Database user: app
- Database password: run cat ~/.my.cnf in your Docker and use the password you'll find there.
- Select `New database`, give it a name of your choice and start the installation
- Fill in the Basic shop set-up how you see fit.

**Done!** You’ve now successfully installed Shopware 6.

**Demo data**

If you’d like you could install demo data as well. To do this you’ll need to login the backend: <http://APPNAME.hypernode.io/admin/> with the credentials you entered during the step: Basic shop set-up at the installation. At your first login you’ll see the “First Run Wizard”, make sure to install the Demo data at the “Demo data” menu.
