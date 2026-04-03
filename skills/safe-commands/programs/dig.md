# dig

**Platforms:** Multi-platform
**Category:** Network/DNS

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Query DNS | `dig domain` |
| Show help | `dig -h` |
| Specific type | `dig domain TYPE` |
| Short output | `dig +short domain` |
| Trace route | `dig +trace domain` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `dig` with large queries | May trigger rate limits |
| Any dig is read-only | Generally safe |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe dig Inspection Script

# Query DNS
dig example.com

# Short output
dig +short example.com

# MX records
dig example.com MX
```
