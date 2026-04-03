# metricbeat

**Platforms:** Multi-platform
**Category:** Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `metricbeat --version` |
| Show help | `metricbeat --help` |
| Test config | `metricbeat test config` |
| Show output | `metricbeat test output` |
| List modules | `metricbeat modules list` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `metricbeat -e` | Runs metricbeat (sends data) |
| `metricbeat setup` | Sets up indices/dashboards |
| Any metricbeat execution | Sends metrics |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe metricbeat Inspection Script

# Show version
metricbeat --version

# Test config
metricbeat test config

# List modules
metricbeat modules list
```
