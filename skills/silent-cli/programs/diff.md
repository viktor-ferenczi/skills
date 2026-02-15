# diff

**Platforms:** Multi-platform  
**Category:** File Comparison

## Quick Reference

| Goal | Command |
|------|---------|
| Compare files | `diff file1 file2` |
| Unified format | `diff -u file1 file2` |
| Quiet check | `diff -q file1 file2` |
| Recursive dirs | `diff -ru dir1 dir2` |

## Command-Line Flags

```bash
diff file1 file2                     # Default format
diff -u file1 file2                  # Unified format (patch)
diff -c file1 file2                  # Context format
diff -q file1 file2                  # Quiet (exit code only)
diff -ru dir1 dir2                   # Recursive unified
diff -rN dir1 dir2                   # Treat missing as empty
diff --ignore-all-space file1 file2  # Ignore whitespace
diff -i file1 file2                  # Case insensitive
diff -w file1 file2                  # Ignore all whitespace
```
- `-u` or `-U NUM`: Unified format (NUM lines context)
- `-c` or `-C NUM`: Context format
- `-q` or `--brief`: Report only if files differ
- `-r` or `--recursive`: Recursive directories
- `-N` or `--new-file`: Treat missing files as empty
- `-i` or `--ignore-case`: Case insensitive
- `-w` or `--ignore-all-space`: Ignore all whitespace
- `-b` or `--ignore-space-change`: Ignore space changes
- `-B` or `--ignore-blank-lines`: Ignore blank lines
- `--strip-trailing-cr`: Strip trailing CR
