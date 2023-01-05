# Release process

This document describes our release process for open-source projects.

## Contributors

### New features, changes and deprecations

When adding new features (i.e., functions, or classes), docstrings should properly
indicate in which version the feature first appeared using the `.. versionadded::`
directive.

When changing the API,` .. versionchanged::` should be used. And deprecations should
be indicated with `.. deprecated::`. Read
[ploomber-core docs](https://ploomber-core.readthedocs.io/en/latest/deprecation.html)
for details.


### CHANGELOG

Each repository contains a `CHANGELOG` file in the root directory. Each PR should
contain a list of items so we keep it up-to-date. Note that the `CHANGELOG` targets
end-users (while `git log` targets the Ploomber development team); this implies
that there might changes that we don't include in the `CHANGELOG` but they exist
in the `git log`, for example: changes to the CI configuration, new tests
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


## Releasing

We ship changes rapidly. This means that we do not wait for changes to accumulate before
releasing. A small fix is enough to make a new release. Once a PR is merged, and the
`master`/`main` branch passes. We can tag a new release with the following command:

```sh
invoke version
```

This will ask us to confirm the version number and then, proceed to tag the commit and
push it.

`invoke version` will also run a few checks before creating tagged commit:

- Check there are no pending deprecations (e.g., if we said we'd remove function `do_something` in version `1.0`, such function should not appear in a release tagged as `1.0`)
- Check that `.. versionchanged::` and `.. versionadded::` are correct (they point to either the current release or previous releases)

Note that this process is only valid for minor releases (i.e., releases that do not
break the current API).

## GitHub Action

A GitHub action runs after every push to `master`/`main` that checks if the latest commit
is tagged. If so, it'll push a new version to PyPI once all tests pass.

## Releasing major versions

We avoid unnecessary changes that break the API; however, sometimes we have to do it.
PRs with changes that break the API should be merged to the corresponding development
version. For example, if we're in version `0.10.1dev`, the next major version is
`0.11`. So we should have a branch named `0.11` and merge breaking API PRs there.

The purpose of having a separate branch is that we do not want to keep breaking the
API every now and then, in this case, we group breaking API changes and ship them all
at once. Note that given our deprecation policy of deprecating and keeping
compatibility for two major releases, we give our users enough time to make appropriate
changes.

Once we make a new major release, we merge the branch to `master`/`main` and follow the
release process.