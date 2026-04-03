# apt

**Platforms:** Debian, Ubuntu
**Category:** Package Management

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List packages | `apt list --installed` |
| Search packages | `apt search pattern` |
| Show package info | `apt show package` |
| List available | `apt list --upgradable` |
| Cache stats | `apt-cache stats` |
| Policy info | `apt policy package` |
| Download info | `apt download --print-uris package` |
| Changelog | `apt changelog package` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `apt install` | Installs packages (modifies system) |
| `apt remove` | Removes packages |
| `apt purge` | Removes packages + config |
| `apt upgrade` | Upgrades packages |
| `apt full-upgrade` | Full system upgrade |
| `apt autoremove` | Removes auto-installed packages |
| `apt clean` | Clears package cache |

## Environment Variables for Safe Operation

| Variable | Description |
|----------|-------------|
| `DEBIAN_FRONTEND` | `noninteractive` for unattended |
| `APT_CONFIG` | Custom config file |
| `LC_ALL` | Output language |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe apt Inspection Script

# List installed packages
apt list --installed | head -20

# Search for package
apt search "nginx"

# Show package details
apt show nginx

# Check upgradable packages
apt list --upgradable

# Package policy
apt policy nginx
```
