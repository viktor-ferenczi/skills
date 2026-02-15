# xz / unxz / xzcat

**Platforms:** Multi-platform  
**Category:** Compression

## Quick Reference

| Goal | Command |
|------|---------|
| Compress | `xz file` |
| Decompress | `unxz file.xz` |
| Keep original | `xz -k file` |
| To stdout | `xzcat file.xz` |

## Command-Line Flags

```bash
xz file                      # Compress (replaces file)
xz -k file                   # Keep original
xz -c file > file.xz         # Compress to stdout
unxz file.xz                 # Decompress
xzcat file.xz                # Decompress to stdout
```
- `-k` or `--keep`: Keep input files
- `-c` or `--stdout`: Write to stdout
- `-d` or `--decompress`: Decompress
- `-f` or `--force`: Force overwrite
- `-t` or `--test`: Test integrity
- `-v` or `--verbose`: Verbose
- `-0` to `-9`: Compression level
- `-e` or `--extreme`: Extreme compression
- `-T N` or `--threads=N`: Multithreading
- `-q` or `--quiet`: Quiet
