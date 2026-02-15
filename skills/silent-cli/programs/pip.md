# pip

**Platforms:** Multi-platform  
**Category:** Package Manager (Python)

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet install | `pip install -q package` |
| No progress | `pip install --no-input package` |
| Requirements | `pip install -q -r requirements.txt` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `PIP_NO_INPUT` | `1` | Disable prompt input |
| `PIP_QUIET` | `1` | Quiet mode |
| `PIP_DISABLE_PIP_VERSION_CHECK` | `1` | Skip version check |
| `PIP_INDEX_URL` | `https://...` | Package index |

## Command-Line Flags

```bash
pip install -q package               # Quiet
pip install --quiet package          # Quiet
pip install --no-input package       # No prompts
pip install -q -r requirements.txt   # Install from requirements
pip install -q --no-deps package     # No dependencies
pip install -q --upgrade package     # Upgrade
pip list -q                          # Quiet list
pip freeze -q                        # Quiet freeze
pip uninstall -q -y package          # Uninstall quietly
```
- `-q` or `--quiet`: Quiet (can use multiple times)
- `--no-input`: Disable prompting
- `-r` or `--requirement`: Requirements file
- `--no-deps`: Don't install dependencies
- `-U` or `--upgrade`: Upgrade
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
