# conda

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `conda --version` |
| Show info | `conda info` |
| List envs | `conda env list` |
| Show config | `conda config --show` |
| Search packages | `conda search name` |
| List packages | `conda list` |
| Show package | `conda search --name` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `conda install` | Installs packages |
| `conda update` | Updates packages |
| `conda create` | Creates environments |
| `conda remove` | Removes packages |
| `conda env create` | Creates env |
| `conda env delete` | Deletes env |
| `conda config --add` | Modifies config |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe conda Inspection Script

# Show version
conda --version

# Show info
conda info

# List environments
conda env list

# Show config
conda config --show
```
