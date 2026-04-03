# ansible-vault

**Platforms:** Multi-platform
**Category:** Automation/Security

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `ansible-vault --version` |
| Show help | `ansible-vault --help` |
| View encrypted | `ansible-vault view file` |
| Encrypt file | `ansible-vault encrypt file` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `ansible-vault decrypt` | Decrypts files |
| `ansible-vault edit` | Edits encrypted files |
| `ansible-vault rekey` | Changes encryption key |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe ansible-vault Inspection Script

# Show version
ansible-vault --version

# View encrypted (read-only)
ansible-vault view secrets.yml
```
