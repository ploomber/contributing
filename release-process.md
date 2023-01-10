# Release process

This document describes our release process for open-source projects.

## Contributors

### New features, changes, and deprecations

When adding new features (i.e., functions or classes), docstrings should properly
indicate in which version the feature first appeared using the `.. versionadded::`
directive.

When changing the API,` .. versionchanged::` should be used. And deprecations should
be indicated with `.. deprecated::`. Read
[ploomber-core docs](https://ploomber-core.readthedocs.io/en/latest/deprecation.html)
for details.


### CHANGELOG

Each repository contains a `CHANGELOG` file in the root directory. Each PR should
contain a list of items, so we keep it up-to-date. Note that the `CHANGELOG` targets
end-users (while `git log` targets the Ploomber development team); this implies
that there might be changes that we don't include in the `CHANGELOG`, but they exist
in the `git log`, for example changes to the CI configuration, new tests
added/fixed.

These are changes that we add to the `CHANGELOG`:

- [Doc] Important documentation changes
- [Feature] New features
- [API Change] API breaking changes
- [Fix] Bug fixes

Each new line in the `CHANGELOG` must be prefixed by its category. Example:

```md
- [Fix] Fixes an error that caused function `do_something` to break when passing `0` as input
```

If there is an issue related to the change, it should be added to the end:

```md
- [Fix] Fixes an error that caused function `do_something` to break when passing `0` as input (#99)
```

Note that we're not adding the link to GitHub, this will happen automatically during the release process.

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