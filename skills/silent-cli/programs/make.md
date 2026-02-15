# make

**Platforms:** Multi-platform  
**Category:** Build Automation

## Quick Reference

| Goal | Command |
|------|---------|
| Silent | `make -s` |
| No colors | `make --no-print-directory` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `MAKEFLAGS` | `-s` | Default flags |

## Command-Line Flags

```bash
make -s                              # Silent (no commands echoed)
make --silent                        # Silent
make V=0                             # Silent (common convention)
make V=1                             # Verbose (common convention)
```
- `-s` or `--silent`: Silent

## Recommended Unattended Usage

```bash
#!/bin/bash

# Silent parallel build
make -s -j$(nproc)

# Or with environment
MAKEFLAGS="-s -j$(nproc)" make
```
