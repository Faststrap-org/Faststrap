"""Theme and defaults utilities for Faststrap.

This module provides:
- Built-in color themes (10 themes)
- Dark/Light/Auto mode support for all themes
- Custom theme creation with mode support
- Component defaults system
"""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Style

# Mode type for theme variants
ModeType = Literal["light", "dark", "auto"]

# ============================================================================
# Built-in Theme Color Definitions
# These define the COLOR SCHEME only - mode (light/dark) is applied separately
# ============================================================================

_BUILTIN_THEMES: dict[str, dict[str, str]] = {
    "green-nature": {
        "--bs-primary": "#7BA05B",
        "--bs-primary-rgb": "123, 160, 91",
        "--bs-secondary": "#48C774",
        "--bs-secondary-rgb": "72, 199, 116",
        "--bs-info": "#36A3EB",
        "--bs-info-rgb": "54, 163, 235",
        "--bs-warning": "#FFC107",
        "--bs-warning-rgb": "255, 193, 7",
        "--bs-danger": "#FF6B6B",
        "--bs-danger-rgb": "255, 107, 107",
        "--bs-success": "#28A745",
        "--bs-success-rgb": "40, 167, 69",
    },
    "blue-ocean": {
        "--bs-primary": "#0D6EFD",
        "--bs-primary-rgb": "13, 110, 253",
        "--bs-secondary": "#6C757D",
        "--bs-secondary-rgb": "108, 117, 125",
        "--bs-info": "#17A2B8",
        "--bs-info-rgb": "23, 162, 184",
        "--bs-warning": "#FFC107",
        "--bs-warning-rgb": "255, 193, 7",
        "--bs-danger": "#DC3545",
        "--bs-danger-rgb": "220, 53, 69",
        "--bs-success": "#28A745",
        "--bs-success-rgb": "40, 167, 69",
    },
    "purple-magic": {
        "--bs-primary": "#6F42C1",
        "--bs-primary-rgb": "111, 66, 193",
        "--bs-secondary": "#E9ECEF",
        "--bs-secondary-rgb": "233, 236, 239",
        "--bs-info": "#17A2B8",
        "--bs-info-rgb": "23, 162, 184",
        "--bs-warning": "#FFC107",
        "--bs-warning-rgb": "255, 193, 7",
        "--bs-danger": "#DC3545",
        "--bs-danger-rgb": "220, 53, 69",
        "--bs-success": "#28A745",
        "--bs-success-rgb": "40, 167, 69",
    },
    "red-alert": {
        "--bs-primary": "#DC3545",
        "--bs-primary-rgb": "220, 53, 69",
        "--bs-secondary": "#6C757D",
        "--bs-secondary-rgb": "108, 117, 125",
        "--bs-info": "#17A2B8",
        "--bs-info-rgb": "23, 162, 184",
        "--bs-warning": "#FFC107",
        "--bs-warning-rgb": "255, 193, 7",
        "--bs-danger": "#FF6B6B",
        "--bs-danger-rgb": "255, 107, 107",
        "--bs-success": "#28A745",
        "--bs-success-rgb": "40, 167, 69",
    },
    "orange-sunset": {
        "--bs-primary": "#FD7E14",
        "--bs-primary-rgb": "253, 126, 20",
        "--bs-secondary": "#6C757D",
        "--bs-secondary-rgb": "108, 117, 125",
        "--bs-info": "#17A2B8",
        "--bs-info-rgb": "23, 162, 184",
        "--bs-warning": "#FFC107",
        "--bs-warning-rgb": "255, 193, 7",
        "--bs-danger": "#DC3545",
        "--bs-danger-rgb": "220, 53, 69",
        "--bs-success": "#28A745",
        "--bs-success-rgb": "40, 167, 69",
    },
    "teal-oasis": {
        "--bs-primary": "#20C997",
        "--bs-primary-rgb": "32, 201, 151",
        "--bs-secondary": "#6C757D",
        "--bs-secondary-rgb": "108, 117, 125",
        "--bs-info": "#17A2B8",
        "--bs-info-rgb": "23, 162, 184",
        "--bs-warning": "#FFC107",
        "--bs-warning-rgb": "255, 193, 7",
        "--bs-danger": "#DC3545",
        "--bs-danger-rgb": "220, 53, 69",
        "--bs-success": "#28A745",
        "--bs-success-rgb": "40, 167, 69",
    },
    "indigo-night": {
        "--bs-primary": "#6610F2",
        "--bs-primary-rgb": "102, 16, 242",
        "--bs-secondary": "#6C757D",
        "--bs-secondary-rgb": "108, 117, 125",
        "--bs-info": "#17A2B8",
        "--bs-info-rgb": "23, 162, 184",
        "--bs-warning": "#FFC107",
        "--bs-warning-rgb": "255, 193, 7",
        "--bs-danger": "#DC3545",
        "--bs-danger-rgb": "220, 53, 69",
        "--bs-success": "#28A745",
        "--bs-success-rgb": "40, 167, 69",
    },
    "pink-love": {
        "--bs-primary": "#E83E8C",
        "--bs-primary-rgb": "232, 62, 140",
        "--bs-secondary": "#6C757D",
        "--bs-secondary-rgb": "108, 117, 125",
        "--bs-info": "#17A2B8",
        "--bs-info-rgb": "23, 162, 184",
        "--bs-warning": "#FFC107",
        "--bs-warning-rgb": "255, 193, 7",
        "--bs-danger": "#DC3545",
        "--bs-danger-rgb": "220, 53, 69",
        "--bs-success": "#28A745",
        "--bs-success-rgb": "40, 167, 69",
    },
    "cyan-sky": {
        "--bs-primary": "#17A2B8",
        "--bs-primary-rgb": "23, 162, 184",
        "--bs-secondary": "#6C757D",
        "--bs-secondary-rgb": "108, 117, 125",
        "--bs-info": "#17A2B8",
        "--bs-info-rgb": "23, 162, 184",
        "--bs-warning": "#FFC107",
        "--bs-warning-rgb": "255, 193, 7",
        "--bs-danger": "#DC3545",
        "--bs-danger-rgb": "220, 53, 69",
        "--bs-success": "#28A745",
        "--bs-success-rgb": "40, 167, 69",
    },
    "gray-mist": {
        "--bs-primary": "#6C757D",
        "--bs-primary-rgb": "108, 117, 125",
        "--bs-secondary": "#ADB5BD",
        "--bs-secondary-rgb": "173, 181, 189",
        "--bs-info": "#17A2B8",
        "--bs-info-rgb": "23, 162, 184",
        "--bs-warning": "#FFC107",
        "--bs-warning-rgb": "255, 193, 7",
        "--bs-danger": "#DC3545",
        "--bs-danger-rgb": "220, 53, 69",
        "--bs-success": "#28A745",
        "--bs-success-rgb": "40, 167, 69",
    },
}

