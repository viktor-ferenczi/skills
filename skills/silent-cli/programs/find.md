# find

**Platforms:** Multi-platform  
**Category:** File Search

## Quick Reference

| Goal | Command |
|------|---------|
| Find files | `find . -name '*.txt'` |
| Silent | `find . -name '*.txt' 2>/dev/null` |
| Execute | `find . -name '*.log' -delete` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `POSIXLY_CORRECT` | `1` | POSIX behavior |

## Command-Line Flags

```bash
find . -name '*.txt'                    # By name
find . -type f -name '*.log'            # Files only
find . -type d -name 'node_modules'     # Directories
find . -mtime +7 -delete                # Delete old files
find . -exec rm {} \;                   # Execute on each
find . -print0 | xargs -0 rm            # Safe for spaces
```
- `-name`: Name pattern
- `-type`: f=file, d=directory
- `-mtime`: Modified time (days)
- `-exec`: Execute command
- `-delete`: Delete files
- `-print0`: Null-terminated output
