# grep

**Platforms:** Multi-platform  
**Category:** Text Search

## Quick Reference

| Goal | Command |
|------|---------|
| Silent check (exit code only) | `grep -q pattern file` |
| No color | `grep --color=never pattern file` |
| Count only | `grep -c pattern file` |
| Null-terminated output | `grep -Z pattern file \| xargs -0 cmd` |

## Command-Line Flags

- `-q` or `--quiet` or `--silent`: Suppress all output (exit code only — 0 if found, 1 if not)
- `--color=never`: Disable color output (prevents ANSI codes in piped/logged output)
- `-c`: Count matches only (numeric output)
- `-l`: Print only filenames with matches (machine-parseable)
- `-Z`: Null-terminated output (safe for filenames with spaces)

`grep` is inherently non-interactive. Use `-q` for silent existence checks in scripts, and `--color=never` when output is captured or logged.
