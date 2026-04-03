# telegraf

**Platforms:** Multi-platform
**Category:** Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `telegraf --version` |
| Show help | `telegraf --help` |
| Test config | `telegraf --test --config` |
| List inputs | `telegraf --section-filter inputs` |
| Sample config | `telegraf config` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `telegraf --config` | Runs telegraf (sends data) |
| Any telegraf execution | Collects and sends metrics |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe telegraf Inspection Script

# Show version
telegraf --version

# Test config
telegraf --test --config telegraf.conf
```
