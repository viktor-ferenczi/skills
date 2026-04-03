# nmap

**Platforms:** Multi-platform
**Category:** Security & Network Scanning

## Safe Commands (Read-Only / Non-Intrusive)

| Goal | Command |
|------|---------|
| Basic port scan | `nmap -sT host` (TCP connect) |
| Quick scan | `nmap -F host` (top 100 ports) |
| Version detection | `nmap -sV host` |
| OS detection | `nmap -O host` |
| Service scan | `nmap -sV --version-intensity 1 host` |
| Ping scan | `nmap -sn host` (no port scan) |
| List scan | `nmap -sL network` (DNS only) |
| Output to file | `nmap -oN output.txt host` |
| Fast scan | `nmap -T4 host` |
| Common ports | `nmap --top-ports 1000 host` |

## Potentially Intrusive Commands (Use with Caution)

| Command | Risk Level |
|---------|------------|
| `nmap -sS host` | SYN scan (may trigger IDS) |
| `nmap -A host` | Aggressive scan (multiple probes) |
| `nmap --script vuln host` | Vulnerability scripts |
| `nmap -sZ host` | SCTP scan (unusual) |
| `nmap -sN/-sF/-sX host` | Null/Fin/Xmas scans (evasive) |

## Environment Variables for Safe Operation

| Variable | Description |
|----------|-------------|
| `NMAPDIR` | Custom Nmap directory |
| `NMAPPATH` | Custom path for Nmap binaries |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe nmap Network Inspection Script

# Basic host discovery (ping only)
nmap -sn 192.168.1.0/24

# Quick port scan with version detection
nmap -sV -F 192.168.1.1

# Service enumeration (low intensity)
Nmap -sV --version-intensity 1 192.168.1.1

# Output results to file
nmap -sV -oN scan_results.txt 192.168.1.1

# Check common services
nmap -p 22,80,443,3306,5432 192.168.1.1
```
