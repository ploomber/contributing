# Contributing

This is a general guide applicable to all our projects. However, there might be particular details on some repositories so check out the `CONTRIBUTING.md` for the project you're working on as well.

For an introduction to open-source contributions, check out our [blog post](https://ploomber.io/blog/open-source/).

## Setup

All of our projects have a `tasks.py` file in the root directory that allows you to quickly setup your development environment. Note that this requires [miniconda](https://docs.conda.io/en/latest/miniconda.html) to be installed:

```sh
pip install invoke

invoke setup
```

## Coding

### Linting


We use [black](https://github.com/psf/black) for formatting code. *Please run black before submitting*. To apply black formatting:

```sh
black .
```

We use [flake8](https://flake8.pycqa.org/en/latest/) for linting. *Please check your code with flake8 before submitting*:

```sh
# run this in the project directory to check code with flake8
flake8
```
*Note:* If you created a virtual env in a child directory, exclude it from `flake8` using the `--exclude` argument (e.g., `flake8 --exclude my-venv`).

If you don't see any output after running `flake8`, you're good to go!


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

### Telemetry

To measure usage, we add telemetry to our packages. See the [user guide.](https://ploomber-core.readthedocs.io/en/latest/telemetry.html)

### Optional dependencies

If the feature you're implementing requires extra packages, we might consider adding them as optional dependencies. [Check out the guide.](https://ploomber-core.readthedocs.io/en/latest/dependencies.html)

## Testing

* We use [pytest](https://docs.pytest.org/en/6.2.x/) for testing. A basic understanding of `pytest` is highly recommended to get started
* In most cases, for a given in `src/ploomber/{module-name}`, there is a testing module in `tests/{module-name}`, if you're working on a particular module, you can execute the corresponding testing module for faster development but when submitting a pull request, all tests will run
* If you're checking error messages and they include absolute paths to files, you may encounter some issues when running the Windows CI since the Github Actions VM has some symlinks. If the test calls `Pathlib.resolve()` ([resolves symlinks](https://docs.python.org/3/library/pathlib.html#id5)), call it in the test as well, if it doesn't, use `os.path.abspath()` (does not resolve symlinks).

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
