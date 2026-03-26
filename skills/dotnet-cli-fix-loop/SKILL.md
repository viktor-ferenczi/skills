---
name: dotnet-cli-fix-loop
description: Iterates on a .NET CLI project buildable with `dotnet build` until it builds and runs without errors.
allowed-tools: Read, Bash(dotnet build *), Bash(dotnet run *)
license: MIT
---

Iterate on the specified .NET project until it builds and runs successfully. If no project is specified, ask which project to work on in the current solution.

## Safety

- **CRITICAL**: REFUSE to use this skill if operating in a production environment.
- **CRITICAL**: NEVER delete or disable any pre-existing tests.
- Keep working in the current branch, do not switch between branches.

## Steps

1. Build the project using `dotnet build`.
2. If the build fails, fix the **first** issue in the code. If the project is in a Git repository, commit the fix into the current branch. Then go to step 1.
3. Run the project using `dotnet run`.
4. If there is no error, then stop and provide a concise report of all fixes made.
5. Fix the **first** problem reported. If the project is in a Git repository, commit the fix into the current branch. Then go to step 1.

## Remarks

- Skip all Git commits if there is no Git repository in the same folder as the solution or project.
- Focus on fixing one issue at a time to keep changes minimal and reviewable.
- Use descriptive commit messages that explain what was fixed.
- Do not introduce unnecessary changes beyond what is needed to fix each issue.
