# influx (InfluxDB CLI)

**Platforms:** Multi-platform  
**Category:** Time Series Database

## Quick Reference

| Goal | Command |
|------|---------|
| Execute query | `influx query 'from(bucket: "mybucket")'` |
| Non-interactive | `influx bucket list --json` |
| Write data | `influx write 'measurement,tag=value field=1'` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `INFLUX_TOKEN` | `token` | API token |
| `INFLUX_ORG` | `org` | Organization |
| `INFLUX_HOST` | `http://localhost:8086` | InfluxDB URL |

## Command-Line Flags

```bash
influx bucket list                   # List buckets
influx bucket list --json            # JSON output
influx query 'from(bucket:"b") |> range(start:-1h)'
influx write 'm,t=v f=1i 1234567890'
influx ping                          # Health check
influx setup --username admin --password pass --org org --bucket default --force
```
- `--json`: JSON output
- `--org`: Organization
- `--bucket`: Bucket
- `--token`: Token
- `--host`: Host URL
