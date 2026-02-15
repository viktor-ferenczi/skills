# ansible-playbook

**Platforms:** Multi-platform  
**Category:** Configuration Management

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive run | `ansible-playbook site.yml` |
| Non-interactive vault | `ansible-playbook site.yml --vault-password-file=.vault_pass` |

## Command-Line Flags

- `--vault-password-file`: Read vault password from file (avoids `--ask-vault-pass` interactive prompt)
- `--check`: Dry run (no changes, safe for automation)
- `--diff`: Show diffs of changes
- `--syntax-check`: Validate playbook syntax without running

> **Warning:** Avoid `--step` (confirms each task interactively) and `--ask-become-pass` (prompts for password) in unattended mode.

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate
ansible-playbook --syntax-check site.yml || exit 1

# Test run
ansible-playbook --check --diff site.yml || exit 1

# Deploy
ansible-playbook --diff site.yml
```
