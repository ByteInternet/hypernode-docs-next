<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-use-node-js-and-npm-on-hypernode/ -->

# How to Use Node.js and NPM on Hypernode

This article explains how to use and install other versions of Node.js and also how to install NPM packages on Hypernode

- [Using the Installed Version of Node.js](#Using-the-Installed-Version-of-Node.js)
- [Installing Node.js v10.16](#Installing-Node.js-v10.16)
- [Downgrading to Node.js v6](#Downgrading-to-Node.js-v6)
- [Setting your PATH](#Setting-your-PATH)
- [Installing Packages](#Installing-Packages)
  - [Install Gulp](#Install-Gulp)
  - [Install Grunt](#Install-Grunt)
  - [Install Sass](#Install-Sass)
  - [Install Compass](#Install-Compass)
  - [Install Less](#Install-Less)
  - [Install Yarn](#Install-Yarn)
- [Using a newer version of Node.js](#Using-a-newer-version-of-Node.js)
  - [Install a newer version of Node.js](#Install-a-newer-version-of-Node.js)
  - [Configure a Manually Installed Node.js](#Configure-a-Manually-Installed-Node.js)
- [Troubleshooting](#Troubleshooting)

## Using the Installed Version of Node.js

If you use the installed version, you can just start using node and npm.

## Installing Node.js v10.24.0

By default, the installed NodeJS version on our Hypernode platform is v10. You can check this on your Hypernode by running the command `node -v`. If you need to manually upgrade an app to Node.js v10, you can use the command below:

```nginx
hypernode-systemctl settings nodejs_version --value 10
```

## Downgrading to Node.js v6

You can also downgrade to Node.js v6 by running this command:

```nginx
hypernode-systemctl settings nodejs_version --value 6
```

## Setting your PATH

If you want to execute the tools that you installed using npm, you should make sure these executables can be located by the shell. This can be easily done this by adjusting your PATH setting.

This PATH variable is used by the Bash shell to locate binaries and scripts. You can adjust it by exporting the PATH variable:

```nginx
 export PATH="/data/web/node_modules/.bin:$PATH"
```

If you want this setting to be configured every time you log in to your Hypernode, you can add this setting to your ~/.profile, this file is loaded every time a new shell is spawned.

To configure your PATH variable at login time, run the following command:

```nginx
 echo 'export PATH="/data/web/node_modules/.bin:$PATH"' >> ~/.profile
```

Now every time you log in, the Bash shell is configured to look for tools in /data/web/node_modules/.bin and /data/web/.node/bin.

## Installing Packages

Let's install some packages.

When your PATH is setup correctly, after the installation with npm install, you should immediately be able to use the newly installed tool.

To find the latest command line tool installed, run: `ls -ltr /data/web/node_modules/.bin | tail -1`

### Install Gulp

```nginx
 npm install gulp gulp-cli
```

### Install Grunt

```nginx
npm install grunt grunt-cli
```

### Install Sass

```nginx
npm install sass
```

### Install Compass

```nginx
 npm install compass
```

When your Hypernode is using the OS [Debian Buster](https://changelog.hypernode.com/changelog/release-7351-new-hypernodes-will-be-booted-on-debian-buster/) then the aforementioned method will not be applicable. Instead you can use the following command to install compass

```nginx
gem install --user-install compass
```

Next you need to set the correct path so you don't have to type the absolute path to access compass each time. You can do s with the command:

```nginx
export PATH="/data/web/.gem/ruby/2.5.0/gems/compass-1.0.3/bin:$PATH"
```

### Install Less

```nginx
npm install less
```

### Install Yarn

*To install yarn, a more recent version of nodejs is required, so*[*follow the instructions and download and unpack a newer version of nodejs*](https://archive.support.hypernode.com/knowledgebase/use-nodejs-npm-hypernode/#Using_a_newer_version_of_NodeJs)*first*

```nginx
npm install yarn
```

## **Using a newer version of Node.js**

### **Install a newer version of Node.js**

If you want to use a more recent version, it is very easy to install the latest version of Node.js yourself.

NodeJs offers [precompiled packages on their website](https://nodejs.org/en/) that are ready to use on your Hypernode.
All we need to do is download and unpack them to make use of node and npm and install your own node modules.

In this example we use version v14.17.6 but the installation process is the same when using older or newer versions.

- First, create the directory where we will unpack Node.js:

```nginx
mkdir /data/web/.node
```

- Then, get the precompiled package from the Node.js website and unpack it in our directory:

```nginx
wget [https://nodejs.org/dist/v14.17.6/node-v14.17.6-linux-x64.tar.xz](https://nodejs.org/dist/v4.4.5/node-v4.4.5-linux-x64.tar.xz) -O /tmp/node.txz
cd ~/.node && tar xvfJ /tmp/node.txz -C . --strip-components=1
rm /tmp/node.txz
```

That’s it, you now have a precompiled node installation in `~/node`

### Configure a Manually Installed Node.js

To run the manually installed executables, you need to change your PATH variable to make sure your node is located by the Bash shell before the pre-installed version.

To do this, run the following command to add the locations to your PATH:

```nginx
 export PATH="/data/web/node_modules/.bin:/data/web/.node/bin:$PATH"
```

Or to make the settings permanent, add it to your `~/.profile`:

```nginx
 echo 'export PATH="/data/web/node_modules/.bin:/data/web/.node/bin:$PATH"' >> ~/.profile
```

Both the installations (the already installed or the precompiled self-downloaded version) use `/data/web/node_modules` as their location to install new packages to when using npm.

## Troubleshooting

- When using npm search, so much memory is used that on Hypernode Grow plans, your shell will get killed and you’ll be automagically logged out of your Hypernode due to our out of memory protection.
