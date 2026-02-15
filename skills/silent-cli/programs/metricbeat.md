# metricbeat

**Platforms:** Multi-platform  
**Category:** Metrics Shipper

## Quick Reference

| Goal | Command |
|------|---------|
| Run | `metricbeat -e -c metricbeat.yml` |
| Config test | `metricbeat test config` |
| Modules | `metricbeat modules list` |

## Command-Line Flags

```bash
metricbeat -e                        # Log to stderr
metricbeat -c metricbeat.yml         # Config file
metricbeat test config               # Test config
metricbeat test output               # Test output
metricbeat setup                     # Setup dashboards
metricbeat setup --dashboards
metricbeat setup --index-management
metricbeat modules list              # List modules
metricbeat modules enable system
metricbeat modules disable system
metricbeat -e -system.hostfs=/hostfs  # Container host filesystem
```
- `-e`: Log to stderr
- `-c`: Config file
- `test config/output`: Validate/test
- `setup`: Setup dashboards and templates
- `modules list/enable/disable`: Module management
- `-system.hostfs`: Set host filesystem (containers)

## Recommended Unattended Usage

```bash
#!/bin/bash

metricbeat test config || exit 1
metricbeat -e -c metricbeat.yml
```
