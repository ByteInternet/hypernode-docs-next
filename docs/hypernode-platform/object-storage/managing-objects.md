---
myst:
  html_meta:
    description: Learn how to manage objects in Hypernode Object Storage
    title: Hypernode Object Storage | Managing Objects
---

# Managing Objects

You can manage your objects using the `hypernode-object-storage objects` subcommand.
It supports all common operations--listing, copying, moving, and deleting files--while also allowing you to sync files in the background and monitor the progress of an ongoing sync.

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects --help
usage: hypernode-object-storage objects [-h] {sync,cp,ls,mv,rm,show} ...

Manage objects in object storage

positional arguments:
  {sync,cp,ls,mv,rm,show}
    sync                Synchronize files between a local directory and an object storage location
    cp                  Copy a file or object from one location to another
    ls                  List objects in an S3 bucket or folder
    mv                  Move or rename a file or object
    rm                  Delete an object from S3
    show                Display the current status of an ongoing sync process

options:
  -h, --help            show this help message and exit
```

It is important to note that `hypernode-object-storage objects` supports all optional flags available in `aws s3`, allowing you to customize its behavior for advanced configurations.

## Syncing files and monitoring progress

Syncing files between your local directory and object storage is simple. Run the following command:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects sync /example/local/path/ s3://example/bucket/uri/
Syncing objects from /example/local/path/ to s3://example/bucket/uri/...
Sync process started with PID 1234 in the background.
```

The `sync` operation runs in the background, and you can monitor its progress by using the `show` command, for example:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects show 1234
Completed 9.7 GiB/~30.0 GiB (118.2 MiB/s) with ~5 file(s) remaining (calculating...)
```

If you run the `show` command after the sync operation has finished, you’ll see output like this:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects show 1234
Process 1234 does not exist anymore
```

## Empty up an Object Storage

To remove all objects from an Object Storage, use the `rm` subcommand with the `--recursive` flag. This will delete every object within the specified Object Storage. For example:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects rm s3://main --recursive
delete: s3://main/file1.txt
delete: s3://main/file2.txt
```

Be careful when using `--recursive`, as this action is irreversible and will permanently remove all data from the Object Storage.
