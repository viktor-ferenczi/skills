# cmake

**Platforms:** Multi-platform  
**Category:** Build System Generator

## Quick Reference

| Goal | Command |
|------|---------|
| Configure | `cmake -B build` |
| Build | `cmake --build build` |
| Silent | `cmake -DCMAKE_RULE_MESSAGES=OFF ...` |

## Command-Line Flags

```bash
cmake -B build                       # Configure in build/
cmake -B build -S .                  # Specify source
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake -B build -DCMAKE_INSTALL_PREFIX=/usr/local
cmake --build build                  # Build
cmake --build build --parallel       # Parallel build
cmake --build build -j4              # 4 parallel jobs
cmake --build build --target install # Install
cmake --install build                # Install
cmake -P script.cmake                # Run script
cmake --version                      # Version
cmake -L build                       # List cache variables
cmake -LA build                      # List all cache variables
cmake -LH build                      # List with help
```
- `-B`: Build directory
- `-S`: Source directory
- `-D`: Define variable
- `--build`: Build directory
- `--parallel` or `-j`: Parallel jobs
- `--target` or `-t`: Build specific target
- `--install`: Install
- `-P`: Run CMake script
- `-L`: List cache variables

## Recommended Unattended Usage

```bash
#!/bin/bash

# Configure and build quietly
cmake -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_RULE_MESSAGES=OFF
cmake --build build --parallel -- -s
```
