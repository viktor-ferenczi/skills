# head

**Platforms:** Multi-platform  
**Category:** Text Processing

## Quick Reference

| Goal | Command |
|------|---------|
| First 10 lines | `head file` |
| First N lines | `head -n 20 file` |
| First N bytes | `head -c 100 file` |
| Multiple files | `head file1 file2` |

## Command-Line Flags

```bash
head file                            # First 10 lines
head -n 5 file                       # First 5 lines
head -5 file                         # First 5 lines (legacy)
head -n -5 file                      # All except last 5 lines
head -c 100 file                     # First 100 bytes
head -c 1k file                      # First 1KB
head -c 1M file                      # First 1MB
head -q file1 file2                  # No headers
head -v file                         # Always show header
head -z file                         # Null-terminated lines
head file1 file2                     # Multiple files
head -n 5 file1 file2                # 5 lines from each
```
- `-n`: Number of lines
- `-c`: Number of bytes
- `-q` or `--quiet`: No filename headers
- `-v` or `--verbose`: Always show filename
- `-z` or `--zero-terminated`: Null-terminated
