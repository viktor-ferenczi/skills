# cargo

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `cargo --version` |
| Show help | `cargo --help` |
| Check code | `cargo check` |
| Show metadata | `cargo metadata` |
| List packages | `cargo pkgid` |
| Show tree | `cargo tree` |
| Search crates | `cargo search name` |
| Show config | `cargo config get` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `cargo build` | Compiles code |
| `cargo run` | Runs program |
| `cargo test` | Runs tests |
| `cargo clean` | Deletes artifacts |
| `cargo publish` | Publishes crate |
| `cargo install` | Installs crate |
| `cargo update` | Updates dependencies |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe cargo Inspection Script

# Show version
cargo --version

# Check code (no build)
cargo check

# Show metadata
cargo metadata --format-version 1 | head -50

# Show dependency tree
cargo tree
```
