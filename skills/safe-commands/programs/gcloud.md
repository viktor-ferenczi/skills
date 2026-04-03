# gcloud (Google Cloud SDK)

**Platforms:** Multi-platform
**Category:** Cloud Platforms

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `gcloud version` |
| Show help | `gcloud --help` |
| List projects | `gcloud projects list` |
| Show config | `gcloud config list` |
| List compute | `gcloud compute instances list` |
| List storage | `gsutil ls` |
| Show info | `gcloud info` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `gcloud compute instances create` | Creates VMs |
| `gcloud compute instances delete` | Deletes VMs |
| `gcloud projects create` | Creates projects |
| `gcloud projects delete` | Deletes projects |
| `gsutil cp ... gs://` | Uploads data |
| `gsutil rm` | Deletes objects |
| `gcloud config set` | Changes config |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe gcloud Inspection Script

# Show version
gcloud version

# List projects
gcloud projects list

# Show config
gcloud config list

# List compute instances
gcloud compute instances list
```
