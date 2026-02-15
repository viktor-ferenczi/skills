# nikto

**Platforms:** Multi-platform  
**Category:** Web Vulnerability Scanner

## Quick Reference

| Goal | Command |
|------|---------|
| Basic scan | `nikto -h http://target` |
| Output | `nikto -h target -o scan.txt` |
| Quiet | `nikto -h target -Display V` |

## Command-Line Flags

```bash
nikto -h http://target               # Scan host
nikto -h target -p 8080              # Custom port
nikto -h target -ssl                 # Force SSL
nikto -h target -o scan.txt          # Output to file
nikto -h target -o scan.html -Format html
nikto -h target -Display V           # Show vulnerabilities only
nikto -h target -Tuning 123          # Specific tests
nikto -h target -C all               # Scan all CGI dirs
nikto -h target -update              # Update database
```
- `-h`: Target host
- `-p`: Port
- `-ssl`: Force SSL
- `-o`: Output file
- `-Format`: Output format (csv, htm, nbe, txt, xml)
- `-Display`: Control output (1=show redirects, V=show only vulns)
- `-Tuning`: Test tuning (1=interesting, 2=misconfig, 3=info disclosure, etc.)
- `-C`: CGI scan (all, none, or specific)

## Recommended Unattended Usage

```bash
#!/bin/bash

nikto -h http://target -o nikto.txt -Format txt -Display V 2>&1 | grep -v "^+"
```
