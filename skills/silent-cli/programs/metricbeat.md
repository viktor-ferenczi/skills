# metricbeat

**Platforms:** Multi-platform  
**Category:** Metrics Shipper

## Command-Line Flags

```bash
metricbeat -e                        # Log to stderr
metricbeat -c metricbeat.yml         # Config file
metricbeat test config               # Test config
```
- `-e`: Log to stderr
- `-c`: Config file

## Recommended Unattended Usage

```bash
#!/bin/bash

metricbeat test config || exit 1
metricbeat -e -c metricbeat.yml
```
