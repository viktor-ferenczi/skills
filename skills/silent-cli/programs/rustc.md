# rustc

**Platforms:** Multi-platform  
**Category:** Rust Compiler

## Quick Reference

| Goal | Command |
|------|---------|
| Suppress warnings | `rustc -A warnings main.rs` |

## Command-Line Flags

- `-A warnings`: Allow (suppress) all warnings — quieter output for automated builds
- `-D warnings`: Deny warnings (treat as errors) — useful for CI to enforce clean builds
