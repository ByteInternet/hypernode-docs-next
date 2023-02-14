---
myst:
  html_meta:
    description: 'Supervisor enables you to use programs that need to run all the
      time on your Hypernode. Discover how to use supervisor step-by-step. '
    title: How to use Supervisor? | Hypernode
redirect_from:
  - /en/hypernode/tools/how-to-use-supervisor/
---

<!-- source: https://support.hypernode.com/en/hypernode/tools/how-to-use-supervisor/ -->

# How to Use Supervisor

Supervisor enables you to use programs that need to run all the time on your Hypernode. These (usually long running) programs should not fail if there is an error. To accomplish this Supervisor watches your programs and restarts them if they might fail. Supervisor works great for use cases where a web hook or metrics always needs to run.

## How to Use Supervisor

Before we start using Supervisor we first need to enable it on the Hypernode.

```nginx
hypernode-systemctl settings supervisor_enabled True
```

To test if Supervisor is properly running the following command should open Supervisor.

```nginx
supervisorctl
```

To store the long running programs we create a folder on the Hypernode.

```nginx
mkdir /data/web/long_running
```

In this folder we create a program that we want to keep running no matter what. For this example we create a simple Python program that will crash every 10 seconds.

```nginx
nano /data/web/long_running/supervisortest.py
```

And the contents of our test program.

```nginx
#!/usr/bin/env python3

from time import sleep

def main():
    sleep(10)
    raise Exception("Application Crashing")

if __name__ == "__main__":
    print("Starting the simple test application")
    main()
```

We can test if our test program works.

```nginx
python3 /data/web/long_running/supervisortest.py
```

If our program works we can add it to Supervisor. To do this we add a config file in the folder `/data/web/supervisor`. This file needs to have the `*.conf` extension.

```nginx
mkdir -p /data/web/supervisor
nano /data/web/supervisor/supervisortest.conf
```

We need a name for the program and a command for Supervisor to run, so we fill the config file with the following content.

```nginx
[program:supervisor_test_program]
command=/usr/bin/python3 /data/web/long_running/supervisortest.py
```

Supervisor does not yet know about the programs existence. For Supervisor to run the program we add it to Supervisor.

```nginx
app@abbrdk-appname-magweb-cmbl:~$ supervisorctl
supervisor> reread
supervisor_test_program: available
supervisor> avail
supervisor_test_program avail auto 999:999
supervisor> add supervisor_test_program
supervisor_test_program: added process group
supervisor> status
supervisor_test_program RUNNING pid 13165, uptime 0:00:02
supervisor>
```

To check if the application is really running you can check the `status` command, this command should show the uptime resetting every 10 seconds. For a more detailed log of how the program is running the log files can be found in `/data/var/log/supervisor/` or in a specified file by using `stdout_logfile=` and `stderr_logfile=` in the config file.

Now you can create long running programs on your Hypernode.
