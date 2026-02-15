# sed

**Platforms:** Multi-platform  
**Category:** Stream Editor

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet (suppress auto-print) | `sed -n '5p' file` |
| In-place edit | `sed -i 's/old/new/g' file` |

## Command-Line Flags

- `-n`: Quiet — suppress automatic printing of pattern space (only print explicit `p` output)
- `-i`: Edit in-place (no interactive confirmation)
- `-i.bak`: Edit in-place with backup

## Recommended Unattended Usage

```bash
#!/bin/bash

# Safe in-place edit with backup
sed -i.bak 's/old/new/g' file.txt

# Quiet extraction
value=$(sed -n 's/^key=//p' config.txt)
```
