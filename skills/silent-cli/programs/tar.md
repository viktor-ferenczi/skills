# tar

**Platforms:** Multi-platform  
**Category:** Archiving

## Quick Reference

| Goal | Command |
|------|---------|
| Silent extract | `tar -xf archive.tar` |
| Silent create | `tar -czf archive.tar.gz dir/` |
| List contents | `tar -tf archive.tar` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `TAPE` | `/dev/rst0` | Default tape device |

## Command-Line Flags

```bash
tar -xf archive.tar.gz -C /target          # Extract to directory
tar -czf archive.tar.gz -C /source .       # Create archive
tar -xjf archive.tar.bz2                   # Extract bz2
tar -xJf archive.tar.xz                    # Extract xz
```
- `-c`: Create
- `-x`: Extract
- `-t`: List
- `-f`: File
- `-z`: gzip
- `-j`: bzip2
- `-J`: xz
- `-C`: Change directory
- `-v`: Verbose (omit for silent)
