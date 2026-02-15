# jenkins-cli

**Platforms:** Multi-platform  
**Category:** CI/CD

## Quick Reference

| Goal | Command |
|------|---------|
| Silent build | `jenkins-cli build jobname -s` |
| Non-interactive auth | `java -jar jenkins-cli.jar -s http://jenkins -noKeyAuth` |

## Command-Line Flags

- `-s` or `--wait`: Wait for build completion (blocks until done)
- `-f` or `--follow`: Follow build output
- `-noKeyAuth`: No key authentication (non-interactive)
- `-auth user:token`: Authentication via token (non-interactive)
- `-p` or `--parameter`: Set build parameter

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive build, wait for completion
java -jar jenkins-cli.jar -s http://jenkins:8080/ -auth user:token build jobname -s -p param=value
```
