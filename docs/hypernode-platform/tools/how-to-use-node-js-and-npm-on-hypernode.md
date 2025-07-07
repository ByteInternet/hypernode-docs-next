---
myst:
  html_meta:
    description: This article explains how to use and install other versions of Node.js
      and also how to install NPM packages on Hypernode.
    title: How to Use Node.js and NPM on Hypernode?
redirect_from:
  - /en/hypernode/tools/how-to-use-node-js-and-npm-on-hypernode/
---

# How to Use Node.js and NPM on Hypernode

This article explains how to use and install other versions of Node.js and also how to install NPM packages on Hypernode.

## Using the Installed Version of Node.js

If you use the installed version, you can just start using node and npm.

## Upgrading and downgrading Node.js

By default, the installed NodeJS version on our Hypernode platform is v18. You can check this on your Hypernode by running the command `node -v`. If you need to manually upgrade an app to another Node.js version, for example 20, you can use the command below:

```bash
hypernode-systemctl settings nodejs_version 20
```

Supported Node.js versions are: 6, 10, 16, 18 and 20.

## Setting your PATH

If you want to execute the tools that you installed using `npm`, you should make sure these executables can be located by the shell. This can be easily done this by adjusting your PATH setting.

This PATH variable is used by the Bash shell to locate binaries and scripts. You can adjust it by exporting the PATH variable:

```bash
export PATH="/data/web/node_modules/.bin:$PATH"
```

If you want this setting to be configured every time you log in to your Hypernode, you can add this setting to your `~/.profile`, this file is loaded every time a new shell is spawned.

To configure your PATH variable at login time, run the following command:

```bash
echo 'export PATH="/data/web/node_modules/.bin:$PATH"' >> ~/.profile
```

Now every time you log in, the Bash shell is configured to look for tools in `/data/web/node_modules/.bin` and `/data/web/.node/bin`.

## Installing Packages

Let's install some packages.

When your `PATH` is set up correctly, after the installation with `npm install`, you should immediately be able to use the newly installed tool.

To find the latest command line tool installed, run:

```bash
ls -ltr /data/web/node_modules/.bin | tail -1
```

### Install Gulp

```bash
npm install gulp gulp-cli
```

### Install Grunt

```bash
npm install grunt grunt-cli
```

### Install Sass

```bash
npm install sass
```

Next you need to set the correct path so you don't have to type the absolute path to access compass each time. You can do s with the command:

```bash
export PATH="/data/web/.gem/ruby/2.5.0/gems/compass-1.0.3/bin:$PATH"
```

### Install Less

```bash
npm install less
```

### Install Yarn

```bash
npm install yarn
```

## Using an unsupported Node.js version

```{note}
Installing and using unsupported Node.js versions is no longer supported on the Hypernode Platform. We strongly advise against using unsupported versions, as we cannot provide any assistance or guarantee compatibility.
```

If you want to use a more recent version, it is very easy to install the latest version of Node.js yourself.

NodeJs offers [precompiled packages on their website](https://nodejs.org/en/) that are ready to use on your Hypernode.
All we need to do is download and unpack them to make use of node and npm and install your own node modules.

In this example, we use version v14.17.6, but the installation process is the same when using older or newer versions.

- First, create the directory where we will unpack Node.js:
  ```bash
  mkdir /data/web/.node
  ```
- Then, get the precompiled package from the Node.js website and unpack it in our directory:
  ```bash
  wget https://nodejs.org/dist/v14.17.6/node-v14.17.6-linux-x64.tar.xz -O /tmp/node.txz
  tar xvfJ /tmp/node.txz -C ~/.node --strip-components=1
  rm /tmp/node.txz
  ```

To be able to run this manually installed version when you run `node`, you need to add `~/.node/bin` to your `PATH` variable, so that your shell knows where it should look when you type `node`.

To do this, run the following commands to add the locations to your `PATH` variable:

```bash
export PATH="/data/web/.node/bin:$PATH"
echo 'export PATH="/data/web/.node/bin:$PATH"' >> ~/.profile
```

Both the installations (the already installed or the precompiled self-downloaded version) use `/data/web/node_modules` as their location to install new packages to when using npm.

## Troubleshooting

- When running `npm search`, the command may consume a significant amount of memory. On smaller Hypernode plans, this can trigger our out-of-memory protection, causing your shell session to be terminated and resulting in an automatic logout from your Hypernode.
