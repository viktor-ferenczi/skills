# ufw (Uncomplicated Firewall)

**Platforms:** Linux (Ubuntu/Debian)  
**Category:** Firewall

## Command-Line Flags

- `--force`: Skip confirmation prompts (for `enable`, `reset`, etc.)

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
