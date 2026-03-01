---
name: consistency-check
description: Checks the internal consistency of a software project, fixes any issues found.
license: MIT
---

1. Check the internal consistency of the code base. If any issues are found, then fix them and go to 1. again.
2. Check the consistency of configuration with the code base. If any issues are found, then fix them and go to 2. again.
3. Run the linters (if there is any defined for the project). If any issues are found, then fix them and go to 3. again.
4. Update the documentation as needed to reflect the current code and configuration.
5. Check the consistency of the code, configuration and documentation together. If any issues are found, then fix them and go to 3. again.

Once you are done:
- Commit the changes to the Git working copy, if any.  
- Provide a concise report of the fixes made, if any.
