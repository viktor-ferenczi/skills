# mvn (Maven)

**Platforms:** Multi-platform  
**Category:** Java Build Tool

## Quick Reference

| Goal | Command |
|------|---------|
| Build | `mvn clean package` |
| Quiet | `mvn -q clean package` |
| Batch | `mvn -B clean package` |
| Offline | `mvn -o clean package` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `MAVEN_OPTS` | `-Xmx512m` | JVM options |

## Command-Line Flags

```bash
mvn clean package                    # Clean and package
mvn -q clean package                 # Quiet
mvn --quiet clean package            # Quiet
mvn -B clean package                 # Batch mode
mvn --batch-mode clean package       # Batch mode
mvn -o clean package                 # Offline mode
mvn --offline clean package          # Offline
mvn -U clean package                 # Force updates
mvn --update-snapshots clean package # Force updates
mvn -X clean package                 # Debug
mvn -e clean package                 # Errors
mvn clean install -DskipTests        # Skip tests
mvn clean install -Dmaven.test.skip=true  # Skip tests and compile
mvn dependency:tree                  # Show deps
mvn dependency:resolve               # Resolve deps
mvn compile                          # Compile
mvn test                             # Run tests
mvn verify                           # Run checks
mvn deploy                           # Deploy
mvn site                             # Generate site
mvn clean                            # Clean
mvn help:effective-pom               # Show effective POM
mvn versions:display-dependency-updates  # Check updates
```
- `-q` or `--quiet`: Quiet
- `-B` or `--batch-mode`: Batch mode (non-interactive)
- `-o` or `--offline`: Offline mode
- `-U` or `--update-snapshots`: Force snapshot updates
- `-X`: Debug output
- `-e`: Error messages
- `-D`: Set property

## Recommended Unattended Usage

```bash
#!/bin/bash

# Batch mode, quiet, offline if possible
mvn -B -q -o clean package -DskipTests
```
