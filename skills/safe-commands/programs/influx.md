# influx (InfluxDB CLI)

**Platforms:** Multi-platform
**Category:** Database

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `influx version` |
| Show help | `influx --help` |
| List buckets | `influx bucket list` |
| Query data | `influx query "FROM..."` |
| Show orgs | `influx org list` |
| Show tasks | `influx task list` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `influx write` | Writes data |
| `influx bucket create` | Creates buckets |
| `influx bucket delete` | Deletes buckets |
| `influx delete` | Deletes data |
| `influx task create` | Creates tasks |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe influx Inspection Script

# List buckets
influx bucket list

# Query data
influx query "from(bucket:\"my-bucket\") |> range(start:-1h)"

# Show orgs
influx org list
```
