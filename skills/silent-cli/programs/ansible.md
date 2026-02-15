# ansible

**Platforms:** Multi-platform  
**Category:** Configuration Management

## Quick Reference

| Goal | Command |
|------|---------|
| Ping | `ansible all -m ping` |
| Command | `ansible all -a 'uptime'` |
| Playbook | `ansible-playbook site.yml` |
| Syntax check | `ansible-playbook --syntax-check site.yml` |

## Command-Line Flags

```bash
ansible all -m ping                  # Ping all hosts
ansible webservers -m ping           # Ping group
ansible server1 -a 'uptime'          # Run command
ansible all -a 'whoami' -b           # Become root
ansible all -m setup                 # Gather facts
ansible all -m apt -a 'name=nginx state=present' -b
ansible all -m copy -a 'src=file dest=/tmp/file'
ansible all -m template -a 'src=template.j2 dest=/etc/config'
ansible all -m service -a 'name=nginx state=started' -b
ansible all -i inventory.ini -m ping
ansible all --list-hosts             # List hosts
ansible all --limit webservers -m ping
ansible-playbook site.yml            # Run playbook
ansible-playbook site.yml --check    # Dry run
ansible-playbook site.yml --diff     # Show diffs
ansible-playbook site.yml --syntax-check
ansible-playbook site.yml --list-tasks
ansible-playbook site.yml --list-hosts
ansible-playbook site.yml --start-at-task='Task Name'
ansible-playbook site.yml --tags deploy
ansible-playbook site.yml --skip-tags test
ansible-playbook site.yml --limit webservers
ansible-playbook site.yml -i inventory.ini
ansible-playbook site.yml -e 'var=value'
ansible-playbook site.yml -e '@vars.yml'
ansible-playbook site.yml -v         # Verbose
ansible-playbook site.yml -vvv       # More verbose
ansible-playbook site.yml --step     # Step by step
ansible-playbook site.yml --ask-become-pass
ansible-playbook site.yml --private-key=~/.ssh/id_rsa
ansible-galaxy init role_name        # Init role
ansible-galaxy install user.role
ansible-galaxy list
ansible-vault create secrets.yml     # Create encrypted file
ansible-vault edit secrets.yml
ansible-vault decrypt secrets.yml
ansible-vault encrypt secrets.yml
```
- `-i` or `--inventory`: Inventory file
- `-m` or `--module-name`: Module to use
- `-a` or `--args`: Module arguments
- `-b` or `--become`: Become superuser
- `-e` or `--extra-vars`: Extra variables
- `-v`: Verbose (vvv for more)
- `--check`: Dry run
- `--diff`: Show diffs
- `--limit`: Limit to hosts
- `--tags`/`--skip-tags`: Tag filtering
- `--syntax-check`: Validate syntax

## Environment Variables

```bash
export ANSIBLE_HOST_KEY_CHECKING=False
export ANSIBLE_RETRY_FILES_ENABLED=False
export ANSIBLE_PIPELINING=True
export ANSIBLE_FORKS=10
```

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
