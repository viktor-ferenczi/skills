# puppet

**Platforms:** Multi-platform
**Category:** Automation

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `puppet --version` |
| Show help | `puppet --help` |
| Apply dry-run | `puppet apply --noop` |
| Agent test | `puppet agent --test --noop` |
| Describe | `puppet describe resource` |
| Config print | `puppet config print` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `puppet apply` | Applies manifests |
| `puppet agent` | Applies catalog |
| Without --noop | Makes changes |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe puppet Inspection Script

# Dry-run apply
puppet apply --noop manifest.pp

# Agent test (dry-run)
puppet agent --test --noop
```
