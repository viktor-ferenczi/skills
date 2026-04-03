# gitlab-runner

**Platforms:** Multi-platform
**Category:** CI/CD

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `gitlab-runner --version` |
| Show help | `gitlab-runner --help` |
| List runners | `gitlab-runner list` |
| Show info | `gitlab-runner info` |
| Verify | `gitlab-runner verify` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `gitlab-runner register` | Registers runner |
| `gitlab-runner uninstall` | Uninstalls runner |
| `gitlab-runner start` | Starts runner |
| `gitlab-runner stop` | Stops runner |
| `gitlab-runner restart` | Restarts runner |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe gitlab-runner Inspection Script

# Show version
gitlab-runner --version

# List runners
gitlab-runner list

# Verify runner
gitlab-runner verify
```
