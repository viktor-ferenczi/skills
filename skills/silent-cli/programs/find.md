# find

**Platforms:** Multi-platform  
**Category:** File Search

## Quick Reference

| Goal | Command |
|------|---------|
| Suppress errors silently | `find . -name '*.txt' 2>/dev/null` |
| Null-terminated output | `find . -print0 \| xargs -0 cmd` |

## Command-Line Flags

- `-print0`: Null-terminated output (safe for filenames with spaces/special chars in pipelines)

`find` is inherently non-interactive. Redirect stderr (`2>/dev/null`) to suppress permission-denied errors in unattended scripts. Use `-print0` with `xargs -0` for safe automated processing of filenames.
