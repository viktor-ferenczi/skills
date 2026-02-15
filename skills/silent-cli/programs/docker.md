# docker

**Platforms:** Multi-platform  
**Category:** Container Runtime

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet build | `docker build -q -t image .` |
| Silent run | `docker run -d --rm image` |
| No progress | `docker pull -q image` |
| Force prune (no prompt) | `docker system prune -f` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `BUILDKIT_PROGRESS` | `plain` | Plain progress output (no fancy TUI) |
| `DOCKER_BUILDKIT` | `1` | Use BuildKit (supports `--progress`) |

## Command-Line Flags

- `-q` or `--quiet`: Suppress output (returns image ID only for build, IDs only for list)
- `--progress=auto|plain|tty`: Control progress output type (`plain` for CI/scripts)
- `-d` or `--detach`: Run container in background (non-interactive)
- `--rm`: Auto-remove container on exit
- `-f` or `--force`: Force removal/prune without confirmation prompt

## Recommended Unattended Usage

```bash
#!/bin/bash

export DOCKER_BUILDKIT=1
export BUILDKIT_PROGRESS=plain

# Build quietly
image_id=$(docker build -q -t myapp:latest .)

# Run detached
docker run -d --name myapp --rm -p 8080:80 myapp:latest

# Wait for health
docker inspect --format='{{.State.Health.Status}}' myapp
```
