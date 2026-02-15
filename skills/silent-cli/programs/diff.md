# diff

**Platforms:** Multi-platform  
**Category:** File Comparison

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet check (exit code only) | `diff -q file1 file2` |

## Command-Line Flags

- `-q` or `--brief`: Report only whether files differ (exit code only, minimal output)

`diff` is inherently non-interactive. Use `-q` for silent operation where you only need to know if files differ (exit code 0 = same, 1 = different).

## Recommended Unattended Usage

```bash
#!/bin/bash

# Silent comparison — check exit code only
if diff -q file1 file2 >/dev/null 2>&1; then
    echo "Files are identical"
else
    echo "Files differ"
fi
```
