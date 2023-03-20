# Contributing

> **Note**
> If you get stuck in the contribution process, send us a message on [Slack](https://ploomber.io/community) and we'll help you.


This is a general guide applicable to all our projects. However, there might be particular details on some repositories so check out the `CONTRIBUTING.md` for the project you're working on as well.

For an introduction to open-source contributions, check out our [blog post](https://ploomber.io/blog/open-source/).

> **Note**
> If you're contributing with documentation (API docs, tutorials, etc.), check out the [doc contribution](documentation/README.md) document.

## Setup

> **Warning**
> Some of our projects have a `tasks.py` file in the root directory (e.g., [Ploomber](https://github.com/ploomber/ploomber)), if that's the case for the project you want to contribute to, go to the [next section](#setup-projects-with-taskspy)

Setting up your environment requires [miniconda](https://docs.conda.io/en/latest/miniconda.html), once installed, verify it's working with:

```sh
conda --help
```

If `conda` is activated, you should see `(base)` as the prefix of your terminal prompt.


Now, let's setup your development environment:

```sh
pip install pkgmt --upgrade

# this command will create a conda environment for you
pkgmt setup

# if you want to build the documentation locally, pass --doc
pkgmt setup --doc
```

Now, let's verify your [development installation.](#verifying-installation)

## Setup (projects with `tasks.py`)


If the project you want to contribute has a `tasks.py` file, follow these instructions.


Setting up your environment requires [miniconda](https://docs.conda.io/en/latest/miniconda.html), once installed, verify it's working with:


```sh
conda --help
```

If `conda` is activated, you should see `(base)` as the prefix of your terminal prompt.

Now, let's setup your development environment:

```sh
pip install invoke --upgrade

# this command will setup the development environment
invoke setup

# if you want to build the documentation locally, pass --doc
invoke setup --doc
```

There might be other commands available, to list them:

```sh
invoke --list
```

To get more information about a command:

```sh
invoke COMMAND --help
```

## Verifying installation

At the end of the setup command, you'll see the name of the environment, activate it with:

```sh
conda activate ENVIRONMENT_NAME
```

To verify that your environment has been installed correctly, execute the following:

```sh
python -c 'import PACKAGE_NAME; print(PACKAGE_NAME)'
```

Substitute `PACKAGE_NAME` with the package you are contributing to; to get the package name, open the `src/` directory. For example in [JupySQL's case](https://github.com/ploomber/jupysql/tree/master/src), the package name is `sql`, so to verify the installation, we can execute:

```sh
python -c 'import sql; print(sql)'
```

The command above should print something like this:

```python
<module 'PACKAGE_NAME' from '/path/to/jupysql/src/PACKAGE_NAME/__init__.py'>
```

The printed path should match the location where you cloned the repository. Note that the `setup` command installs the package in "editable mode", which means that any changes to the source code will be reflected whenever you run the tests or use the package in a Python session, or Jupyter notebook (however, you must restart the Python session or Jupyter kernel for the changes to take effect).

A common error happens when your package ends up installed in the conda environment, in such case, the output of previous command will look like this:

```python
<module 'PACKAGE_NAME' from '/path/to/miniconda3/envs/ENV_NAME/lib/python3.10/site-packages/PACKAGE_NAME/__init__.py'>
```

If your installation looks like that, try installing again or send us a message on [Slack.](https://ploomber.io/community)

## Building the documentation

> **Note**
> If you have issues building the documentation, send us a message on [Slack.](https://ploomber.io/community) and we'll help you.

We build the documentation on each Pull Request; however, you might run it locally for faster previews. We've standardized the setup process for the most part but send us a message on [Slack](https://ploomber.io/community) if you have issues.

The steps are the same as in the [Setup](#setup), but you need to ensure you pass the `--doc` argument to the `pkgmt setup` (or `invoke setup`) command. Once you'r ready, ensure you activate the conda environment (printed at the end of the command):

```sh
conda activate ENVIRONMENT_NAME
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

> **Warning**
> If the project you're contributing to has a `tasks.py` file in the root directory (e.g., [Ploomber](https://github.com/ploomber/ploomber)), you must run `invoke doc` to build the docs. If you have issues, send us a message on [Slack.](https://ploomber.io/community). The source code for the `invoke` commands is in `tasks.py` so you might want to check it out as well.


To learn more about writing docs, see [documentation/README.md](documentation/README.md)

## Coding

### Linting/Formatting

Before running the tests on GitHub, we lint the code, notebooks and documentation with `flake8`, if you want to check your code locally:

```sh
pip install pkgmt --upgrade
pkgmt lint
```

> **Note**
> `pkgmt lint` is a wrapper around [`flake8`](https://flake8.pycqa.org/en/latest/) that lints `.py`, `.ipynb` and `.md` files.

If you encounter errors, you need to fix them; otherwise your Pull Request will fail. Most errors can be fixed with automated formatting:

```sh
pip install pkgmt --upgrade
pkgmt format
```

> **Note**
> `pkgmt lint` is a wrapper around [`black`](https://github.com/psf/black) and [`nbQA`](https://github.com/nbQA-dev/nbQA) that formats `.py`, `.ipynb` and `.md` files.


To automatically lint your code before pushing:

```sh
pip install pkgmt --upgrade
pkgmt hook
```

The command above will install a git pre-push hook. To uninstall:

```sh
pkgmt hook --uninstall
```

### Maintaining backwards compatibility

We keep backwards compatibility for one major release, if we've made a major release recently, we might keep it backwards compatibility for two major releases.

A major release is a bump in the middle number in `X.Y.Z`. For example, if we deprecate a function (this means we'll show a warning is somebody uses it), make a release (say, `0.5`), we'll remove the function in version `0.6`.

To deprecate code, use the [module in `ploomber-core`.](https://ploomber-core.readthedocs.io/en/latest/deprecation.html)

### Documenting changes and new features

The documentation must be updated when you make changes to the API (add arguments, add a new class, etc.) (we use the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format).

We keep track of API changes in the the `Notes` section, by using the `.. versionadded` directive for new classes, functions, or methods.

For example, if we added `SomeClass` in version `1.2` and `some_method` in `1.3`:

```python
class SomeClass:
    """
    Notes
    -----
    .. versionadded:: 1.2
    """
    def some_method(self, existing, new):
        """
        Parameters
        ----------
        existing : bool, default=None
            Some description

        new : str, default=None
            Another description (Added in version X.Y.Z)

        Notes
        ----
        .. versionadded:: 1.3
        """
        pass
```

Apart from docstrings, we often write tutorials and examples, for more information, check out our [documentation framework.](documentation/README.md)

#### Which version to put?

If your change is not making breaking API changes, look at the current development version in [CHANGELOG.md](CHANGELOG.md), then drop the `dev` portion.

If the change breaks the API, the version will be handled case by case. However, in most situations, the change will be scheduled for the next major release. For example, if the `dev` version is `0.20.1dev`, the next major release is `0.21`.

### CHANGELOG

Each repository contains a `CHANGELOG` file in the root directory. Each PR should
contain a list of items, so we keep it up-to-date. Note that the `CHANGELOG` targets
end-users (while `git log` targets the Ploomber development team); this implies
that there might be changes that we don't include in the `CHANGELOG`, but they exist
in the `git log`, for example changes to the CI configuration, new tests
added/fixed.

These are changes that we add to the `CHANGELOG` (in this order):

- [API Change] API breaking changes
- [Feature] New features
- [Fix] Bug fixes
- [Doc] Important documentation changes (e.g., new sections, major re-organization)

Each new line in the `CHANGELOG` must be prefixed by its category. Example:

```md
- [Fix] Fixes an error that caused function `do_something` to break when passing `0` as input
```

If there is an issue related to the change, it should be added to the end:

```md
- [Fix] Fixes an error that caused function `do_something` to break when passing `0` as input (#99)
```

Note that we're not adding the link to GitHub, this will happen automatically during the release process.


### Rules of thumb for CHANGELOG messages

Keep in mind this guidelines when writing changelog messages:


- Use full sentences
    - Example: [Fix] Fix an error that caused the function `do_something` to break when passing `0` as an input
- Appropriately identify modules, functions or classes affect with backticks (`) and write the name exactly as it appears on the source code (do not use abbreviations)
    - Example: [Feature] Add `some_module.Report` to generate reports from profiling data

### Telemetry

To measure usage, we add telemetry to our packages. See the [user guide.](https://ploomber-core.readthedocs.io/en/latest/telemetry.html)

### Optional dependencies

If the feature you're implementing requires extra packages, we might consider adding them as optional dependencies. [Check out the guide.](https://ploomber-core.readthedocs.io/en/latest/dependencies.html)

## Testing

* We use [pytest](https://docs.pytest.org/en/7.2.x/) for testing. A basic understanding of `pytest` is highly recommended to get started, especially [fixtures](https://docs.pytest.org/en/7.2.x/fixture.html), [parametrization](https://docs.pytest.org/en/7.2.x/parametrize.html), and [debugging](https://docs.pytest.org/en/7.2.x/how-to/failures.html)
* In most cases, for a given in `src/ploomber/MODULE_NAME`, there is a testing module in `tests/MODULE_NAME`, if you're working on a particular module, you can execute the corresponding testing module for faster development but when submitting a pull request, all tests will run
* If you're checking error messages and they include absolute paths to files, you may encounter some issues when running the Windows CI since the Github Actions VM has some symlinks. If the test calls `Pathlib.resolve()` ([resolves symlinks](https://docs.python.org/3/library/pathlib.html#id5)), call it in the test as well, if it doesn't, use `os.path.abspath()` (does not resolve symlinks).

Before running the unit tests locally, ensure you're in the right conda environment. To list environments:

```sh
conda env list
```

To activate an environment:

```sh
conda activate ENVIRONMENT_NAME
```

In most cases, to run the tests, you must run:

```sh
pytest
```

However, some projects require specific arguments, to know what's the right argument, check out the `.github/workflows` directory, where you'll find the configuration file for running tests (usually named `ci.yml`). There, you'll see how we're running tests. For example in JupySQL's case, we run [this command](https://github.com/ploomber/jupysql/blob/84c299624b97f743bdcef447292988e505f9d3e0/.github/workflows/ci.yaml#L39):

```sh
pytest --durations-min=5 --ignore=src/tests/integration
```

## Pull Requests

We receive contributions via Pull Requests (PRs). [We recommend you check out this guide.](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)


When you have finished the feature development and you are ready for a Code Review (a.k.a Pull Request in Github), make sure you `"squash"` the commits in your development branch before creating a PR.


> [What is `git rebase`](https://www.delftstack.com/tutorial/git/git-rebase/#what-is-git-rebase)

```
$ git rebase -i <-i for interactive>

# "squash" the command history
# for example

pick commit_hash_1 commit_message_1
s    commit_hash_2 commit_message_2
s    commit_hash_3 commit_message_3
s    commit_hash_4 commit_message_4
```
