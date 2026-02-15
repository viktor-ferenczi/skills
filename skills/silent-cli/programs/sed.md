# sed

**Platforms:** Multi-platform  
**Category:** Stream Editor

## Quick Reference

| Goal | Command |
|------|---------|
| Replace | `sed 's/old/new/' file` |
| In-place | `sed -i 's/old/new/' file` |
| Quiet | `sed -n '5p' file` |
| Delete | `sed '3d' file` |

## Command-Line Flags

```bash
sed 's/old/new/' file                # Replace first occurrence per line
sed 's/old/new/g' file               # Replace all occurrences
sed 's/old/new/2' file               # Replace 2nd occurrence
sed 's/old/new/2g' file              # Replace from 2nd onward
sed -i 's/old/new/g' file            # Edit in-place
sed -i.bak 's/old/new/g' file        # Backup original
sed -n '5p' file                     # Print line 5 only
sed -n '5,10p' file                  # Print lines 5-10
sed '3d' file                        # Delete line 3
sed '3,5d' file                      # Delete lines 3-5
sed '/pattern/d' file                # Delete matching lines
sed -e 's/a/b/' -e 's/c/d/' file     # Multiple commands
sed -f script.sed file               # Script file
sed 's|/path|/newpath|' file         # Alternate delimiter
sed 's/old/new/I' file               # Case-insensitive
sed -r 's/(a)(b)/\2\1/' file         # Extended regex
sed -E 's/(a)(b)/\2\1/' file         # Extended regex (BSD)
sed '1i\New first line' file         # Insert at line 1
sed '$a\New last line' file          # Append after last
sed '/pattern/a\New line' file       # Append after pattern
sed -z 's/\n/ /g' file               # Multi-line (null-separated)
```
- `-i`: Edit in-place
- `-i.bak`: Edit in-place with backup
- `-n`: Quiet (no auto-print)
- `-e`: Multiple commands
- `-f`: Script file
- `-r` or `-E`: Extended regex
- `-z`: Null-separated (multi-line)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Safe in-place edit with backup
sed -i.bak 's/old/new/g' file.txt

# Quiet extraction
value=$(sed -n 's/^key=//p' config.txt)
```