# ============================================================================
# Light/Dark Mode CSS Variable Definitions
# ============================================================================

_LIGHT_MODE_VARS: dict[str, str] = {
    "--bs-body-bg": "#ffffff",
    "--bs-body-color": "#212529",
    "--bs-light": "#F8F9FA",
    "--bs-light-rgb": "248, 249, 250",
    "--bs-dark": "#343A40",
    "--bs-dark-rgb": "52, 58, 64",
    "--bs-primary-text-emphasis": "#052c65",
    "--bs-primary-bg-subtle": "#e7f0ff",
    "--bs-primary-border-subtle": "#9ec5fe",
    "--bs-secondary-text-emphasis": "#2b2f32",
    "--bs-secondary-bg-subtle": "#f8f9fa",
    "--bs-secondary-border-subtle": "#e2e3e5",
    "--bs-tertiary-bg": "#f8f9fa",
    "--bs-emphasis-color": "#000000",
    "--bs-border-color": "#dee2e6",
    "--bs-heading-color": "inherit",
    "--bs-link-color": "#0d6efd",
    "--bs-link-hover-color": "#0a58ca",
    "--bs-code-color": "#d63384",
}

_DARK_MODE_VARS: dict[str, str] = {
    "--bs-body-bg": "#212529",
    "--bs-body-color": "#dee2e6",
    "--bs-light": "#343A40",
    "--bs-light-rgb": "52, 58, 64",
    "--bs-dark": "#121212",
    "--bs-dark-rgb": "18, 18, 18",
    "--bs-primary-text-emphasis": "#6ea8fe",
    "--bs-primary-bg-subtle": "#031633",
    "--bs-primary-border-subtle": "#084298",
    "--bs-secondary-text-emphasis": "#a7acb1",
    "--bs-secondary-bg-subtle": "#212529",
    "--bs-secondary-border-subtle": "#495057",
    "--bs-tertiary-bg": "#2b3035",
    "--bs-emphasis-color": "#ffffff",
    "--bs-border-color": "#495057",
    "--bs-heading-color": "inherit",
    "--bs-link-color": "#6ea8fe",
    "--bs-link-hover-color": "#8bb9fe",
    "--bs-code-color": "#e685b5",
}


