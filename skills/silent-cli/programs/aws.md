# aws (AWS CLI)

**Platforms:** Multi-platform  
**Category:** Cloud (Amazon Web Services)

## Quick Reference

| Goal | Command |
|------|---------|
| List S3 | `aws s3 ls` |
| List EC2 | `aws ec2 describe-instances` |
| List regions | `aws ec2 describe-regions` |
| Configure | `aws configure` |

## Command-Line Flags

```bash
aws s3 ls                            # List buckets
aws s3 ls s3://mybucket              # List bucket contents
aws s3 cp file.txt s3://mybucket/    # Copy to S3
aws s3 cp s3://mybucket/file.txt .   # Copy from S3
aws s3 sync local/ s3://mybucket/    # Sync directory
aws s3 rm s3://mybucket/file.txt     # Delete file
aws ec2 describe-instances           # List EC2 instances
aws ec2 describe-instances --instance-ids i-xxx
aws ec2 start-instances --instance-ids i-xxx
aws ec2 stop-instances --instance-ids i-xxx
aws ec2 terminate-instances --instance-ids i-xxx
aws iam list-users                   # List IAM users
aws iam list-roles
aws iam get-user --user-name myuser
aws rds describe-db-instances        # List RDS instances
aws lambda list-functions            # List Lambda functions
aws cloudformation list-stacks       # List CF stacks
aws cloudwatch list-metrics          # List CloudWatch metrics
aws logs describe-log-groups         # List log groups
aws sts get-caller-identity          # Get current identity
aws configure                        # Interactive config
aws configure set region us-east-1
aws configure list                   # Show config
aws --region us-west-2 s3 ls         # Override region
aws --profile prod s3 ls             # Use profile
aws --output json ec2 describe-instances
aws --output text ec2 describe-instances
aws --output table ec2 describe-instances
aws --query 'Reservations[*].Instances[*].InstanceId' ec2 describe-instances
aws --no-paginate s3api list-objects --bucket mybucket
```
- `--region`: AWS region
- `--profile`: Credential profile
- `--output`: Output format (json, text, table)
- `--query`: JMESPath query
- `--no-paginate`: Disable auto-pagination
- `--debug`: Debug mode

## Environment Variables

```bash
export AWS_ACCESS_KEY_ID=xxx
export AWS_SECRET_ACCESS_KEY=xxx
export AWS_DEFAULT_REGION=us-east-1
export AWS_PROFILE=default
export AWS_CA_BUNDLE=/path/to/ca.crt
export AWS_SHARED_CREDENTIALS_FILE=~/.aws/credentials
export AWS_CONFIG_FILE=~/.aws/config
```

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive with explicit credentials
aws s3 sync ./build s3://mybucket/     --region us-east-1     --no-progress     --only-show-errors

# Query and process output
aws ec2 describe-instances     --query 'Reservations[*].Instances[*].{ID:InstanceId,State:State.Name}'     --output json
```
