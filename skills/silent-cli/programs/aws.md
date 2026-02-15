# aws (AWS CLI)

**Platforms:** Multi-platform  
**Category:** Cloud (Amazon Web Services)

## Quick Reference

| Goal | Command |
|------|---------|
| Suppress progress | `aws s3 sync ./build s3://bucket/ --no-progress` |
| Errors only | `aws s3 sync ./build s3://bucket/ --only-show-errors` |
| Machine-readable output | `aws ec2 describe-instances --output json` |
| Disable pager | `aws --no-cli-pager <command>` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `AWS_PAGER` | `""` | **Disable interactive pager** (critical for scripts) |
| `AWS_DEFAULT_OUTPUT` | `json` | Machine-readable output format |
| `AWS_CLI_AUTO_PROMPT` | `off` | Disable auto-prompt feature |

## Command-Line Flags

- `--output json|text|table`: Output format (`json` or `text` for machine-readable)
- `--query`: JMESPath query to filter output
- `--no-paginate`: Disable auto-pagination
- `--no-cli-pager`: Disable interactive pager
- `--no-progress`: Suppress S3 transfer progress
- `--only-show-errors`: Suppress all output except errors

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive with explicit credentials
aws s3 sync ./build s3://mybucket/ \
    --region us-east-1 \
    --no-progress \
    --only-show-errors

# Query and process output
aws ec2 describe-instances \
    --query 'Reservations[*].Instances[*].{ID:InstanceId,State:State.Name}' \
    --output json
```
