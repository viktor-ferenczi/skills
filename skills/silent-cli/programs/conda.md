# conda

**Platforms:** Multi-platform  
**Category:** Package/Environment Manager

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet install | `conda install -q package` |
| Yes to all | `conda install -y package` |
| Silent | `conda install -qy package` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `CONDA_ALWAYS_YES` | `true` | Auto-confirm (equivalent to -y) |
| `CONDA_QUIET` | `true` | Quiet mode (equivalent to -q) |

## Command-Line Flags

```bash
conda install -qy package            # Quiet, yes
conda install --quiet --yes package  # Same
conda create -qy -n envname python   # Create env quietly
conda activate envname               # Activate (no quiet)
conda list -q                        # Quiet list
conda env list -q                    # List envs quietly
conda update -qy conda               # Update conda quietly
conda remove -qy package             # Remove quietly
conda search -q package              # Search quietly
```
- `-q` or `--quiet`: Quiet
- `-y` or `--yes`: Auto-confirm
- `-c` or `--channel`: Channel
- `-n` or `--name`: Environment name
- `-p` or `--prefix`: Environment prefix
- `--offline`: Offline mode

## Recommended Unattended Usage

```bash
#!/bin/bash

# Create and setup environment
conda create -qy -n myenv python=3.11
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate myenv
conda install -qy numpy pandas
```
