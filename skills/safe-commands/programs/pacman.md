# pacman

**Platforms:** Linux (Arch)
**Category:** Package Management

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `pacman --version` |
| Show help | `pacman --help` |
| List installed | `pacman -Q` |
| Search packages | `pacman -Ss name` |
| Show package info | `pacman -Si package` |
| List files | `pacman -Ql package` |
| Check upgrades | `pacman -Qu` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `pacman -S` | Installs packages |
| `pacman -R` | Removes packages |
| `pacman -Syu` | Upgrades system |
| `pacman -Sc` | Cleans cache |
| `pacman -Scc` | Deep clean |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe pacman Inspection Script

# List installed
pacman -Q | head -20

# Search packages
pacman -Ss firefox

# Check upgrades
pacman -Qu
```
