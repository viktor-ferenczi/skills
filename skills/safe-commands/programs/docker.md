# docker

**Platforms:** Multi-platform
**Category:** Container & Orchestration

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List running containers | `docker ps` |
| List all containers | `docker ps -a` |
| List images | `docker images` |
| Container details | `docker inspect <container>` |
| View logs | `docker logs <container>` |
| Container stats | `docker stats --no-stream` |
| List networks | `docker network ls` |
| List volumes | `docker volume ls` |
| Image history | `docker history <image>` |
| Container processes | `docker top <container>` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `docker run` | Creates new containers |
| `docker start` | Starts stopped containers |
| `docker stop/kill` | Stops running containers |
| `docker rm` | Deletes containers |
| `docker rmi` | Deletes images |
| `docker build` | Builds new images |
| `docker commit` | Creates new images |
| `docker exec` | Executes commands in container |
| `docker system prune` | Deletes unused data |

## Environment Variables for Safe Operation

| Variable | Description |
|----------|-------------|
| `DOCKER_HOST` | Docker daemon socket |
| `DOCKER_TLS_VERIFY` | Enable TLS verification |
| `DOCKER_CERT_PATH` | Certificate path |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe Docker Inspection Script

echo "=== Running Containers ==="
docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}"

echo "=== All Containers ==="
docker ps -a --format "table {{.ID}}\t{{.Image}}\t{{.Status}}"

echo "=== Images ==="
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

echo "=== Container Details ==="
for container in $(docker ps -q --format '{{.Names}}'); do
    echo "--- $container ---"
    docker inspect --format '{{.State.Status}}: {{.State.Health.Status}}' $container 2>/dev/null || echo "No health check"
done

echo "=== Recent Logs (last 50 lines) ==="
docker logs --tail 50 $(docker ps -q | head -1) 2>/dev/null
```
