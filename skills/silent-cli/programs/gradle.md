# gradle

**Platforms:** Multi-platform  
**Category:** Java Build Tool

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet build | `gradle -q build` |
| Plain console (no colors/progress) | `gradle --console=plain build` |
| CI mode (no daemon, plain) | `gradle --console=plain --no-daemon build` |

## Command-Line Flags

- `-q` or `--quiet`: Quiet mode (suppress most output, show only errors)
- `--console`: Console output type — `plain` disables colors and progress bar (use for CI/scripts), `auto` detects TTY
- `--no-daemon`: Don't use the Gradle daemon (avoids background processes in CI)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Plain console for CI, no daemon
gradle --console=plain --no-daemon build -x test
```
