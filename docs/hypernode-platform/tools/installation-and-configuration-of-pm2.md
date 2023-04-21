---
myst:
  html_meta:
    description: PM2 is a process manager which keeps your application running as
      a daemon. In this article we’ll cover the installation and configuration process
      of PM2.
    title: How to install and configure PM2 on Hypernode?
redirect_from:
  - /en/support/solutions/articles/48001208544-installation-and-configuration-of-pm2/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001208544-installation-and-configuration-of-pm2/ -->

# Installation and configuration of PM2

PM2 is a process manager which keeps your application running as a daemon. It can be used to run Node.js applications like PWA apps or even internal services to support your eCommerce application. In this article we'll cover the installation and configuration process of PM2.

We will run PM2 in combination with a program called supervisord to make sure that PM2 keeps running even when you upgrade/downgrade your Hypernode.

## Installing PM2

PM2 can be installed in various ways. In this article we'll install the process manager globally for the app user. We'll be running PM2 daemonless by using `pm2-runtime` instead of `pm2`. We don't want that to happen, because we want PM2 to be managed by supervisord.

```console
app@abbt5w-example-magweb-cmbl:~$ # Set NPM prefix to ~/.npm
app@abbt5w-example-magweb-cmbl:~$ npm config set prefix ~/.npm
app@abbt5w-example-magweb-cmbl:~$ # Install PM2 in NPM prefix
app@abbt5w-example-magweb-cmbl:~$ npm install --quiet -g pm2
/data/web/.npm/bin/pm2-dev -> /data/web/.npm/lib/node_modules/pm2/bin/pm2-dev
/data/web/.npm/bin/pm2 -> /data/web/.npm/lib/node_modules/pm2/bin/pm2
/data/web/.npm/bin/pm2-docker -> /data/web/.npm/lib/node_modules/pm2/bin/pm2-docker
/data/web/.npm/bin/pm2-runtime -> /data/web/.npm/lib/node_modules/pm2/bin/pm2-runtime
+ pm2@5.1.2
added 181 packages from 200 contributors in 7.411s
app@abbt5w-example-magweb-cmbl:~$ # Add user NPM prefix bin directory to PATH
app@abbt5w-example-magweb-cmbl:~$ echo 'export PATH="$PATH:$HOME/.npm/bin"' >> ~/.bashrc
app@abbt5w-example-magweb-cmbl:~$ # Reload bash config
app@abbt5w-example-magweb-cmbl:~$ source ~/.bashrc
app@abbt5w-example-magweb-cmbl:~$ # Check if pm2 program can be found
app@abbt5w-example-magweb-cmbl:~$ which pm2
/data/web/.npm/bin/pm2
```

## Enabling supervisord

To make use of supervisord, we first have to make sure it is enabled and running. This can be done by running the command `hypernode-systemctl settings supervisor_enabled true`. Then run the command `livelog` to wait for the changes to be applied.

## The example application

For this article we'll use a simple web server application written in Python. Feel free to use your own application!

```python
#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class MyApplication(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Hello, Visitor!\n", "utf-8"))

def main():
    print("Starting the example application")
    web_server = HTTPServer(("localhost", 8000), MyApplication)
    print("Server started at http://localhost:8000/")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped")

if __name__ == '__main__':
    main()
```

The application only handles `GET` requests and responds with the text "Hello, Visitor!". Save the file to `/data/web/my_application/main.py` and give it execution permissions with the command chmod +x `/data/web/my_application/main.py.`

## Configuring and running PM2

Now that we have PM2 installed, supervisor available and an application to run, we can combine all the things together. Create a file at /data/web/supervisor/my_application.conf with the following contents.

```ini
[program:pm2_my_application]
directory=/data/web/my_application
command=/data/web/.npm/bin/pm2-runtime --interpreter=python3 start main.py
autostart=true
autorestart=true
```

````{note}
In this example, we try to run a Python application, so we specify the interpreter.
Most likely, you're running a Node.js application. In that case you don't need to specify the `--interpreter` option, for example:

  ```ini
  [program:pm2_my_application]
  directory=/data/web/my_application
  command=/data/web/.npm/bin/pm2-runtime start main.js
  autostart=true
  autorestart=true
  ```
````

For more information about options and configuration of PM2 and supervisor, please see the following links:

- [Supervisord configuration file](http://supervisord.org/configuration.html#program-x-section-settings)
- [PM2 quick start](https://pm2.keymetrics.io/docs/usage/quick-start/)

Now we're almost done, we only need to execute a few commands to load the supervisord configuration and start the PM2 process manager.

```console
app@abbt5w-example-magweb-cmbl:~$ # Reload supervisor config files
app@abbt5w-example-magweb-cmbl:~$ supervisorctl reread
pm2_my_application: available
app@abbt5w-example-magweb-cmbl:~$ # Check which processes are available
app@abbt5w-example-magweb-cmbl:~$ supervisorctl avail
pm2_my_application               avail     auto      999:999
app@abbt5w-example-magweb-cmbl:~$ # Add our process to be managed by supervisor
app@abbt5w-example-magweb-cmbl:~$ supervisorctl add pm2_my_application
pm2_my_application: added process group
app@abbt5w-example-magweb-cmbl:~$ # Check status of running processes
app@abbt5w-example-magweb-cmbl:~$ supervisorctl status
pm2_my_application               RUNNING   pid 25139, uptime 0:00:04
app@abbt5w-example-magweb-cmbl:~$ curl http://localhost:8000/
Hello, Visitor!
```
