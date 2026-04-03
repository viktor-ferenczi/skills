# nft (nftables)

**Platforms:** Linux
**Category:** Firewall/Security

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List rulesets | `nft list ruleset` |
| List tables | `nft list tables` |
| List chains | `nft list chains` |
| Show help | `nft --help` |
| Show version | `nft --version` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `nft add` | Adds rules |
| `nft delete` | Deletes rules |
| `nft insert` | Inserts rules |
| `nft flush` | Flushes ruleset |
| `nft replace` | Replaces rules |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe nft Inspection Script

# List ruleset
nft list ruleset

# List tables
nft list tables
```
