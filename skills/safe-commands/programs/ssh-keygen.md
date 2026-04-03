# ssh-keygen

**Platforms:** Multi-platform
**Category:** Security/SSH

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `ssh-keygen -V` |
| Show help | `ssh-keygen --help` |
| View key | `ssh-keygen -l -f key.pub` |
| Check key | `ssh-keygen -l -f key` |
| Convert key | `ssh-keygen -p -m PEM` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `ssh-keygen -t rsa` | Generates new keys |
| `ssh-keygen -f newkey` | Creates new key files |
| Any ssh-keygen key generation | Creates key pairs |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe ssh-keygen Inspection Script

# View public key fingerprint
ssh-keygen -l -f ~/.ssh/id_rsa.pub

# View private key fingerprint
ssh-keygen -l -f ~/.ssh/id_rsa
```
