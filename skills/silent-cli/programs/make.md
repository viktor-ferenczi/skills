# make

**Platforms:** Multi-platform  
**Category:** Build Automation

## Quick Reference

| Goal | Command |
|------|---------|
| Build | `make` |
| Silent | `make -s` |
| No colors | `make --no-print-directory` |
| Parallel | `make -j4` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `MAKEFLAGS` | `-s` | Default flags |

## Command-Line Flags

```bash
make                                 # Build default target
make all                             # Build all
make target                          # Build specific target
make -s                              # Silent (no commands echoed)
make --silent                        # Silent
make -n                              # Dry run (print commands)
make --just-print                    # Dry run
make -j4                             # 4 parallel jobs
make -j$(nproc)                      # Use all CPUs
make -k                              # Keep going on errors
make --keep-going                    # Keep going
make -B                              # Always build (unconditional)
make --always-make                   # Always build
make -f Makefile.custom              # Use custom makefile
make -C /path/to/dir                 # Change directory
make -e                              # Environment overrides makefile
make --environment-overrides         # Environment overrides
make V=0                             # Silent (common convention)
make V=1                             # Verbose (common convention)
make clean                           # Clean target
make install                         # Install target
make uninstall                       # Uninstall target
```
- `-s` or `--silent`: Silent
- `-n` or `--just-print`: Dry run
- `-j`: Parallel jobs
- `-k` or `--keep-going`: Continue on errors
- `-B` or `--always-make`: Unconditional
- `-f`: Makefile name
- `-C`: Change directory
- `-e` or `--environment-overrides`: Environment overrides vars

## Recommended Unattended Usage

```bash
#!/bin/bash

# Silent parallel build
make -s -j$(nproc)

# Or with environment
MAKEFLAGS="-s -j$(nproc)" make
```
