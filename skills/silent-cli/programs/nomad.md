# nomad (HashiCorp)

**Platforms:** Multi-platform  
**Category:** Workload Orchestration

## Quick Reference

| Goal | Command |
|------|---------|
| Status | `nomad status` |
| Jobs | `nomad job status` |
| Run | `nomad job run job.nomad` |
| Stop | `nomad job stop jobname` |

## Command-Line Flags

```bash
nomad agent -dev                     # Development mode
nomad status                         # Server status
nomad node status                    # Node status
nomad job status                     # Job status
nomad job status myjob               # Specific job status
nomad job run job.nomad              # Run job
nomad job run -check-index 0 job.nomad  # Conditional run
nomad job stop myjob                 # Stop job
nomad job stop -purge myjob          # Purge job
nomad job plan job.nomad             # Plan job
nomad job validate job.nomad         # Validate job
nomad job dispatch myperiodic        # Dispatch periodic
nomad job promote myjob              # Promote canary
nomad job revert myjob 4             # Revert to version
nomad alloc status alloc_id          # Allocation status
nomad alloc logs alloc_id            # Allocation logs
nomad alloc logs -stderr alloc_id    # Stderr logs
nomad alloc exec alloc_id /bin/sh    # Execute in alloc
nomad alloc restart alloc_id         # Restart alloc
nomad alloc stop alloc_id            # Stop alloc
nomad deployment status              # Deployment status
nomad deployment fail deploy_id      # Fail deployment
nomad deployment promote deploy_id   # Promote deployment
nomad eval status eval_id            # Evaluation status
nomad quota status                   # Quota status
nomad operator raft list-peers       # Raft peers
nomad tls ca create                  # Create CA
nomad tls cert create -server        # Create server cert
nomad var get myvar                  # Get variable
nomad var put myvar key=value        # Put variable
```
- `-address`: Server address
- `-token`: ACL token
- `-namespace`: Namespace
- `-region`: Region
- `-tls-server-name`: TLS server name
- `-tls-skip-verify`: Skip TLS verify

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate and run job
nomad job validate myjob.nomad || exit 1
nomad job run myjob.nomad
```
