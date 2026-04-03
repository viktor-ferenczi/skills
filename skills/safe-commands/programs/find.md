# find

**Platforms:** Linux, macOS
**Category:** File Operations

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List files by name | `find . -name "*.txt"` |
| Find by type | `find . -type f` (files) or `-type d` (dirs) |
| Find by size | `find . -size +100M` |
| Find by date | `find . -mtime -7` (last 7 days) |
| Find empty files | `find . -empty` |
| Count files | `find . -type f | wc -l` |
| Find permissions | `find . -perm 644` |
| Find by owner | `find . -user username` |
| List with details | `find . -ls` |
| Find symlinks | `find . -type l` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `find . -delete` | Deletes files/directories |
| `find . -exec rm {} \;` | Deletes matched files |
| `find . -exec chmod {} \;` | Changes permissions |
| `find . -exec mv {} \;` | Moves files |
| `find . -prune -exec rm` | Dangerous prune patterns |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe find Inspection Script

# Find all files in current directory
find . -type f -name "*.log"

# Find large files (>100MB)
find . -type f -size +100M -ls

# Find recently modified (last 24 hours)
find . -type f -mmin -1440 -ls

# Find files by extension
find . -type f \( -name "*.conf" -o -name "*.cfg" \) -ls

# Count files by type
echo "Files: $(find . -type f | wc -l)"
echo "Directories: $(find . -type d | wc -l)"
echo "Symlinks: $(find . -type l | wc -l)"
```
