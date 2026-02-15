# wc

**Platforms:** Multi-platform  
**Category:** Text Statistics

## Quick Reference

| Goal | Command |
|------|---------|
| Count all | `wc file` |
| Lines | `wc -l file` |
| Words | `wc -w file` |
| Characters | `wc -c file` |

## Command-Line Flags

```bash
wc file                              # Lines, words, bytes
wc -l file                           # Lines only
wc -w file                           # Words only
wc -c file                           # Bytes only
wc -m file                           # Characters (multibyte aware)
wc -L file                           # Max line length
cat file | wc -l                     # Count lines from stdin
ls | wc -l                           # Count files
grep pattern file | wc -l            # Count matches
wc file1 file2                       # Multiple files
wc -l file1 file2                    # Line counts
wc --files0-from=list.txt            # File list (null-terminated)
```
- `-l`: Lines
- `-w`: Words
- `-c`: Bytes
- `-m`: Characters
- `-L`: Maximum line length
- `--files0-from`: Read file list
