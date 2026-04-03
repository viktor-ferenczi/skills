# circleci

**Platforms:** Multi-platform
**Category:** CI/CD

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `circleci version` |
| Show help | `circleci --help` |
| Show config | `circleci config validate` |
| List checks | `circleci checks` |
| Show diagnostics | `circleci diagnostic` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `circleci build` | Runs builds |
| `circleci run` | Executes jobs |
| `circleci start` | Starts pipelines |
| `circleci trigger` | Triggers pipelines |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe circleci Inspection Script

# Show version
circleci version

# Validate config
circleci config validate

# Show diagnostics
circleci diagnostic
```
