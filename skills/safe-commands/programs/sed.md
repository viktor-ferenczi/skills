# sed

**Platforms:** Linux, macOS
**Category:** Text Processing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `sed --version` |
| Show help | `sed --help` |
| Print lines | `sed -n '1,10p' file` |
| Search | `sed -n '/pattern/p' file` |
| Substitute (stdout) | `sed 's/old/new/g' file` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `sed -i` | In-place edit |
| `sed -i.bak` | Creates backup + edits |
| Any sed with -i | Modifies files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe sed Inspection Script

# Print first 10 lines
sed -n '1,10p' file.txt

# Search pattern
sed -n '/error/p' file.txt

# Substitute (to stdout only)
sed 's/old/new/g' file.txt
```
