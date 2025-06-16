---
myst:
  html_meta:
    description: Learn how to manage objects in Hypernode Object Storage using the
      CLI
    title: Hypernode Object Storage | Managing Objects
---

# Managing Objects

The `hypernode-object-storage objects` command provides a comprehensive set of tools for managing your objects in storage. This guide covers all available subcommands and their usage.

## Synchronizing Objects

The `sync` command synchronizes files between a local directory and an object storage location.

```console
hypernode-object-storage objects sync <source> <destination>
```

### Basic Usage

```console
# Sync local directory to object storage
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects sync /path/to/local/dir/ s3://bucket-name/path/

# Sync object storage to local directory
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects sync s3://bucket-name/path/ /path/to/local/dir/
```

### Advanced Options

- `--exclude`: Exclude files matching pattern
- `--include`: Include only files matching pattern
- `--delete`: Delete files in destination not in source
- `--dryrun`: Show what would be done without making changes

### Progress Monitoring

The sync process runs in the background. Monitor progress using the `show` command:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects sync /media/ s3://main/media/
Syncing objects from /media/ to s3://main/media/...
Sync process started with PID 1234 in the background.

app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects show 1234
Completed 9.7 GiB/~30.0 GiB (118.2 MiB/s) with ~5 file(s) remaining
```

## Copying Objects

The `cp` command copies files or objects between locations.

```console
hypernode-object-storage objects cp <source> <destination>
```

### Basic Copy Operations

```console
# Copy single file
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects cp file.txt s3://main/dir/file.txt

# Copy between object storage locations
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects cp s3://main/dir1/file.txt s3://main/dir2/file.txt
```

### Recursive Copying

```console
# Copy entire directory
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects cp -r /path/to/dir/ s3://main/dir/
```

### Pattern Matching

```console
# Copy only specific file types
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects cp -r /path/to/dir/ s3://main/dir/ --exclude "*" --include "*.jpg"
```

## Listing Objects

The `ls` command lists objects in an S3 bucket or folder.

```console
hypernode-object-storage objects ls [path]
```

### Basic Listing

```console
# List root directory
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects ls s3://main/

# List specific directory
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects ls s3://main/media/
```

### Output Formatting

```console
# JSON output
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects ls s3://main/ -F json
```

## Moving Objects

The `mv` command moves or renames files and objects.

```console
hypernode-object-storage objects mv <source> <destination>
```

### Basic Move Operations

```console
# Move single file
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects mv file.txt s3://main/dir/file.txt

# Rename object
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects mv s3://main/oldname.txt s3://main/newname.txt
```

### Batch Operations

```console
# Move multiple files
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects mv /path/to/files/* s3://main/dir/
```

## Deleting Objects

The `rm` command deletes objects from storage.

```console
hypernode-object-storage objects rm <path>
```

### Basic Delete Operations

```console
# Delete single file
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects rm s3://main/file.txt

# Delete with confirmation
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects rm s3://main/file.txt --force
```

### Recursive Deletion

```console
# Delete directory and contents
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects rm s3://main/dir/ --recursive
```

## Empty up an Object Storage

To remove all objects from an Object Storage, use the `rm` subcommand with the `--recursive` flag. This will delete every object within the specified Object Storage. For example:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects rm s3://main --recursive
delete: s3://main/file1.txt
delete: s3://main/file2.txt
```

### Troubleshooting

If the process is not found:

```console
app@abcdef-example-magweb-cmbl:~$ hypernode-object-storage objects show 1234
Process 1234 does not exist anymore
```

This could mean:

- The operation completed successfully
- The process was terminated
- The PID was incorrect
