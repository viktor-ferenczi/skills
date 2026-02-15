# circleci

**Platforms:** Multi-platform  
**Category:** CI/CD

## Quick Reference

| Goal | Command |
|------|---------|
| Validate config | `circleci config validate` |
| Run locally | `circleci local execute --job jobname` |
| Quiet | `circleci --skip-update-check` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `CIRCLECI_CLI_TOKEN` | `token` | API token |

## Command-Line Flags

```bash
circleci config validate             # Validate config
circleci config validate -c .circleci/config.yml
circleci local execute --job build   # Run job locally
circleci local execute --config .circleci/config.yml
circleci namespace create namespace vcs-type org-name
circleci orb list namespace          # List orbs
```
- `--job`: Job to run
- `--config`: Config file path
- `--skip-update-check`: Skip update check
- `-c`: Config file for validate
