# dev start convenience script
#!/usr/bin/env bash
set -euo pipefail

# Load .env if present (simple)
if [ -f .env ]; then
  echo "Loading .env"
  export $(grep -v '^#' .env | xargs)
fi

PORT="${1:-${PORT:-8000}}"
echo "Starting uvicorn on port $PORT"
uvicorn src.app.main:app --reload --port "$PORT"