# ============================================================================
# Theme Class
# ============================================================================


class Theme:
    """Theme definition for Faststrap.

    A Theme contains color variables (primary, secondary, etc.) and can
    generate CSS for light mode, dark mode, or auto mode.

    Example:
        >>> theme = Theme({"--bs-primary": "#7BA05B"})
        >>> style = theme.to_style(mode="dark")
    """

    def __init__(self, variables: dict[str, str]):
        """Initialize theme with color variables.

        Args:
            variables: CSS variable definitions for colors (primary, secondary, etc.)
        """
        self.variables = variables

    def _get_mode_vars(self, mode: Literal["light", "dark"]) -> dict[str, str]:
        """Get CSS variables for a specific mode."""
        base_mode_vars = _LIGHT_MODE_VARS if mode == "light" else _DARK_MODE_VARS
        merged = {**base_mode_vars, **self.variables}

        # Smart mapping: If user provided a "dark" or "light" color,
        # use it for the body background in that mode.
        if mode == "dark" and "--bs-dark" in self.variables:
            merged["--bs-body-bg"] = self.variables["--bs-dark"]
            merged["--bs-tertiary-bg"] = self.variables["--bs-dark"]
        elif mode == "light" and "--bs-light" in self.variables:
            merged["--bs-body-bg"] = self.variables["--bs-light"]
            merged["--bs-tertiary-bg"] = self.variables["--bs-light"]

        return merged

    def to_style(self, mode: ModeType = "auto") -> Style:
        """Convert theme to FastHTML Style element.

        This generates CSS variables for light and dark modes, and adds
        overrides to ensure components use the custom theme colors.

        Args:
            mode: Initial mode ("light", "dark", or "auto")

        Returns:
            FastHTML Style element with CSS variables
        """
        light_vars = self._get_mode_vars("light")
        dark_vars = self._get_mode_vars("dark")

        light_css = "; ".join(f"{k}: {v}" for k, v in light_vars.items())
        dark_css = "; ".join(f"{k}: {v}" for k, v in dark_vars.items())

        # Determine initial variables for :root
        if mode == "auto":
            initial_css = f"""
            {light_css};
            @media (prefers-color-scheme: dark) {{
                {dark_css};
            }}
            """
        else:
            initial_css = light_css if mode == "light" else dark_css

        # Build comprehensive CSS with overrides for specific components
        # that don't always inherit correctly from :root variables.
        css_content = f"""
:root {{ {initial_css} }}
[data-bs-theme="light"] {{ {light_css} }}
[data-bs-theme="dark"] {{ {dark_css} }}

/* Component overrides for custom theme colors */
.btn-primary {{
    --bs-btn-bg: var(--bs-primary); --bs-btn-border-color: var(--bs-primary);
    --bs-btn-hover-bg: var(--bs-primary); --bs-btn-hover-border-color: var(--bs-primary);
    --bs-btn-active-bg: var(--bs-primary); --bs-btn-active-border-color: var(--bs-primary);
    filter: saturate(1.2) brightness(0.95);
}}
.btn-secondary {{ --bs-btn-bg: var(--bs-secondary); --bs-btn-border-color: var(--bs-secondary); }}
.btn-success {{ --bs-btn-bg: var(--bs-success); --bs-btn-border-color: var(--bs-success); }}
.btn-danger {{ --bs-btn-bg: var(--bs-danger); --bs-btn-border-color: var(--bs-danger); }}
.btn-warning {{ --bs-btn-bg: var(--bs-warning); --bs-btn-border-color: var(--bs-warning); }}
.btn-info {{ --bs-btn-bg: var(--bs-info); --bs-btn-border-color: var(--bs-info); }}

.badge.bg-primary {{ background-color: var(--bs-primary) !important; }}
.badge.bg-secondary {{ background-color: var(--bs-secondary) !important; }}
.text-bg-primary {{ background-color: var(--bs-primary) !important; }}
.text-bg-secondary {{ background-color: var(--bs-secondary) !important; }}

.progress-bar {{ background-color: var(--bs-primary); }}
.spinner-border.text-primary, .spinner-grow.text-primary {{ color: var(--bs-primary) !important; }}
"""
        return Style(css_content.strip())

    def to_dict(self) -> dict[str, str]:
        """Return theme color variables as dict."""
        return self.variables.copy()

    def __repr__(self) -> str:
        primary = self.variables.get("--bs-primary", "default")
        return f"Theme(primary={primary})"


