# consul (HashiCorp)

**Platforms:** Multi-platform  
**Category:** Service Discovery

## Quick Reference

| Goal | Command |
|------|---------|
| JSON output | `consul acl bootstrap -format=json` |

## Command-Line Flags

- `-format`: Output format — use `json` for machine-readable output in scripts
- `-token`: ACL token (avoids interactive auth)
- `-http-addr`: HTTP API address (avoids interactive discovery)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive bootstrap
consul acl bootstrap -format=json 2>/dev/null

# Get service health
consul health service web -passing-only
```
