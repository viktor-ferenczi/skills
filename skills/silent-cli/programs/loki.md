# logcli (Loki CLI)

**Platforms:** Multi-platform  
**Category:** Log Aggregation

## Quick Reference

| Goal | Command |
|------|---------|
| Query logs | `logcli query '{job="myjob"}'` |
| Non-interactive | `logcli query --output=jsonl '...'` |
| Stream labels | `logcli labels` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `LOKI_ADDR` | `http://localhost:3100` | Loki address |
| `LOKI_ORG_ID` | `tenant1` | Tenant ID |

## Command-Line Flags

```bash
logcli query '{job="varlogs"}'       # Query logs
logcli query --since=1h '{job="app"}' # Last hour
logcli query --output=jsonl '{job="app"}' # JSON lines
logcli labels                        # List labels
logcli labels job                    # Label values
logcli series '{job="app"}'          # List series
```
- `--since`: Relative start time
- `--from`: Absolute start time
- `--to`: Absolute end time
- `--limit`: Limit results
- `--output`: Output format (default, jsonl)
- `--tail`: Tail mode
