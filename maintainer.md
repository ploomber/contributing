# Maintainer's guide

This guide documents the process for code maintainers.

## Roles

- **Reviewer:** Performs code reviews for Pull Requests; their objective is to ensure code quality
- **Owner:** Reviews code, ensures that Pull Requests do not get stalled, clicks the **squash and merge** button, and is responsible for ensuring the that we ship functional, high-quality code

### Which one am I?

- You're a reviewer if someone from the team has requested your review on GitHub
- You're an owner if the `Owner: YourName` label has been applied to the GitHub issue or Pull Request

> **Note**
> A contributor cannot be the owner of their Pull Request

## Reviewer/Owner checklist

When performing a code review, verify the following:

- Unit tests have been added and they're rigorously testing the code changes
- An appropriate [CHANGELOG](CONTRIBUTING.md#changelog) entry has been added (when needed)
- The code meets the quality bar
    - Re-usable (e.g., abstracts common patterns in functions)
    - Clear (i.e., descriptive variable names, inline comments when needed) - this also applies to unit tests
- New features are documented: either a [docstring example](https://sklearn-evaluation.ploomber.io/en/latest/api/plot.html#confusionmatrix) (for minor features) or a full [tutorial](https://jupysql.ploomber.io/en/latest/integrations/duckdb.html) (major features) and the documentation is clear an concise

Owners also have the following responsibilities:

- If breaking API changes are introduced, a PR is merged with a [deprecation warning](CONTRIBUTING.md#maintaining-backwards-compatibility)
- If breaking API changes are introduced: a [major version bump](CONTRIBUTING.md#maintaining-backwards-compatibility) is performed
- Ensure that all CI checks passed before merging a Pull Request
- [Only applicable for PRs from external contributors] Approve CI executions (when an external contributor opens a PR, someone from the team needs to approve the CI run by clicking on a button)
- If the CI fails, provide guidance to the contributor. If you suspect the CI is broken due an external factor (e.g., a dependency that its API), send a message on Slack
- If the Pull Request does not meet the quality bar, address it with concrete action items to the contributor
- Run [quality assurance](#quality-assurance) and use your best judgment to determine if this is ready to be merged to the main branch

## Quality assurance

The easiest way to test code contributions is via Binder (a hosted JupyterLab). When
reviewing a pull request, click on the [documentation link](documentation/README.md#previewing-docs).

If the Pull Request is introducing a new feature that includes an interactive
tutorial, navigate to it. If not, stay in the home page.

Launch Binder by clicking on the 🚀 button at the top, then click on "Binder":

![binder button](documentation/assets/binder-button.png)

Once it loads, you'll be able to test the code from the Pull Request.


**Note:** If Binder is misconfigured (i.e., does not load or the code does not match the Pull Request), let us know. Also, always verify the link you're clicking to ensure there isn't any misconfiguration, the format is as follows:

For Pull Requests opened from branches in the original repository

```
https://binder.ploomber.io/v2/gh/ploomber/NAME/BRANCH?urlpath=path/to/notebook
```

Pull Requests opened from forks:

```
https://binder.ploomber.io/v2/gh/USER/NAME/BRANCH?urlpath=path/to/notebook
```

When testing the code: put yourself in the user's shoes (who has never executed this code) and ask yourself if it's clear what the new code is doing and how it can benefit them. These are some questions to ask yourself:

- Is this feature easy to discover? (e.g., via documentation)
- Is the documentation clear for me to understand why should I care?
- Is it easy to get started?
- When things break under simple scenarios, is it easy to know how to fix it/ask for help? (we encourage you to break the code!)
- Is the API consistent? Verify if there might be potential issues with existing features or if the new code itself is inconsistent (e.g., there are no naming conventions, confusing parameter names) 

> **Note**
> If you consider that there are missing parts in the PR, 
> use your best jugment to determine if those missing pieces are critical (e.g., unclear
> documentation, inconsistent API) or not (e.g., documentation could be a bit clearer,
> some extra examples needed). In the former case, we should not merge the PR, but in
> the latter case we should merge it and you can open a new issue to discuss further
> improvements.

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

