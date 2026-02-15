# vagrant

**Platforms:** Multi-platform  
**Category:** VM Management

## Quick Reference

| Goal | Command |
|------|---------|
| Init | `vagrant init ubuntu/focal64` |
| Up | `vagrant up` |
| SSH | `vagrant ssh` |
| Destroy | `vagrant destroy` |

## Command-Line Flags

```bash
vagrant init ubuntu/focal64          # Initialize Vagrantfile
vagrant init --minimal ubuntu/focal64
vagrant up                           # Start VM
vagrant up --provision               # Start and provision
vagrant up --no-provision
vagrant halt                         # Stop VM
vagrant halt --force
vagrant reload                       # Restart VM
vagrant reload --provision
vagrant suspend                      # Suspend VM
vagrant resume                       # Resume VM
vagrant destroy                      # Destroy VM
vagrant destroy -f                   # Force destroy
vagrant status                       # VM status
vagrant global-status                # All VMs status
vagrant ssh                          # SSH into VM
vagrant ssh -c 'command'             # Run command via SSH
vagrant provision                    # Run provisioners
vagrant provision --provision-with shell
vagrant box list                     # List boxes
vagrant box add ubuntu/focal64
vagrant box update                   # Update boxes
vagrant box remove ubuntu/focal64
vagrant package                      # Package VM
vagrant plugin list                  # List plugins
vagrant plugin install vagrant-vbguest
vagrant snapshot save name           # Save snapshot
vagrant snapshot restore name        # Restore snapshot
vagrant snapshot delete name         # Delete snapshot
vagrant port                         # Show port mappings
vagrant rsync-auto                   # Auto rsync
```
- `--provision`/`--no-provision`: Control provisioning
- `--parallel`: Parallel execution
- `--provider`: Specify provider

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive destroy and recreate
vagrant destroy -f
vagrant up --provision

# Batch command execution
vagrant ssh -c 'sudo apt-get update && sudo apt-get upgrade -y'
```
