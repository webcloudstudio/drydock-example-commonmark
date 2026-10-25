#!/bin/sh
# full_test.sh — scoring entry point. Do not filter, skip, or reinterpret.
#
# `drydock uat` runs `sh sources/full_test.sh` from the completed application root and takes its
# exit code and output as the score. The interface check is separate from the conformance run so
# that a missing or non-executable program and a genuine conformance failure are distinguishable
# in the evidence. The program path is the harness's only knowledge of the implementation
# language; the harness itself is language-neutral.
#
# The suite runs unfiltered: no --pattern, no --number, no selector of any kind. spec_tests.py
# exits with failed + errored, so exit 0 means the complete CommonMark 0.31.2 suite passed.
set -eu

if [ ! -x ./commonmark ]; then
    echo "error: no executable ./commonmark at the application root." >&2
    echo "The deliverable is an executable named commonmark that reads UTF-8 Markdown on stdin" >&2
    echo "and writes HTML to stdout." >&2
    exit 1
fi

# spec_tests.py imports cmark and normalize as siblings, so the staged directory has to be on the
# import path. The program is passed absolute because the runner spawns it from its own cwd.
PYTHONPATH="$PWD/sources${PYTHONPATH:+:$PYTHONPATH}"
export PYTHONPATH

set +e
output=$(python3 sources/spec_tests.py --program "$PWD/commonmark" --spec sources/spec.txt 2>&1)
status=$?
set -e

printf '%s\n' "$output"

# The runner exits with failed + errored, which a shell truncates modulo 256: exactly 256 or 512
# failures would exit 0 and read as a pass. The harness therefore confirms the tally rather than
# trusting the status alone, and reports a clean run only when both agree. This is the scoring
# instrument reading its own instrument; the acceptance check above it still asserts nothing but
# this script's exit code.
if [ "$status" -ne 0 ]; then
    exit 1
fi
if ! printf '%s\n' "$output" | grep -q '0 failed, 0 errored, 0 skipped'; then
    echo "error: conformance runner exited 0 but did not report a clean unfiltered suite." >&2
    exit 1
fi
