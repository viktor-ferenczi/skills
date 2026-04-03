# filebeat

**Platforms:** Multi-platform
**Category:** Log Shipping

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `filebeat --version` |
| Show help | `filebeat --help` |
| Test config | `filebeat test config` |
| Show modules | `filebeat modules list` |
| Show output | `filebeat test output` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `filebeat -e` | Runs filebeat (sends data) |
| `filebeat setup` | Sets up indices/dashboards |
| Any filebeat execution | Ships log data |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe filebeat Inspection Script

# Show version
filebeat --version

# Test config
filebeat test config

# List modules
filebeat modules list
```
