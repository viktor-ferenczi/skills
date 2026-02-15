# sqlite3

**Platforms:** Multi-platform  
**Category:** Database Client (SQLite)

## Quick Reference

| Goal | Command |
|------|---------|
| Execute | `sqlite3 db.sqlite 'SELECT 1'` |
| Import | `sqlite3 db.sqlite < script.sql` |
| CSV output | `sqlite3 -csv db.sqlite 'SELECT *'` |

## Command-Line Flags

```bash
sqlite3 db.sqlite "SELECT 1"         # Execute query
sqlite3 db.sqlite < script.sql       # Import SQL
sqlite3 -csv db.sqlite "SELECT *"    # CSV output
sqlite3 -json db.sqlite "SELECT *"   # JSON output
sqlite3 -line db.sqlite "SELECT *"   # Line mode
sqlite3 -list db.sqlite "SELECT *"   # List mode
sqlite3 -noheader db.sqlite "SELECT *"  # No headers
sqlite3 -header db.sqlite "SELECT *" # With headers
sqlite3 -batch db.sqlite "SELECT *"  # Batch mode
sqlite3 -init init.sql db.sqlite     # Run init file
```
- `-csv`: CSV mode
- `-json`: JSON mode
- `-line`: Line mode (key: value)
- `-list`: List mode
- `-header`: Show headers
- `-noheader`: No headers
- `-batch`: Batch mode (no interactive)
- `-init`: Initialization file
- `-echo`: Print commands before execution

## Recommended Unattended Usage

```bash
#!/bin/bash

# CSV export
sqlite3 -csv -noheader db.sqlite "SELECT * FROM table" > output.csv

# JSON export
sqlite3 -json db.sqlite "SELECT * FROM table" > output.json

# Batch import
sqlite3 db.sqlite <<EOF
BEGIN;
CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, msg TEXT);
INSERT INTO logs (msg) VALUES ('test');
COMMIT;
EOF
```
