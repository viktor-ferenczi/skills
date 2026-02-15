# smbpasswd

**Platforms:** Linux, macOS
**Category:** Samba User Management

## Quick Reference

| Goal | Command |
|------|---------|
| Set SMB password non-interactively | `echo -e 'newpass\nnewpass' \| smbpasswd -s user` |
| Add user silently | `echo -e 'newpass\nnewpass' \| smbpasswd -s -a user` |

## Command-Line Flags

```bash
smbpasswd -s user                  # Silent mode (read password from stdin)
smbpasswd -s -a user               # Add user silently
smbpasswd -d user                  # Disable user (no prompt)
smbpasswd -e user                  # Enable user (no prompt)
smbpasswd -x user                  # Delete user (no prompt)
smbpasswd -n user                  # Set null password (no prompt)
smbpasswd -s -r server -U user     # Remote change, silent mode
```
- `-s`: Silent mode — reads password from stdin instead of prompting on terminal
- `-a`: Add user (combined with `-s` for non-interactive)
- `-d`: Disable user (no prompt needed)
- `-e`: Enable user (no prompt needed)
- `-x`: Delete user (no prompt needed)
- `-n`: Set null password (no prompt needed)

## Non-Interactive Password Setting

The `-s` flag is the standard way to use `smbpasswd` non-interactively.
It reads the new password from stdin instead of prompting.

```bash
# Set SMB password for existing user
echo -e 'newpassword\nnewpassword' | smbpasswd -s username

# Add a new SMB user with password
echo -e 'newpassword\nnewpassword' | smbpasswd -s -a username

# Using a variable (avoid exposing in ps output)
SMB_PASS="$(cat /run/secrets/smb_password)"
printf '%s\n%s\n' "$SMB_PASS" "$SMB_PASS" | smbpasswd -s -a username

# Change password on a remote Samba server
printf '%s\n%s\n%s\n' "$OLD_PASS" "$NEW_PASS" "$NEW_PASS" | smbpasswd -s -r server -U username
```

## Recommended Unattended Usage

```bash
#!/bin/bash

# Create system user if not exists
id username &>/dev/null || useradd -M -s /sbin/nologin username

# Set Samba password non-interactively
SMB_PASS="$(cat /run/secrets/smb_password)"
printf '%s\n%s\n' "$SMB_PASS" "$SMB_PASS" | smbpasswd -s -a username

# Disable a Samba user account
smbpasswd -d olduser

# Enable a previously disabled user
smbpasswd -e username
```

## Notes

- The `-s` flag is essential for unattended use; without it, `smbpasswd` prompts on the terminal
- Password must be provided twice (new password + confirmation) separated by newlines
- For remote password changes (`-r`), three lines are needed: old password, new password, confirmation
- The user must already exist as a system user before adding to Samba
- Avoid passing passwords on the command line; use stdin redirection from files or secret managers
