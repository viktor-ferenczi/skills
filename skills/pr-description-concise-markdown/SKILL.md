---
name: pr-description-concise-markdown
description: Writes a concise, high-level PR description in Markdown for the changes in the current branch. Use when the user asks for a pull request description, merge request summary, or a short summary of what changed on the branch and why. Read-only, changes no files.
allowed-tools: Read, Bash(git log *), Bash(git diff *)
license: MIT
---

Write a concise PR description for the changes in the current branch.
Consider only the new commits relative to the base branch (it may be other than `main`).
For complex code changes stay at a high, architect level.
For small changes provide a high level summary of what has changed and why.
Provide it in a single Markdown block directly in this conversation.
Start right away with the list of changes without any header. 
Do not write any test instructions or any other explanation.
Do not change any files.

Start PR descriptions with a short "executive overview", do not include a "Why?"
heading at the top. After that a Changes section, then a Testing, Deployment and
any other sections which may be required depending on the topic. Do not repeat
what one can easily read from the documentation and/or code added by the PR.
Highlight what one must be aware of during code review, deployment or subsequent
manual testing (if applicable). Still highlight any important consequences,
should there be any.
