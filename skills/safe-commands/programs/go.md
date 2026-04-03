# go

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `go version` |
| Show help | `go help` |
| Show env | `go env` |
| List modules | `go list -m` |
| Show mod | `go mod edit -json` |
| Download (dry-run) | `go mod download -x` |
| Vet code | `go vet` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `go build` | Builds code |
| `go run` | Runs program |
| `go install` | Installs package |
| `go mod tidy` | Modifies go.mod |
| `go mod vendor` | Creates vendor |
| `go get` | Gets packages |
| `go fmt` | Modifies files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe go Inspection Script

# Show version
go version

# Show env
go env

# List modules
go list -m all

# Show module info
go mod edit -json
```
