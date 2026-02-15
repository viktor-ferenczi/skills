# ant

**Platforms:** Multi-platform  
**Category:** Java Build Tool

## Quick Reference

| Goal | Command |
|------|---------|
| Build | `ant` |
| Quiet | `ant -q` |
| Silent | `ant -S` |
| Log file | `ant -logfile build.log` |

## Command-Line Flags

```bash
ant                                  # Default target
ant build                            # Specific target
ant -q                               # Quiet
ant -quiet                           # Quiet
ant -S                               # Silent (no output)
ant -silent                          # Silent
ant -v                               # Verbose
ant -verbose                         # Verbose
ant -d                               # Debug
ant -debug                           # Debug
ant -logfile build.log               # Log to file
ant -logger org.apache.tools.ant.listener.SimpleBigProjectLogger
ant -emacs                           # Emacs-friendly output
ant -Dproperty=value                 # Set property
ant -propertyfile props.properties   # Load properties
ant -buildfile build.xml             # Specific buildfile
ant -f build.xml                     # Specific buildfile
ant -find                            # Find buildfile upward
ant -noinput                         # Disable interactive input
ant -keep-going                      # Keep going on errors
ant -k                               # Keep going
```
- `-q` or `-quiet`: Quiet
- `-S` or `-silent`: Silent
- `-v` or `-verbose`: Verbose
- `-d` or `-debug`: Debug
- `-logfile`: Log file
- `-logger`: Logger class
- `-emacs`: Emacs-friendly
- `-D`: Set property
- `-propertyfile`: Properties file
- `-buildfile` or `-f`: Build file
- `-noinput`: No interactive input
- `-k` or `-keep-going`: Keep going
