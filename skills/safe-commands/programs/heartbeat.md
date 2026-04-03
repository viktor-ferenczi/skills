# heartbeat (Elastic Stack)

**Platforms:** Multi-platform
**Category:** Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `heartbeat --version` |
| Show help | `heartbeat --help` |
| Test config | `heartbeat test config` |
| Show output | `heartbeat test output` |
| List modules | `heartbeat modules list` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `heartbeat -e` | Runs heartbeat (sends data) |
| `heartbeat setup` | Sets up indices |
| Any heartbeat execution | Sends monitoring data |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe heartbeat Inspection Script

# Show version
heartbeat --version

# Test config
heartbeat test config

# List modules
heartbeat modules list
```
