# gpg (GnuPG)

**Platforms:** Multi-platform  
**Category:** Encryption/Signing

## Quick Reference

| Goal | Command |
|------|---------|
| Batch mode (no prompts) | `gpg --batch --yes --encrypt --recipient user@email file` |
| Non-interactive decrypt | `gpg --batch --yes --pinentry-mode loopback --passphrase "$PASS" --decrypt file.gpg` |
| Batch key generation | `gpg --batch --gen-key gen-key-script` |

## Command-Line Flags

- `--batch`: Batch mode (disable all interactive prompts)
- `--yes`: Auto-confirm all prompts (overwrite, delete, etc.)
- `--passphrase`: Provide passphrase on command line (avoids pinentry prompt)
- `--pinentry-mode loopback`: Allow passphrase from command line/env (required for `--passphrase` in newer GPG versions)
- `--no-tty`: Do not use the terminal for any output

## Recommended Unattended Usage

```bash
#!/bin/bash

# Encrypt with batch mode
gpg --batch --yes --encrypt --recipient admin@example.com file.txt

# Decrypt with passphrase
gpg --batch --yes --pinentry-mode loopback --passphrase "$PASS" --decrypt file.gpg
```
