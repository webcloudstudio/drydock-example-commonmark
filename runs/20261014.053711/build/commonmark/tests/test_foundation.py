"""Foundation tests: project tree, package skeleton, and the stdlib-only dependency contract."""

import importlib
import os
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

import pytest

RESERVED_MODULES = ["blocks", "inlines", "refs", "entities", "render", "cli"]
# `cli` gained its entry point in the executable block; `blocks`, `render` and `inlines` gained
# behavior in the block-engine build; `entities` gained the backslash unescape helper in the
# backslash-escapes build; `refs` gained the reference map and label normalization in the
# link-reference-definitions build. No reserved module remains behavior-free.
NO_BEHAVIOR_MODULES: list[str] = []


def test_foundation_package_imports(project_root: Path) -> None:
    """Acceptance: the mdparser package and each reserved module import cleanly."""
    sys.path.insert(0, str(project_root))

    importlib.import_module("mdparser")
    for name in RESERVED_MODULES:
        full = "mdparser." + name
        module = importlib.import_module(full)
        assert module.__name__ == full


@pytest.mark.parametrize("name", RESERVED_MODULES)
def test_reserved_module_has_documented_responsibility(name: str) -> None:
    module = importlib.import_module("mdparser." + name)
    assert module.__doc__ and module.__doc__.strip()


@pytest.mark.parametrize("name", NO_BEHAVIOR_MODULES)
def test_reserved_module_has_no_behavior_yet(name: str) -> None:
    module = importlib.import_module("mdparser." + name)
    public = [attr for attr in vars(module) if not attr.startswith("_")]
    assert public == []


def test_package_is_named_mdparser_not_commonmark() -> None:
    package = importlib.import_module("mdparser")
    assert package.__name__ == "mdparser"
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("commonmark")


def test_package_declares_no_runtime_dependencies(project_root: Path) -> None:
    data = tomllib.loads((project_root / "pyproject.toml").read_text(encoding="utf-8"))
    assert data["project"]["dependencies"] == []


def test_package_declares_supported_python(project_root: Path) -> None:
    data = tomllib.loads((project_root / "pyproject.toml").read_text(encoding="utf-8"))
    assert data["project"]["requires-python"] == ">=3.11"


def test_dev_group_provides_pytest(project_root: Path) -> None:
    data = tomllib.loads((project_root / "pyproject.toml").read_text(encoding="utf-8"))
    assert any(req.startswith("pytest") for req in data["dependency-groups"]["dev"])


def test_lockfile_is_committed_on_disk(project_root: Path) -> None:
    assert (project_root / "uv.lock").is_file()


def test_test_launcher_is_executable(project_root: Path) -> None:
    launcher = project_root / "bin" / "test.sh"
    assert launcher.is_file()
    assert os.access(launcher, os.X_OK)


def test_package_imports_under_plain_python3_without_venv(project_root: Path) -> None:
    """The package must import under plain python3 with no virtual environment activated."""
    python = shutil.which("python3")
    assert python is not None
    env = {key: value for key, value in os.environ.items() if key != "VIRTUAL_ENV"}
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        [python, "-c", "import mdparser.cli, mdparser.render, mdparser.inlines"],
        cwd=project_root,
        env=env,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0
