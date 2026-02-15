# filebeat

**Platforms:** Multi-platform  
**Category:** Log Shipper

## Quick Reference

| Goal | Command |
|------|---------|
| Run | `filebeat -e -c filebeat.yml` |
| Config test | `filebeat test config` |
| Output | `filebeat test output` |

## Command-Line Flags

```bash
filebeat -e                          # Log to stderr
filebeat -c filebeat.yml             # Config file
filebeat -e -c filebeat.yml          # Stderr + custom config
filebeat test config                 # Test config
filebeat test config -c filebeat.yml
filebeat test output                 # Test output
filebeat setup                       # Setup dashboards/templates
filebeat setup --dashboards          # Setup dashboards only
filebeat setup --index-management    # Setup index templates
filebeat setup --pipelines           # Setup ingest pipelines
filebeat modules list                # List modules
filebeat modules enable system       # Enable module
filebeat modules disable system      # Disable module
filebeat run -e                      # Run once
filebeat export config               # Export config
filebeat export template             # Export index template
filebeat -e -d '*'                   # Debug selectors
filebeat -e -v                       # Verbose
filebeat -e --httpprof localhost:6060  # Profiling endpoint
```
- `-e`: Log to stderr (and syslog)
- `-c`: Config file
- `test config`: Validate config
- `test output`: Test output connection
- `setup`: Setup index templates and dashboards
- `modules list/enable/disable`: Module management
- `export config/template`: Export configurations
- `-d`: Debug selectors
- `-v`: Verbose
- `--httpprof`: HTTP profiling endpoint

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate and run
filebeat test config -c filebeat.yml || exit 1
filebeat test output -c filebeat.yml || exit 1

filebeat -e -c filebeat.yml -d '*' 2>&1 | grep -v "INFO"
```
