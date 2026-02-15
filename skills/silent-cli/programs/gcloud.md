# gcloud (Google Cloud CLI)

**Platforms:** Multi-platform  
**Category:** Cloud (Google Cloud Platform)

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive auth | `gcloud auth activate-service-account --key-file=key.json` |
| Suppress prompts | `gcloud --quiet <command>` |
| Machine-readable output | `gcloud --format=json <command>` |

## Environment Variables

```bash
export CLOUDSDK_CORE_DISABLE_PROMPTS=1     # Equivalent to --quiet (disable all prompts)
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json  # Service account key (avoids interactive login)
```

## Command-Line Flags

- `--quiet` or `-q`: Disable all interactive prompts (auto-accept defaults)
- `--format`: Output format (`json`, `yaml`, `table`, `text`, `none`) — use `json` for machine-readable output

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive deployment
gcloud app deploy app.yaml --quiet --promote

# List with JSON output for scripting
gcloud compute instances list --format=json
```
