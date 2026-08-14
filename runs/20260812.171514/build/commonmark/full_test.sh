#!/bin/sh
# Run the complete staged CommonMark conformance suite.
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$SCRIPT_DIR/spec_tests.py" \
    --program "$SCRIPT_DIR/cmark" \
    --spec "$SCRIPT_DIR/spec.txt"
