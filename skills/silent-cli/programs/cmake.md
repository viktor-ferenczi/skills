# cmake

**Platforms:** Multi-platform  
**Category:** Build System Generator

## Quick Reference

| Goal | Command |
|------|---------|
| Silent build | `cmake --build build -- -s` |
| Suppress rule messages | `cmake -B build -DCMAKE_RULE_MESSAGES=OFF` |

## Command-Line Flags

- `-DCMAKE_RULE_MESSAGES=OFF`: Suppress per-rule progress messages during build
- `-- -s`: Pass `-s` (silent) flag to the underlying make tool

## Recommended Unattended Usage

```bash
#!/bin/bash

# Configure and build quietly
cmake -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_RULE_MESSAGES=OFF
cmake --build build --parallel -- -s
```
