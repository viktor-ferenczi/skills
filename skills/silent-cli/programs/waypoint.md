# waypoint (HashiCorp)

**Platforms:** Multi-platform  
**Category:** Application Deployment

## Command-Line Flags

- `-plain`: Plain output (no colors, no interactive elements)

## Recommended Unattended Usage

```bash
#!/bin/bash

waypoint init || exit 1
waypoint build -plain || exit 1
waypoint deploy -plain || exit 1
waypoint release -plain
```
