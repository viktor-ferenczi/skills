# uniq

**Platforms:** Multi-platform  
**Category:** Text Processing

## Recommended Unattended Usage

```bash
#!/bin/bash

# Count unique occurrences, sorted by frequency
sort file.txt | uniq -c | sort -nr

# Get truly unique lines (case-insensitive)
sort -f file.txt | uniq -i
```
