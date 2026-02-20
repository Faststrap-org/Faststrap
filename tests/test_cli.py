"""Tests for Faststrap CLI doctor checks."""

from pathlib import Path

from faststrap.cli import check_common_preset_misuse, check_toast_container


def test_doctor_missing_toast_container(tmp_path: Path):
    app_file = tmp_path / "app.py"
    app_file.write_text(
        "from faststrap.presets import toast_response\n"
        "def x():\n"
        "    return toast_response(content='ok', message='done')\n",
        encoding="utf-8",
    )
    issues = check_toast_container(tmp_path)
    assert any(issue.code == "missing-toast-container" for issue in issues)


def test_doctor_preset_target_warning(tmp_path: Path):
    app_file = tmp_path / "app.py"
    app_file.write_text(
        "from faststrap.presets import ActiveSearch\nActiveSearch('/x')", encoding="utf-8"
    )
    issues = check_common_preset_misuse(tmp_path)
    assert any(issue.code == "preset-target" for issue in issues)
