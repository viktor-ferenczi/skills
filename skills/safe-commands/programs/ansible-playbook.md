# ansible-playbook

**Platforms:** Multi-platform
**Category:** Automation

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `ansible-playbook --version` |
| Show help | `ansible-playbook --help` |
| Dry-run | `ansible-playbook --check` |
| List tasks | `ansible-playbook --list-tasks` |
| List hosts | `ansible-playbook --list-hosts` |
| Diff mode | `ansible-playbook --diff` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `ansible-playbook playbook.yml` | Executes changes |
| Without --check | Applies modifications |
| `--step` with confirm | May apply changes |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe ansible-playbook Inspection Script

# Show version
ansible-playbook --version

# Dry-run
ansible-playbook playbook.yml --check

# List tasks
ansible-playbook playbook.yml --list-tasks
```
