# yq (YAML Processor)

**Platforms:** Multi-platform
**Category:** Text Processing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `yq --version` |
| Show help | `yq --help` |
| Read YAML | `yq eval ".key" file.yaml` |
| Show all | `yq eval "." file.yaml` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `yq eval -i` | In-place edit |
| `yq write` | Writes to file |
| `yq delete` | Deletes from file |
| Any yq with -i or write | Modifies files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe yq Inspection Script

# Read YAML
yq eval ".spec" file.yaml

# Show all
yq eval "." file.yaml
```
