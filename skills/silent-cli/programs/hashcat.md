# hashcat

**Platforms:** Multi-platform  
**Category:** Password Cracker (GPU)

## Quick Reference

| Goal | Command |
|------|---------|
| Crack | `hashcat -m 0 -a 0 hash.txt wordlist.txt` |
| Benchmark | `hashcat -b` |
| Restore | `hashcat --restore` |

## Command-Line Flags

```bash
hashcat -m 0 -a 0 hash.txt wordlist.txt  # MD5, dictionary
hashcat -m 100 -a 0 hash.txt wordlist.txt  # SHA1
hashcat -m 1000 -a 0 hash.txt wordlist.txt  # NTLM
hashcat -m 0 -a 3 hash.txt '?l?l?l?l'  # Brute force
hashcat -m 0 -a 0 hash.txt wordlist.txt -r rules/best64.rule
hashcat -b                           # Benchmark
hashcat -b -m 0                      # Benchmark MD5
hashcat --restore                    # Restore session
hashcat -o cracked.txt -m 0 hash.txt wordlist.txt  # Output to file
hashcat --show -m 0 hash.txt         # Show cracked
hashcat --potfile-disable -m 0 hash.txt wordlist.txt
hashcat --force -m 0 hash.txt wordlist.txt
hashcat --status -m 0 hash.txt wordlist.txt  # Show status
hashcat --status-timer 10 -m 0 hash.txt wordlist.txt
```
- `-m`: Hash type (0=MD5, 100=SHA1, 1000=NTLM, etc.)
- `-a`: Attack mode (0=dictionary, 3=brute force, etc.)
- `-r`: Rules file
- `-o`: Output file
- `--show`: Show cracked hashes
- `--restore`: Restore session
- `--potfile-disable`: Disable pot file
- `--force`: Force run
- `--status`: Show status
- `-O`: Optimized kernel

## Recommended Unattended Usage

```bash
#!/bin/bash

# Crack with status updates to file
hashcat -m 0 -a 0 hash.txt wordlist.txt -o cracked.txt --status --status-timer 60 2>/dev/null
```
