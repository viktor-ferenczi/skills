# gradle

**Platforms:** Multi-platform  
**Category:** Java Build Tool

## Quick Reference

| Goal | Command |
|------|---------|
| Build | `gradle build` |
| Quiet | `gradle -q build` |
| Silent | `gradle --console=plain build` |
| No daemon | `gradle --no-daemon build` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `GRADLE_OPTS` | `-Xmx512m` | JVM options |

## Command-Line Flags

```bash
gradle build                         # Build
gradle -q build                      # Quiet
gradle --quiet build                 # Quiet
gradle --console=plain build         # Plain console (no colors/progress)
gradle --console=rich build          # Rich console
gradle --console=verbose build       # Verbose console
gradle --no-daemon build             # No daemon
gradle --daemon                      # Use daemon
gradle --stop                        # Stop daemon
gradle --status                      # Daemon status
gradle clean build                   # Clean and build
gradle build -x test                 # Skip tests
gradle build --offline               # Offline mode
gradle build --refresh-dependencies  # Refresh deps
gradle build --parallel              # Parallel build
gradle build --build-cache           # Use build cache
gradle dependencies                  # Show deps
gradle tasks                         # List tasks
gradle wrapper                       # Generate wrapper
gradle init                          # Init project
```
- `-q` or `--quiet`: Quiet
- `--console`: Console type (plain, auto, rich, verbose)
- `--no-daemon`: Don't use daemon
- `--daemon`: Use daemon
- `-x`: Exclude task
- `--offline`: Offline mode
- `--refresh-dependencies`: Refresh dependencies
- `--parallel`: Parallel build
- `--build-cache`: Enable build cache

## Recommended Unattended Usage

```bash
#!/bin/bash

# Plain console for CI, no daemon
gradle --console=plain --no-daemon build -x test
```
