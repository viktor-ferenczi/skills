# docker-compose

**Platforms:** Multi-platform  
**Category:** Container Orchestration

## Quick Reference

| Goal | Command |
|------|---------|
| Detached (background) | `docker-compose up -d` |
| Quiet pull | `docker-compose pull -q` |
| No color | `docker-compose --no-ansi up` |
| Quiet build | `docker-compose build -q` |

## Command-Line Flags

- `-d` or `--detach`: Detached mode (run in background, no interactive output)
- `-q` or `--quiet`: Suppress pull/build output
- `--no-color`: Disable color output
- `--quiet-pull`: Suppress progress output during image pulls

## Recommended Unattended Usage

```bash
#!/bin/bash

# Pull and start in background, no progress output
docker-compose pull -q
docker-compose up -d --quiet-pull --no-color
```
