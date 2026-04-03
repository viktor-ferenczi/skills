# cmake

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `cmake --version` |
| Show help | `cmake --help` |
| Show manual | `cmake --help-manual` |
| List configs | `cmake -L` |
| Show cache | `cmake -LH` |
| Show system info | `cmake --system-information` |
| Show presets | `cmake --list-presets` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `cmake path` | Configures build |
| `cmake --build` | Builds project |
| `cmake --install` | Installs project |
| `cmake -E` | Removes cache |
| `cmake -U` | Unlinks cache |
| Any cmake configuration | Creates build files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe cmake Inspection Script

# Show version
cmake --version

# Show help
cmake --help

# List cache variables (read-only)
cmake -LH

# Show system info
cmake --system-information | head -50
```
