# ssh-keygen

**Platforms:** Multi-platform  
**Category:** SSH Key Management

## Quick Reference

| Goal | Command |
|------|---------|
| Generate key (no passphrase, no prompts) | `ssh-keygen -t ed25519 -f key -N ''` |

## Command-Line Flags

- `-f`: Output filename — avoids interactive filename prompt
- `-N`: New passphrase (`''` for none) — avoids interactive passphrase prompt

## Recommended Unattended Usage

```bash
#!/bin/bash

# Generate key without passphrase
ssh-keygen -t ed25519 -f /tmp/deploy_key -N '' -C 'deploy@$(hostname)'

# Get public key fingerprint
fingerprint=$(ssh-keygen -lf /tmp/deploy_key.pub | awk '{print $2}')
```
