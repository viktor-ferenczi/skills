# patch

**Platforms:** Multi-platform  
**Category:** File Patching

## Quick Reference

| Goal | Command |
|------|---------|
| Force (no prompts) | `patch -f < file.patch` |
| Batch mode | `patch -t < file.patch` |
| Dry run | `patch --dry-run < file.patch` |

## Command-Line Flags

```bash
patch --dry-run < file.patch         # Test without applying
patch -f < file.patch                # Force (no prompts)
patch -t < file.patch                # Batch mode (assume -f)
patch -N < file.patch                # Ignore previously applied
```
- `-f` or `--force`: Force (no prompts)
- `-t` or `--batch`: Similar to -f (batch/non-interactive)
- `-N` or `--forward`: Ignore reversed/applied patches
- `--dry-run`: Test without applying

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
