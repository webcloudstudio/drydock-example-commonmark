"""Shared pytest fixtures for the mdparser test suite."""

from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def project_root() -> Path:
    """Absolute path to the application root, where `commonmark` and `pyproject.toml` live."""
    return PROJECT_ROOT
