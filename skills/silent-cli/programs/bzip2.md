# bzip2 / bunzip2 / bzcat

**Platforms:** Multi-platform  
**Category:** Compression

## Quick Reference

| Goal | Command |
|------|---------|
| Compress | `bzip2 file` |
| Decompress | `bunzip2 file.bz2` |
| Keep original | `bzip2 -k file` |
| To stdout | `bzcat file.bz2` |

## Command-Line Flags

```bash
bzip2 file                   # Compress (replaces file)
bzip2 -k file                # Keep original
bzip2 -c file > file.bz2     # Compress to stdout
bunzip2 file.bz2             # Decompress
bzcat file.bz2               # Decompress to stdout
```
- `-k` or `--keep`: Keep input files
- `-c` or `--stdout`: Write to stdout
- `-d` or `--decompress`: Decompress
- `-f` or `--force`: Force overwrite
- `-t` or `--test`: Test integrity
- `-v` or `--verbose`: Verbose
- `-1` to `-9`: Compression level
- `-q` or `--quiet`: Quiet
