# uniq

**Platforms:** Multi-platform  
**Category:** Text Processing

## Quick Reference

| Goal | Command |
|------|---------|
| Remove duplicates | `uniq file` |
| Count | `uniq -c file` |
| Only duplicates | `uniq -d file` |
| Only unique | `uniq -u file` |
| Skip fields | `uniq -f 1 file` |

## Command-Line Flags

```bash
uniq file                            # Remove adjacent duplicates
sort file | uniq                     # Remove all duplicates
sort file | uniq -c                  # Count occurrences
sort file | uniq -d                  # Show only duplicates
sort file | uniq -u                  # Show only unique lines
uniq -i file                         # Case-insensitive
uniq -s 5 file                       # Skip first 5 characters
uniq -w 10 file                      # Compare first 10 chars only
uniq -f 1 file                       # Skip first field
uniq --all-repeated=prepend file     # Mark all repeated lines
uniq --group                         # Group repeated lines
uniq --repeated                      # Same as -d
uniq --unique                        # Same as -u
sort file | uniq -c | sort -nr       # Frequency count (most first)
```
- `-c`: Count occurrences
- `-d`: Only duplicates
- `-u`: Only unique
- `-i`: Case-insensitive
- `-s`: Skip characters
- `-w`: Compare max characters
- `-f`: Skip fields
- `--all-repeated`: Mark repeats
- `--group`: Group repeats

## Recommended Unattended Usage

```bash
#!/bin/bash

# Count unique occurrences, sorted by frequency
sort file.txt | uniq -c | sort -nr

# Get truly unique lines (case-insensitive)
sort -f file.txt | uniq -i
```
