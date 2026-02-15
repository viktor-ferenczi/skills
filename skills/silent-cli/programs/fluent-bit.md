# fluent-bit

**Platforms:** Multi-platform  
**Category:** Log Processing

## Quick Reference

| Goal | Command |
|------|---------|
| Validate config (no run) | `fluent-bit --dry-run -c fluent-bit.conf` |

## Command-Line Flags

- `--dry-run`: Validate configuration without running (useful for automated config checks)

`fluent-bit` is inherently non-interactive when run as a service. Use `--dry-run` in CI/CD pipelines to validate configuration files before deployment.
