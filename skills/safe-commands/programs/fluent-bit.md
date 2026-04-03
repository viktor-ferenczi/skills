# fluent-bit

**Platforms:** Multi-platform
**Category:** Log Processing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `fluent-bit --version` |
| Show help | `fluent-bit --help` |
| Show plugins | `fluent-bit --list_plugins` |
| Validate config | `fluent-bit --validate` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `fluent-bit -c config` | Runs fluent-bit (processes data) |
| Any fluent-bit execution | Processes and forwards logs |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe fluent-bit Inspection Script

# Show version
fluent-bit --version

# List plugins
fluent-bit --list_plugins

# Validate config
fluent-bit --validate -c fluent-bit.conf
```
