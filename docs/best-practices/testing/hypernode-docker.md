---
myst:
  html_meta:
    description: This image can be used to set up a local development environment,
      or as a build machine in a CI environment representative of the production environment.
    title: Hypernode Docker | Everything you need to know | Testing
redirect_from:
  - /en/best-practices/testing/hypernode-docker/
  - /knowledgebase/hypernode-docker/
---

<!-- source: https://support.hypernode.com/en/best-practices/testing/hypernode-docker/ -->

# Hypernode-docker

The official Hypernode Docker image for Magento development is now available. This image can be used to set up a fast and easy local development environment for Hypernode, or as a build machine in a CI environment representative of the production environment. The image contains the exact same packages and configuration as a real Hypernode except for some Docker specific tweaks. By testing and developing against this image you can be sure that when you deploy to a Hypernode in production there will be no surprises because of different software versions or configurations.

Interested in a case study? Read [this article](https://blog.guapa.nl/local-development-with-the-hypernode-docker-container-linux/) about the Hypernode docker of one of our partners!

## About the Hypernode Docker Image

We build this image multiple times a day (every time we do a [release](https://changelog.hypernode.com/)) by applying our configuration management on the [phusion/baseimage-docker](https://github.com/phusion/baseimage-docker) ["fat" container](https://blog.phusion.nl/2015/01/20/baseimage-docker-fat-containers-treating-containers-vms/). By treating the Docker as a lightweight VM instead of as a vehicle for a single process we stay close to what an actual Hypernode actually looks like. No micro-services or a multi-container application, but a single instance with minimal network overhead and all batteries included.

The `hypernode-docker` image has SSH, PHP, NGINX, MySQL, Redis, Varnish and Elasticsearch. The biggest difference between a real Hypernode and this container is that this environment does not have an [init system](https://en.wikipedia.org/wiki/Init). While it is possible to [run systemd within a Docker Container](https://developers.redhat.com/blog/2014/05/05/running-systemd-within-docker-container/) if the host is also runs [systemd](https://www.freedesktop.org/wiki/Software/systemd/), we choose not to do so to achieve greater compatibility and user-friendliness.

\*\*\*New:\*\*On the newest Hypernode-docker image is Elasticsearch 7.x by default included. There is nothing you'd have to do to be able to use it since ES 7.x is enabled by default.

## Usage

First of all download the latest version of Docker for Windows or Mac from the [Docker website](https://www.docker.com/get-started) and make sure to install Docker on your computer. If you are working with Linux you can find all the info to install Docker in their documentation [Docker Docs](https://docs.docker.com/install).

Now you need to decide which \*\*[image](https://github.com/byteinternet/hypernode-docker)\*\*you need. We've several images, all with other PHP and MySQL versions. After you decided which images fits your requirements you can pull the image to your local machine and start a new Docker container. In the below example we used the image "hypernode-buster-docker-php74-mysql57". If you need another you can change that name in both commands below to the image you want to use.

### Start the Docker and logging in

Starting a container

```
docker pull docker.hypernode.com/byteinternet/hypernode-buster-docker-php74-mysql57:latest
docker run -p 222:22 -p 8080:80 -p 8025:8025 docker.hypernode.com/byteinternet/hypernode-buster-docker-php74-mysql57:latest
```

This makes the SSH, HTTP, and Mailhog ports available on the localhost. If you need any other ports (Such as 443 for HTTPS, or 2222 for sftp) available, you can insert these in the command above. In this example you should use the following command to connect to the container:

```
# Login as app user, obviously you can replace "app" with "root" to login as root
ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -p 222 app@127.0.0.1
```

The password is ‘*insecure_docker_ssh_password*’.

**Checker whether or not you're are in the Docker environment**

```
# This file does not exist on real Hypernodes
app@e4b7d958e69c:~$ ls /etc/hypernode/is_docker
/etc/hypernode/is_docker
```

Now you're ready to use the hypernode-importer to import a shop from a remote server.

```
hypernode-importer --host yourhypernode.hypernode.io --path /data/web/public --set-default-url
```

To see the container in your browser you should change the base-url to “[http://127.0.0.1:8080/”](http://127.0.0.1:8080/%E2%80%9D) and don’t forget to flush your cache afterwards:

#### **Magento 1**[How to change base-urls in Magento 1](../../ecommerce-applications/magento-1/how-to-change-the-base-url-in-magento-1-x.md)

```
magerun ca:fl
```

#### **Magento 2**[How to change base-url in Magento 2](../../ecommerce-applications/magento-2/how-to-change-your-magento-2-base-urls.md)

```
magerun ca:fl
```

```
cd magento2
magerun2 ca:fl
```

#### **General Docker Commands**

You might want to start several docker containers to develop multiple webshops. These commands may come in handy:

```
# Get the container ID of the Hypernode docker
HN_CONTAINER_ID=$(docker ps -aq -f "ancestor=docker.hypernode.com/byteinternet/hypernode-docker:latest")

# Find the IP address of the container
docker inspect -f '{{ .NetworkSettings.IPAddress }}' $HN_CONTAINER_ID
172.17.0.2

# Run/Start container
docker start 9187ce8348b0

# Stop container
docker stop 9187ce8348b0

# Remove container (container must be stop before it could be removed)
docker rm 9187ce8348b0
```

### Restarting services

Because `systemctl` is not available inside the container, the services are started by an [init script](https://github.com/phusion/baseimage-docker#running-scripts-during-container-startup) on container startup. Note that because the systemd unit files are not parsed there could be a slight drift between what commandline flags the processes actually use in production compared to in this contanier.

To restart all services run:

```
bash /etc/my_init.d/60_restart_services.sh
```

If you only want to restart a specific service, inspect the restart_services.sh script and kill the screen for the service you want to restart. Then run the corresponding screen command to start the service again.

## Starting the container

### Running the container on the foreground

To start the container in the foreground, run the following command:

```
$ docker pull docker.hypernode.com/byteinternet/hypernode-docker:latest
$ docker run -p 222:22 -p 8080:80 -p 8025:8025 docker.hypernode.com/byteinternet/hypernode-docker:latest
*** Running /etc/my_init.d/00_regen_ssh_host_keys.sh...
*** Running /etc/my_init.d/10_login_instructions.sh...
_
/\ /\_ _ _ __ ___ _ __ _ __ ___ __| | ___
/ /_/ / | | | '_ \ / _ \ '__| '_ \ / _ \ / _` |/ _ \
/ __ /| |_| | |_) | __/ | | | | | (_) | (_| | __/
\/ /_/ \__, | .__/ \___|_| |_| |_|\___/ \__,_|\___|
|___/|_|

Host/IP: xxxxx-dummytag-docker.nodes.hypernode.io (172.17.0.3)
Account_id: 666
Release: release-5278-28-ga9d3844 @ 2018-06-05 12:56:34 UTC

Handy commands (more at https://support.hypernode.com):

livefpm (see live PHP status)
tal | pnl (follow live requests)

hypernode-importer (import a Magento shop)
hypernode-image-optimizer (reduce image size)
hypernode-ftp (manage FTP accounts)

magerun list (many useful extensions)

------------------------------------------------------------------------------
The SSH daemon will be up in a couple of seconds, you can login with: ssh -A app@172.17.0.3
*** Running /etc/my_init.d/50_copy_key.sh...
*** Running /etc/my_init.d/50_fix_mailname.sh...
*** Running /etc/my_init.d/51_postfix.sh...
* Starting Postfix Mail Transport Agent postfix
...done.
*** Running /etc/my_init.d/60_restart_services.sh...
Killing old Hypernode services
Killing any old NGINX service
Killing any old Redis service
Killing any old PHP-FPM service
Killing any old MySQL service
Killing any old Mailhog service
Killing any old Varnish service
Giving any old services 5 seconds to stop..
No Sockets found in /var/run/screen/S-root.

Starting new detached hypernode services. See screen -x
Starting NGINX
Starting Redis
Starting PHP
Starting MySQL
Starting Mailhog
Starting Varnish
Giving the new services a couple of seconds to start..
hypernode-docker status: everything ok
*** Running /etc/rc.local...
*** Booting runit daemon...
*** Runit started as PID 312
```

You can now log in with SSH using the IP address seen in the output.

### Running The Container on The Background

To start the container in the background, run the following command:

```
$ docker run -d -p 222:22 -p 8080:80 -p 8025:8025 docker.hypernode.com/byteinternet/hypernode-docker:latest
36532b58822cf27f74234f6afc01db21fca15b480bf43634ae725db35047dc5a
```

The IP address of the container can then be found with:

```
$ docker inspect -f '{{ .NetworkSettings.IPAddress }}' 36532b58822cf27f74234f6afc01db21fca15b480bf43634ae725db35047dc5a
172.17.0.3
```

You can view the logs with docker logs:

```
$ docker logs 36532b58822cf27f74234f6afc01db21fca15b480bf43634ae725db35047dc5a
*** Running /etc/my_init.d/00_regen_ssh_host_keys.sh...
*** Running /etc/my_init.d/10_login_instructions.sh...
_
/\ /\_ _ _ __ ___ _ __ _ __ ___ __| | ___
/ /_/ / | | | '_ \ / _ \ '__| '_ \ / _ \ / _` |/ _ \
/ __ /| |_| | |_) | __/ | | | | | (_) | (_| | __/
\/ /_/ \__, | .__/ \___|_| |_| |_|\___/ \__,_|\___|
|___/|_|

Host/IP: xxxxx-dummytag-docker.nodes.hypernode.io (172.17.0.3)
Account_id: 666
Release: release-5278-28-ga9d3844 @ 2018-06-05 12:56:34 UTC

Handy commands (more at https://support.hypernode.com):

livefpm (see live PHP status)
tal | pnl (follow live requests)

hypernode-importer (import a Magento shop)
hypernode-image-optimizer (reduce image size)
hypernode-ftp (manage FTP accounts)

magerun list (many useful extensions)

------------------------------------------------------------------------------
The SSH daemon will be up in a couple of seconds, you can login with: ssh -A app@172.17.0.3
*** Running /etc/my_init.d/50_copy_key.sh...
*** Running /etc/my_init.d/50_fix_mailname.sh...
*** Running /etc/my_init.d/51_postfix.sh...
* Starting Postfix Mail Transport Agent postfix
...done.
*** Running /etc/my_init.d/60_restart_services.sh...
Killing old Hypernode services
Killing any old NGINX service
Killing any old Redis service
Killing any old PHP-FPM service
Killing any old MySQL service
Killing any old Mailhog service
Killing any old Varnish service
Giving any old services 5 seconds to stop..
No Sockets found in /var/run/screen/S-root.

Starting new detached hypernode services. See screen -x
Starting NGINX
Starting Redis
Starting PHP
Starting MySQL
Starting Mailhog
Starting Varnish
Giving the new services a couple of seconds to start..
hypernode-docker status: everything ok
*** Running /etc/rc.local...
*** Booting runit daemon...
*** Runit started as PID 312
```

## Importing a Magento shop

1. Add a hosts entry for the Docker:

```
grep -q hypernode.hypernode.local /etc/hosts || echo "172.17.0.2 hypernode.hypernode.local" >> /etc/hosts
```

2. Start an SSH agent and add your key:

```
eval $(ssh-agent -s)
ssh-add # Add your keys
```

3. Log in to the hypernode-docker container:

```
# Log in with SSH agent forwarding
# The default password is 'insecure_docker_ssh_password', or use the insecure key
ssh -A root@172.17.0.2
```

4. Double-check you are in the Docker environment and not the real Hypernode:

```
# This file does not exist on real Hypernodes
app@e4b7d958e69c:~$ ls /etc/hypernode/is_docker
/etc/hypernode/is_docker
```

5. Import application

Run the [hypernode-importer](../../hypernode-platform/tools/how-to-migrate-your-shop-to-hypernode.md#option-2-for-all-customers-migrate-your-shop-via-shell-using-the-hypernode-importer) to import a shop from a real Hypernode:

```
hypernode-importer --host yourhypernode.hypernode.io --path /data/web/public --set-default-url
```

6. Point your browser to the importer shop:

Go to <http://hypernode.hypernode.local/>

## Adding keys to Container

To create a Docker instance of hypernode-docker with your own keys, create a directory with your public key in it and a Dockerfile.

```
$ ls
key.pub Dockerfile
$ cat Dockerfile
FROM docker.hypernode.com/byteinternet/hypernode-docker:latest
MAINTAINER yourname

ADD key.pub /tmp/key.pub
RUN cat /tmp/key.pub > /root/.ssh/authorized_keys && cat /tmp/key.pub > /data/web/.ssh/authorized_keys && rm -f /tmp/deployment.pub
```

Then build the Docker with:

```
docker build -t hypernode-with-keys .
```

And once finished, start the Docker with

```
docker run hypernode-with-keys
```

Note: remember that you will also need to change the default app and root user passwords if you're looking to create a secure environment.

## Inspecting Emails Sent from The Docker

Like in the [hypernode-vagrant](https://github.com/ByteInternet/hypernode-vagrant#mail) project, all emails are caught and redirected to a [MailHog](https://github.com/mailhog/MailHog) instance. You can visit the mailhog web interface on port `8025`. So for example, if the IP of your container is `172.17.0.2` you would be able to access MailHog on <http://172.17.0.2:8025/>.

Alternatively you could set up a hosts entry like so on the host (not in the Docker):

```
grep -q hypernode.hypernode.local /etc/hosts || echo "172.17.0.2 hypernode.hypernode.local" >> /etc/hosts
```

And then visit the MailHog instance on [http://hypernode.hypernode.local:8025](http://hypernode.hypernode.local:8025/).

## Installing Magento 1

Make sure you have a hosts entry set up:

```
# Note that you need root to write to /etc/hosts
grep -q hypernode.hypernode.local /etc/hosts || echo "172.17.0.2 hypernode.hypernode.local" >> /etc/hosts
```

Switch to a Magento 1 compatible PHP version

```
# Log in as root
$ ssh root@172.17.0.2 -i keys/insecure_key
# Change the PHP service version to 7.0
sed -i 's/7\.1/7.0/g' /etc/my_init.d/60_restart_services.sh
# Update PHP symlinks
update-alternatives --set php $(which php7.0)
# Restart services
bash /etc/my_init.d/60_restart_services.sh
# Log out of the Docker
exit
```

Log in to the container as the app user

```
ssh app@172.17.0.2 -i keys/insecure_key
```

Remove any Magento 2 specific NGINX configuration

```
rm -rf /data/web/nginx/magento2.flag
```

Create a new database:

```
echo 'create database magento;' | mysql
```

Install Magento with [n98-magerun](https://github.com/netz98/n98-magerun):

```
# Write the n98-magerun config file:
cat << EOF > /data/web/.n98-magerun.yaml
commands:
N98\Magento\Command\Installer\InstallCommand:
installation:
defaults:
currency: EUR
locale: nl_NL
timezone: UTC
use_secure: no
use_rewrites: yes
session_save: files
admin_username: admin
admin_firstname: Firstname
admin_lastname: Lastname
admin_password: thisisanexamplePassword123456
admin_frontname: example
admin_email: example@example.com
encryption_key:
installation_folder: /data/web/public

magento-packages:
- name: byte-mag-mirror-latest
version: 1.9
dist:
url: http://magento.mirror.hypernode.com/releases/magento-latest.tar.gz
type: tar
extra:
sample-data: sample-data-1.9.1.0
EOF

# Install Magento 1
php -d memory_limit=1024M /usr/local/bin/n98-magerun install --magentoVersionByName=byte-mag-mirror-latest \
--dbHost=127.0.0.1 --dbUser=app --dbPass=$(cat /data/web/.my.cnf | grep pass | awk '{print$3}') \
--dbName=magento --installSampleData=no --useDefaultConfigParams=yes --installationFolder=/data/web/public \
--baseUrl=http://hypernode.hypernode.local --replaceHtaccessFile=no --no-interaction
```

## Varnish on Docker

By default Varnish is already enabled, but won’t work because the server is missing some configuration in order to work correctly. This isn’t implemented because there were earlier issues with Varnish on a Vagrant environment.

If you want to experiment with Varnish in your Docker environment you should overwrite the content of “/etc/nginx/outside.conf”, to do this you need to log in as root user:

```
# Log in as the root user
ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -p 222 root@127.0.0.1
```

Overwrite the content of “/etc/nginx/outside.conf” to the following:

```
## This file defines the vhosts that are facing outward (port 80 / 443 for public, 8880 and 8888 / 8443 for staging).
# This is the auto server definition for docroot public
server {
# Log nullbytes in checkout pages post bodies
access_by_lua_file "/etc/nginx/request_security.lua";

## default vhost definition
# we need to define multiple ports because there is no overlap between what is allowed by some external services (cloudflare and adyen)
listen 80 default_server;

# Outside.conf will pass remote_addr to fastcgi as remote_addr, but inside.conf must
# pass http_x_real_ip. In order to still share the fastcgi_params file inside an include
# inside an include, we set this variable to remote_addr and set it to something else in inside.conf.
root /data/web/public;
## i'm redirecting to varnish here!
location / {
set $log_handler varnish;
proxy_pass http://127.0.0.1:6081;
proxy_read_timeout 900s; # equal to fastcgi_read_timeout at handlers.conf:16
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Forwarded-Port $server_port;
proxy_set_header Host $http_host;
}
include /etc/nginx/security.conf;
# phpmyadmin should never pass through Varnish, so include an alias and a handler here
include /etc/nginx/phpmyadmin.conf;
include /etc/nginx/app/public.*;
include /etc/nginx/app/server.*;
# in case the user wants to route a part of the site directly to FPM in override files
include /etc/nginx/handlers.conf;
# blocking bots tool
include /etc/nginx/server.blocked_bots.conf;
}
# This is the auto server definition for docroot staging
server {
# Log nullbytes in checkout pages post bodies
access_by_lua_file "/etc/nginx/request_security.lua";

## default vhost definition
# we need to define multiple ports because there is no overlap between what is allowed by some external services (cloudflare and adyen)
listen 8880 default_server;
listen 8888;

# Outside.conf will pass remote_addr to fastcgi as remote_addr, but inside.conf must
# pass http_x_real_ip. In order to still share the fastcgi_params file inside an include
# inside an include, we set this variable to remote_addr and set it to something else in inside.conf.
root /data/web/staging;
# Set a default document root, and store it in a variable. This variable will be used in the
# named location '@fastcgi_backend' to set the documentroot from which PHP-files will be served.
# This is needed to be able to change the documentroot for phpmyadmin later on.
include /etc/nginx/security.conf;
include /etc/nginx/magento.conf;
include /etc/nginx/phpmyadmin.conf;
include /etc/nginx/app/server.*;
# Cannot use an Nginx var in include statements. -WdG
# This line will include staging.* and public.* files if they exist.
include /etc/nginx/app/staging.*;

# blocking bots tool
include /etc/nginx/server.blocked_bots.conf;
}
```

## Restart Services

Restart the services after you changed the config file.

`bash /etc/my_init.d/60_restart_services.sh`

That’s it, Varnish should be working fine now! You can see the results when you enter ‘varnishhist’ in the CLI and click around in your webshop at <http://127.0.0.1:8080/>
