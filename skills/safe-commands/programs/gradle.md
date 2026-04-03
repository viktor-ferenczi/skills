# gradle

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `gradle --version` |
| Show help | `gradle --help` |
| List tasks | `gradle tasks` |
| Show project | `gradle projects` |
| Show dependencies | `gradle dependencies` |
| Show config | `gradle properties` |
| Dry-run | `gradle --dry-run` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `gradle build` | Builds project |
| `gradle clean` | Cleans output |
| `gradle test` | Runs tests |
| `gradle assemble` | Assembles |
| `gradle publish` | Publishes |
| `gradle init` | Initializes |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe gradle Inspection Script

# Show version
gradle --version

# List tasks
gradle tasks

# Show dependencies
gradle dependencies

# Dry-run
gradle build --dry-run
```
