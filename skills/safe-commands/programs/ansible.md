# ansible

**Platforms:** Multi-platform
**Category:** Automation & DevOps

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Dry-run | `ansible-playbook --check` |
| Diff mode | `ansible-playbook --diff` |
| List tasks | `ansible-playbook --list-tasks` |
| List hosts | `ansible-playbook --list-hosts` |
| Show config | `ansible --version` |
| Show inventory | `ansible-inventory --list` |
| Show host vars | `ansible-inventory --host hostname` |
| Show config path | `ansible --config` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `ansible-playbook` (normal) | Executes changes |
| `ansible` module execution | Runs modules on hosts |
| `ansible-playbook --diff` with apply | Shows and applies |
| Any ansible without --check | May modify systems |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe ansible Inspection Script

# Show version
ansible --version

# List inventory
ansible-inventory --list

# Show host vars
ansible-inventory --host web01

# Dry-run playbook
ansible-playbook playbook.yml --check

# List tasks
ansible-playbook playbook.yml --list-tasks

# List hosts
ansible-playbook playbook.yml --list-hosts
```
