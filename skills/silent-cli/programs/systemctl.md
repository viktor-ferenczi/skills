# systemctl

**Platforms:** Linux (systemd)  
**Category:** Service Management

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet check | `systemctl -q is-active service` |
| No pager | `systemctl --no-pager status service` |

## Command-Line Flags

- `--no-pager`: Disable pager — output goes directly to stdout (essential for scripts)
- `-q` or `--quiet`: Quiet — suppress output, only return exit code

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
