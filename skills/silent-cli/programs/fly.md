# fly (Concourse CI)

**Platforms:** Multi-platform  
**Category:** CI/CD

## Quick Reference

| Goal | Command |
|------|---------|
| Login | `fly -t target login -c concourse-url` |
| Trigger build | `fly -t target trigger-job -j pipeline/job` |
| Hijack | `fly -t target intercept -j pipeline/job` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `FLY_HOME` | `~/.fly` | Fly config directory |

## Command-Line Flags

```bash
fly -t target login -c https://concourse.example.com
fly -t target sync                   # Sync CLI
fly -t target pipelines              # List pipelines
fly -t target trigger-job -j pipeline/job
fly -t target watch -j pipeline/job  # Watch build
fly -t target builds                 # List builds
fly -t target intercept -j pipeline/job  # Debug
```
- `-t` or `--target`: Target name
- `-j` or `--job`: Pipeline/job
- `-c` or `--concourse-url`: Concourse URL
- `-n` or `--team`: Team name
