---
myst:
  html_meta:
    description: Learn how to preinstallfor you Hypernode.
    title: Preinstall | Hypernode
---

# Hypernode-API Perform Preinstall

The following endpoints are available:

```python
POST: https://api.hypernode.com/v2/app/<your_app_name>/perform_preinstall/
```

## POST

`POST` can be used for performing a preinstall for your Hypernode. You have to specify the following data in the post request:

- `preinstall_type`: ("magento_1", "magento_2", "akeneo_3_2", "akeneo_4_0") - Indicates what to install on the node.
- `sample_data`: boolean - Indicates whether or not to install sample data with the installation.
