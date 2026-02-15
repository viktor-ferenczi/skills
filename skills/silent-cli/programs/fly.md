# fly (Concourse CI)

**Platforms:** Multi-platform  
**Category:** CI/CD

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive login | `fly -t target login -c url -u user -p pass` |

## Command-Line Flags

- `-t` or `--target`: Target name (required, avoids interactive selection)

`fly` commands are generally non-interactive once a target is authenticated. The main concern for unattended use is providing credentials non-interactively during `fly login` (via `-u`/`-p` flags or token-based auth).
