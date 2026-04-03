# diff

**Platforms:** Linux, macOS
**Category:** Text Processing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Compare files | `diff file1 file2` |
| Unified format | `diff -u file1 file2` |
| Context format | `diff -C 3 file1 file2` |
| Recursive | `diff -r dir1 dir2` |
| Ignore whitespace | `diff -w file1 file2` |
| Ignore case | `diff -i file1 file2` |
| Brief output | `diff -q file1 file2` |
| Side by side | `diff -y file1 file2` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `diff` piped to patch without review | May modify files |
| `diff -r` with write operations | May modify directories |
| Any diff output used for modification | Affects system state |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe diff Inspection Script

# Compare files
diff file1.txt file2.txt

# Unified format
diff -u config.old config.new

# Recursive (read-only)
diff -r /etc/old /etc/new

# Ignore whitespace
diff -w file1.txt file2.txt

# Brief output
diff -q file1.txt file2.txt
```
