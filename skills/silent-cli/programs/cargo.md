# cargo

**Platforms:** Multi-platform  
**Category:** Rust Package Manager

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet build | `cargo build -q` |
| Disable colors | `CARGO_TERM_COLOR=never cargo build` |
| JSON output | `cargo test --message-format=json` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `CARGO_TERM_COLOR` | `never` | Disable colored output |
| `CARGO_NET_OFFLINE` | `true` | Offline mode (no network prompts) |

## Command-Line Flags

- `-q` or `--quiet`: Quiet mode — suppress output
- `--message-format json|short`: Machine-readable output format
- `--offline`: Offline mode (no network access)

## Recommended Unattended Usage

```bash
#!/bin/bash

export CARGO_TERM_COLOR=never

# Release build quietly
cargo build --release -q

# Run tests quietly
cargo test -q
```
