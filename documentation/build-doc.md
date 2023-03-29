# Building documentation

```{note}
If you have issues building the documentation, send us a message on [Slack](https://ploomber.io/community) and we'll help you.
```

We build the documentation on each Pull Request; however, you might run it locally for faster previews. We've standardized the setup process for the most part but send us a message on [Slack](https://ploomber.io/community) if you have issues.

The steps are the same as in the [Setup](../contributing/setup.md#setup), but you need to ensure you pass the `--doc` argument to the `pkgmt setup` (or `invoke setup`) command. Once you'r ready, ensure you activate the conda environment (printed at the end of the command):

```sh
conda activate ENV_NAME
```

To build the docs:

```sh
pip install pkgmt --upgrade
pkgmt doc
```

In some cases, the documentation cache might cause issues, to perform a clean doc build:

```sh
pkgmt doc --clean
```

```{warning}
If the project you're contributing to has a `tasks.py` file in the root directory (e.g., [Ploomber](https://github.com/ploomber/ploomber)), you must run `invoke doc` to build the docs. If you have issues, send us a message on [Slack.](https://ploomber.io/community). The source code for the `invoke` commands is in `tasks.py` so you might want to check it out as well.
```

To learn more about writing docs, [see here](../maintainer/doc-guide.md)