# ============================================================================
# Theme Factory Functions
# ============================================================================


def create_theme(
    primary: str | None = None,
    secondary: str | None = None,
    success: str | None = None,
    danger: str | None = None,
    warning: str | None = None,
    info: str | None = None,
    **extra_vars: str,
) -> Theme:
    """Create a custom theme from color values.

    Args:
        primary: Primary color (e.g., "#7BA05B")
        secondary: Secondary color
        success: Success color (defaults to Bootstrap green)
        danger: Danger color (defaults to Bootstrap red)
        warning: Warning color (defaults to Bootstrap yellow)
        info: Info color (defaults to Bootstrap cyan)
        **extra_vars: Additional CSS variables

    Returns:
        Theme instance

    Example:
        >>> theme = create_theme(
        ...     primary="#7BA05B",
        ...     secondary="#48C774",
        ... )
        >>> add_bootstrap(app, theme=theme, mode="dark")
    """
    variables: dict[str, str] = {}

    # Add provided colors with auto-generated RGB values
    color_map = {
        "primary": primary,
        "secondary": secondary,
        "success": success,
        "danger": danger,
        "warning": warning,
        "info": info,
    }

    for name, color in color_map.items():
        if color:
            variables[f"--bs-{name}"] = color
            # Auto-generate RGB value from hex
            rgb = _hex_to_rgb(color)
            if rgb:
                variables[f"--bs-{name}-rgb"] = rgb

    # Add any extra variables
    for key, value in extra_vars.items():
        # Normalize key to CSS variable format
        if not key.startswith("--"):
            key = f"--bs-{key.replace('_', '-')}"
        variables[key] = value

    return Theme(variables)


def _hex_to_rgb(hex_color: str) -> str | None:
    """Convert hex color to RGB string."""
    try:
        hex_color = hex_color.lstrip("#")
        if len(hex_color) == 3:
            hex_color = "".join(c * 2 for c in hex_color)
        if len(hex_color) != 6:
            return None
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return f"{r}, {g}, {b}"
    except (ValueError, IndexError):
        return None


def get_builtin_theme(name: str) -> Theme:
    """Get a built-in theme by name.

    Args:
        name: Theme name (e.g., "green-nature", "blue-ocean")

    Returns:
        Theme instance

    Raises:
        ValueError: If theme name is not found
    """
    if name not in _BUILTIN_THEMES:
        available = ", ".join(sorted(_BUILTIN_THEMES.keys()))
        raise ValueError(f"Unknown theme: '{name}'. Available themes: {available}")
    return Theme(_BUILTIN_THEMES[name])


