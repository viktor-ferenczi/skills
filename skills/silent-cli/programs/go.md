# go

**Platforms:** Multi-platform  
**Category:** Programming Language

## Quick Reference

| Goal | Command |
|------|---------|
| JSON test output | `go test -json ./...` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `GOFLAGS` | `-json` | Default flags (can set JSON output globally) |

## Command-Line Flags

- `-json`: JSON output for test results (machine-readable, suitable for CI parsing)

`go` build tools are inherently non-interactive. The main concern for unattended use is producing machine-readable output from `go test` via `-json`.

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
