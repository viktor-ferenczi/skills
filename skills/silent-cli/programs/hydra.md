# hydra

**Platforms:** Multi-platform  
**Category:** Password Brute Forcer

## Command-Line Flags

- `-o`: Output results to file
- `-f`: Stop on first valid result
- `-t`: Number of parallel tasks

## Recommended Unattended Usage

```bash
#!/bin/bash

# Test single credential quietly
hydra -l admin -p password ssh://target -t 4 -o result.txt 2>/dev/null
```
