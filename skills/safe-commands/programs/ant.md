# ant

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `ant -version` |
| Show help | `ant -help` |
| Show project info | `ant -projecthelp` |
| List targets | `ant -p` |
| Dry-run build | `ant -dryrun` (if supported) |
| Show diagnostics | `ant -diagnostics` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `ant` (default) | Executes build targets |
| `ant compile` | Compiles code |
| `ant dist` | Creates distribution |
| `ant clean` | Deletes build artifacts |
| `ant test` | Runs tests |
| Any ant execution | May modify files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe ant Inspection Script

# Show version
ant -version

# Show project help
ant -projecthelp

# List targets
ant -p

# Show diagnostics
ant -diagnostics
```
