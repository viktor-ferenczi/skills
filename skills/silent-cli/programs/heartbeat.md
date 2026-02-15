# heartbeat

**Platforms:** Multi-platform  
**Category:** Uptime Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| Run | `heartbeat -e -c heartbeat.yml` |
| Config test | `heartbeat test config` |
| Setup | `heartbeat setup` |

## Command-Line Flags

```bash
heartbeat -e                         # Log to stderr
heartbeat -c heartbeat.yml           # Config file
heartbeat test config                # Test config
heartbeat test output                # Test output
heartbeat setup                      # Setup dashboards
heartbeat setup --dashboards
heartbeat setup --index-management
heartbeat -e -d '*'                  # Debug
```
- `-e`: Log to stderr
- `-c`: Config file
- `test config/output`: Validate/test
- `setup`: Setup dashboards and templates
- `-d`: Debug selectors
