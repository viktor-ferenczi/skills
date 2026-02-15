# netstat

**Platforms:** Linux, macOS, Windows  
**Category:** Network Statistics

## Command-Line Flags

```bash
netstat -n                           # Numeric (no DNS, faster non-interactive)
```
- `-n`: Numeric (avoids DNS lookups, better for non-interactive use)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Check if port 80 is listening
netstat -tlnp | grep ':80 '

# Get connection count per state
netstat -ant | awk '{print $6}' | sort | uniq -c | sort -n
```
