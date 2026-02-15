# slabtop

**Platforms:** Linux
**Category:** System Monitoring (Kernel Slab Cache)

## Quick Reference

| Goal | Command |
|------|---------|
| Single snapshot | `slabtop -o` |
| Sorted by cache size | `slabtop -o -s c` |

## Command-Line Flags

- `-o` or `--once`: Display one snapshot and exit (non-interactive)
- `-s S` or `--sort=S`: Sort criteria (`a` active objects, `b` objects per slab, `c` cache size, `l` slabs, `v` active slabs, `n` name, `o` total objects, `p` pages per slab, `s` object size, `u` utilization)

No iteration count flag exists. For multiple samples, use a loop with `-o`.

## Recommended Unattended Usage

```bash
#!/bin/bash

# Single snapshot sorted by cache size
slabtop -o -s c
```
