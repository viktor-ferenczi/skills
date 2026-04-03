# uniq

**Platforms:** Linux, macOS
**Category:** Text Processing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show help | `uniq --help` |
| Show version | `uniq --version` |
| Remove duplicates | `uniq file` |
| Count occurrences | `uniq -c file` |
| Show duplicates | `uniq -d file` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `uniq` with output redirect | May overwrite files |
| Any uniq with output redirect | Creates/modifies files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe uniq Inspection Script

# Count occurrences
echo -e "a\na\nb" | uniq -c

# Show duplicates
echo -e "a\na\nb" | uniq -d
```
