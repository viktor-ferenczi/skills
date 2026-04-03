# docker-compose

**Platforms:** Multi-platform
**Category:** Container & Orchestration

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List services | `docker-compose ls` |
| Config render | `docker-compose config` |
| List images | `docker-compose images` |
| Show processes | `docker-compose ps` |
| Show ports | `docker-compose port service` |
| Show version | `docker-compose --version` |
| Show help | `docker-compose --help` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `docker-compose up` | Starts containers |
| `docker-compose down` | Stops/removes containers |
| `docker-compose start` | Starts containers |
| `docker-compose stop` | Stops containers |
| `docker-compose restart` | Restart containers |
| `docker-compose kill` | Kills containers |
| `docker-compose rm` | Removes containers |
| `docker-compose build` | Builds images |
| `docker-compose exec` | Executes in container |
| `docker-compose run` | Runs new container |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe docker-compose Inspection Script

# List compose projects
docker-compose ls

# Render config (dry-run)
docker-compose config

# List images
docker-compose images

# Show processes
docker-compose ps

# Show specific port
docker-compose port web 80
```
