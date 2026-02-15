# nikto

**Platforms:** Multi-platform  
**Category:** Web Vulnerability Scanner

## Quick Reference

| Goal | Command |
|------|---------|
| Output to file | `nikto -h target -o scan.txt` |
| Quiet | `nikto -h target -Display V` |

## Command-Line Flags

```bash
nikto -h target -o scan.txt          # Output to file
nikto -h target -o scan.html -Format html  # HTML output
nikto -h target -Display V           # Show vulnerabilities only (reduced output)
```
- `-o`: Output file
- `-Format`: Output format (csv, htm, nbe, txt, xml)
- `-Display`: Control output (V=show only vulns)

## Recommended Unattended Usage

```bash
#!/bin/bash

nikto -h http://target -o nikto.txt -Format txt -Display V 2>&1 | grep -v "^+"
```
