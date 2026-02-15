# masscan

**Platforms:** Linux  
**Category:** Network Scanner (High Speed)

## Quick Reference

| Goal | Command |
|------|---------|
| Quick scan | `masscan 192.168.1.0/24 -p80,443 --rate 1000` |
| Output | `masscan ... -oG scan.txt` |
| Exclude | `masscan ... --excludefile exclude.txt` |

## Command-Line Flags

```bash
masscan 192.168.1.0/24 -p80,443      # Scan subnet
masscan 0.0.0.0/0 -p0-65535          # Internet scan (dangerous!)
masscan 192.168.1.0/24 -p0-65535 --rate 10000
masscan 192.168.1.0/24 -p80,443 -oG scan.txt
masscan 192.168.1.0/24 -p80,443 -oJ scan.json
masscan 192.168.1.0/24 -p80,443 --excludefile exclude.txt
masscan 192.168.1.0/24 -p80,443 --echo > config.conf  # Save config
masscan -c config.conf               # Load config
```
- `-p`: Port specification
- `--rate`: Packets per second
- `-oG`: Grepable output
- `-oJ`: JSON output
- `-oL`: Simple list
- `-oX`: XML output
- `--excludefile`: Exclude ranges file
- `-c`: Config file
- `--echo`: Show config

## Recommended Unattended Usage

```bash
#!/bin/bash

# Fast scan with output
masscan 192.168.1.0/24 -p80,443,22,3389 --rate 10000 -oG scan.txt 2>/dev/null
```
