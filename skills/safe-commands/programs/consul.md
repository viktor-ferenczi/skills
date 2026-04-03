# consul

**Platforms:** Multi-platform
**Category:** Service Mesh

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `consul --version` |
| Show help | `consul --help` |
| Show members | `consul members` |
| Get key | `consul kv get key` |
| List keys | `consul kv list` |
| Show config | `consul info` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `consul kv put` | Writes data |
| `consul kv delete` | Deletes data |
| `consul join` | Joins cluster |
| `consul leave` | Leaves cluster |
| `consul force-leave` | Forces leave |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe consul Inspection Script

# Show version
consul --version

# Show members
consul members

# List keys
consul kv list
```
