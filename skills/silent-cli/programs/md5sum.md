# md5sum / md5 / shasum / sha256sum

**Platforms:** Multi-platform  
**Category:** Checksum

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet verify | `md5sum --quiet -c checksums.md5` |

## Command-Line Flags

### md5sum / sha256sum (Linux)
```bash
md5sum --quiet -c checksums.md5      # Quiet verify
```
- `--quiet`: Don't print OK
- `--status`: Exit code only

### md5 / shasum (macOS)
```bash
md5 -q file                          # Quiet (hash only)
```
- `-q`: Quiet
