# gpg (GnuPG)

**Platforms:** Multi-platform
**Category:** Security/Encryption

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `gpg --version` |
| Show help | `gpg --help` |
| List keys | `gpg --list-keys` |
| List secret keys | `gpg --list-secret-keys` |
| Decrypt (read) | `gpg -d file.gpg` |
| Verify | `gpg --verify file.sig` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `gpg --gen-key` | Generates new keys |
| `gpg --delete-key` | Deletes keys |
| `gpg --import` | Imports keys |
| `gpg --encrypt` | Encrypts files |
| `gpg --sign` | Signs files |
| `gpg --export` | Exports keys |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe gpg Inspection Script

# Show version
gpg --version

# List keys
gpg --list-keys

# Verify signature
gpg --verify file.sig
```
