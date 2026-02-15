# rustc

**Platforms:** Multi-platform  
**Category:** Rust Compiler

## Quick Reference

| Goal | Command |
|------|---------|
| Compile | `rustc main.rs -o app` |
| Optimize | `rustc -C opt-level=3 main.rs` |
| Quiet | `rustc -o app main.rs 2>&1` |

## Command-Line Flags

```bash
rustc main.rs                        # Compile
rustc main.rs -o app                 # Output name
rustc -C opt-level=3 main.rs         # Optimization level 3
rustc -C lto main.rs                 # Link-time optimization
rustc --crate-type=bin main.rs       # Binary crate
rustc --crate-type=lib main.rs       # Library crate
rustc -g main.rs                     # Debug info
rustc -W warnings                    # Warn on warnings
rustc -A warnings                    # Allow warnings
rustc -D warnings                    # Deny warnings (treat as errors)
rustc --emit=asm main.rs             # Emit assembly
rustc --emit=llvm-ir main.rs         # Emit LLVM IR
rustc --emit=mir main.rs             # Emit MIR
rustc --emit=dep-info main.rs        # Emit deps
rustc --edition=2021 main.rs         # Edition
rustc -L path                        # Library search path
rustc -l lib                         # Link library
```
- `-o`: Output file
- `-C opt-level`: Optimization (0-3, s, z)
- `-C lto`: Link-time optimization
- `--crate-type`: Crate type
- `-g`: Debug info
- `-W/-A/-D`: Warning levels
- `--emit`: Output type
- `--edition`: Rust edition
- `-L`: Library path
- `-l`: Link library
