# firewall-cmd

**Platforms:** Linux (firewalld)  
**Category:** Firewall

## Quick Reference

| Goal | Command |
|------|---------|
| Status | `sudo firewall-cmd --state` |
| List all | `sudo firewall-cmd --list-all` |
| Add port | `sudo firewall-cmd --add-port=80/tcp` |
| Add service | `sudo firewall-cmd --add-service=http` |
| Permanent | `sudo firewall-cmd --permanent --add-service=http` |
| Reload | `sudo firewall-cmd --reload` |

## Command-Line Flags

```bash
sudo firewall-cmd --state            # Check state
sudo firewall-cmd --reload           # Reload config
sudo firewall-cmd --complete-reload  # Complete reload
sudo firewall-cmd --list-all         # List all config
sudo firewall-cmd --list-all-zones   # All zones
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --zone=public --list-all
sudo firewall-cmd --get-default-zone
sudo firewall-cmd --set-default-zone=public
sudo firewall-cmd --add-port=80/tcp
sudo firewall-cmd --add-port=80/tcp --permanent
sudo firewall-cmd --remove-port=80/tcp
sudo firewall-cmd --add-service=http
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --remove-service=http
sudo firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" accept'
sudo firewall-cmd --list-ports
sudo firewall-cmd --list-services
sudo firewall-cmd --add-masquerade
sudo firewall-cmd --add-forward-port=port=8080:proto=tcp:toport=80
sudo firewall-cmd --runtime-to-permanent
sudo firewall-cmd --check-config
```
- `--state`: Check status
- `--reload`: Reload rules
- `--list-all`: List configuration
- `--zone`: Specify zone
- `--add-port`/`--remove-port`: Port rules
- `--add-service`/`--remove-service`: Service rules
- `--permanent`: Make permanent
- `--runtime-to-permanent`: Save runtime

## Recommended Unattended Usage

```bash
#!/bin/bash

# Check if running
sudo firewall-cmd --state || exit 1

# Add services and reload
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```
