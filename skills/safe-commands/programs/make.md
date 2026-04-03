# make

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `make --version` |
| Show help | `make --help` |
| List targets | `make -n` (dry-run) |
| Show makefile | `make -p` |
| Dry-run | `make --dry-run` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `make` | Executes targets |
| `make all` | Builds project |
| `make install` | Installs files |
| `make clean` | Removes files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe make Inspection Script

# Dry-run
make -n

# Show makefile
make -p | head -50
```
