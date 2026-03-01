---
name: stabilization-loop
description: Environment variables and parameters for running command line programs reliably in non-interactive environments (unattended). Includes silent modes, color/disable TTY, and reduced output options for 155 CLI tools.
license: MIT
---

Stabilize the project:
1. If there are any local changes, then commit the current code into the local Git repository with commit message "Claude".
2. Make sure that the code compiles and the linter checks pass. If not, then fix those and go to step 1. 
3. Run the server, wait until it starts.
4. Run the tests.
5. If the tests succeed and the server hasn't crashed or logged any errors, then STOP.
6. If the test fails, then analyze the test errors, try to fix them and go to step 1.
7. If the server crashes or logged an error, then analyze the crashes or errors, try to fix them and go to step 1.

Once you are done:
- Stop the server.
- Tag the latest commit message in the local Git repository as "works".  
- Provide a concise report of the problems found and fixed.

Remarks:
- Keep working in the current branch, do not switch between branches.
- Add logging as needed, but at them at the debug level, so they can be turned off later.
- If you add expensive logging, then protect it with the condition on debug log level. 
