# grafana-cli

**Platforms:** Multi-platform  
**Category:** Monitoring (Grafana)

## Quick Reference

| Goal | Command |
|------|---------|
| Install plugin | `grafana-cli plugins install plugin-id` |
| List plugins | `grafana-cli plugins ls` |
| Silent | `grafana-cli plugins install id --pluginsDir=/path` |

## Command-Line Flags

```bash
grafana-cli plugins install grafana-clock-panel
grafana-cli plugins install grafana-clock-panel --pluginUrl https://...
grafana-cli plugins ls               # List plugins
grafana-cli plugins remove plugin-id
grafana-cli plugins upgrade-all
grafana-cli plugins upgrade plugin-id
grafana-cli admin reset-admin-password newpassword
```
- `--pluginsDir`: Plugins directory
- `--pluginUrl`: Custom plugin URL
- `--repo`: Plugin repository URL
- `--insecure`: Skip TLS verification
