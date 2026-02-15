# grep

**Platforms:** Multi-platform  
**Category:** Text Search

## Quick Reference

| Goal | Command |
|------|---------|
| Search | `grep pattern file` |
| Quiet | `grep -q pattern file` |
| Count | `grep -c pattern file` |
| Invert | `grep -v pattern file` |

## Command-Line Flags

```bash
grep pattern file                    # Search file
grep -r pattern dir/                 # Recursive
grep -i pattern file                 # Case-insensitive
grep -v pattern file                 # Invert match
grep -c pattern file                 # Count matches
grep -n pattern file                 # Show line numbers
grep -l pattern file*                # Show only filenames
grep -L pattern file*                # Show non-matching filenames
grep -q pattern file                 # Quiet (exit 0 if found)
grep -w pattern file                 # Whole word
grep -x pattern file                 # Whole line
grep -E pattern file                 # Extended regex
grep -F pattern file                 # Fixed strings
grep -o pattern file                 # Only matching part
grep --color=never pattern file      # No colors
grep -h pattern file                 # No filename
grep -H pattern file                 # With filename
grep -m 5 pattern file               # Max 5 matches
grep -A 3 pattern file               # 3 lines after
grep -B 3 pattern file               # 3 lines before
grep -C 3 pattern file               # 3 lines context
grep -f patterns.txt file            # Patterns from file
grep -e pattern1 -e pattern2 file    # Multiple patterns
grep -Z pattern file | xargs -0      # Null-terminated
grep -P pattern file                 # Perl regex
```
- `-r` or `-R`: Recursive
- `-i`: Case-insensitive
- `-v`: Invert match
- `-c`: Count
- `-n`: Line numbers
- `-l`: Files with matches
- `-L`: Files without matches
- `-q`: Quiet
- `-w`: Whole word
- `-x`: Whole line
- `-E`: Extended regex
- `-F`: Fixed strings
- `-o`: Only matching
- `--color`: Color output
- `-h`/`-H`: Filename control
- `-m`: Max count
- `-A`/`-B`/`-C`: Context lines
- `-f`: Pattern file
- `-e`: Multiple patterns
- `-Z`: Null-terminated output
- `-P`: Perl-compatible regex
