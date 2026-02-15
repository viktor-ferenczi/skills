# ansible-vault

**Platforms:** Multi-platform  
**Category:** Configuration Management (Secrets)

## Quick Reference

| Goal | Command |
|------|---------|
| Encrypt | `ansible-vault encrypt file.yml` |
| Decrypt | `ansible-vault decrypt file.yml` |
| Edit | `ansible-vault edit file.yml` |

## Command-Line Flags

```bash
ansible-vault create secrets.yml     # Create encrypted file
ansible-vault encrypt file.yml       # Encrypt file
ansible-vault decrypt file.yml       # Decrypt file
ansible-vault edit file.yml          # Edit encrypted file
ansible-vault view file.yml          # View encrypted file
ansible-vault rekey file.yml         # Change password
ansible-vault encrypt_string 'secret' --name 'variable_name'
ansible-vault encrypt file.yml --output encrypted.yml
```
- `--ask-vault-pass`: Prompt for password
- `--vault-password-file`: Read password from file
- `--output`: Output file
- `--encrypt-vault-id`: Vault ID to encrypt with
