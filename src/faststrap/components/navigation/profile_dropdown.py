"""ProfileDropdown authenticated user menu component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import A, Div, Img, Span

from ...core._stability import experimental
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="navigation")
@experimental
def ProfileDropdown(
    name: str,
    *,
    subtitle: str | None = None,
    src: str | None = None,
    items: list[tuple[str, str]] | None = None,
    alignment: str = "end",
    **kwargs: Any,
) -> Div:
    """Authenticated user menu for dashboards and portals.

    Renders a dropdown toggle showing the user's avatar/initials and a
    menu of account actions.

    Args:
        name: User display name.
        subtitle: Optional role, team, or email shown below the name.
        src: Optional avatar image URL. When omitted, initials are shown.
        items: Optional list of ``(label, href)`` tuples for the dropdown
            menu. When ``None``, an empty dropdown is rendered.
        alignment: Bootstrap dropdown menu alignment, typically
            ``"end"`` for right-aligned menus.
        **kwargs: Additional HTML attributes for the wrapper.

    Returns:
        FastHTML ``Div`` element containing the profile dropdown.
    """
    user_cls = kwargs.pop("cls", "")
    base_cls = "faststrap-profile-dropdown dropdown"

    initials = "".join(part[0] for part in name.split()[:2]).upper()
    avatar_content: Any
    if src:
        avatar_content = Img(src=src, alt=name, cls="rounded-circle", width=32, height=32)
    else:
        avatar_content = Span(
            initials,
            cls="rounded-circle bg-primary text-white d-inline-flex align-items-center justify-content-center",
            style="width: 32px; height: 32px; font-size: 0.875rem;",
        )

    toggle_inner_children: list[Any] = [
        Span(avatar_content, cls="me-2"),
        Span(name, cls="d-none d-lg-inline"),
    ]
    if subtitle:
        toggle_inner_children.append(
            Span(subtitle, cls="d-block w-100 text-muted small", style="font-size: 0.75rem;")
        )

    toggle = Div(
        *toggle_inner_children,
        cls="dropdown-toggle",
        data_bs_toggle="dropdown",
        aria_expanded="false",
        aria_haspopup="true",
        role="button",
        tabindex="0",
    )

    menu_children: list[Any] = []
    if items:
        for label, href in items:
            menu_children.append(A(label, href=href, cls="dropdown-item"))

    menu = Div(*menu_children, cls=f"dropdown-menu dropdown-menu-{alignment}") if items else None

    attrs: dict[str, Any] = {
        "cls": merge_classes(base_cls, user_cls),
    }
    if items:
        attrs["data_fs_items"] = "true"
    attrs.update(convert_attrs(kwargs))

    return Div(
        Div(
            toggle,
            menu,
        ),
        **attrs,
    )
