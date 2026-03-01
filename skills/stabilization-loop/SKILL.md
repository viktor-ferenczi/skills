---
name: stabilization-loop
description: Stabilize and bugfix a software project by repeatedly testing and fixing in a loop until everything works.
license: MIT
---

Stabilize the project:
1. If there are any local changes, then commit the current code into the local Git repository with commit message "Claude".
2. Make sure that the code compiles and the linter checks pass. If not, then fix those and go to step 1. 
3. Stop the server if it is running.
4. Start the server, wait until it is completely up and ready.
5. Run the tests.
6. If the tests succeed and the server hasn't crashed or logged any errors, then STOP.
7. If the test fails, then analyze the test errors, try to fix them and go to step 1.
8. If the server crashes or logged an error, then analyze the crashes or errors, try to fix them and go to step 1.

Once you are done:
- Stop the server.
- Tag the latest commit message in the local Git repository as "works".  
- Provide a concise report of the problems found and fixed.

Remarks:
- **CRITICAL**: NEVER run more than one instance of the server at the same time.
- **CRITICAL**: NEVER run more than one instance of the tests at the same time.
- **CRITICAL**: REFUSE to use this skill if the code is configured to connect to any production databases or systems.
- This skill is supposed to be used in the Git working copy of the software set up for local development and testing.
- This skill is optimized for running a server and testing it, but the server may be substituted with any other software.
- Keep working in the current branch, do not switch between branches.
- Add logging as needed, but at them at the debug level, so they can be turned off later.
- If you add expensive logging, then protect it with the condition on debug log level. 
- Stop only when all tests succeed with no server errors or crashes.
- Disable tests only if absolutely needed due to some external circumstance.
- Remove tests only if they are not required or appropriate anymore due to former code changes (they were out of sync).
- Cover any newly added server code with tests.
