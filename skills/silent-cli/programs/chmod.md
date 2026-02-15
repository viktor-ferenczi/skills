# chmod / chown / chgrp

**Platforms:** Multi-platform  
**Category:** Permission Management

## Quick Reference

| Goal | Command |
|------|---------|
| Set permissions | `chmod 755 file` |
| Recursive | `chmod -R 755 dir/` |
| Change owner | `chown user:group file` |

## Command-Line Flags

### chmod
```bash
chmod 755 file                          # rwxr-xr-x
chmod u+x file                          # Add execute
chmod -R 755 dir/                       # Recursive
chmod -R g+w,o-w dir/                   # Group write, other no write
```
- `-R`: Recursive
- `-v`: Verbose
- `-c` or `--changes`: Like verbose but only on change
- `--reference=RFILE`: Copy mode from file

### chown
```bash
chown user file
chown user:group file
chown -R user:group dir/
chown --reference=file1 file2
```
- `-R`: Recursive
- `-v`: Verbose

### chgrp
```bash
chgrp group file
chgrp -R group dir/
```
