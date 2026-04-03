# nomad (HashiCorp)

**Platforms:** Multi-platform
**Category:** Orchestration

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `nomad version` |
| Show help | `nomad --help` |
| List jobs | `nomad job status` |
| Get job | `nomad job status job-name` |
| List nodes | `nomad node status` |
| List allocations | `nomad allocation status` |
| Show config | `nomad operator config` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `nomad job run` | Deploys jobs |
| `nomad job stop` | Stops jobs |
| `nomad job scale` | Scales jobs |
| `nomad node drain` | Drains nodes |
| `nomad job restart` | Restarts jobs |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe nomad Inspection Script

# List jobs
nomad job status

# List nodes
nomad node status
```
