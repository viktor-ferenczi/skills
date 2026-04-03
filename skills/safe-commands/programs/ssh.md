# ssh

**Platforms:** Multi-platform
**Category:** Network & Remote Access

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Connect and run command | `ssh user@host 'command'` |
| Check version | `ssh -V` |
| Test connection | `ssh -O check user@host` |
| List keys | `ssh-add -l` |
| Show config | `ssh -G user@host` |
| Copy keys | `ssh-copy-id user@host` |
| Verbose test | `ssh -vvv user@host 'exit'` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `ssh` with interactive shell | May execute unintended commands |
| `ssh` piped to remote writes | Modifies remote system |
| `ssh-add -D` | Deletes keys |
| `ssh-keygen -f` with overwrite | Overwrites key files |
| Any ssh used for remote modification | Affects remote system state |

## Environment Variables for Safe Operation

| Variable | Description |
|----------|-------------|
| `SSH_USER` | Remote user name |
| `SSH_HOST` | Remote host |
| `SSH_PORT` | Remote port |
| `SSH_KEY` | Key file path |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe ssh Inspection Script

# Test connection only
ssh -O check user@host

# Run read-only command remotely
ssh user@host 'ps aux | head -20'

# Show SSH config
ssh -G user@host | head -30

# List local keys
ssh-add -l
```
