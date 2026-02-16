# Unix/Linux Usage Examples

## Debian/Ubuntu Package Installation
```bash
export DEBIAN_FRONTEND=noninteractive
export CI=true
apt-get update -qq && apt-get install -y -qq package-name
```

## NPM CI Installation
```bash
export CI=true
export NODE_ENV=production
npm ci --silent --no-progress
```

## Docker Unattended
```bash
export DOCKER_CLI_EXPERIMENTAL=enabled
export BUILDKIT_PROGRESS=plain
docker build --progress=plain -t myimage .
```

## Python Script
```bash
export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE=1
python script.py
```
