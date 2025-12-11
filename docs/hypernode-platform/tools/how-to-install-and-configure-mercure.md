---
myst:
  html_meta:
    description: Mercure is a real-time communication protocol that enables server-sent
      events (SSE) for live updates in web applications. Learn how to install and
      configure Mercure on your Hypernode.
    title: How to install and configure Mercure on Hypernode?
---

# How to install and configure Mercure on Hypernode

Mercure is a real-time communication protocol that enables server-sent events (SSE) for live updates in web applications. It's particularly useful for applications that need real-time notifications, live chat, or dynamic content updates.

In this guide, we'll walk you through installing and configuring Mercure on your Hypernode using Supervisor to ensure it runs reliably as a background service. This may be required for Pimcore in the future.

```{warning}
Hypernode Support can't help or support this service on your Hypernode.
```

## Installing Mercure

### Step 1: Download the Mercure binary

First, navigate to the [Mercure releases page](https://github.com/dunglas/mercure/releases) and find the most recent legacy Linux x86_64 tar.gz file. For this example, we'll use version 0.20.2:

```console
app@abc-example-magweb-cmbl:~$ mkdir ~/mercure
app@abc-example-magweb-cmbl:~$ cd ~/mercure
app@abc-example-magweb-cmbl:~$ wget https://github.com/dunglas/mercure/releases/download/v0.20.2/mercure-legacy_Linux_x86_64.tar.gz
app@abc-example-magweb-cmbl:~$ tar -xvzf mercure-legacy_Linux_x86_64.tar.gz
app@abc-example-magweb-cmbl:~$ rm mercure-legacy_Linux_x86_64.tar.gz
```

This will extract the `mercure` binary to your `~/mercure` directory.

### Step 2: Generate JWT keys

Mercure uses JWT (JSON Web Tokens) for authorization. You'll need to generate a secret key for signing JWTs. You can generate a secure random key using:

```console
app@abc-example-magweb-cmbl:~$ openssl rand -base64 32
```

Save this key securely - you'll need it for both the Mercure server configuration and your application's JWT generation.

## Configuring Mercure with Supervisor

### Step 3: Create Supervisor configuration

Create a Supervisor configuration file for Mercure. This ensures Mercure runs as a background service and automatically restarts if it crashes:

```console
app@abc-example-magweb-cmbl:~$ mkdir -p ~/supervisor
app@abc-example-magweb-cmbl:~$ nano ~/supervisor/mercure.conf
```

Add the following configuration to the file:

```ini
[program:mercure]
command=/data/web/mercure/mercure run -jwt-key=your-jwt-key --addr :8001
directory=/data/web/mercure
autostart=true
autorestart=true
stderr_logfile=/data/web/supervisor/mercure.err.log
stdout_logfile=/data/web/supervisor/mercure.out.log
user=app
```

**Important**: Replace `your-jwt-key` with the actual JWT secret key you generated in Step 2.

### Step 4: Enable Supervisor (if not already enabled)

If Supervisor isn't already enabled on your Hypernode, enable it:

```console
app@abc-example-magweb-cmbl:~$ hypernode-systemctl settings supervisor_enabled true
app@abc-example-magweb-cmbl:~$ livelog
```

Wait for the changes to be applied before proceeding.

### Step 5: Start Mercure

Now reload Supervisor and start the Mercure service:

```console
app@abc-example-magweb-cmbl:~$ supervisorctl reread
mercure: available
app@abc-example-magweb-cmbl:~$ supervisorctl update
mercure: added process group
app@abc-example-magweb-cmbl:~$ supervisorctl start mercure
```

### Step 6: Verify Mercure is running

Check that Mercure is running correctly:

```console
app@abc-example-magweb-cmbl:~$ supervisorctl status
mercure                         RUNNING   pid 12345, uptime 0:00:05
app@abc-example-magweb-cmbl:~$ curl http://localhost:8001/.well-known/mercure
```

If Mercure is working correctly, you should see a response indicating the Mercure hub is available.
