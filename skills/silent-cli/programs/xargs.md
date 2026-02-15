# xargs

**Platforms:** Multi-platform  
**Category:** Command Building

## Command-Line Flags

- `--no-run-if-empty`: Skip if empty input (safe for automation)
- `-0` or `--null`: Null delimiter (safe for filenames with spaces)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Safe file processing with null delimiter
find . -name '*.log' -print0 | xargs -0 -I {} gzip {}

# Parallel processing
find . -name '*.jpg' -print0 | xargs -0 -P4 -I {} convert {} {}.png
```
