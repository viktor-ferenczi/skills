# gcloud (Google Cloud CLI)

**Platforms:** Multi-platform  
**Category:** Cloud (Google Cloud Platform)

## Quick Reference

| Goal | Command |
|------|---------|
| List projects | `gcloud projects list` |
| Set project | `gcloud config set project myproject` |
| List instances | `gcloud compute instances list` |
| List buckets | `gsutil ls` |

## Command-Line Flags

```bash
gcloud projects list                 # List projects
gcloud config set project myproject  # Set project
gcloud config get-value project      # Get current project
gcloud config configurations list    # List configurations
gcloud compute instances list        # List VM instances
gcloud compute instances start myvm
gcloud compute instances stop myvm
gcloud compute instances delete myvm
gcloud compute zones list            # List zones
gcloud compute regions list          # List regions
gcloud app services list             # App Engine services
gcloud app deploy                    # Deploy App Engine
gcloud functions list                # Cloud Functions
gcloud functions deploy myfunc --runtime python39
gcloud run services list             # Cloud Run services
gcloud run deploy myservice --image gcr.io/project/image
gcloud storage buckets list          # Cloud Storage buckets
gcloud storage ls gs://mybucket      # List bucket
gcloud storage cp file.txt gs://mybucket/  # Copy to bucket
gcloud storage cp gs://mybucket/file.txt . # Copy from bucket
gcloud sql instances list            # Cloud SQL instances
gcloud iam service-accounts list     # Service accounts
gcloud auth list                     # List accounts
gcloud auth activate-service-account --key-file=key.json
gcloud auth login                    # Interactive login
gcloud auth application-default login
gcloud --quiet sql instances delete mydb  # No prompts
gcloud --format=json compute instances list
gcloud --format='table(name,zone,status)' compute instances list
gcloud --project=myproject compute instances list
gcloud config set compute/zone us-central1-a
```
- `--project`: Project ID
- `--quiet`: Disable prompts
- `--format`: Output format (json, yaml, table, text)
- `--zone`: Zone
- `--region`: Region

## Environment Variables

```bash
export CLOUDSDK_CORE_PROJECT=myproject
export CLOUDSDK_COMPUTE_ZONE=us-central1-a
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
```

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive deployment
gcloud app deploy app.yaml --quiet --promote

# List with JSON output for scripting
gcloud compute instances list --format=json
```
