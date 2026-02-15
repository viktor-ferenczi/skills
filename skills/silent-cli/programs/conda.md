# conda

**Platforms:** Multi-platform  
**Category:** Package/Environment Manager

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `conda install -qy package` |
| Auto-confirm | `conda install -y package` |
| Quiet mode | `conda install -q package` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `CONDA_ALWAYS_YES` | `true` | Auto-confirm all prompts (equivalent to `-y`) |
| `CONDA_QUIET` | `true` | Quiet mode (equivalent to `-q`) |

## Command-Line Flags

- `-q` or `--quiet`: Quiet mode — suppress output
- `-y` or `--yes`: Auto-confirm all prompts

## Recommended Unattended Usage

```bash
#!/bin/bash

# Create and setup environment
conda create -qy -n myenv python=3.11
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate myenv
conda install -qy numpy pandas
```
