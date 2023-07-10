# Process outline

This guide provides an overview of what the contribution process is like.

1. Get an issue assigned
2. Describe what's the acceptance criteria (what I'm going to work on, what's the definition of done)
3. Submit a PR
4. Review Process
5. Demo

Let's dive into each of these sections.

## 1. Getting issue assigned

The project's maintainers may assign you an issue, or  you can choose one that you're
interested in working on.

## 2. Describe the Acceptance Criteria

- Before starting to work on the issue, describe the acceptance criteria (AC). 
- The AC stage should be resolve in **24 hours** from issue assignment.
- Describing the criteria includes what you're going to work on,
  and what the definition of done looks like (I'm going to add a function to  
  class X, I'm going to test it, document how to use it etc.). 
  This helps to ensure that everyone is on the same page and that the work meets 
  the project's standards. 
- **There are a few mandatory things that has to happen in 
  any of the PRs:**
  1. Changelog entry 
  2. Code
  3. Tests (unit, integration, CI/CD integration etc.)
  4. Documentation
  5. Telemetry
  6. Release post/Demo (except for small doc changes/fixes). 
- Once the scope is agreed, you can start working on the pull request. 
- Unless otherwise noticed, the person who opened the issue should give the thumbs up for the acceptance criteria (the only exception is when someone outside of our team opened an issue in an open-source project, in such case, someone from the team should approve the acceptance criteria)
- Once the criteria is set, update the pull request text to have that criteria as a check-list
  both you and the reviewer can reference.

## 3. Submit a Draft Pull Request

```{note}
For more information, see [](submitting-pr.md).
```

- Once you've completed the work, submit a draft pull request to the repository. 
- The pull request will include the changes you've made and any relevant 
  information or comments you want to share with your reviewer.

## 4. Review Process

```{note}
For more information, see [](responding-pr-review.md).
```

- Your pull request will be reviewed by the maintainers. They will provide feedback on your work, including any suggested changes or improvements. 
- Address their feedback and make any necessary changes to your work. 
- This step shouldn't take more than **1-2 days**, and you should 
focus on closing existing issues (your active PR) instead of taking new issues. 
- Finally, once the PR is approved, your changes will be merged into the main branch and the reviewer
will delete the branch.

## 5. Demo (Optional)

- Once your pull request has been approved and merged, demonstrate your work to the team. 
  This helps to ensure that everyone is aware of the changes made and that they meet 
  the project's standards. It also helps us spread the word on what we're currently
  working on. 
- You can also talk about challenges you had as part of the issue.



