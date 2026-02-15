# promtool

**Platforms:** Multi-platform  
**Category:** Monitoring (Prometheus)

## Quick Reference

| Goal | Command |
|------|---------|
| Check config | `promtool check config prometheus.yml` |
| Check rules | `promtool check rules rules.yml` |
| Test rules | `promtool test rules test.yml` |

## Command-Line Flags

```bash
promtool check config prometheus.yml
promtool check rules /path/to/rules/*.yml
promtool check webconfig web.yml
promtool test rules test.yml         # Unit tests
promtool query instant http://localhost:9090 'up'
promtool query range --start=-5m http://localhost:9090 'up'
```
- `check config`: Validate config file
- `check rules`: Validate recording/alerting rules
- `check webconfig`: Validate web config
- `test rules`: Run rule unit tests
- `query instant`: Instant query
- `query range`: Range query