def list_builtin_themes() -> list[str]:
    """List all available built-in theme names.

    Returns:
        List of theme names
    """
    return list(_BUILTIN_THEMES.keys())


# ============================================================================
# Component Defaults System
# ============================================================================

# Base default values for all components (immutable reference)
_DEFAULT_COMPONENT_DEFAULTS: dict[str, dict[str, Any]] = {
    "Alert": {"variant": "primary", "dismissible": False},
    "Badge": {"variant": "primary", "pill": False},
    "Breadcrumb": {},
    "Button": {"variant": "primary", "size": None, "outline": False},
    "Card": {"header_cls": "", "body_cls": "", "footer_cls": ""},
    "Drawer": {"placement": "start", "backdrop": True},
    "Dropdown": {"variant": "primary", "direction": "down"},
    "Input": {"size": None, "input_type": "text"},
    "Modal": {"size": None, "centered": False, "scrollable": False},
    "Navbar": {"expand": "lg", "color_scheme": "light"},
    "Pagination": {"size": None, "align": "start"},
    "Progress": {"variant": "primary", "striped": False, "animated": False},
    "Select": {"size": None},
    "Spinner": {"variant": "primary", "size": None, "spinner_type": "border"},
    "Tabs": {"variant": "tabs", "fill": False, "justified": False},
    "Toast": {"autohide": True, "delay": 5000},
}

# Mutable working copy of defaults (can be modified via set_component_defaults)
_COMPONENT_DEFAULTS: dict[str, dict[str, Any]] = {
    k: v.copy() for k, v in _DEFAULT_COMPONENT_DEFAULTS.items()
}


def get_component_defaults(component: str) -> dict[str, Any]:
    """Get default values for a component.

    Args:
        component: Component name (e.g., "Button")

    Returns:
        Dict of default values
    """
    return _COMPONENT_DEFAULTS.get(component, {}).copy()


def set_component_defaults(component: str, **defaults: Any) -> None:
    """Set default values for a component globally.

    Args:
        component: Component name (e.g., "Button")
        **defaults: Default values to set

    Example:
        >>> set_component_defaults("Button", variant="outline-primary", size="sm")
        >>> # Now all Button() calls use these defaults unless overridden
    """
    if component not in _COMPONENT_DEFAULTS:
        _COMPONENT_DEFAULTS[component] = {}
    _COMPONENT_DEFAULTS[component].update(defaults)


def reset_component_defaults(component: str | None = None) -> None:
    """Reset component defaults to original values.

    Args:
        component: Component name to reset, or None to reset all
    """
    global _COMPONENT_DEFAULTS

    if component is None:
        # Reset all components to original defaults
        _COMPONENT_DEFAULTS = {
            k: v.copy() for k, v in _DEFAULT_COMPONENT_DEFAULTS.items()
        }
    elif component in _DEFAULT_COMPONENT_DEFAULTS:
        # Reset specific component to original default
        _COMPONENT_DEFAULTS[component] = _DEFAULT_COMPONENT_DEFAULTS[component].copy()


def resolve_defaults(component: str, **kwargs: Any) -> dict[str, Any]:
    """Resolve component attributes by merging defaults with user arguments.

    Priority (highest to lowest):
    1. Explicit user arguments (if not None)
    2. Global component defaults (set via set_component_defaults)

    Args:
        component: Component name (e.g., "Button")
        **kwargs: Arguments passed by the user

    Returns:
        Dict of resolved attributes

    Example:
        >>> set_component_defaults("Button", variant="secondary")
        >>> resolve_defaults("Button", variant=None, size="lg")
        {"variant": "secondary", "size": "lg"}
    """
    defaults = get_component_defaults(component)
    resolved = defaults.copy()

    for key, value in kwargs.items():
        if value is not None:
            resolved[key] = value

    return resolved
