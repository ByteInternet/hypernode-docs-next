---
myst:
  html_meta:
    description: To set an environment for Shopware 5 is the same process as for Magento,
      with the exception that you’ll have to add an additional NGINX configuration
      file.
    title: 'How to install Shopware 5 on Hypernode Docker? '
redirect_from:
  - /en/ecommerce/shopware/how-to-install-shopware-5-on-hypernode-docker/
---

<!-- source: https://support.hypernode.com/en/ecommerce/shopware/how-to-install-shopware-5-on-hypernode-docker/ -->

# How to Install Shopware 5 on Hypernode Docker

The Hypernode Docker Image can be used to set up a local test environment for Magento as well as Shopware. To set such an environment for Shopware is basically the same process as for Magento, with the exception that you'll have to add an additional nginx configuration file named `server.shopware`.

## Step One - Start a Docker Container

Before you can start a Docker container make sure that Docker is running. Next you need to choose which Docker image you want to run depending on the PHP and MySQL version. You can see all available images **[here](https://github.com/byteinternet/hypernode-docker).**

After you've chosen the image you need to pull the image to your local machine. Once the image is pulled, you can start a Docker container from that image. Use the format below and if needed change the name "hypernode-buster-docer-php7.4-mysql57" to your right version.

```nginx
docker pull docker.hypernode.com/byteinternet/hypernode-buster-docker-php74-mysql57:latest
docker run -p 222:22 -p 8080:80 -p 8025:8025 docker.hypernode.com/byteinternet/hypernode-buster-docker-php74-mysql57:latest

```

This will expose port 222 on the container and port 8080 on the localhost. In this example you should use the following command to connect to the container:

```nginx
# Login as app user

ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -p 222 app@127.0.0.1

```

The password is `insecure_docker_ssh_password`.

## Step Two - Add the Shopware Nginx Config File

Create a **server.shopware** in \*\*/data/web/nginx/\*\*with the content of this [snippet](https://gist.github.com/hn-support/232aa50cd89476aacb54efb6aa56efd8)

## Step Three - Create a Database for Your Shopware shop via Your Terminal

Run the command below to create the database "shopware_5".

```nginx
mysql -e 'create database if not exists shopware_5'

```

## Step Four - Download Shopware

Download the latest Shopware version (version 5 in this example) to your Docker environment:

- Browse to the [Shopware website](https://www.shopware.com/en/download/#shopware-5)
- Left click on the "Download for free" button -> "Copy Link Address".
- Run a `wget` from your Docker environment and paste the Link Address. i.e.:
- `wget http://releases.shopware.com/install_5.5.10_edfcb8e82f331fa5a0935a6c6ff35fe4348bf262.zip`
- unzip the files in /data/web/public:
- `unzip install_5.5.10_edfcb8e82f331fa5a0935a6c6ff35fe4348bf262.zip -d /data/web/public`

## Step Five - Install Shopware via Your Browser

- Open your browser and browse to: “[http://127.0.0.1:8080/recovery/install”](http://127.0.0.1:8080/recovery/install/index.php%E2%80%9D)
- Click "Next"
- Agree to the terms of service.
- Make sure to configure your database correctly:
- Database Server: localhost
- Database User: app
- You can find the password of the database by running the following command in your Docker environment: `cat ~/.my.cnf`
- Select the database you created earlier.
- Click "Next"
- Start the installation.
- Press "Next"
- Select “No, I would like to use the free Community Edition” and click "Next"
- Enter whatever you prefer, but note your credentials as you need them to login to the backend and click "Next"

That's it! You can now visit your Shopware demo-shop and the backend with the following URLs:

`http://127.0.0.1:8080/`

`http://127.0.0.1:8080/backend`
