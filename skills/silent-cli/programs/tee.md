# tee

**Platforms:** Multi-platform  
**Category:** Output Redirection

## Recommended Unattended Usage

```bash
#!/bin/bash

# Log output and display it
make 2>&1 | tee build.log

# Append to log with timestamp
echo "$(date): Starting process" | tee -a process.log
```
