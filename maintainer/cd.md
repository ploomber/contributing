# Continuous deployment

> **Warning**
> This is work in progresa and hasn't been deployed yet.

We use an automated process to tag and deploy new versions to PyPI using GitHub Actions and `pkgmt`. This process is triggered on the master branch
using the special keyword `[release]` (must be at the beginning of the commit message), after a successfull CI.

We can choose any of these options to release a new version:

- Add a commit message `[release]` to the PR
- Add an empty commit message `[release]` to the master branch

## Reviewing Pull Requests


Once the Pull Request is reviewed and approved, the owner determines
what happens next. Most often, the following action would be to deploy a new minor version
to PyPI, so once the PR is merged and the CI passes in `master`/`main`, a new minor version will be uploaded to PyPI.

Another action can be "no release", implying that the PR is merged, but no release
happens. Typical scenarios for this would be PRs that only change the documentation,
refactoring that doesn't have any end-user impact, or we might decide to wait a bit to
have a few more PRs for a new release.

The final action can be a "major release." A major release implies breaking API changes,
so we should carefully plan with deprecation warnings to give our users
a heads-up. In this case, once the PR is merged, a new major release is created (via `git tag`), and pushed to PyPI.

The owner will indicate what action to take by adding one *command* when merging
the PR.

- `[minor]` - Release a new minor version
- `[major]` - Release a new major version

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

