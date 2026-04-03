# vagrant

**Platforms:** Multi-platform
**Category:** Virtualization

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `vagrant --version` |
| Show help | `vagrant --help` |
| List boxes | `vagrant box list` |
| Status | `vagrant status` |
| Global status | `vagrant global-status` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `vagrant up` | Starts VMs |
| `vagrant destroy` | Destroys VMs |
| `vagrant halt` | Stops VMs |
| `vagrant reload` | Reloads VMs |
| `vagrant box add` | Adds boxes |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe vagrant Inspection Script

# List boxes
vagrant box list

# Show status
vagrant status
```
