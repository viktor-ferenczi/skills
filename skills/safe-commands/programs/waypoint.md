# waypoint (HashiCorp)

**Platforms:** Multi-platform
**Category:** Deployment

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `waypoint --version` |
| Show help | `waypoint --help` |
| List projects | `waypoint project list` |
| List runs | `waypoint run list` |
| Show config | `waypoint config get` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `waypoint up` | Deploys application |
| `waypoint destroy` | Destroys deployment |
| `waypoint build` | Builds application |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe waypoint Inspection Script

# List projects
waypoint project list

# List runs
waypoint run list
```
