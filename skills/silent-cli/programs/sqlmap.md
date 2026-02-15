# sqlmap

**Platforms:** Multi-platform  
**Category:** SQL Injection Scanner

## Quick Reference

| Goal | Command |
|------|---------|
| Batch mode (auto-answer prompts) | `sqlmap -u '...' --batch` |

## Command-Line Flags

- `--batch`: Auto-answer all prompts with defaults — essential for non-interactive use

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive scan with auto-answers
sqlmap -u 'http://target/page.php?id=1' --batch --output-dir=/tmp/sqlmap
```
