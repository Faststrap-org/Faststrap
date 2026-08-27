"""Shared visual tokens for consistent component surfaces.

These helpers give Faststrap components a common vocabulary for radius and
shadow so that custom surfaces (toasts, cards, floating elements) can be
tuned without guessing at raw Bootstrap utility classes.

Values intentionally mirror Bootstrap 5.3 utilities:

- radius: ``none`` -> ``rounded-0``, ``sm`` -> ``rounded-2``,
  ``md`` -> ``rounded-3``, ``lg`` -> ``rounded-4``, ``pill`` -> ``rounded-pill``
- shadow: ``none`` -> ``shadow-none``, ``sm`` -> ``shadow-sm``,
  ``md`` -> ``shadow``, ``lg`` -> ``shadow-lg``
"""

from __future__ import annotations

from typing import Literal

RadiusToken = Literal["none", "sm", "md", "lg", "pill"]
ShadowToken = Literal["none", "sm", "md", "lg"]

RADIUS_CLASSES: dict[str, str] = {
    "none": "rounded-0",
    "sm": "rounded-2",
    "md": "rounded-3",
    "lg": "rounded-4",
    "pill": "rounded-pill",
}

SHADOW_CLASSES: dict[str, str] = {
    "none": "shadow-none",
    "sm": "shadow-sm",
    "md": "shadow",
    "lg": "shadow-lg",
}


def radius_class(
    radius: RadiusToken | str | None,
) -> str:
    """Return the Bootstrap border-radius utility for a token.

    ``None`` or unknown values return an empty string so callers keep their
    component's own default rounding.
    """
    if not radius:
        return ""
    return RADIUS_CLASSES.get(str(radius), "")


def shadow_class(shadow: ShadowToken | str | None) -> str:
    """Return the Bootstrap box-shadow utility for a token.

    ``None`` or unknown values return an empty string so callers keep their
    component's own default shadow.
    """
    if not shadow:
        return ""
    return SHADOW_CLASSES.get(str(shadow), "")
