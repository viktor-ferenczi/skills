# ssh-keygen

**Platforms:** Multi-platform  
**Category:** SSH Key Management

## Quick Reference

| Goal | Command |
|------|---------|
| Generate key | `ssh-keygen -t ed25519 -f key -N ''` |
| No passphrase | `ssh-keygen -t rsa -b 4096 -f key -N ''` |
| Change comment | `ssh-keygen -c -C 'comment' -f key` |

## Command-Line Flags

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ''
ssh-keygen -t rsa -b 4096 -f key -N '' -C 'comment'
ssh-keygen -y -f private_key > public_key.pub
ssh-keygen -lf ~/.ssh/id_rsa.pub           # Show fingerprint
ssh-keygen -F github.com                   # Check known hosts
ssh-keygen -R github.com                   # Remove from known hosts
ssh-keygen -R 192.168.1.1                  # Remove by IP
ssh-keygen -t ed25519 -a 100               # KDF rounds
ssh-keygen -o                              # New format
```
- `-t`: Type (rsa, dsa, ecdsa, ed25519)
- `-b`: Bits (for RSA)
- `-f`: Filename
- `-N`: New passphrase ('' for none)
- `-C`: Comment
- `-y`: Output public key from private
- `-l`: Show fingerprint
- `-F`: Find hostname in known_hosts
- `-R`: Remove hostname from known_hosts
- `-a`: KDF rounds (higher = slower)
- `-o`: Use new key format

## Recommended Unattended Usage

```bash
#!/bin/bash

# Generate key without passphrase
ssh-keygen -t ed25519 -f /tmp/deploy_key -N '' -C 'deploy@$(hostname)'

# Get public key fingerprint
fingerprint=$(ssh-keygen -lf /tmp/deploy_key.pub | awk '{print $2}')
```
