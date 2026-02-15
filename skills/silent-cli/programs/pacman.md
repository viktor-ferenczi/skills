# pacman

**Platforms:** Linux (Arch, Manjaro)  
**Category:** Package Management

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet install | `pacman -S --needed --noprogressbar -q package` |
| Quiet update | `pacman -Syu --noprogressbar -q` |

> **WARNING:** `--noconfirm` skips all confirmation prompts, including safety-critical ones
> (e.g. removing conflicting packages, replacing packages). This is a security-sensitive
> flag. **Confirm with the human operator before using `--noconfirm`.**

## Command-Line Flags

```bash
pacman -S --needed --noprogressbar -q package  # Quiet install
pacman -Syu --noprogressbar -q                 # Quiet update
# Use --noconfirm only with human operator approval:
pacman -S --noconfirm --needed --noprogressbar package
pacman -Syu --noconfirm --noprogressbar
```
- `--noconfirm`: Skip confirmation prompts (**security-sensitive, get human approval first**)
- `--needed`: Skip reinstall of up-to-date packages
- `--noprogressbar`: No progress bar
- `-q`: Quiet operation

## Configuration (/etc/pacman.conf)

```ini
[options]
Color = never
```
