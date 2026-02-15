# nft

**Platforms:** Linux (iptables successor)  
**Category:** Firewall

## Quick Reference

| Goal | Command |
|------|---------|
| JSON output | `sudo nft list ruleset -j` |
| Load from file | `sudo nft -f /etc/nftables.conf` |

## Command-Line Flags

```bash
sudo nft list ruleset -j             # JSON output (machine-readable)
sudo nft -f /etc/nftables.conf       # Load from file (non-interactive)
sudo nft -c -f /etc/nftables.conf    # Check config (dry run)
```
- `-j`: JSON output (machine-readable)
- `-f`: Load from file (non-interactive)
- `-c`: Check only (dry run)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Check and load rules
sudo nft -c -f /etc/nftables.conf && sudo nft -f /etc/nftables.conf

# Save current ruleset
sudo nft list ruleset > /etc/nftables.conf
```
