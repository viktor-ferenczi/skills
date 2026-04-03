# glab (GitLab CLI)

**Platforms:** Multi-platform
**Category:** Version Control

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `glab --version` |
| Show help | `glab --help` |
| List projects | `glab project list` |
| View project | `glab project view` |
| List issues | `glab issue list` |
| List MRs | `glab mr list` |
| View MR | `glab mr view` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `glab project create` | Creates project |
| `glab issue create` | Creates issue |
| `glab mr create` | Creates merge request |
| `glab mr merge` | Merges MR |
| `glab project delete` | Deletes project |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe glab Inspection Script

# Show version
glab --version

# List projects
glab project list

# List MRs
glab mr list
```
