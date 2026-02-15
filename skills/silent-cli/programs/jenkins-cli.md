# jenkins-cli

**Platforms:** Multi-platform  
**Category:** CI/CD

## Quick Reference

| Goal | Command |
|------|---------|
| Silent | `java -jar jenkins-cli.jar -s http://jenkins -noKeyAuth` |
| Groovy | `jenkins-cli groovy = < script.groovy` |
| Build job | `jenkins-cli build jobname -s` |

## Command-Line Flags

```bash
java -jar jenkins-cli.jar -s http://jenkins:8080/ who-am-i
java -jar jenkins-cli.jar -s http://jenkins:8080/ build jobname -s
java -jar jenkins-cli.jar -s http://jenkins:8080/ console jobname
java -jar jenkins-cli.jar -s http://jenkins:8080/ list-jobs
```
- `-s` or `--server`: Jenkins URL
- `-noKeyAuth`: No key authentication
- `-auth user:token`: Authentication
- `-i` or `--ssh`: SSH private key

## Build Options

```bash
jenkins-cli build jobname -s -v      # Wait and view output
jenkins-cli build jobname -p param=value  # With parameters
jenkins-cli build jobname -f         # Follow build
```
- `-s` or `--wait`: Wait for completion
- `-f` or `--follow`: Follow output
- `-v` or `--verbose`: Verbose
- `-p` or `--parameter`: Set parameter
