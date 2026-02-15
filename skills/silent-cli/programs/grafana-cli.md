# grafana-cli

**Platforms:** Multi-platform  
**Category:** Monitoring (Grafana)

## Quick Reference

| Goal | Command |
|------|---------|
| Install plugin (non-interactive) | `grafana-cli plugins install plugin-id` |
| Reset admin password (non-interactive) | `grafana-cli admin reset-admin-password newpassword` |

`grafana-cli` is inherently non-interactive. Commands execute without prompts. The `admin reset-admin-password` command accepts the password as an argument to avoid prompting.
