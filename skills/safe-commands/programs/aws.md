# aws (AWS CLI)

**Platforms:** Multi-platform
**Category:** Cloud Platforms

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List EC2 instances | `aws ec2 describe-instances` |
| List S3 buckets | `aws s3 ls` |
| List S3 objects | `aws s3 ls s3://bucket/` |
| Get S3 object | `aws s3 cp s3://bucket/file .` |
| List IAM users | `aws iam list-users` |
| List Lambda functions | `aws lambda list-functions` |
| Get CloudWatch logs | `aws logs tail /aws/lambda/func` |
| Describe RDS instances | `aws rds describe-db-instances` |
| List ECR repositories | `aws ecr describe-repositories` |
| Get ECS services | `aws ecs list-services` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `aws ec2 run-instances` | Creates resources (costs money) |
| `aws ec2 terminate-instances` | Destroys instances |
| `aws s3 rm` | Deletes objects/buckets |
| `aws s3 cp ... s3://` | Uploads/modifies data |
| `aws iam create-user` | Modifies IAM |
| `aws lambda delete-function` | Deletes functions |
| `aws rds delete-db-instance` | Destroys databases |
| `aws cloudformation delete-stack` | Destroys stacks |

## Environment Variables for Safe Operation

| Variable | Description |
|----------|-------------|
| `AWS_PROFILE` | Use read-only profile |
| `AWS_ACCESS_KEY_ID` | Use read-only credentials |
| `AWS_SECRET_ACCESS_KEY` | Use read-only credentials |
| `AWS_DEFAULT_REGION` | Set default region |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe AWS Inspection Script

export AWS_PROFILE=readonly
export AWS_DEFAULT_REGION=us-east-1

echo "=== EC2 Instances ==="
aws ec2 describe-instances --query 'Reservations[].Instances[].InstanceId'

echo "=== S3 Buckets ==="
aws s3 ls

echo "=== Lambda Functions ==="
aws lambda list-functions --query 'Functions[].FunctionName'

echo "=== IAM Users ==="
aws iam list-users --query 'Users[].UserName'
```
