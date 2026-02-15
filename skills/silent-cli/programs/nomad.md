# nomad (HashiCorp)

**Platforms:** Multi-platform  
**Category:** Workload Orchestration

## Command-Line Flags

```bash
nomad job validate job.nomad         # Validate job (non-interactive check)
nomad job run job.nomad              # Run job (non-interactive)
nomad job run -check-index 0 job.nomad  # Conditional run (non-interactive)
```

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate and run job
nomad job validate myjob.nomad || exit 1
nomad job run myjob.nomad
```
