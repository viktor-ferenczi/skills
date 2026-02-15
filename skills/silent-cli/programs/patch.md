# patch

**Platforms:** Multi-platform  
**Category:** File Patching

## Quick Reference

| Goal | Command |
|------|---------|
| Apply patch | `patch < file.patch` |
| Apply to file | `patch file file.patch` |
| Dry run | `patch --dry-run < file.patch` |
| Reverse | `patch -R < file.patch` |

## Command-Line Flags

```bash
patch < file.patch                   # Apply patch from stdin
patch -p1 < file.patch               # Strip first path component
patch -p0 < file.patch               # Don't strip paths
patch file file.patch                # Apply to specific file
patch --dry-run < file.patch         # Test without applying
patch -R < file.patch                # Reverse patch
patch -f < file.patch                # Force (no prompts)
patch -t < file.patch                # Batch mode (assume -f)
patch -N < file.patch                # Ignore previously applied
```
- `-p NUM` or `--strip=NUM`: Strip NUM leading path components
- `-R` or `--reverse`: Reverse patch
- `-f` or `--force`: Force (no prompts)
- `-t` or `--batch`: Similar to -f
- `-N` or `--forward`: Ignore reversed/applied patches
- `--dry-run`: Test without applying
- `-i FILE` or `--input=FILE`: Read patch from file
- `-d DIR` or `--directory=DIR`: Change directory first

## Recommended Unattended Usage

```bash
#!/bin/bash

# Apply patch safely
if patch --dry-run -p1 < fix.patch > /dev/null 2>&1; then
    patch -p1 < fix.patch
else
    echo "Patch cannot be applied"
    exit 1
fi

# Force apply
patch -f -p1 < fix.patch
```
