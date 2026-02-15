# john (John the Ripper)

**Platforms:** Multi-platform  
**Category:** Password Cracker

## Command-Line Flags

- `--restore`: Restore interrupted session (non-interactive resume)
- `--status`: Show status of session
- `--pot`: Custom pot file (output)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Crack with wordlist (stderr suppressed)
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt 2>/dev/null

# Show results
john --show hashes.txt
```
