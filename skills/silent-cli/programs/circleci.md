# circleci

**Platforms:** Multi-platform  
**Category:** CI/CD

## Quick Reference

| Goal | Command |
|------|---------|
| Skip update check | `circleci --skip-update-check config validate` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `CIRCLECI_CLI_TOKEN` | `token` | API token (avoids interactive login) |

## Command-Line Flags

- `--skip-update-check`: Skip interactive update check (important for CI/scripts)
