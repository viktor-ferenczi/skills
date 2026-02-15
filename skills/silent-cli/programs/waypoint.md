# waypoint (HashiCorp)

**Platforms:** Multi-platform  
**Category:** Application Deployment

## Quick Reference

| Goal | Command |
|------|---------|
| Init | `waypoint init` |
| Build | `waypoint build` |
| Deploy | `waypoint deploy` |
| Release | `waypoint release` |
| Up | `waypoint up` |

## Command-Line Flags

```bash
waypoint init                        # Initialize project
waypoint init -from-project=other
waypoint init -update                # Update project
waypoint build                       # Build application
waypoint build -var 'key=value'
waypoint deploy                      # Deploy application
waypoint deploy -release=false
waypoint release                     # Release deployment
waypoint up                          # Build + Deploy + Release
waypoint up -var-file=vars.wpvars
waypoint destroy                     # Destroy deployment
waypoint status                      # Application status
waypoint logs                        # Show logs
waypoint exec /bin/sh                # Execute command
waypoint artifact list               # List artifacts
waypoint artifact push
waypoint artifact build
waypoint config get                  # Get config
waypoint config set key=value
waypoint config source-set -type=vault -config='key=value'
waypoint context list                # List contexts
waypoint context set mycontext
waypoint context use mycontext
waypoint context verify
waypoint context clear
waypoint install -platform=kubernetes -accept-tos
waypoint server bootstrap
waypoint ui -authenticate            # Open UI with auth
waypoint version
```
- `-var`: Set variable
- `-var-file`: Variable file
- `-local`: Local mode
- `-plain`: Plain output

## Recommended Unattended Usage

```bash
#!/bin/bash

waypoint init || exit 1
waypoint build -plain || exit 1
waypoint deploy -plain || exit 1
waypoint release -plain
```
