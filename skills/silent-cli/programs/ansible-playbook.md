# ansible-playbook

**Platforms:** Multi-platform  
**Category:** Configuration Management

## Quick Reference

| Goal | Command |
|------|---------|
| Run | `ansible-playbook site.yml` |
| Check | `ansible-playbook --check site.yml` |
| Syntax | `ansible-playbook --syntax-check site.yml` |
| List tasks | `ansible-playbook --list-tasks site.yml` |

## Command-Line Flags

```bash
ansible-playbook site.yml
ansible-playbook site.yml -i inventory.ini
ansible-playbook site.yml --limit webservers
ansible-playbook site.yml --limit 'webservers:!staging'
ansible-playbook site.yml --tags deploy
ansible-playbook site.yml --tags 'deploy,config'
ansible-playbook site.yml --skip-tags test
ansible-playbook site.yml --check    # Dry run
ansible-playbook site.yml --diff     # Show changes
ansible-playbook site.yml --check --diff
ansible-playbook site.yml --syntax-check
ansible-playbook site.yml --list-tasks
ansible-playbook site.yml --list-hosts
ansible-playbook site.yml --list-tags
ansible-playbook site.yml --start-at-task='Install packages'
ansible-playbook site.yml --step     # Confirm each task
ansible-playbook site.yml -e 'var=value'
ansible-playbook site.yml -e '@vars.yml'
ansible-playbook site.yml -e '@vars.json'
ansible-playbook site.yml -v         # Verbose
ansible-playbook site.yml -vvv       # Debug
ansible-playbook site.yml --flush-cache
ansible-playbook site.yml --force-handlers
ansible-playbook site.yml -b         # Become
ansible-playbook site.yml -b --ask-become-pass
ansible-playbook site.yml --private-key=~/.ssh/id_rsa
ansible-playbook site.yml --user=admin
ansible-playbook site.yml --connection=local
ansible-playbook site.yml --forks=10
ansible-playbook site.yml --timeout=30
ansible-playbook site.yml --vault-password-file=.vault_pass
ansible-playbook site.yml --ask-vault-pass
```
- `-i`: Inventory
- `-e`: Extra vars
- `-v`: Verbose
- `-b`: Become
- `--check`: Dry run
- `--diff`: Show diffs
- `--syntax-check`: Validate
- `--limit`: Host limit
- `--tags`/`--skip-tags`: Tags
- `--list-tasks`/`--list-hosts`/`--list-tags`: List info
- `--start-at-task`: Start at specific task
- `--step`: Step through

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
