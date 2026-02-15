# gitlab-runner

**Platforms:** Multi-platform  
**Category:** CI/CD

## Quick Reference

| Goal | Command |
|------|---------|
| Register | `gitlab-runner register -n --url URL --token TOKEN` |
| Run | `gitlab-runner run` |
| Single job | `gitlab-runner exec docker jobname` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `CI_SERVER_URL` | `https://gitlab.com` | GitLab URL |
| `REGISTRATION_TOKEN` | `token` | Registration token |

## Command-Line Flags

```bash
gitlab-runner register -n            # Non-interactive
gitlab-runner register --url https://gitlab.com --token TOKEN
gitlab-runner register --executor docker --docker-image alpine
gitlab-runner list                   # List runners
gitlab-runner verify                 # Verify runners
gitlab-runner run                    # Run runner
gitlab-runner exec docker test       # Execute job locally
gitlab-runner unregister --name name # Unregister
```
- `-n` or `--non-interactive`: Non-interactive
- `--url`: GitLab URL
- `--token`: Registration token
- `--executor`: Executor type
- `--docker-image`: Default Docker image

## Recommended Unattended Usage

```bash
#!/bin/bash

gitlab-runner register -n     --url "https://gitlab.com"     --registration-token "$TOKEN"     --executor docker     --docker-image alpine:latest     --description "docker-runner"     --tag-list "docker"     --run-untagged="true"     --locked="false"     --access-level="not_protected"
```
