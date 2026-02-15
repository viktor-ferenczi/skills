# systemctl

**Platforms:** Linux (systemd)  
**Category:** Service Management

## Quick Reference

| Goal | Command |
|------|---------|
| Status | `systemctl status service` |
| Start | `systemctl start service` |
| Enable | `systemctl enable service` |
| List | `systemctl list-units` |

## Command-Line Flags

```bash
systemctl status service             # Service status
systemctl start service              # Start service
systemctl stop service               # Stop service
systemctl restart service            # Restart service
systemctl reload service             # Reload config
systemctl enable service             # Enable on boot
systemctl disable service            # Disable on boot
systemctl is-active service          # Check if active (returns exit code)
systemctl is-enabled service         # Check if enabled
systemctl is-failed service          # Check if failed
systemctl list-units                 # List active units
systemctl list-units --type=service  # List services only
systemctl list-unit-files            # List unit files
systemctl --failed                   # List failed units
systemctl daemon-reload              # Reload systemd
systemctl show service               # Show properties
systemctl cat service                # Show unit file
systemctl edit service               # Edit unit file
systemctl edit --full service        # Full edit
systemctl mask service               # Mask unit
systemctl unmask service             # Unmask unit
systemctl preset service             # Apply preset
systemctl list-dependencies service  # Show dependencies
systemctl isolate target             # Change target
systemctl get-default                # Get default target
systemctl set-default target         # Set default target
systemctl --no-pager status service  # No pager
systemctl -q is-active service       # Quiet
```
- `--no-pager`: No pager
- `-q` or `--quiet`: Quiet
- `--type`: Filter by type (service, socket, target, etc.)
- `--state`: Filter by state
- `--failed`: Show only failed

## Recommended Unattended Usage

```bash
#!/bin/bash

# Check if service is running
systemctl -q is-active nginx && echo "Running" || echo "Not running"

# Start and enable service
systemctl enable --now nginx

# Get status without pager
systemctl --no-pager status nginx
```
