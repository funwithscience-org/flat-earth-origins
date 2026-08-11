#!/usr/bin/env bash
# Fail-loud test runner. Blocking, not advisory: fix red before committing.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# CLEAR THE BYTECODE CACHE FIRST. Found 2026-08-11 by a mutation test: a file that is
# restored (git checkout, stash pop, a bundle fetch, an editor undo) can land with an
# mtime that still matches the .pyc compiled from the MUTATED source, and Python then
# serves the stale bytecode. The suite duly tested the version that no longer exists —
# it stayed RED after the source was correct, and would just as happily stay GREEN after
# the source went wrong. Every check in this file is downstream of the import, so this
# one line decides whether any of the other 195 mean anything.
find "$ROOT/scripts" -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true

echo "== rebuilding dataset + page from source =="
python3 "$ROOT/scripts/build.py" > /dev/null
python3 "$ROOT/scripts/render.py"
echo "== invariants =="
python3 "$ROOT/tests/test_provenance.py"
