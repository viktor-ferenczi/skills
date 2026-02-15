# amtool

**Platforms:** Multi-platform  
**Category:** Monitoring (Alertmanager)

## Quick Reference

| Goal | Command |
|------|---------|
| Check config | `amtool check-config alertmanager.yml` |
| Test routes | `amtool config routes test --label=alertname=test` |
| Silence | `amtool silence add alertname=Test` |

## Command-Line Flags

```bash
amtool check-config alertmanager.yml
amtool check-config alertmanager.yml --verbose
amtool config routes test --label=alertname=Test
amtool silence add alertname=Test --duration=1h
amtool silence add alertname=Test --author="user" --comment="maintenance"
amtool silence expire silence-id
amtool silence list
amtool silence query alertname=Test
```
- `--alertmanager.url`: Alertmanager URL
- `--output`: Output format (simple, extended, json)
- `--duration`: Silence duration
- `--author`: Silence author
- `--comment`: Silence comment
