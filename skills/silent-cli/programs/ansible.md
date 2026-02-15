# ansible

**Platforms:** Multi-platform  
**Category:** Configuration Management

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive run | `ansible-playbook site.yml` |
| Syntax check | `ansible-playbook --syntax-check site.yml` |
| Non-interactive vault | `ansible-playbook site.yml --vault-password-file=.vault_pass` |

## Environment Variables

```bash
export ANSIBLE_HOST_KEY_CHECKING=False   # Disable SSH host key prompts (critical for automation)
export ANSIBLE_RETRY_FILES_ENABLED=False # Disable .retry file creation
export ANSIBLE_PIPELINING=True           # Reduce connection overhead
```

## Command-Line Flags

- `--vault-password-file`: Read vault password from file (avoids interactive prompt)
- `--check`: Dry run (no changes)
- `--diff`: Show diffs
- `--syntax-check`: Validate syntax without running

> **Warning:** Avoid `--ask-become-pass`, `--ask-vault-pass`, and `--step` in unattended mode — they require interactive input.

## Recommended Unattended Usage

```bash
#!/bin/bash

# Syntax check first
ansible-playbook --syntax-check site.yml || exit 1

# Check mode (dry run)
ansible-playbook --check --diff site.yml || exit 1

# Run playbook
ansible-playbook -i inventory.ini site.yml
```
