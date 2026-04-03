# kibana (curl API)

**Platforms:** Multi-platform
**Category:** Monitoring/Visualization

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Check status | `curl GET localhost:5601/api/status` |
| List indices | `curl GET localhost:5601/api/saved_objects/_find` |
| Get config | `curl GET localhost:5601/api/kibana/settings` |
| List spaces | `curl GET localhost:5601/api/spaces/space` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `curl PUT/POST/DELETE` | Modifies Kibana |
| `curl POST /api/saved_objects` | Creates objects |
| `curl DELETE /api/saved_objects` | Deletes objects |
| Any write operation | Modifies Kibana state |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe kibana Inspection Script

# Check status
curl -s localhost:5601/api/status

# List spaces
curl -s localhost:5601/api/spaces/space
```
