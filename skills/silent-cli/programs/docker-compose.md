# docker-compose

**Platforms:** Multi-platform  
**Category:** Container Orchestration

## Quick Reference

| Goal | Command |
|------|---------|
| Detached | `docker-compose up -d` |
| Quiet pull | `docker-compose pull -q` |
| No color | `docker-compose --no-ansi up` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `COMPOSE_PARALLEL_LIMIT` | `4` | Parallel limit |
| `COMPOSE_PROJECT_NAME` | `myproject` | Project name |
| `COMPOSE_FILE` | `docker-compose.yml` | Compose file |

## Command-Line Flags

```bash
docker-compose up -d                 # Detached
docker-compose up -d --quiet-pull    # Quiet image pulls
docker-compose up -d --no-color      # No color
docker-compose build -q              # Quiet build
docker-compose pull -q               # Quiet pull
docker-compose ps                    # List containers
docker-compose logs -f               # Follow logs
docker-compose down                  # Stop and remove
docker-compose down -v               # Remove volumes too
```
- `-d` or `--detach`: Detached mode
- `-q` or `--quiet`: Quiet
- `--no-color`: No color
- `--quiet-pull`: No progress on pull
- `-f` or `--file`: Compose file
- `-p` or `--project-name`: Project name
- `-v`: Remove volumes (with down)
