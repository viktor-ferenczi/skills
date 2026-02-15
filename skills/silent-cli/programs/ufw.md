# ufw (Uncomplicated Firewall)

**Platforms:** Linux (Ubuntu/Debian)  
**Category:** Firewall

## Quick Reference

| Goal | Command |
|------|---------|
| Status | `sudo ufw status` |
| Enable | `sudo ufw enable` |
| Allow | `sudo ufw allow 22` |
| Deny | `sudo ufw deny 3306` |
| Delete | `sudo ufw delete allow 80` |

## Command-Line Flags

```bash
sudo ufw status                      # Show status
sudo ufw status verbose              # Verbose status
sudo ufw status numbered             # With rule numbers
sudo ufw enable                      # Enable firewall
sudo ufw disable                     # Disable firewall
sudo ufw reset                       # Reset to defaults
sudo ufw allow 22                    # Allow port
sudo ufw allow 22/tcp                # Allow TCP port
sudo ufw allow 1000:2000/tcp         # Port range
sudo ufw allow ssh                   # Allow by service name
sudo ufw allow from 192.168.1.0/24   # Allow from network
sudo ufw allow from 192.168.1.50 to any port 22
sudo ufw deny 3306                   # Deny port
sudo ufw delete allow 22             # Delete rule
sudo ufw delete 3                    # Delete rule by number
sudo ufw default deny incoming       # Default deny incoming
sudo ufw default allow outgoing      # Default allow outgoing
sudo ufw limit 22/tcp                # Rate limit
sudo ufw limit ssh                   # Rate limit SSH
sudo ufw app list                    # List application profiles
sudo ufw app info 'Nginx Full'       # App profile info
sudo ufw allow 'Nginx Full'          # Allow app profile
sudo ufw reload                      # Reload rules
sudo ufw show raw                    # Show raw rules
sudo ufw show added                  # Show added rules
```
- `status`: Show status
- `enable`/`disable`: Control firewall
- `allow`/`deny`/`reject`: Rule actions
- `delete`: Remove rule
- `reset`: Reset defaults
- `default`: Set defaults
- `limit`: Rate limiting
- `reload`: Reload rules
- `app list`/`app info`: Application profiles

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive setup
sudo ufw --force reset
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw --force enable
```
