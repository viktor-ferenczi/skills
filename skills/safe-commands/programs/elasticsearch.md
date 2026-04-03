# elasticsearch (curl API)

**Platforms:** Multi-platform
**Category:** Database/Search

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Cluster health | `curl GET localhost:9200/_cluster/health` |
| List indices | `curl GET localhost:9200/_cat/indices` |
| Get doc | `curl GET localhost:9200/index/doc/id` |
| Search | `curl GET localhost:9200/index/_search` |
| Cluster stats | `curl GET localhost:9200/_cluster/stats` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `curl PUT/POST/DELETE` | Modifies data |
| `curl DELETE /index` | Deletes index |
| `curl PUT /index/doc` | Creates/updates docs |
| Any write operation | Modifies cluster state |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe elasticsearch Inspection Script

# Cluster health
curl -s localhost:9200/_cluster/health

# List indices
curl -s localhost:9200/_cat/indices

# Cluster stats
curl -s localhost:9200/_cluster/stats
```
