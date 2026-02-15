# puppet

**Platforms:** Multi-platform  
**Category:** Configuration Management

## Quick Reference

| Goal | Command |
|------|---------|
| Apply | `puppet apply manifest.pp` |
| Test | `puppet apply --noop manifest.pp` |
| JSON | `puppet facts --render-as json` |

## Command-Line Flags

```bash
puppet apply manifest.pp             # Apply manifest
puppet apply --noop manifest.pp      # Dry run
puppet apply --verbose manifest.pp   # Verbose
puppet apply --debug manifest.pp     # Debug
puppet agent -t                      # Test agent
puppet agent --enable                # Enable agent
puppet agent --disable               # Disable agent
puppet facts                         # Show facts
puppet facts --render-as json        # JSON facts
puppet module list                   # List modules
puppet module install module-name    # Install module
```
- `--noop`: No operation (dry run)
- `--verbose`: Verbose output
- `--debug`: Debug output
- `--render-as`: Output format (json, yaml, console)
- `-t` or `--test`: Test mode (enable, then exit)
