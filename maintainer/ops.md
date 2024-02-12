# Operations

This document explains the processes to keep our shipping process up and running.

## Versioning

```{important}
Only repository administrators can execute this process.
```

To create a new release version:

```sh
pkgmt version
```

This will ask us to confirm the version number and then proceed to tag the commit and push it.

`pkgmt version` will also run a few checks before creating a tagged commit:

- Check there are no pending deprecations (e.g., if we said we'd remove function `do_something` in version `1.0`, such function should not appear in a release tagged as `1.0`)
- Check that `.. versionchanged::` and `.. versionadded::` are correct (they point to either the current release or previous releases)
- If making a new minor release, check that there are no `[API Change]` changes in the CHANGELOG


## Releasing

```{important}
Only repository administrators can execute this process.
```

```{note}
In some projects, we've automated the release process, to learn more, see [Continuous Delivery](#continuous-delivery).
```

To upload a package to PyPI, execute:

```sh
pkgmt release VERSION
```

Where `VERSION` is the version to release. By default, this command uploads to PyPI's test server, to upload to the production server:

```sh
pkgmt release VERSION --production
```

## Continuous Delivery

```{important}
Ensure you're running the latest `pkgmt` version before proceeding: `pip install pkgmt -U`

Only repository administrators can execute this process.
```

We've auomated uploading to PyPI in some projects (`pkgmt`, `ploomber-core`, `jupysql`, and `ploomber-engine`).

To make a new release, move to the `master` (or `main`) branch in a local copy of the git repository and execute:

```sh
pkgmt version
```

The command will ask for confirmation. Once confirmed, it'll push a new commit and a git tag; then, if all tests pass, the version will be uploaded to PyPI.

You can see a sample GitHub Actions workflow [here](https://github.com/ploomber/contributing/blob/main/sample-github-workflows/ci.yml).


## GitHub Actions workflows

We have a few workflows to automate tasks, you can find the templates in the in the `sample-github-workflows/` directory in this repository.

- `chatops.yml`: triggers certain actions when posting specific comments in a PR
- `changelog.yml`: comments on a PR if the `CHANGELOG.md` file hasn't been updated

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
    * Update `source.sha256`, you can get that from `https://pypi.org/project/{package-name}/{version}/#files`, just change the `{package-name}`,`{version}`, and copy the SHA256 hash from the `.tar.gz` file
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

## Repository quality checklist

This is a checklist of things we need to routinely verify:

- Unit tests in the CI should run with the `pytest` command (no arguments), if arguments are needed you can [add them to the `pyproject.toml`file](https://docs.pytest.org/en/7.1.x/reference/customize.html) (The exception are repositories where we have unit and integration tests separated, for example, in JupySQL's case, where we have different configurations)
- Broken links should be checked using `pkgmt check-links`
- Unit testing from Python 3.8 until 3.11 on Linux, macOS, and Windows
- Lint with `pkgmt lint` (this runs `black` and `nbqa`)
- There must be a [Pull Request template](https://github.com/ploomber/jupysql/blob/master/.github/pull_request_template.md)
- Read the docs must be configured to build docs on each Pull Request
- `pkgmt setup` must install development dependencies (alternatively, there must be a `tasks.py` file with a `setup` command)
- `pkgmt doc`  must build docs (alternatively, there must be a `tasks.py` file with a `setup` command)
- Ensure we have [tag protections](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/configuring-tag-protection-rules) for *all tags*

If anything is missing, open a GitHub issue in the corresponding repository.

## Maintained projects

- [JupySQL](https://github.com/ploomber/jupysql)
- [Ploomber](https://github.com/ploomber/ploomber)
- [ploomber-engine](https://github.com/ploomber/ploomber-engine)
- [Soopervisor](https://github.com/ploomber/soopervisor)
- [sklearn-evaluation](https://github.com/ploomber/sklearn-evaluation)
- [pkgmt](https://github.com/ploomber/pkgmt)
- [Jupyblog](https://github.com/ploomber/jupyblog)
- [ploomber-core](https://github.com/ploomber/core)
- [debuglater](https://github.com/ploomber/debuglater)