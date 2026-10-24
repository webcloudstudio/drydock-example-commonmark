"""Verification tests: the terminal conformance gate from FEATURE-Verification.md.

The declared check runs the complete, unfiltered CommonMark 0.31.2 suite through the supplied scoring
entry point and reads back its exit status. The captured output is printed only for diagnosis; no test
matches on the text of the runner's summary.
"""

import subprocess
from pathlib import Path


# --- Declared acceptance checks (transcribed from FEATURE-Verification.md) ---


def test_full_conformance_suite(project_root: Path) -> None:
    """AC full-conformance-suite: the complete supplied suite passes when run unfiltered."""
    result = subprocess.run(
        ["sh", "sources/full_test.sh"],
        capture_output=True,
        text=True,
        cwd=project_root,
        check=False,
    )
    print(result.stdout)
    print(result.stderr)
    assert result.returncode == 0, f"full_test.sh exited {result.returncode}"
