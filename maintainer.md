# Maintainer guide


## Continuous integration

We use GitHub Actions to test our projects. Each one should test against these configuration:

- OS: macOS, Linux, and Windows
- Python version: 3.7, 3.8, 3.9, 3.10
- [Documentation preview](https://github.com/readthedocs/actions/tree/v1/preview)
- General checks (via `pkgmt check`)
- Multiprocessing the tests via [pytest-xdist](https://github.com/pytest-dev/pytest-xdist)

## Continuous deployment

We use an automated process to tag and deploy new versions to PyPI using GitHub Actions and `pkgmt`. This process is triggered on the master branch
using the special keyword `[release]` (must be at the beginning of the commit message), after a successfull CI.

We can choose any of these options to release a new version:

- Add a commit message `[release]` to the PR
- Add an empty commit message `[release]` to the master branch

## Reviewing Pull Requests

Once the Pull Request is reviewed and approved, the reviewer determines
what happens next. Most often, the following action would be to deploy a new minor version
to PyPI, so once the PR is merged and the CI passes in `master`/`main`, a new minor version will be uploaded to PyPI.

Another action can be "no release", implying that the PR is merged, but no release
happens. Typical scenarios for this would be PRs that only change the documentation,
refactoring that doesn't have any end-user impact, or we might decide to wait a bit to
have a few more PRs for a new release.

The final action can be a "major release." A major release implies breaking API changes,
so we should carefully plan with deprecation warnings to give our users
a heads-up. In this case, once the PR is merged, a new major release is created (via `git tag`), and pushed to PyPI.

The reviewer will indicate what action to take by adding one *command* when merging
the PR.

- `[minor]` - Release a new minor version
- `[major]` - Release a new major version

## Releasing

*Note: this describes the steps to upload to PyPI. However, they will be automated in a GitHub Action*

We ship changes rapidly. This means that we do not wait for changes to accumulate before
releasing. A minor fix is enough to make a new release. Once a PR is merged, the
`master`/`main` branch passes. We can tag a new release with the following command:

```sh
invoke version
```

This will ask us to confirm the version number and then proceed to tag the commit and
push it.

`invoke version` will also run a few checks before creating a tagged commit:

- Check there are no pending deprecations (e.g., if we said we'd remove function `do_something` in version `1.0`, such function should not appear in a release tagged as `1.0`)
- Check that `.. versionchanged::` and `.. versionadded::` are correct (they point to either the current release or previous releases)
- If making a new minor release, check that there are no `[API Change]` changes in the CHANGELOG

## Planning for a major version release

We avoid unnecessary changes that break the API; however, sometimes, we have to do it.
PRs with changes that break the API should be merged into the corresponding development
version. For example, if we're in version `0.10.1dev`, the next major version is
`0.11`. So we should have a branch named `0.11` and merge breaking API PRs there.

The purpose of having a separate branch is that we do not want to keep breaking the  API. In this case, we group breaking API changes and ship them all at once. Furthermore, it allows us to release hotfixes from `master`/`main`, at any
time.

Note that given our deprecation policy of deprecating and keeping
compatibility for two major releases, we give our users enough time to make appropriate
changes.

Once we make a new major release, we merge the branch to `master`/`main` and follow the
release process.

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

## Sync GitHub labels

To sync labels across repositories, we use [this tool](https://github.com/Financial-Times/github-label-sync).

```sh
# setup
conda create --name label-sync nodejs
conda activate label-sync
npm install -g github-label-sync


# pass the github token
export GH_TOKEN=XXX

# pass the repository
export REPO=ploomber/ploomber-engine

# sync labels: pass --dry-run to do a test, remove the flag once you're sure
github-label-sync --access-token $GH_TOKEN \
    $REPO  --labels labels.yaml --dry-run
```

## Checklist

This is a checklist of thiings we need to routinely verify:

- Unit tests in the CI should run with the `pytest` command (no arguments), if arguments are needed you can [add them to the `pyproject.toml`file](https://docs.pytest.org/en/7.1.x/reference/customize.html) (The exception are repositories where we have unit and integration tests separated, for example, in JupySQL's case, where we have different configurations)
- Broken links should be checked using `pkgmt check-links`
- Unit testing from Python 3.8 until 3.11 on Linux, macOS, and Windows
- Lint with `pkgmt lint` (this runs `black` and `nbqa`)
- There must be a [Pull Request template](https://github.com/ploomber/jupysql/blob/master/.github/pull_request_template.md)
- Read the docs must be configured to build docs on each Pull Request
- `pkgmt setup` must install development dependencies (alternatively, there must be a `tasks.py` file with a `setup` command)
- `pkgmt doc`  must build docs (alternatively, there must be a `tasks.py` file with a `setup` command)

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