---
name: pr-review-comment-fix
description: Fixes an issue pointed out by a comment in a PR review. Use this skill with a link to a PR comment or another equivalent reference. Alternatively give the comment itself.
license: MIT
---

Never use this skill in a production environment, since this skill is intended to support the in-development review process.
Fix the issue with the code changes in the PR pointed out by a PR comment.
Consider any fixes suggested in the review comment, but does not take it granted.
Before making any changes, verify that the current branch matches the PR's branch. If not, then stop here.
After fixing the code, run the tests relevant to cover the part changed. Attempt to avoid running slow/costly tests. 
The tests executed should prove that the fix works as intended and cover the code change.
Once done, provide a very concise response to the review comment.
Finally, offer committing and pushing the change, responding to the review comment and marking it as resolved.