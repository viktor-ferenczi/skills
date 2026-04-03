# jenkins-cli

**Platforms:** Multi-platform
**Category:** CI/CD

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show help | `jenkins-cli help` |
| List jobs | `jenkins-cli list-jobs` |
| Get job info | `jenkins-cli get-job` |
| Show version | `jenkins-cli version` |
| Console output | `jenkins-cli console` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `jenkins-cli build` | Triggers builds |
| `jenkins-cli create-job` | Creates jobs |
| `jenkins-cli delete-job` | Deletes jobs |
| `jenkins-cli disable` | Disables jobs |
| `jenkins-cli enable` | Enables jobs |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe jenkins-cli Inspection Script

# List jobs
jenkins-cli list-jobs

# Get job info
jenkins-cli get-job job-name

# Show console
jenkins-cli console job-name
```
