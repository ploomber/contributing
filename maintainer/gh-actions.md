# GitHub actions

Here are the GitHub actions we use for our projects. Note that some of them might need modifications. Check the `.yml` file for details

## Test and deploy

[`ci.yml`](../sample-github-workflows/ci.yml)

This workflow runs unit tests, checks the project and uploads to PyPI.

## Broken links

[`broken-links.yml`](../sample-github-workflows/broken-links.yml)

Checks for broken links anywhere in the project.

For configuration details, [see here.](https://pkgmt.readthedocs.io/en/latest/check-links.html)

## ChatOps

[`chatops.yml`](../sample-github-workflows/chatops.yml)

Implements operations triggered with messages in the GitHub chat.

- `/format`: runs `pkgmt format`

## Workflow edits

[`workflow-edits.yml`](../sample-github-workflows/workflow-edits.yml)

Only passes if `.github/workflows/` **have not been modified**. This workflow is a security measure.

If `.github/workflows/` has been modified, a mantainer needs to add the `allow-workflow-edits` label to the PR and the contributor must push again.

```sh
git commit --allow-empty -m 'trigger workflows'
```

```{tip}
See [](ops.md#sync-github-labels) for a tool to add GitHub labels programmatically.
```