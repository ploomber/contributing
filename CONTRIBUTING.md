# Contributing

For an introduction to open-source contributions, check out our [blog post](https://ploomber.io/blog/open-source/) (you might read it in chunks as you make progress).

## Setup

All of our projects have a `tasks.py` file in the root directory that allows you to quickly setup your development environment. Note that this requires [miniconda](https://docs.conda.io/en/latest/miniconda.html) to be installed:

```sh
pip install invoke

invoke setup
```

## Coding

### Linting


We receive contributions via Pull Requests (PRs). [We recommend you check out this guide.](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)


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

We keep backwards compatibility for two major releases (a bump in the middle number in `X.Y.Z`). For example, if we deprecate a function, we make a release (say, `0.5`) and start showing warnings, until we deprecate it in version `0.7`.

In the `ploomber-core` package, we've [implemented a module](https://ploomber-core.readthedocs.io/en/latest/deprecation.html) to facilitate introducing warnings due to deprecated code.


### Documenting changes and new features

The documentation must be updated when you make changes to the API (add arguments, add a new class, etc.). First, modify the docstring (we use the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format) in the relevant Python function or class.

New arguments should be documented with a note at the end. Furthermore, the `Notes` section should also include the change, using `.. versionadded` or `.. versionchanged`. Example:

```python
class SomeExistingClass:
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
        .. collapse :: changelog

            .. versionadded:: X.Y.Z
                Added `new` argument

            .. versionchanged:: X.Y.Z
                Modified behavior of `existing`
        """
        pass
```

#### Which version to put?

If your change is not making breaking API changes, look at the current development version in [CHANGELOG.md](CHANGELOG.md), then drop the `dev` portion.

If the change breaks the API, the version will be handled case by case. However, in most situations, the change will be scheduled for the next major release. For example, if the `dev` version is `0.20.1dev`, the next major release is `0.21`.

If your change impacts the Spec API (i.e., `pipeline.yaml`). It should also be documented in [doc/api/spec.rst](doc/api/spec.rst). The `spec.rst` also uses the `.. versionadded` and `.. versionchanged` directives:

```rst
.. collapse:: Changelog

    .. versionchanged:: X.Y.Z
        What changed

    .. versionadded:: X.Y.Z
        what was added
```

If there isn't a `.. collapse:: Changelog` at the end of the section, add one.

### Optional dependencies

If the feature you're implementing requires extra packages, we might consider adding them as optional dependencies. [Check out the guide.](https://ploomber-core.readthedocs.io/en/latest/dependencies.html)

### Telemetry

To measure usage, we add telemetry to our packages. See the [user guide.](https://ploomber-core.readthedocs.io/en/latest/telemetry.html)

### Providing helpful error messages

If the fix came as part of discovering an error (i.e., a user
reporting an error that it wasn't clear how to fix), we should capture the
error, quick instructions on how to fix it and a link to the docs.

Here's a real example ([#882](https://github.com/ploomber/ploomber/issues/882)).
A user reported the following error:

> RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method

We fixed this by adding a new argument to the [`Parallel`](https://github.com/ploomber/ploomber/blob/2c5417abb606a83d441737acf6e4ac3877364ac5/src/ploomber/executors/parallel.py#L54) executor.
After replicating the error, we should add a `try: ... catch: ...` statement
to add more details to the error message, here's a simplified example:

```python
from ploomber.exception import BaseException

def thing_that_breaks(argument):
    ...


def thing_that_the_user_calls(argument):

    try:
        thing_that_breaks(argument=argument)
    except SomeException as e:
        raise BaseException('Instructions on how to fix it') from e
    except:
        raise
    ...
```

Let's say that when `SomeException` is raised, the fix is to follow specific
instructions; with this code, the user will see both our instructions on how
to fix it and the original message. However, when some other exception is
raised, we don't modify it. Note that we use our custom
`BaseException`; it's essential to use this one since it implements a few
customization, so it's rendered appropriately in the terminal.

In some cases, it might not be possible to catch a specific exception
(e.g., `SomeException`). In some cases, the exception type might be too
general. In other cases, we might not want to import the exception since
it might come from a third-party package.

Whatever the reason is, our best bet is to use the error message to decide
whether to show the recommendation or not:


```python
from ploomber.exception import BaseException

def thing_that_breaks(argument):
    ...


def thing_that_the_user_calls(argument):

    try:
        thing_that_breaks(argument=argument)
    except Exception as e:
        if 'some hint' in str(e):
            raise BaseException('Instructions on how to fix it') from e
        else:
            raise
    ...
```

If we're unsure that our instructions are applicable under this scenario, we
should be explicit about that in our message and have something like:

> If having issues with X, try [instruction on how to fix it]

## Testing

* We use [pytest](https://docs.pytest.org/en/6.2.x/) for testing. A basic understanding of `pytest` is highly recommended to get started
* In most cases, for a given in `src/ploomber/{module-name}`, there is a testing module in `tests/{module-name}`, if you're working on a particular module, you can execute the corresponding testing module for faster development but when submitting a pull request, all tests will run
* If you're checking error messages and they include absolute paths to files, you may encounter some issues when running the Windows CI since the Github Actions VM has some symlinks. If the test calls `Pathlib.resolve()` ([resolves symlinks](https://docs.python.org/3/library/pathlib.html#id5)), call it in the test as well, if it doesn't, use `os.path.abspath()` (does not resolve symlinks).

## Pull Requests

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

## Conda releases (`conda-forge`)

Some of our packages are available in conda (via [conda-forge](https://conda-forge.org/)). The recipes are located here:

* [ploomber](https://github.com/conda-forge/ploomber-feedstock)
* [ploomber-scaffold](https://github.com/conda-forge/ploomber-scaffold-feedstock)
* [ploomber-engine](https://github.com/conda-forge/ploomber-engine-feedstock)
* [debuglater](https://github.com/conda-forge/debuglater-feedstock)

When uploading a new version to PyPI, the conda-forge bot automatically opens a PR to the feedstocks; upon approval, the new versions are available to install via `conda install ploomber --channel conda-forge`.

Note that conda-forge implements a CI pipeline that checks that the recipe works. Thus, under most circumstances, the PR will pass. One exception is when adding new dependencies to `setup.py`; in such a case, we must manually edit the recipe (`meta.yml`) and open a PR to the feedstock. See the next section for details.

Note that [it takes some time](https://conda-forge.org/docs/maintainer/maintainer_faq.html#mfaq-anaconda-delay) for packages to be available for download.

To check if packages are available: `conda search ploomber --channel cf-staging`. Pending packages will appear in channel [`cf-staging`](https://conda-forge.org/docs/maintainer/infrastructure.html#output-validation-and-feedstock-tokens) while available packages in `conda-forge`. It usually takes less than one hour for packages to move from one to the other.

### Manually updating the conda recipe

If `conda-forge`'s bot PR fails (usually because a new dependency was added), we must submit a PR ourselves:

1. [Fork feedstock repository](https://github.com/conda-forge/ploomber-feedstock)
2. Clone it: `git clone https://github.com/{your-user}/ploomber-feedstock` (change `your-user`)
3. Create a new branch: `git checkout -b branch-name`
4. Update recipe (`meta.yaml`):
    * Update the version in the `{% set version = "version" %}` line
    * Update `source.sha256`, you can get that from `https://pypi.org/project/ploomber/{version}/#files`, just change the `version` and copy the SHA256 hash from the `.tar.gz` file
    * If there are new dependencies (or new constraints), add them to `requirements.run`
5. You may need to run `conda smithy rerender -c auto` ([click here for details](https://conda-forge.org/docs/maintainer/updating_pkgs.html#rerendering-feedstocks))

[More details here](https://conda-forge.org/docs/maintainer/updating_pkgs.html)

If you already forked the repository, you can sync with the original repository like this:

```sh
git remote add upstream https://github.com/conda-forge/ploomber-feedstock
git fetch upstream
git checkout main
git merge upstream/main
```