# tr

**Platforms:** Multi-platform  
**Category:** Text Translation

## Quick Reference

| Goal | Command |
|------|---------|
| Replace | `tr 'a-z' 'A-Z'` |
| Delete | `tr -d '\n'` |
| Squeeze | `tr -s ' '` |
| Complement | `tr -cd 'a-z'` |

## Command-Line Flags

```bash
echo 'hello' | tr 'a-z' 'A-Z'        # Uppercase
echo 'HELLO' | tr 'A-Z' 'a-z'        # Lowercase
echo 'hello world' | tr ' ' ' '      # Replace spaces with newlines
echo 'hello' | tr -d 'l'             # Delete 'l'
echo 'hello   world' | tr -s ' '     # Squeeze spaces
echo 'hello123' | tr -d '0-9'        # Delete digits
echo 'hello123' | tr -cd '0-9'       # Keep only digits (complement delete)
echo 'hello' | tr '[:lower:]' '[:upper:]'  # Character classes
echo 'hello' | tr -c 'a-z' ' '       # Complement (split on non-lowercase)
tr -d '' < file.txt > file_unix.txt  # Convert CRLF to LF
cat /dev/urandom | tr -dc 'a-zA-Z0-9' | head -c 16  # Generate random string
```
- `-d`: Delete
- `-s`: Squeeze repeats
- `-c` or `-C`: Complement
- Character classes: `[:alnum:]`, `[:alpha:]`, `[:digit:]`, `[:lower:]`, `[:upper:]`, `[:space:]`, `[:punct:]`

## Recommended Unattended Usage

```bash
#!/bin/bash

# Clean input: remove non-printable, squeeze spaces
cleaned=$(echo "$input" | tr -cd '[:print:]' | tr -s ' ')

# Generate random password
tr -dc 'a-zA-Z0-9' < /dev/urandom | head -c 32
```
