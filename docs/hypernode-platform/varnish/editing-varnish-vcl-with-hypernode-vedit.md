---
myst:
  html_meta:
    description: Learn how to easily edit your Varnish VCL with hypernode-vedit.
    title: Editing Varnish VCL with hypernode-vedit
---

# Editing Varnish VCL with hypernode-vedit

While we generally advise developers to keep their Varnish VCL in a file of their own (like `/data/web/app.vcl`), there are cases where you might want to make quick changes directly to the active VCL. For example, when testing a change or debugging an issue.

The `hypernode-vedit` CLI tool allows you to edit the active Varnish VCL on your Hypernode. The command will store the active VCL in a temporary file, open it in the default editor, and then reload the edited VCL back into Varnish when you save and exit.

```console
app@example-magweb-cmbl ~ $ hypernode-vedit
Checking VCL syntax...
Syntax OK.
Apply this VCL now? [y/N] y
VCL loaded and activated as 'vcl_1780641679'.
Waiting for the VCL to be saved to disk...
VCL saved to /data/var/varnish/default.vcl.
```

In this example, you of course don't see the actual editing process, but after you save and exit the editor, the new VCL is loaded and activated in Varnish. The activated VCL is also written to `/data/var/varnish/default.vcl`, the file Varnish loads when it starts, so your change survives a restart of Varnish or of your Hypernode.
