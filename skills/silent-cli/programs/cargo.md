# cargo

**Platforms:** Multi-platform  
**Category:** Rust Package Manager

## Quick Reference

| Goal | Command |
|------|---------|
| Build | `cargo build --release` |
| Test | `cargo test` |
| Quiet | `cargo build -q` |
| JSON | `cargo test --message-format=json` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `CARGO_TERM_COLOR` | `never` | Disable colors |
| `CARGO_NET_OFFLINE` | `true` | Offline mode |

## Command-Line Flags

```bash
cargo build                          # Debug build
cargo build --release                # Release build
cargo build -q                       # Quiet
cargo build -v                       # Verbose
cargo build -vv                      # Very verbose
cargo test                           # Run tests
cargo test -q                        # Quiet tests
cargo test --no-fail-fast            # Run all tests
cargo test --lib                     # Library tests only
cargo run                            # Run project
cargo run -q                         # Quiet
cargo check                          # Check without building
cargo check -q
cargo clippy                         # Lint
cargo fmt                            # Format
cargo doc                            # Generate docs
cargo doc --no-deps                  # No dependencies
cargo update                         # Update deps
cargo clean                          # Clean build
cargo install --path .               # Install locally
cargo publish -q                     # Publish crate
```
- `-q` or `--quiet`: Quiet
- `-v` or `--verbose`: Verbose
- `--release`: Release build
- `--message-format`: Output format (human, json, short)
- `--no-fail-fast`: Don't stop on first failure
- `--offline`: Offline mode

## Recommended Unattended Usage

```bash
#!/bin/bash

export CARGO_TERM_COLOR=never

# Release build quietly
cargo build --release -q

# Run tests quietly
cargo test -q
```
