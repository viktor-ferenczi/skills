# filebeat

**Platforms:** Multi-platform  
**Category:** Log Shipper

## Quick Reference

| Goal | Command |
|------|---------|
| Validate config (non-interactive) | `filebeat test config -c filebeat.yml` |
| Test output connectivity | `filebeat test output -c filebeat.yml` |

## Command-Line Flags

- `-e`: Log to stderr (instead of syslog — useful for capturing output in scripts)
- `-c`: Specify config file path

`filebeat` is inherently non-interactive when run as a service. The key concern for unattended use is validating configuration before starting.

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate and run
filebeat test config -c filebeat.yml || exit 1
filebeat test output -c filebeat.yml || exit 1

filebeat -e -c filebeat.yml -d '*' 2>&1 | grep -v "INFO"
```
