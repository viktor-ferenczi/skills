# gpg (GnuPG)

**Platforms:** Multi-platform  
**Category:** Encryption/Signing

## Quick Reference

| Goal | Command |
|------|---------|
| Encrypt | `gpg --encrypt --recipient user@email file` |
| Decrypt | `gpg --decrypt file.gpg` |
| Sign | `gpg --sign file` |
| Batch | `gpg --batch --yes ...` |

## Command-Line Flags

```bash
gpg --encrypt --recipient user@email file
gpg --encrypt --armor --recipient user@email file  # ASCII armor
gpg --decrypt file.gpg > file
gpg --decrypt --batch --passphrase 'password' file.gpg
gpg --sign file                      # Sign
gpg --clearsign file                 # Clear sign
gpg --detach-sign file               # Detached signature
gpg --verify file.sig file           # Verify
gpg --gen-key                        # Generate key (interactive)
gpg --batch --gen-key gen-key-script  # Batch keygen
gpg --list-keys                      # List public keys
gpg --list-secret-keys               # List private keys
gpg --import key.asc                 # Import key
gpg --export -a user@email           # Export public key
gpg --export-secret-keys -a user@email  # Export private key
gpg --batch --yes --delete-keys keyID
gpg --batch --yes --delete-secret-keys keyID
gpg --pinentry-mode loopback --passphrase 'pass' --decrypt file.gpg
```
- `--encrypt` or `-e`: Encrypt
- `--decrypt` or `-d`: Decrypt
- `--sign` or `-s`: Sign
- `--recipient` or `-r`: Recipient
- `--armor` or `-a`: ASCII armor
- `--batch`: Batch mode
- `--yes`: Auto-confirm
- `--passphrase`: Passphrase
- `--pinentry-mode loopback`: Allow passphrase from command

## Recommended Unattended Usage

```bash
#!/bin/bash

# Encrypt with batch mode
gpg --batch --yes --encrypt --recipient admin@example.com file.txt

# Decrypt with passphrase
gpg --batch --yes --pinentry-mode loopback --passphrase "$PASS" --decrypt file.gpg
```
