# gzip / gunzip / zcat

**Platforms:** Multi-platform  
**Category:** Compression

## Quick Reference

| Goal | Command |
|------|---------|
| Compress | `gzip file` |
| Decompress | `gunzip file.gz` |
| Keep original | `gzip -k file` |
| To stdout | `zcat file.gz > output` |

## Command-Line Flags

```bash
gzip file                    # Compress (replaces file)
gzip -k file                 # Compress, keep original
gzip -c file > file.gz       # Compress to stdout
gunzip file.gz               # Decompress
gunzip -c file.gz            # Decompress to stdout
zcat file.gz                 # Same as gunzip -c
```
- `-k` or `--keep`: Keep input files
- `-c` or `--stdout`: Write to stdout
- `-d` or `--decompress`: Decompress
- `-f` or `--force`: Force overwrite
- `-t` or `--test`: Test integrity
- `-v` or `--verbose`: Verbose
- `-1` to `-9`: Compression level (1=fast, 9=best)
- `-q` or `--quiet`: Quiet
