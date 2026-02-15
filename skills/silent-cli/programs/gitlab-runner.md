# gitlab-runner

**Platforms:** Multi-platform  
**Category:** CI/CD

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive register | `gitlab-runner register -n --url URL --token TOKEN --executor docker --docker-image alpine` |

## Command-Line Flags

- `-n` or `--non-interactive`: Non-interactive registration (all options must be provided via flags)

## Recommended Unattended Usage

```bash
#!/bin/bash

gitlab-runner register -n \
    --url "https://gitlab.com" \
    --registration-token "$TOKEN" \
    --executor docker \
    --docker-image alpine:latest \
    --description "docker-runner" \
    --tag-list "docker" \
    --run-untagged="true" \
    --locked="false" \
    --access-level="not_protected"
```
