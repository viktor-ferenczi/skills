# awk

**Platforms:** Multi-platform  
**Category:** Text Processing

## Quick Reference

| Goal | Command |
|------|---------|
| Print column | `awk '{print $1}' file` |
| Filter | `awk '$3 > 100' file` |
| Sum | `awk '{sum+=$1} END {print sum}' file` |
| Quiet | `awk '...' file > /dev/null` |

## Command-Line Flags

```bash
awk '{print $1}' file                # Print first field
awk '{print $NF}' file               # Print last field
awk '{print $(NF-1)}' file           # Print second-to-last
awk '{print $1, $3}' file            # Print fields 1 and 3
awk -F: '{print $1}' /etc/passwd     # Custom delimiter
awk -F '[,:]' '{print $1}' file      # Multiple delimiters
awk '$3 > 100' file                  # Filter rows
awk '$3 == "test"' file              # String match
awk '$1 ~ /pattern/' file            # Pattern match
awk 'NR==5' file                     # Line 5
awk 'NR>=5 && NR<=10' file           # Lines 5-10
awk 'BEGIN {sum=0} {sum+=$1} END {print sum}' file
awk '{count[$1]++} END {for(i in count) print i, count[i]}' file
awk -v var=value '{print var}' file  # Pass variable
awk -f script.awk file               # Script file
awk 'NF' file                        # Skip empty lines
awk '!seen[$0]++' file               # Remove duplicates
awk '{gsub(/old/, "new"); print}' file  # Substitute
awk '{print $1 | "sort"}' file       # Pipe to command
awk 'BEGIN {OFS=","} {print $1, $2}' file  # Output separator
```
- `-F`: Field separator
- `-v`: Set variable
- `-f`: Script file
- `BEGIN`: Execute before processing
- `END`: Execute after processing
- `NR`: Line number
- `NF`: Number of fields
- `OFS`: Output field separator

## Recommended Unattended Usage

```bash
#!/bin/bash

# Parse CSV, get column 3 where column 1 matches
awk -F, '$1 == "key" {print $3}' data.csv

# Sum values in column 2
total=$(awk '{sum+=$2} END {print sum}' data.txt)
```
