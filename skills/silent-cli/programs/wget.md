# wget

**Platforms:** Multi-platform  
**Category:** Data Transfer

## Quick Reference

| Goal | Command |
|------|---------|
| Silent download | `wget -q -O file url` |
| Quiet progress | `wget --progress=dot -O file url` |
| Continue partial | `wget -c -q url` |

## Command-Line Flags

- `-q` or `--quiet`: Quiet mode (no output)
- `--no-verbose`: Errors only
- `--progress=dot`: Dot-style progress (less noisy than bar)
- `-O -`: Output to stdout (for piping)
