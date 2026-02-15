# go

**Platforms:** Multi-platform  
**Category:** Programming Language

## Quick Reference

| Goal | Command |
|------|---------|
| Build | `go build -o app` |
| Test | `go test ./...` |
| Silent | `go build -ldflags="-s -w"` |
| JSON output | `go test -json ./...` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `GO111MODULE` | `on` | Enable modules |
| `GOPROXY` | `https://proxy.golang.org` | Module proxy |
| `CGO_ENABLED` | `0` | Disable CGO |

## Command-Line Flags

```bash
go build                             # Build current package
go build -o app                      # Output binary
go build -v                          # Verbose
go build -x                          # Print commands
go build -ldflags="-s -w"            # Strip symbols (smaller)
go test ./...                        # Run tests
go test -v ./...                     # Verbose tests
go test -json ./...                  # JSON output
go test -cover ./...                 # With coverage
go test -race ./...                  # Race detector
go get -u package                    # Update package
go mod download                      # Download modules
go mod tidy                          # Clean up modules
go mod verify                        # Verify modules
go fmt ./...                         # Format code
go vet ./...                         # Vet code
go generate ./...                    # Run generators
```
- `-o`: Output file
- `-v`: Verbose
- `-x`: Print commands
- `-ldflags`: Linker flags (`-s` strip, `-w` no DWARF)
- `-u`: Update
- `-json`: JSON output (test)
- `-cover`: Coverage
- `-race`: Race detector

## Recommended Unattended Usage

```bash
#!/bin/bash

export CGO_ENABLED=0
export GO111MODULE=on

# Build production binary
go build -ldflags="-s -w -X main.version=1.0" -o app

# Run tests with JSON output for CI
go test -json ./... > test-results.json
```
