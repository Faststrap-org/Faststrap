"""Helpers for mapping backend validation errors to FormGroup."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .formgroup import FormGroup


def extract_field_error(errors: Mapping[str, Any] | None, field: str) -> str | None:
    """Extract a single displayable error message for a field."""
    if not errors or field not in errors:
        return None
    value = errors[field]
    if isinstance(value, str):
        return value
    if isinstance(value, (list, tuple)):
        if not value:
            return None
        return str(value[0])
    if isinstance(value, dict):
        if "msg" in value:
            return str(value["msg"])
        if "message" in value:
            return str(value["message"])
    return str(value)


def map_formgroup_validation(
    errors: Mapping[str, Any] | None,
    field: str,
) -> dict[str, Any]:
    """Return FormGroup-ready validation flags for a given field."""
    error = extract_field_error(errors, field)
    return {
        "error": error,
        "is_invalid": bool(error),
    }


def FormGroupFromErrors(
    input_element: Any,
    field: str,
    errors: Mapping[str, Any] | None = None,
    **kwargs: Any,
) -> Any:
    """Build FormGroup and auto-apply backend error state for one field."""
    mapping = map_formgroup_validation(errors, field)
    return FormGroup(input_element, **mapping, **kwargs)
