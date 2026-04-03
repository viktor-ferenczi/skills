# mvn (Maven)

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `mvn --version` |
| Show help | `mvn --help` |
| Show effective | `mvn help:effective-settings` |
| Show pom | `mvn help:effective-pom` |
| Show deps | `mvn dependency:tree` |
| Show plugins | `mvn plugin:help` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `mvn compile` | Compiles code |
| `mvn package` | Creates package |
| `mvn install` | Installs to repo |
| `mvn deploy` | Deploys to server |
| `mvn clean` | Cleans output |
| `mvn test` | Runs tests |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe mvn Inspection Script

# Show version
mvn --version

# Show effective pom
mvn help:effective-pom | head -50

# Show dependency tree
mvn dependency:tree
```
