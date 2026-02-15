# john (John the Ripper)

**Platforms:** Multi-platform  
**Category:** Password Cracker

## Quick Reference

| Goal | Command |
|------|---------|
| Crack | `john hashes.txt` |
| Show cracked | `john --show hashes.txt` |
| Specific format | `john --format=raw-md5 hashes.txt` |

## Command-Line Flags

```bash
john hashes.txt                      # Crack hashes
john --show hashes.txt               # Show cracked passwords
john --format=raw-md5 hashes.txt     # Specific format
john --wordlist=passwords.txt hashes.txt
john --rules hashes.txt              # Use rules
john --incremental hashes.txt        # Incremental mode
john --external=Keyboard hashes.txt  # External mode
john --restore                       # Restore session
john --status                        # Show status
john --make-charset=custom.chr hashes.txt
john --pot=custom.pot hashes.txt     # Custom pot file
```
- `--show`: Show cracked passwords
- `--format`: Hash format
- `--wordlist`: Wordlist file
- `--rules`: Enable word mangling rules
- `--incremental`: Brute force mode
- `--external`: External mode
- `--restore`: Restore interrupted session
- `--status`: Show status of session
- `--pot`: Custom pot file

## Recommended Unattended Usage

```bash
#!/bin/bash

# Crack with wordlist
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt 2>/dev/null

# Show results
john --show hashes.txt
```
