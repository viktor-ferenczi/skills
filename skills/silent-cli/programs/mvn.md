# mvn (Maven)

**Platforms:** Multi-platform  
**Category:** Java Build Tool

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet | `mvn -q clean package` |
| Batch | `mvn -B clean package` |
| Offline | `mvn -o clean package` |

## Command-Line Flags

```bash
mvn -q clean package                 # Quiet
mvn --quiet clean package            # Quiet
mvn -B clean package                 # Batch mode (non-interactive)
mvn --batch-mode clean package       # Batch mode
mvn -o clean package                 # Offline mode
mvn --offline clean package          # Offline
```
- `-q` or `--quiet`: Quiet
- `-B` or `--batch-mode`: Batch mode (non-interactive)
- `-o` or `--offline`: Offline mode

## Recommended Unattended Usage

```bash
#!/bin/bash

# Batch mode, quiet, offline if possible
mvn -B -q -o clean package -DskipTests
```
