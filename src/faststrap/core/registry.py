"""Component registry for FastStrap."""

from __future__ import annotations

import warnings
from collections.abc import Callable
from typing import Any, TypeVar

# Global registry for component metadata
_component_registry: dict[str, dict[str, Any]] = {}

F = TypeVar("F", bound=Callable[..., Any])


def register(
    name: str | None = None,
    category: str | None = None,
    bootstrap_version: str = "5.3.3",
    requires_js: bool = False,
) -> Callable[[F], F]:
    """Decorator to register component metadata.
    Args:
        name: Component name (defaults to function name)
        category: Component category (layout, display, etc.)
        bootstrap_version: Min Bootstrap version required
        requires_js: Whether component needs Bootstrap JS
    Example:
        >>> @register(category="feedback", requires_js=True)
        >>> def Modal(...): ...
    """

    def decorator(func: F) -> F:
        component_name = name or func.__name__

        _component_registry[component_name] = {
            "func": func,
            "category": category,
            "bootstrap_version": bootstrap_version,
            "requires_js": requires_js,
            "module": func.__module__,
            "doc": func.__doc__,
        }

        # Mark function as registered (Ruff B010 requires 'noqa', MyPy requires 'type: ignore')
        # fmt: off
        setattr(func, "__faststrap_registered__", True)  # noqa: B010 # type: ignore[attr-defined]
        setattr(func, "__faststrap_metadata__", _component_registry[component_name])  # noqa: B010 # type: ignore[attr-defined]
        # fmt: on

        return func

    return decorator


def get_registry() -> dict[str, dict[str, Any]]:
    """Get copy of component registry."""
    return _component_registry.copy()


def get_component(name: str) -> Callable[..., Any] | None:
    """Get component function by name."""
    return _component_registry.get(name, {}).get("func")


def list_components(category: str | None = None) -> list[str]:
    """List all registered components, optionally filtered by category.
    Args:
        category: Filter by category (layout, display, feedback, etc.)
    Returns:
        List of component names
    Example:
        >>> list_components(category="feedback")
        ['Alert', 'Toast', 'Modal', 'Spinner']
    """
    if category is None:
        return list(_component_registry.keys())

    return [name for name, meta in _component_registry.items() if meta.get("category") == category]


def autodiscover() -> None:
    """Auto-discover and register all components."""
    import importlib
    import pkgutil

    try:
        from faststrap import components

        # Recursively import all component modules
        for module_info in pkgutil.walk_packages(
            components.__path__, prefix="faststrap.components."
        ):
            try:
                # Access the .name attribute
                importlib.import_module(module_info.name)
            except ImportError as e:
                # Added stacklevel=2 so the warning points to the import context
                warnings.warn(
                    f"Could not import {module_info.name}: {e}",
                    ImportWarning,
                    stacklevel=2,
                )

    except ImportError:
        pass  # Components not yet installed


# Call autodiscover when registry is imported
autodiscover()
