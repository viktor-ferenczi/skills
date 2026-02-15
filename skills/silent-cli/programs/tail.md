# tail

**Platforms:** Multi-platform  
**Category:** Text Processing

## Command-Line Flags

- `-q` or `--quiet`: No headers (suppress filename output)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Monitor log and extract errors
tail -f /var/log/app.log | grep ERROR

# Get last N lines without filename header
tail -q -n 100 file.txt
```
