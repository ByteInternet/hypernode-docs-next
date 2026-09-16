---
myst:
  html_meta:
    description: Set up a Hypernode Deploy CI/CD pipeline with Github Actions, Gitlab
      CI or Bitbucket Pipelines, including build and deploy jobs per stage.
    title: Hypernode Deploy CI/CD Pipelines | Hypernode
---

# CI/CD Pipelines

Hypernode Deploy runs in your CI/CD pipeline: one job builds the artifact, another deploys it to the stage that matches the branch you pushed to. The articles in this chapter contain a complete pipeline configuration per CI/CD system, which you can copy into your repository and adjust.

All three assume you already have a `deploy.php`. If you do not, start with [Install and configure Hypernode Deploy](getting-started/install-and-configure-hypernode-deploy.md).

```{toctree}
---
caption: Chapters
maxdepth: 1
glob:
---
pipelines/*
```
