# hashcat

**Platforms:** Multi-platform  
**Category:** Password Cracker (GPU)

## Command-Line Flags

- `-o`: Output file
- `--potfile-disable`: Disable pot file
- `--force`: Force run (ignore warnings)
- `--status`: Show status updates
- `--status-timer`: Status update interval (seconds)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Crack with status updates to file
hashcat -m 0 -a 0 hash.txt wordlist.txt -o cracked.txt --status --status-timer 60 2>/dev/null
```
