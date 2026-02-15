# vagrant

**Platforms:** Multi-platform  
**Category:** VM Management

## Command-Line Flags

- `-f` or `--force`: Force destroy without confirmation prompt
- `--no-provision`: Skip provisioning prompts
- `--no-tty`: Disable TTY detection

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive destroy and recreate
vagrant destroy -f
vagrant up --provision

# Batch command execution
vagrant ssh -c 'sudo apt-get update && sudo apt-get upgrade -y'
```
