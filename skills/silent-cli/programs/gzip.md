# gzip / gunzip / zcat

**Platforms:** Multi-platform  
**Category:** Compression

## Command-Line Flags

- `-q` or `--quiet`: Quiet
- `-f` or `--force`: Force overwrite (no prompts)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Compress quietly, force overwrite existing
gzip -q -f file

# Decompress quietly, force overwrite
gunzip -q -f file.gz
```
