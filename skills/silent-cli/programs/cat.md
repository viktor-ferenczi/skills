# cat

**Platforms:** Multi-platform  
**Category:** File Display

## Quick Reference

| Goal | Command |
|------|---------|
| Display file | `cat file` |
| Concatenate | `cat file1 file2 > combined` |
| Number lines | `cat -n file` |

## Command-Line Flags

```bash
cat file                            # Display file
cat file1 file2                     # Concatenate
cat file1 file2 > output            # Concatenate to file
cat -n file                         # Number all lines
cat -b file                         # Number non-empty lines
cat -s file                         # Squeeze blank lines
cat -A file                         # Show all non-printing
cat -E file                         # Show $ at end of lines
cat -T file                         # Show tabs as ^I
cat -v file                         # Show non-printing (except tabs/LF)
```
- `-n` or `--number`: Number all lines
- `-b` or `--number-nonblank`: Number non-empty lines
- `-s` or `--squeeze-blank`: Squeeze multiple blank lines
- `-A` or `--show-all`: Show all non-printing
- `-E` or `--show-ends`: Show $ at line ends
- `-T` or `--show-tabs`: Show tabs as ^I
- `-v` or `--show-nonprinting`: Show non-printing
