# fly (Fly.io CLI)

**Platforms:** Multi-platform
**Category:** Cloud Platform

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `fly version` |
| Show help | `fly --help` |
| List apps | `fly apps list` |
| Get app | `fly apps info` |
| List regions | `fly platform regions` |
| Show status | `fly status` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `fly launch` | Creates new app |
| `fly deploy` | Deploys app |
| `fly destroy` | Destroys app |
| `fly scale` | Scales resources |
| `fly secrets set` | Sets secrets |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe fly Inspection Script

# Show version
fly version

# List apps
fly apps list

# Show status
fly status
```
