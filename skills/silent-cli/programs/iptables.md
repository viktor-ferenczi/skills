# iptables

**Platforms:** Linux  
**Category:** Firewall

## Quick Reference

| Goal | Command |
|------|---------|
| List rules | `sudo iptables -L` |
| Add rule | `sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT` |
| Delete | `sudo iptables -D INPUT 1` |
| Save | `sudo iptables-save > rules.iptables` |
| Restore | `sudo iptables-restore < rules.iptables` |

## Command-Line Flags

```bash
sudo iptables -L                     # List rules
sudo iptables -L -v                  # Verbose
sudo iptables -L -n                  # Numeric
sudo iptables -L --line-numbers      # With line numbers
sudo iptables -t nat -L              # NAT table
sudo iptables -t mangle -L           # Mangle table
sudo iptables -t raw -L              # Raw table
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -P INPUT DROP          # Default policy DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT
sudo iptables -D INPUT 1             # Delete rule by number
sudo iptables -D INPUT -p tcp --dport 80 -j ACCEPT  # Delete by spec
sudo iptables -I INPUT 1 -p tcp --dport 22 -j ACCEPT  # Insert at position
sudo iptables -F                     # Flush all rules
sudo iptables -F INPUT               # Flush INPUT chain
sudo iptables -X                     # Delete custom chains
sudo iptables -Z                     # Zero counters
sudo iptables -S                     # Print rules
sudo iptables -N MYCHAIN             # New chain
sudo iptables -A MYCHAIN ...
sudo iptables -A INPUT -j MYCHAIN
sudo iptables -X MYCHAIN             # Delete chain
```
- `-L`: List
- `-v`: Verbose
- `-n`: Numeric
- `--line-numbers`: Show numbers
- `-t`: Table (filter, nat, mangle, raw)
- `-A`: Append
- `-I`: Insert
- `-D`: Delete
- `-P`: Policy
- `-F`: Flush
- `-X`: Delete chain
- `-Z`: Zero counters
- `-S`: Print rules
- `-N`: New chain
- `-j`: Jump target

## Recommended Unattended Usage

```bash
#!/bin/bash

# Backup rules
sudo iptables-save > /etc/iptables/rules.v4

# Restore rules
sudo iptables-restore < /etc/iptables/rules.v4

# Check if rule exists
sudo iptables -C INPUT -p tcp --dport 22 -j ACCEPT 2>/dev/null ||     sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```
