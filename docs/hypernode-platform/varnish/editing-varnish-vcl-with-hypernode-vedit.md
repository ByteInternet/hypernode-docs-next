---
myst:
  html_meta:
    description: Learn how to easily edit your Varnish VCL with hypernode-vedit.
    title: Editing Varnish VCL with hypernode-vedit
---

# Editing Varnish VCL with hypernode-vedit

While we generally advise developers to make changes to the Varnish VCL in a persistent way (like `/data/web/app.vcl`), there are cases where you might want to make temporary changes directly to the active VCL. For example, when testing a change or debugging an issue.

The `hypernode-vedit` CLI tool allows you to edit the active Varnish VCL on your Hypernode. The command will store the active VCL in a temporary file, open it in the default editor, and then reload the edited VCL back into Varnish when you save and exit.

```console
app@example-magweb-cmbl ~ $ hypernode-vedit
Checking VCL syntax...
Syntax OK.
Apply this VCL now? [y/N] y
VCL loaded and activated as 'vcl_1780641679'.
```

In this example, you of course don't see the actual editing process, but after you save and exit the editor, the new VCL is loaded and activated in Varnish.
