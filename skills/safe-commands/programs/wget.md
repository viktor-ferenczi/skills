# wget

**Platforms:** Multi-platform
**Category:** Web/Download

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `wget --version` |
| Show help | `wget --help` |
| Check URL | `wget --spider URL` |
| Headers only | `wget --server-response --spider URL` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `wget URL` | Downloads files |
| `wget -r URL` | Recursive download |
| `wget -O file` | Writes to file |
| Any wget download | Creates files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe wget Inspection Script

# Check URL (spider mode)
wget --spider https://example.com

# Show headers only
wget --server-response --spider https://example.com
```
