# passwd

**Platforms:** Linux, macOS
**Category:** System Utilities

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show help | `passwd --help` |
| Show status | `passwd -S user` |
| Check expiry | `passwd -e user` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `passwd user` | Changes password |
| `passwd -d user` | Deletes password |
| `passwd -l user` | Locks account |
| `passwd -u user` | Unlocks account |
| Any passwd without -S | Modifies passwords |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe passwd Inspection Script

# Show status
passwd -S user

# Check expiry
passwd -e user
```
