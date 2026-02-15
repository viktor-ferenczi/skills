# heartbeat

**Platforms:** Multi-platform  
**Category:** Uptime Monitoring

## Command-Line Flags

- `-e`: Log to stderr (instead of file, useful for containers)
- `-c`: Config file path

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate config before running
heartbeat test config || exit 1

# Run non-interactively with stderr logging
heartbeat -e -c heartbeat.yml
```
