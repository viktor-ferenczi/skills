# nft

**Platforms:** Linux (iptables successor)  
**Category:** Firewall

## Quick Reference

| Goal | Command |
|------|---------|
| List | `sudo nft list ruleset` |
| Add table | `sudo nft add table inet filter` |
| Add chain | `sudo nft add chain inet filter input { type filter hook input priority 0 \; }` |
| Add rule | `sudo nft add rule inet filter input tcp dport 22 accept` |

## Command-Line Flags

```bash
sudo nft list ruleset                # List all rules
sudo nft list tables                 # List tables
sudo nft list table inet filter      # List specific table
sudo nft list table inet filter -a   # With handles
sudo nft list chain inet filter input
sudo nft list ruleset -j             # JSON output
sudo nft add table inet filter
sudo nft add chain inet filter input { type filter hook input priority 0 \; }
sudo nft add rule inet filter input tcp dport 22 accept
sudo nft add rule inet filter input ct state established,related accept
sudo nft add rule inet filter input iif lo accept
sudo nft insert rule inet filter input tcp dport 22 accept
sudo nft delete rule inet filter input handle 10
sudo nft flush table inet filter     # Empty table
sudo nft delete table inet filter    # Delete table
sudo nft -f /etc/nftables.conf       # Load from file
sudo nft -c -f /etc/nftables.conf    # Check config
```
- `list`: List objects
- `add`: Add objects
- `insert`: Insert rules
- `delete`: Delete objects
- `flush`: Empty objects
- `create`: Create with check
- `-a`: Show handles
- `-j`: JSON output
- `-f`: File
- `-c`: Check only

## Recommended Unattended Usage

```bash
#!/bin/bash

# Check and load rules
sudo nft -c -f /etc/nftables.conf && sudo nft -f /etc/nftables.conf

# Save current ruleset
sudo nft list ruleset > /etc/nftables.conf
```
