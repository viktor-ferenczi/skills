# pip

**Platforms:** Multi-platform  
**Category:** Package Manager (Python)

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet install | `pip install -q package` |
| No prompts | `pip install --no-input package` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `PIP_NO_INPUT` | `1` | Disable prompt input |
| `PIP_QUIET` | `1` | Quiet mode |
| `PIP_DISABLE_PIP_VERSION_CHECK` | `1` | Skip version check |

## Command-Line Flags

```bash
pip install -q package               # Quiet
pip install --quiet package          # Quiet
pip install --no-input package       # No prompts
pip uninstall -q -y package          # Uninstall quietly (auto-confirm)
```
- `-q` or `--quiet`: Quiet (can use multiple times)
- `--no-input`: Disable prompting
- `-y`: Auto-confirm uninstall
- `--disable-pip-version-check`: Skip version check
- `--no-color`: Disable colors

## Recommended Unattended Usage

```bash
#!/bin/bash

export PIP_NO_INPUT=1
export PIP_QUIET=1
export PIP_DISABLE_PIP_VERSION_CHECK=1

pip install -r requirements.txt
pip install --no-deps --quiet package
```
