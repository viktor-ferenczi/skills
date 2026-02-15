# boundary (HashiCorp)

**Platforms:** Multi-platform  
**Category:** Identity-based Access

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive auth | `boundary authenticate password -auth-method-id ampw_xxx -login-name admin` |
| Machine-readable output | `boundary targets list -scope-id p_xxx -format json` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `BOUNDARY_ADDR` | `https://boundary.example.com` | Boundary server address (avoids interactive discovery) |
| `BOUNDARY_TOKEN` | `at_xxx` | Auth token (avoids interactive login) |

## Command-Line Flags

- `-format`: Output format — use `json` for machine-readable output
- `-token`: Provide auth token non-interactively
- `-addr`: Boundary address (can also be set via `BOUNDARY_ADDR`)
