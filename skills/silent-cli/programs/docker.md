# docker

**Platforms:** Multi-platform  
**Category:** Container Runtime

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet build | `docker build -q -t image .` |
| Silent run | `docker run -d --rm image` |
| No progress | `docker pull -q image` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `DOCKER_BUILDKIT` | `1` | Use BuildKit |
| `BUILDKIT_PROGRESS` | `plain` | Plain progress |
| `DOCKER_CLI_EXPERIMENTAL` | `enabled` | Enable experimental |

## Command-Line Flags

```bash
docker build -q -t image .           # Quiet build
docker build --quiet -t image .      # Same
docker build --progress=plain -t image .  # Plain progress
docker pull -q image                 # Quiet pull
docker push -q image                 # Quiet push
docker run -d --rm image             # Detached, auto-remove
docker run --log-driver none image   # No logging
docker images -q                     # Quiet list (IDs only)
docker ps -q                         # Quiet list
docker rm -f container               # Force remove
docker system prune -f               # Force prune
```
- `-q` or `--quiet`: Quiet (image ID only)
- `--quiet`: Suppress build output
- `--progress=auto|plain|tty`: Progress output
- `-d` or `--detach`: Run in background
- `--rm`: Auto-remove on stop
- `--log-driver`: Logging driver
- `-f` or `--force`: Force

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
