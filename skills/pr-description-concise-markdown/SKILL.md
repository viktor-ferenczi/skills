---
name: pr-description-concise-markdown
description: Writes a concise, high-level PR description in Markdown for the changes in the current branch. Use when the user asks for a pull request description, merge request summary, or a short summary of what changed on the branch and why. Read-only, changes no files.
allowed-tools: Read, Bash(git log *), Bash(git diff *)
license: MIT
---

Write a concise PR description for the changes in the current branch.
For complex code changes stay at a high, architect level.
For small changes provide a high level summary of what has changed and why.
Provide it in a single Markdown block directly in this conversation.
Start right away with the list of changes without any header. 
Do not write any test instructions or any other explanation.
Do not change any files.