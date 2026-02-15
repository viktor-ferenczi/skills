# nmap

**Platforms:** Multi-platform  
**Category:** Network Security Scanner

## Quick Reference

| Goal | Command |
|------|---------|
| Quick scan | `nmap -T4 -F target` |
| Service scan | `nmap -sV target` |
| Quiet | `nmap -T4 -F --open target` |
| Output to file | `nmap -oN output.txt target` |

## Command-Line Flags

```bash
nmap -T4 -F target                   # Fast scan
nmap -T4 -A target                   # Aggressive scan
nmap -sV target                      # Service version detection
nmap -sP 192.168.1.0/24              # Ping scan (host discovery)
nmap -sn 192.168.1.0/24              # No port scan
nmap -p 80,443 target                # Specific ports
nmap -p- target                      # All ports
nmap --top-ports 1000 target         # Top 1000 ports
nmap -O target                       # OS detection
nmap -sS target                      # SYN scan (root)
nmap -sT target                      # TCP connect scan
nmap -sU target                      # UDP scan
nmap --script vuln target            # Vulnerability scan
nmap -oN output.txt target           # Normal output
nmap -oX output.xml target           # XML output
nmap -oG output.grep target          # Grepable output
nmap -v target                       # Verbose
nmap -vv target                      # More verbose
nmap -d target                       # Debug
nmap --open target                   # Show open only
nmap --reason target                 # Show reason
nmap -n target                       # No DNS resolution
```
- `-T<0-5>`: Timing template (higher is faster)
- `-F`: Fast mode (fewer ports)
- `-sV`: Service version detection
- `-p`: Port specification
- `-O`: OS detection
- `-oN/-oX/-oG`: Output formats
- `--open`: Show only open ports
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
