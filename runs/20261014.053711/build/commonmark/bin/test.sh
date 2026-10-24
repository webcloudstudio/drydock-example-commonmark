#!/bin/bash
# CommandCenter Operation
# Name: Run Test Suite
# Type: batch

# --- Standard Preamble ---
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
LOG_DIR="$PROJECT_DIR/data/logs"
mkdir -p "$LOG_DIR"

TIMESTAMP=$(date '+%Y-%m-%d_%H%M%S')
SCRIPT_NAME=$(basename "$0" .sh)
LOG_FILE="$LOG_DIR/${SCRIPT_NAME}_${TIMESTAMP}.log"

echo "=== $SCRIPT_NAME started at $(date '+%Y-%m-%d %H:%M:%S') ===" | tee "$LOG_FILE"
echo "Arguments: $*" | tee -a "$LOG_FILE"
echo "Working dir: $PROJECT_DIR" | tee -a "$LOG_FILE"
echo "---" | tee -a "$LOG_FILE"

cd "$PROJECT_DIR"

# --- Test Command (pyproject.toml foundation contract: pytest -q, run inside .venv) ---
if [ ! -x .venv/bin/python ]; then
    echo "error: .venv missing; run 'uv venv .venv && uv sync' first" | tee -a "$LOG_FILE" >&2
    exit 1
fi
.venv/bin/python -m pytest -q "$@" 2>&1 | tee -a "$LOG_FILE"

echo "=== $SCRIPT_NAME finished at $(date '+%Y-%m-%d %H:%M:%S') ===" | tee -a "$LOG_FILE"
