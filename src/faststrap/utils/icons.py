"""Bootstrap Icons utilities."""

from typing import Any

from fasthtml.common import I


def Icon(name: str, **kwargs: Any) -> I:
    """Create a Bootstrap Icon.

    Args:
        name: Icon name from Bootstrap Icons (e.g., 'heart', 'star-fill')
        **kwargs: Additional attributes

    Returns:
        I element with Bootstrap icon class

    Example:
        >>> Icon("heart-fill", cls="text-danger")
    """
    cls = kwargs.pop("cls", "")
    return I(cls=f"bi bi-{name} {cls}".strip(), **kwargs)
