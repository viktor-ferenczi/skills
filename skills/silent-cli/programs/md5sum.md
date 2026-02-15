# md5sum / md5 / shasum / sha256sum

**Platforms:** Multi-platform  
**Category:** Checksum

## Quick Reference

| Goal | Command |
|------|---------|
| Calculate MD5 | `md5sum file` |
| Calculate SHA256 | `sha256sum file` |
| Check file | `md5sum -c checksums.md5` |
| String hash | `echo -n 'text' | md5sum` |

## Command-Line Flags

### md5sum / sha256sum (Linux)
```bash
md5sum file                          # Calculate MD5
md5sum file1 file2 > checksums.md5   # Save checksums
md5sum -c checksums.md5              # Verify checksums
md5sum --quiet -c checksums.md5      # Quiet verify
echo -n 'text' | md5sum              # Hash string
sha256sum file                       # SHA256 checksum
sha512sum file                       # SHA512 checksum
```
- `-c` or `--check`: Check checksums from file
- `--quiet`: Don't print OK
- `--status`: Exit code only
- `-b` or `--binary`: Binary mode
- `-t` or `--text`: Text mode

### md5 / shasum (macOS)
```bash
md5 file                             # Calculate MD5
md5 -q file                          # Quiet (hash only)
md5 -s "text"                        # Hash string
shasum -a 256 file                   # SHA256
shasum -a 512 file                   # SHA512
shasum -c checksums.sha              # Verify
```
- `-q`: Quiet
- `-s`: Hash string
- `-a 256|512`: Algorithm (shasum)
