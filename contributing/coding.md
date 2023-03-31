
# Coding

## Linting/Formatting

Before running the tests on GitHub, we lint the code, notebooks and documentation with `flake8`, if you want to check your code locally:

```sh
pip install pkgmt --upgrade
pkgmt lint
```

```{note}
`pkgmt lint` is a wrapper around [`flake8`](https://flake8.pycqa.org/en/latest/) that lints `.py`, `.ipynb` and `.md` files.
```

If you encounter errors, you need to fix them; otherwise your Pull Request will fail. Most errors can be fixed with automated formatting:

```sh
pip install pkgmt --upgrade
pkgmt format
```

```{note}
`pkgmt format` is a wrapper around [`black`](https://github.com/psf/black) and [`nbQA`](https://github.com/nbQA-dev/nbQA) that formats `.py`, `.ipynb` and `.md` files.
```


To automatically lint your code before pushing:

```sh
pip install pkgmt --upgrade
pkgmt hook
```

The command above will install a git pre-push hook. To uninstall:

```sh
pkgmt hook --uninstall
```

## Maintaining backwards compatibility

When breaking the API, we give heads up nnotice to our users so they have enough time to update their code. This involves showing warnings letting them know that a certain feature will be deprecated.

We currently do not have a strict policy so we review cases on a case-by-case basis, but a good rule of thumb is to give at least a month's notice. This implies that Code Owners should ensure that the contributor opens a new PR with deprecation warnings, we merge the PR, and make a new release (by notifying Eduardo or Ido). This process should be prioritized so we make a release as soon as we decide that we'll break the API.

To deprecate code, use the [module in `ploomber-core`.](https://ploomber-core.readthedocs.io/en/latest/deprecation.html)

> **Note**
> ploomber-core must be used for deprecations in most cases. The only exception are some JupySQL modules where we manually show exceptions using the `warnings` module since the API is a [Jupyter magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html), which is currently not compatible with ploomber-core.


When the API is changed, we must bump to a major version release. A major release is a bump in the middle number in `X.Y.Z`. For example, if our current development version is `0.1.3dev`, the first step is to add the deprecation warnings and make the  `0.1.3` release, then, in the PR that breaks the API, we should ensure that the development version is set to `0.2.0dev` in the `CHANGELOG` and `__init__.py` file.

## Documenting changes and new features

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

Apart from docstrings, we often write tutorials and examples, for more information, check out our [documentation framework.](../maintainer/doc-guide.md)

### Which version to put?

If your change is not making breaking API changes, look at the current development version in the `CHANGELOG.md` file, then drop the `dev` portion.

If the change breaks the API, the version will be handled case by case. However, in most situations, the change will be scheduled for the next major release. For example, if the `dev` version is `0.20.1dev`, the next major release is `0.21`.

## CHANGELOG


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

```{tip}
We want to recognize your work: If you wish, you can add your GitHub handle next to your changelog entry! Example:

~~~md
- [Feature] Add a very important feature (by @edublancas)
~~~
```

## Rules of thumb for CHANGELOG messages

Keep in mind this guidelines when writing changelog messages:


- Use full sentences
    - Example: [Fix] Fix an error that caused the function `do_something` to break when passing `0` as an input
- Appropriately identify modules, functions or classes affect with backticks (`) and write the name exactly as it appears on the source code (do not use abbreviations)
    - Example: [Feature] Add `some_module.Report` to generate reports from profiling data

## Telemetry

To measure usage, we add telemetry to our packages. See the [user guide.](https://ploomber-core.readthedocs.io/en/latest/telemetry.html)

## Optional dependencies

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
conda activate ENV_NAME
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