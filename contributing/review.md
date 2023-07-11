# Reviewing PRs

## The first review should be thorough

The first review should be the most detailed one, so upcoming reviews
become smaller and take less time. The only exception is when there's something
obviously broken (e.g., you ran some tests and the feature doesn't work as described in
the acceptance criteria). In such case, you can comment what the problem is and tell
the contributor to re-request your review once the problem is addressed.

## Avoid adding new requirements to existing PRs

The code should be evaluated based on the acceptance criteria and new items should
not be added. However, if you test the PR and encounter that the implementation isn't
complete, it's fine to bring it up. The most common scenario is when the new feature
doesn't handle error correctly (e.g., unclear error messages), in such cases, you can
ask the contributor to tackle it.

## Share concise but direct feedback

Strike a good balance between a short yet understandable message and detailed feedback.
Written communication is hard, so minimize the number of words while maximizing the
amount of information shared.

Avoid using *it* or *this* in your comments, as it leads to ambiguity. Example:

**Bad:** I noticed that it doesn't work if you pass `verbose=True`

**Good**: I noticed that the function `perform_operation` doesn't work if you pass `verbose=True`

## You're responsible for resolving conversations

The reviewer is responsible for clicking on `Resolve conversation`. Contributors should address observations but it's up to the reviewer to mark them as resolved (as they're the ones that verify that their observations were effectively addressed).

![](../assets/resolve-conversation.png)

Once you've addressed all the comments, request another review.

## It's ok to dismiss incomplete PRs

If you receive a request for review but the PR is incomplete (e.g., the CI isn't passing) or there are obvious misses in the acceptance criteria, you can skip your review and check again the next day. It's the contributors responsibility to ensure their PRs are ready to review.