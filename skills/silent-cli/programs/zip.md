# zip / unzip

**Platforms:** Multi-platform  
**Category:** Compression

## Quick Reference

| Goal | Command |
|------|---------|
| Create archive | `zip archive.zip files` |
| Recursive | `zip -r archive.zip dir/` |
| Extract | `unzip archive.zip` |
| List contents | `unzip -l archive.zip` |

## Command-Line Flags

### zip
```bash
zip archive.zip file1 file2
zip -r archive.zip dir/              # Recursive
zip -q archive.zip files             # Quiet
zip -j archive.zip files             # No paths stored
zip -9 archive.zip files             # Best compression
```
- `-r`: Recursive
- `-q`: Quiet
- `-j`: Junk paths (don't store directories)
- `-0` to `-9`: Compression level
- `-x`: Exclude files
- `-u`: Update
- `-d`: Delete

### unzip
```bash
unzip archive.zip
unzip -q archive.zip                 # Quiet
unzip -l archive.zip                 # List contents
unzip archive.zip -d /dest/dir       # Extract to directory
unzip -o archive.zip                 # Overwrite
unzip -n archive.zip                 # Never overwrite
```
- `-q`: Quiet
- `-l`: List
- `-d`: Destination directory
- `-o`: Overwrite
- `-n`: Never overwrite
- `-j`: Junk paths
