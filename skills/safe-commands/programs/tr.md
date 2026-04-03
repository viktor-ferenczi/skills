# tr

**Platforms:** Linux, macOS
**Category:** Text Processing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show help | `tr --help` |
| Show version | `tr --version` |
| Translate | `tr 'a-z' 'A-Z'` |
| Delete chars | `tr -d ' '` |
| Squeeze | `tr -s ' '` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `tr` with file redirect | May overwrite files |
| Any tr with output redirect | Creates/modifies files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe tr Inspection Script

# Translate to uppercase
echo "hello" | tr 'a-z' 'A-Z'

# Delete spaces
echo "hello world" | tr -d ' '
```
