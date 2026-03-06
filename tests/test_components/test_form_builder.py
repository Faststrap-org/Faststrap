"""Tests for Form.from_pydantic builder."""

from __future__ import annotations

from enum import Enum
from typing import Literal

from fasthtml.common import to_xml
from pydantic import BaseModel, EmailStr

from faststrap.components.forms.form import Form


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"


class SignupModel(BaseModel):
    email: EmailStr
    age: int
    ratio: float = 1.5
    role: Role = Role.USER
    status: Literal["active", "disabled"] = "active"
    marketing_opt_in: bool = False


def test_form_from_pydantic_generates_expected_fields() -> None:
    form = Form.from_pydantic(SignupModel, action="/signup")
    html = to_xml(form)

    assert 'action="/signup"' in html
    assert 'name="email"' in html
    assert 'type="email"' in html
    assert 'name="age"' in html
    assert 'type="number"' in html
    assert 'name="ratio"' in html
    assert 'step="any"' in html
    assert 'name="role"' in html
    assert 'name="status"' in html
    assert 'name="marketing_opt_in"' in html
    assert 'type="checkbox"' in html
    assert "btn btn-primary" in html


def test_form_from_pydantic_supports_include_exclude() -> None:
    form = Form.from_pydantic(SignupModel, include=["email", "age"], exclude=["age"])
    html = to_xml(form)

    assert 'name="email"' in html
    assert 'name="age"' not in html
    assert 'name="role"' not in html


def test_form_from_pydantic_rejects_non_model() -> None:
    try:
        Form.from_pydantic(dict)  # type: ignore[arg-type]
        raise AssertionError("Expected TypeError for non-Pydantic model")
    except TypeError as exc:
        assert "BaseModel class" in str(exc)
