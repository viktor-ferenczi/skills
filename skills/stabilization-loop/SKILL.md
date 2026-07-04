---
name: stabilization-loop
description: Iterates on a locally runnable project (typically a server with a test suite) until it builds, runs, and passes all tests cleanly, fixing failures between runs. Use when tests or the running application are failing or flaky after changes and the user wants to loop until green. Requires a local development setup — never run against production.
license: MIT
---

Stabilize the project:
1. If there are any local changes, then commit the current code to the current branch with commit message "Stabilization".
2. Make sure that the code compiles and the project's own linter checks pass (discover them from config files, `package.json`/`Makefile` targets, or CI workflows — do not introduce new tools). If not, then fix those and go to step 1.
3. Stop the server if it is running.
4. Start the server, wait until it is completely up and ready.
5. Run the tests. Capture the full test output and the server log for this iteration.
6. If any test fails, or the server crashes or logs an error:
   - Analyze the captured output and identify the root cause — do not just silence the symptom.
   - Check the failure log (see Remarks) first: if the same failure occurred in an earlier iteration, your previous fix did not work — revert it and try a different approach instead of repeating it.
   - Fix the root cause, record the failure and the fix in the failure log, and go to step 1.
7. Stop the server.
8. Commit any remaining changes into the current branch with commit message "Stabilization".
9. Tag the latest commit as "works" (move the tag if it already exists). Tag only now, when everything passes.
10. Provide a concise report: iterations run, failures encountered, fixes applied, anything left open.

Remarks:
- **CRITICAL**: NEVER run more than one instance of the server at the same time.
- **CRITICAL**: NEVER run more than one instance of the tests at the same time.
- **CRITICAL**: REFUSE to use this skill if the code is configured to connect to a production database or system.
- **CRITICAL**: NEVER delete or disable any pre-existing tests.
- Keep a failure log (a scratch file) across iterations: one line per failure with the fix attempted. This prevents cycling on the same failure.
- If the same failure persists after 3 distinct fix attempts, stop and ask the user for guidance instead of looping further.
- This skill is supposed to be used in the Git working copy of the software set up for local development and testing.
- This skill is optimized for running a server and testing it, but the server may be substituted with any other software.
- Keep working in the current branch, do not switch between branches.
- Add logging as needed, but at the debug level, so it can be turned off later.
- If you add expensive logging, then protect it with a debug-level condition.
- Stop only when all tests succeed with no server errors or crashes.
- Cover any newly added server code with tests.
