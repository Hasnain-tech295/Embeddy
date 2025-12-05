# seeds sample texts/embeddings 
#!/usr/bin/env/bash
set -euo pipefail

#usage: /scripts/seed_sample_data.sh [BASE_URL]
# Example: BASE_URL=http://localhost:8000 ./scripts/seed_sample_data.sh

BASE_URL=${1:-${BASE_URL:-http://localhost:8000}}
DATA_DIR=${2:-examples/data/sample_texts}

if [ ! -d "$DATA_DIR" ]; then
  echo "Error: Directory $DATA_DIR does not exist."
  exit 1
fi

echo "Seeding file from $DATA_DIR to $BASE_URL/insert/"

for file in "$DATA_DIR"/*.txt; do
  [ -e "$file" ] || continue
  doc_id="$(basename "$file" .txt)"
  echo " - Seeding '$doc_id' (file: $file)"
  python - <<PY
import json, urllib.request, sys
path = r"$file"
doc_id = r"$doc_id"
with open(path, "r", encoding="utf-8") as fh:
    text = fh.read()
payload = json.dumps({"doc_id": doc_id, "text": text}).encode("utf-8")
req = urllib.request.Request("$BASE_URL/insert/", data=payload, headers={"Content-Type":"application/json"})
try:
    resp = urllib.request.urlopen(req, timeout=30)
    print("  -> response:", resp.status, resp.read().decode()[:500])
except Exception as e:
    print("  -> error:", e, file=sys.stderr)
    sys.exit(1)
PY
done

echo "Seeding complete."