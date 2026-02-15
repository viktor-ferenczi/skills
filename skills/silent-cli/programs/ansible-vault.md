# ansible-vault

**Platforms:** Multi-platform  
**Category:** Configuration Management (Secrets)

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive encrypt | `ansible-vault encrypt file.yml --vault-password-file=.vault_pass` |
| Non-interactive decrypt | `ansible-vault decrypt file.yml --vault-password-file=.vault_pass` |

## Command-Line Flags

- `--vault-password-file`: Read vault password from a file (avoids interactive `--ask-vault-pass` prompt)

> **Warning:** Avoid `--ask-vault-pass` in unattended mode — it requires interactive input.
