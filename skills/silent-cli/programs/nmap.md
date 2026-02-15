# nmap

**Platforms:** Multi-platform  
**Category:** Network Security Scanner

## Quick Reference

| Goal | Command |
|------|---------|
| Output to file | `nmap -oN output.txt target` |
| XML output | `nmap -oX output.xml target` |

## Command-Line Flags

```bash
nmap -oN output.txt target           # Normal output to file
nmap -oX output.xml target           # XML output (machine-readable)
nmap -oG output.grep target          # Grepable output (machine-readable)
nmap --open target                   # Show open only (reduced output)
nmap -n target                       # No DNS resolution (faster, non-interactive)
```
- `-oN/-oX/-oG`: Output formats (machine-readable)
- `--open`: Show only open ports (reduced output)
- `-n`: No DNS resolution

## Recommended Unattended Usage

```bash
#!/bin/bash

# Fast, quiet scan
nmap -T4 -F --open -oN scan.txt --stylesheet "" target 2>/dev/null

# XML output for parsing
nmap -T4 -F -oX scan.xml target

# No DNS, show open only
nmap -T4 -F -n --open target
```
