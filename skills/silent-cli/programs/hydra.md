# hydra

**Platforms:** Multi-platform  
**Category:** Password Brute Forcer

## Quick Reference

| Goal | Command |
|------|---------|
| SSH brute | `hydra -l admin -P passwords.txt ssh://target` |
| Multiple | `hydra -L users.txt -P passwords.txt target ssh` |
| Quiet | `hydra -l admin -p password ssh://target 2>/dev/null` |

## Command-Line Flags

```bash
hydra -l admin -P passwords.txt ssh://target
hydra -L users.txt -P passwords.txt ssh://target
hydra -l admin -p password ssh://target
hydra -C credentials.txt ssh://target  # Combined list
hydra -l admin -P passwords.txt target http-post-form '/login:user=^USER^&pass=^PASS^:F=invalid'
hydra -l admin -P passwords.txt ftp://target
hydra -l admin -P passwords.txt target smb
hydra -l admin -P passwords.txt -t 4 ssh://target  # 4 parallel
hydra -l admin -P passwords.txt -vV ssh://target   # Verbose
hydra -l admin -P passwords.txt -o output.txt ssh://target
hydra -l admin -P passwords.txt -f ssh://target    # Stop on first
```
- `-l`: Single login
- `-L`: Login list file
- `-p`: Single password
- `-P`: Password list file
- `-C`: Combined login:pass file
- `-t`: Parallel tasks
- `-vV`: Verbose
- `-o`: Output file
- `-f`: Stop on first valid
- `-s`: Port
- `-o`: Output results

## Recommended Unattended Usage

```bash
#!/bin/bash

# Test single credential quietly
hydra -l admin -p password ssh://target -t 4 -o result.txt 2>/dev/null
```
