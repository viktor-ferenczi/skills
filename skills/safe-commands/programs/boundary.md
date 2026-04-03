# boundary

**Platforms:** Multi-platform
**Category:** Security/Access

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `boundary version` |
| Show help | `boundary --help` |
| List scopes | `boundary scopes list` |
| List targets | `boundary targets list` |
| Get target | `boundary targets read` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `boundary targets create` | Creates targets |
| `boundary targets delete` | Deletes targets |
| `boundary targets update` | Updates targets |
| `boundary connect` | Opens connections |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe boundary Inspection Script

# Show version
boundary version

# List scopes
boundary scopes list

# List targets
boundary targets list
```
