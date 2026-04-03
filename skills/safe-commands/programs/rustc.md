# rustc (Rust Compiler)

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `rustc --version` |
| Show help | `rustc --help` |
| Explain error | `rustc --explain E0001` |
| Print cfg | `rustc --print cfg` |
| List sysroots | `rustc --print sysroot` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `rustc file.rs` | Compiles code |
| `rustc --emit` | Produces output |
| Any rustc compilation | Creates binaries |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe rustc Inspection Script

# Show version
rustc --version

# Explain error
rustc --explain E0001

# Print cfg
rustc --print cfg
```
