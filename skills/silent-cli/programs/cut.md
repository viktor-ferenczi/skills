# cut

**Platforms:** Multi-platform  
**Category:** Text Processing

## Quick Reference

| Goal | Command |
|------|---------|
| By field | `cut -f1,3 file` |
| By character | `cut -c1-10 file` |
| By byte | `cut -b1-10 file` |
| Custom delimiter | `cut -d',' -f2 file` |

## Command-Line Flags

```bash
cut -f1 file                         # Field 1 (tab-delimited)
cut -f1,3 file                       # Fields 1 and 3
cut -f1-3 file                       # Fields 1-3
cut -f1,3-5 file                     # Fields 1, 3, 4, 5
cut -d',' -f2 file                   # Field 2 (comma-delimited)
cut -d':' -f1 /etc/passwd            # First field of passwd
cut -c1-10 file                      # Characters 1-10
cut -c1,3,5 file                     # Characters 1, 3, 5
cut -c-10 file                       # First 10 characters
cut -c10- file                       # From character 10
cut -b1-10 file                      # Bytes 1-10
cut --complement -f1 file            # All except field 1
cut -s -f2 file                      # Skip lines without delimiter
cut --output-delimiter=' ' -f1,2 file  # Custom output delimiter
```
- `-f`: Fields (comma-separated or ranges)
- `-d`: Delimiter (default: tab)
- `-c`: Characters
- `-b`: Bytes
- `--complement`: Complement (inverse)
- `-s`: Skip lines without delimiter
- `--output-delimiter`: Output delimiter
