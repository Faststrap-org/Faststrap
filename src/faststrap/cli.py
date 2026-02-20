"""Faststrap CLI."""

from __future__ import annotations

import argparse
import importlib
import os
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DoctorIssue:
    level: str
    code: str
    message: str


def _iter_python_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.py"):
        if ".venv" in path.parts or "site-packages" in path.parts:
            continue
        yield path


def check_import_source(root: Path) -> list[DoctorIssue]:
    issues: list[DoctorIssue] = []
    mod = importlib.import_module("faststrap")
    mod_path = Path(mod.__file__ or "").resolve()
    if "site-packages" in mod_path.parts and (root / "src" / "faststrap").exists():
        issues.append(
            DoctorIssue(
                level="warn",
                code="import-source",
                message=f"Imported faststrap from site-packages: {mod_path}",
            )
        )
    return issues


def check_static_mount_conflicts(root: Path) -> list[DoctorIssue]:
    issues: list[DoctorIssue] = []
    for file in _iter_python_files(root):
        text = file.read_text(encoding="utf-8", errors="ignore")
        if "mount_assets(" not in text:
            continue
        if 'url_path="/static"' in text and "allow_override=True" not in text:
            issues.append(
                DoctorIssue(
                    level="warn",
                    code="static-conflict",
                    message=f"Potential /static conflict in {file}",
                )
            )
    return issues


def check_toast_container(root: Path) -> list[DoctorIssue]:
    issues: list[DoctorIssue] = []
    has_toast_response = False
    has_container = False
    for file in _iter_python_files(root):
        text = file.read_text(encoding="utf-8", errors="ignore")
        if "toast_response(" in text:
            has_toast_response = True
        if "ToastContainer(" in text:
            has_container = True
    if has_toast_response and not has_container:
        issues.append(
            DoctorIssue(
                level="warn",
                code="missing-toast-container",
                message="Found toast_response usage but no ToastContainer found in project files.",
            )
        )
    return issues


def check_common_preset_misuse(root: Path) -> list[DoctorIssue]:
    issues: list[DoctorIssue] = []
    for file in _iter_python_files(root):
        text = file.read_text(encoding="utf-8", errors="ignore")
        if "ActiveSearch(" in text and "target=" not in text:
            issues.append(
                DoctorIssue(
                    level="warn",
                    code="preset-target",
                    message=f"ActiveSearch call may be missing target in {file}",
                )
            )
    return issues


def run_doctor(path: str = ".") -> int:
    root = Path(path).resolve()
    all_issues = [
        *check_import_source(root),
        *check_static_mount_conflicts(root),
        *check_toast_container(root),
        *check_common_preset_misuse(root),
    ]
    if not all_issues:
        print("faststrap doctor: OK")
        return 0

    print("faststrap doctor: issues found")
    for issue in all_issues:
        print(f"[{issue.level}] {issue.code}: {issue.message}")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(prog="faststrap", description="Faststrap CLI")
    subparsers = parser.add_subparsers(dest="command")

    doctor = subparsers.add_parser("doctor", help="Run Faststrap diagnostics")
    doctor.add_argument("--path", default=os.getcwd(), help="Project path to scan")

    args = parser.parse_args()
    if args.command == "doctor":
        return run_doctor(path=args.path)

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
