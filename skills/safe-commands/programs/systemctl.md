# systemctl

**Platforms:** Linux
**Category:** System Administration

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List units | `systemctl list-units` |
| Show status | `systemctl status service` |
| List failed | `systemctl --failed` |
| Show host | `systemctl show-host` |
| List timers | `systemctl list-timers` |
| Show service | `systemctl show service` |
| Is enabled | `systemctl is-enabled service` |
| Is active | `systemctl is-active service` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `systemctl start` | Starts services |
| `systemctl stop` | Stops services |
| `systemctl restart` | Restart services |
| `systemctl reload` | Reloads services |
| `systemctl enable` | Enables services |
| `systemctl disable` | Disables services |
| `systemctl mask` | Masks services |
| `systemctl unmask` | Unmasks services |
| `systemctl isolate` | Changes target |
| `systemctl poweroff` | Powers off system |
| `systemctl reboot` | Reboots system |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe systemctl Inspection Script

# List all units
systemctl list-units | head -30

# Show service status
systemctl status nginx

# List failed units
systemctl --failed

# List timers
systemctl list-timers

# Check if enabled
systemctl is-enabled nginx

# Check if active
systemctl is-active nginx
```
