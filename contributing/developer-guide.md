# Development process

This guide should give you an overview of what the process looks like, the different steps etc.

The flow in general:
1. Get an issue assigned.
2. Describe what's the acceptance criteria (what I'm going to work on, what's the definition of done)
3. Submit a PR.
4. Review Process
5. Demo

Let's dive into each of these sections:
Getting issue assigned: Start by identifying the issue that you're going to work 
on from the project's issue tracker/or the one you got assigned. 
The project's maintainers may assign you an issue or 
you can choose one that you're interested in working on.

Describe the Acceptance Criteria: Before starting to work on the issue, 
describe the acceptance criteria. **This stage should be resolve in 24 hours since issue assignment**.
This includes what you're going to work on and what the definition of done looks 
like (I'm going to add a function to class X, 
I'm going to test it, document how to use it etc.). 
This helps to ensure that everyone is on the same page and that the work meets 
the project's standards. There are a few mandatory things that has to happen in 
any of the PRs: **Changelog entry, code, tests (unit, integration, 
CICD integration etc.), documentation, Telemetry, release post/Demo
(except for small doc changes/fixes)**. Once the scope
is agreed, you can start working on the pull request. Each issue/PR should have 
a main reviewer, if you didn't see anyone aligned, please ask in the issue and tag us.
Once the criteria is set, update the pull request text to have this criteria as a check-list
both you and the reviewer can reference.

Submit a Pull Request: Once you've completed the work, submit a pull request to 
the repository. The pull request includes the changes you've made and any relevant 
information or comments you want to share with your reviewer.

Review Process: Your pull request will be reviewed by the dedicated maintainer
or other team members. They will provide feedback on your work, including any 
suggested changes or improvements. Address their feedback and make any necessary 
changes to your work. This step shouldn't take more than 2-4 days, and you should 
focus on closing existing issues (your active PR) than taking new issues. 
Finally, once that's done, your changes will be merged into the main branch and the reviewer
will delete the branch.

Demo: Once your pull request has been approved and merged, demonstrate your work to the team. 
This helps to ensure that everyone is aware of the changes made and that they meet 
the project's standards. It also helps us spread the word on what we're currently
working on. You can also talk about challenges you had as part of the issue.



