# masscan

**Platforms:** Linux  
**Category:** Network Scanner (High Speed)

## Quick Reference

| Goal | Command |
|------|---------|
| Output | `masscan ... -oG scan.txt` |

## Command-Line Flags

```bash
masscan 192.168.1.0/24 -p80,443 -oG scan.txt   # Grepable output
masscan 192.168.1.0/24 -p80,443 -oJ scan.json   # JSON output
```
- `-oG`: Grepable output
- `-oJ`: JSON output
- `-oL`: Simple list
- `-oX`: XML output

## Recommended Unattended Usage

```bash
#!/bin/bash

# Fast scan with output
masscan 192.168.1.0/24 -p80,443,22,3389 --rate 10000 -oG scan.txt 2>/dev/null
```
