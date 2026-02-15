# sort

**Platforms:** Multi-platform  
**Category:** Text Processing

## Quick Reference

| Goal | Command |
|------|---------|
| Sort | `sort file` |
| Reverse | `sort -r file` |
| Numeric | `sort -n file` |
| Unique | `sort -u file` |
| By field | `sort -k2 file` |

## Command-Line Flags

```bash
sort file                            # Sort alphabetically
sort -r file                         # Reverse sort
sort -n file                         # Numeric sort
sort -nr file                        # Numeric reverse
sort -u file                         # Unique (after sorting)
sort -k2 file                        # Sort by field 2
sort -k2,2 file                      # Sort by field 2 only
sort -k2n file                       # Numeric sort by field 2
sort -t',' -k2 file                  # Comma delimiter, sort by field 2
sort -f file                         # Case-insensitive
sort -M file                         # Month sort
sort -h file                         # Human numeric (K, M, G)
sort -V file                         # Version sort
sort -R file                         # Random sort
sort -m file1 file2                  # Merge sorted files
sort -o output.txt file              # Output to file
sort -S 1G file                      # Use 1GB memory
sort --parallel=4 file               # Parallel sort
sort -c file                         # Check if sorted
sort -C file                         # Check, no output
sort -b file                         # Ignore leading blanks
sort -d file                         # Dictionary order
```
- `-r`: Reverse
- `-n`: Numeric
- `-u`: Unique
- `-k`: Key/field
- `-t`: Delimiter
- `-f`: Case-insensitive
- `-M`: Month names
- `-h`: Human-readable sizes
- `-V`: Version numbers
- `-R`: Random
- `-m`: Merge
- `-o`: Output file
- `-S`: Buffer size
- `--parallel`: Parallel threads
- `-c`/`-C`: Check if sorted
- `-b`: Ignore leading blanks
- `-d`: Dictionary order
