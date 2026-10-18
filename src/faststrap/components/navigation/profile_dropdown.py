"""ProfileDropdown authenticated user menu component."""

from __future__ import annotations

from typing import Any, Literal, cast

from fasthtml.common import A, Div, Hr, Img, Span
from fasthtml.common import Button as FTButton

from ...core._stability import experimental
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...utils.attrs import convert_attrs

AvatarSize = int
ProfileTriggerContent = Literal["avatar", "avatar-name", "avatar-name-subtitle"]


@register(category="navigation")
@experimental
def ProfileDropdown(
    name: str,
    *,
    subtitle: str | None = None,
    src: str | None = None,
    items: list[tuple[str, str]] | list[tuple[str, str, dict[str, Any]]] | None = None,
    alignment: str | None = UNSET,
    avatar_size: int | None = UNSET,
    layout: Literal["horizontal", "stacked"] | None = UNSET,
    trigger_content: ProfileTriggerContent | None = UNSET,
    mobile_content: ProfileTriggerContent | None = UNSET,
    trigger_cls: str = "",
    menu_cls: str = "",
    item_cls: str = "",
    footer: Any | None = None,
    **kwargs: Any,
) -> Div:
    """Authenticated user menu for dashboards and portals.

    Renders a dropdown toggle showing the user's avatar/initials and a
    menu of account actions. The toggle is a native ``<button>`` so the
    menu opens via mouse click, ``Enter``, or ``Space``, and menu items
    render as real ``<a>`` links so navigation works without custom
    JavaScript.

    Args:
        name: User display name.
        subtitle: Optional role, team, or email shown below (``stacked``)
            or beside (``horizontal``) the name.
        src: Optional avatar image URL. When omitted, initials are shown.
        items: Optional menu entries as ``(label, href)`` tuples or
            ``(label, href, attrs)`` where ``attrs`` merges extra HTML
            attributes onto the anchor (e.g. ``{"hx_get": "/logout"}``).
        alignment: Bootstrap dropdown menu alignment, typically ``"end"``.
        avatar_size: Avatar edge length in pixels (default 32).
        layout: Trigger text arrangement: ``"horizontal"`` keeps the
            subtitle on one line beside the name; ``"stacked"`` reproduces
            the original block layout.
        trigger_content: Content shown in the desktop trigger: ``"avatar"``
            (avatar only), ``"avatar-name"`` (avatar and name), or
            ``"avatar-name-subtitle"`` (all identity context).
        mobile_content: Optional compact trigger content for small screens.
            Uses the same values as ``trigger_content``. When omitted, the
            desktop content is shown at every breakpoint.
        trigger_cls: Extra classes for the dropdown toggle button.
        menu_cls: Extra classes for the dropdown menu.
        item_cls: Extra classes for each menu anchor.
        footer: Optional element rendered after the items inside the menu
            (wrapped in a bordered footer section when present).
        **kwargs: Additional HTML attributes for the wrapper.

    Returns:
        FastHTML ``Div`` element containing the profile dropdown.
    """
    cfg = resolve_defaults(
        "ProfileDropdown",
        alignment=alignment,
        avatar_size=avatar_size,
        layout=layout,
        trigger_content=trigger_content,
        mobile_content=mobile_content,
    )
    c_alignment = str(cfg.get("alignment") or "end")
    c_avatar_size = cast(AvatarSize, cfg.get("avatar_size") or 32)
    c_layout = str(cfg.get("layout") or "stacked")
    default_content: ProfileTriggerContent = "avatar-name-subtitle" if subtitle else "avatar-name"
    c_trigger_content = cast(ProfileTriggerContent, cfg.get("trigger_content") or default_content)
    c_mobile_content = cast(ProfileTriggerContent, cfg.get("mobile_content") or c_trigger_content)

    user_cls = kwargs.pop("cls", "")
    base_cls = "faststrap-profile-dropdown dropdown"

    initials = "".join(part[0] for part in name.split()[:2]).upper()
    inline_size = f"width: {c_avatar_size}px; height: {c_avatar_size}px;"
    font_size = f"{max(0.625, round(c_avatar_size / 46.0, 3))}rem"
    avatar_content: Any
    if src:
        avatar_content = Img(
            src=src,
            alt=name,
            cls="rounded-circle",
            width=c_avatar_size,
            height=c_avatar_size,
        )
    else:
        avatar_content = Span(
            initials,
            cls="rounded-circle bg-primary text-white d-inline-flex align-items-center justify-content-center",
            style=f"{inline_size} font-size: {font_size};",
        )

    avatar_wrapper_cls = "me-2 flex-shrink-0"

    def text_content(content: ProfileTriggerContent) -> Any | None:
        if content == "avatar":
            return None
        name_el = Span(name, cls="fw-semibold text-truncate")
        if content == "avatar-name" or not subtitle:
            return Span(name_el, cls="text-start text-truncate")
        subtitle_el = Span(subtitle, cls="text-muted small text-truncate")
        if c_layout == "horizontal":
            return Span(
                name_el,
                subtitle_el,
                cls="d-inline-flex align-items-baseline gap-2 text-start text-truncate",
                style="max-width: 14rem;",
            )
        return Span(
            name_el,
            subtitle_el,
            cls="d-flex flex-column align-items-start text-start lh-sm",
        )

    desktop_text = text_content(c_trigger_content)
    mobile_text = text_content(c_mobile_content)
    toggle_inner_children = [Span(avatar_content, cls=avatar_wrapper_cls)]
    if desktop_text is not None:
        desktop_cls = ""
        if c_mobile_content != c_trigger_content:
            desktop_cls = "d-none d-sm-inline-flex"
        if desktop_cls:
            desktop_text.attrs["class"] = merge_classes(
                desktop_text.attrs.get("class", ""), desktop_cls
            )
        toggle_inner_children.append(desktop_text)
    if mobile_text is not None and c_mobile_content != c_trigger_content:
        mobile_text.attrs["class"] = merge_classes(
            mobile_text.attrs.get("class", ""), "d-inline-flex d-sm-none"
        )
        toggle_inner_children.append(mobile_text)

    menu_children: list[Any] = []
    if items:
        for entry in items:
            label, href = entry[0], entry[1]
            extra_attrs = entry[2] if len(entry) > 2 else {}
            menu_children.append(
                A(label, href=href, cls=merge_classes("dropdown-item", item_cls), **extra_attrs)
            )

    if footer is not None:
        menu_children.append(Hr(cls="dropdown-divider"))
        menu_children.append(Div(footer, cls="px-3 py-2"))

    has_menu = bool(menu_children)
    menu = (
        Div(
            *menu_children,
            cls=merge_classes(f"dropdown-menu dropdown-menu-{c_alignment}", menu_cls),
        )
        if has_menu
        else None
    )

    toggle_kwargs: dict[str, Any] = {"type": "button", "aria_label": name}
    if has_menu:
        toggle_kwargs.update(
            {
                "data_bs_toggle": "dropdown",
                "aria_expanded": "false",
                "aria_haspopup": "true",
            }
        )

    toggle = FTButton(
        *toggle_inner_children,
        cls=merge_classes(
            "dropdown-toggle bg-transparent border-0 d-inline-flex align-items-center", trigger_cls
        ),
        **toggle_kwargs,
    )

    attrs: dict[str, Any] = {
        "cls": merge_classes(base_cls, user_cls),
    }
    attrs.update(convert_attrs(kwargs))

    return Div(
        Div(
            toggle,
            menu,
        ),
        **attrs,
    )
