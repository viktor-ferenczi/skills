# smbpasswd

**Platforms:** Linux, macOS
**Category:** System/Security

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show help | `smbpasswd --help` |
| Show version | `smbpasswd -V` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `smbpasswd user` | Changes password |
| `smbpasswd -a user` | Adds user |
| `smbpasswd -x user` | Deletes user |
| `smbpasswd -d user` | Disables user |
| `smbpasswd -e user` | Enables user |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe smbpasswd Inspection Script

# Show help
smbpasswd --help
```
