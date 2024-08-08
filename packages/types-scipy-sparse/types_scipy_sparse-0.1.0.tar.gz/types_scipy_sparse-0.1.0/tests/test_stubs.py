"""
Test scipy.sparse stubs
"""

import importlib.util
import os
import re
from collections import defaultdict
from collections.abc import Collection, Iterator, Sequence
from typing import Any

import pytest
from mypy import api as mypy_api

TESTS_DIR = os.path.dirname(__file__)
PASS_DIR = os.path.join(TESTS_DIR, "pass")
FAIL_DIR = os.path.join(TESTS_DIR, "fail")
REVEAL_DIR = os.path.join(TESTS_DIR, "reveal")


# output type of pytest.param is not in public API of pytest
def iter_test_cases(
    directory: str,
) -> Iterator[tuple[Sequence[Any], Collection[Any], str | None]]:
    """
    Iterate over all test cases in a directory
    """
    for root, _, files in os.walk(directory):
        for fname in files:
            if os.path.splitext(fname)[-1] != ".py":
                continue
            fullpath = os.path.join(root, fname)
            # Use relative path for nice py.test name
            relpath = os.path.relpath(fullpath, start=directory)

            yield pytest.param(
                fullpath,
                # Manually specify a name for the test
                id=relpath,
            )


@pytest.mark.parametrize("path", iter_test_cases(PASS_DIR))
def test_success(path: str) -> None:
    """Annotations successfully type-check"""
    stdout, _, exitcode = mypy_api.run([path])
    assert exitcode == 0, stdout
    assert re.match(r"Success: no issues found in \d+ source files?", stdout.strip())


@pytest.mark.parametrize("path", iter_test_cases(FAIL_DIR))
def test_fail(path: str) -> None:
    """Annotations fail to type-check as expected"""
    stdout, _, exitcode = mypy_api.run([path])

    assert exitcode != 0

    with open(path, encoding="utf-8") as fin:
        lines = fin.readlines()

    errors: defaultdict[int, str] = defaultdict(str)
    error_lines = stdout.rstrip("\n").split("\n")
    assert re.match(
        r"Found \d+ errors? in \d+ files? \(checked \d+ source files?\)",
        error_lines[-1].strip(),
    )
    for error_line in error_lines[:-1]:
        error_line = error_line.strip()
        if not error_line:
            continue

        lineno = int(error_line.split(":")[1])
        errors[lineno] += error_line

    for i, line in enumerate(lines):
        lineno = i + 1
        if " E:" not in line and lineno not in errors:
            continue

        target_line = lines[lineno - 1]
        if "# E:" in target_line:
            marker = target_line.split("# E:")[-1].strip()
            assert lineno in errors, f'Extra error "{marker}"'
            assert marker in errors[lineno]
        else:
            pytest.fail(f"Error {repr(errors[lineno])} not found")


@pytest.mark.parametrize("path", iter_test_cases(REVEAL_DIR))
def test_reveal(path: str) -> None:
    """Reveal type annotations are correctly reported"""
    stdout, _, _ = mypy_api.run([path])

    with open(path, encoding="utf-8") as fin:
        lines = fin.readlines()

    for error_line in stdout.split("\n"):
        error_line = error_line.strip()
        if not error_line:
            continue
        if re.match(r"Success: no issues found in \d+ source files?", error_line):
            continue

        lineno = int(error_line.split(":")[1])
        assert "Revealed type is" in error_line
        marker = lines[lineno - 1].split("# E:")[-1].strip()
        assert marker in error_line


@pytest.mark.parametrize("path", iter_test_cases(PASS_DIR))
def test_code_runs(path: str) -> None:
    """Successfully typed code runs without exceptions"""
    dirname, filename = path.split(os.sep)[-2:]
    spec = importlib.util.spec_from_file_location(f"{dirname}.{filename}", path)
    assert spec is not None
    test_module = importlib.util.module_from_spec(spec)
    loader = spec.loader
    assert loader is not None
    loader.exec_module(test_module)


# TODO: add to CI:
# stubtest scipy.sparse --allowlist stubtest.allowlist
