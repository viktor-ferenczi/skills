---
name: consistency-check
description: Checks the internal consistency of a software project, fixes any issues found.
license: MIT
---

1. Check the internal consistency of the codebase. If any issues are found, fix them and return to step 1.
2. Check the consistency of the configuration with the codebase. If any issues are found, fix them and return to step 2.
3. Run the linters (if any are defined for the project). If any issues are found, fix them and return to step 3.
4. Update the documentation as needed to reflect the current code and configuration.
5. Check the consistency of the code, configuration, and documentation together. If any issues are found, fix them and return to step 3.

Once done:
- Commit the changes to the Git working copy, if any.
- Provide a concise report of the fixes made, if any.