# passwd

**Platforms:** Linux, macOS
**Category:** User Account Management

## Quick Reference

| Goal | Command |
|------|---------|
| Set password non-interactively | `echo 'user:password' \| chpasswd` |
| Pipe to passwd | `echo -e 'newpass\nnewpass' \| passwd user` |
| Set from stdin (root) | `echo 'newpass' \| passwd --stdin user` |

## Command-Line Flags

```bash
passwd --stdin user                 # Read password from stdin (RHEL/CentOS only)
passwd -l user                     # Lock account (no prompt)
passwd -u user                     # Unlock account (no prompt)
passwd -e user                     # Expire password (no prompt)
passwd -d user                     # Delete password (no prompt)
```

## Non-Interactive Password Setting

### Using chpasswd (Preferred)

The `chpasswd` utility is the standard way to set passwords non-interactively.
It reads `user:password` pairs from stdin and is designed for scripted use.

```bash
# Set password for a single user
echo 'username:newpassword' | chpasswd

# Set password with SHA-512 hash
echo 'username:newpassword' | chpasswd -c SHA512

# Set pre-hashed password
echo 'username:$6$rounds=...' | chpasswd -e

# Set multiple passwords at once
chpasswd <<'EOF'
user1:password1
user2:password2
EOF
```

### Using passwd with stdin

```bash
# Pipe password to passwd (most Linux distros)
echo -e 'newpassword\nnewpassword' | passwd user

# RHEL/CentOS: use --stdin flag
echo 'newpassword' | passwd --stdin user
```

### Using usermod or openssl

```bash
# Set password via usermod with pre-hashed value
usermod -p "$(openssl passwd -6 'newpassword')" user
```

## Recommended Unattended Usage

```bash
#!/bin/bash

# Preferred: use chpasswd for non-interactive password changes
echo "myuser:$(cat /run/secrets/user_password)" | chpasswd

# Alternative: RHEL/CentOS with --stdin
# echo "$(cat /run/secrets/user_password)" | passwd --stdin myuser

# Lock account without prompts
passwd -l olduser

# Force password change on next login
passwd -e myuser
```

## Notes

- `passwd` is inherently interactive; prefer `chpasswd` for unattended use
- `--stdin` flag is non-standard and only available on RHEL/CentOS/Fedora
- Always avoid passing passwords directly on the command line (visible in `ps` output)
- Use file-based or secret-manager-based approaches for password values
