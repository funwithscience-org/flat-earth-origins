#!/usr/bin/env bash
# Fail-loud test runner. Blocking, not advisory: fix red before committing.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "== rebuilding dataset + page from source =="
python3 "$ROOT/scripts/build.py" > /dev/null
python3 "$ROOT/scripts/render.py"
echo "== invariants =="
python3 "$ROOT/tests/test_provenance.py"
