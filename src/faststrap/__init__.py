"""FastStrap - Modern Bootstrap 5 components for FastHTML.

Build beautiful web UIs in pure Python with zero JavaScript knowledge.
"""

__version__ = "0.1.0"
__author__ = "FastStrap Contributors"
__license__ = "MIT"

# Core functionality
from .core.assets import add_bootstrap, get_assets
from .core.base import merge_classes

# Components
from .components.forms.button import Button
from .utils.icons import Icon

__all__ = [
    # Core
    "add_bootstrap",
    "get_assets",
    "merge_classes",
    # Components
    "Button",
    "Icon",
    # Metadata
    "__version__",
    "__author__",
    "__license__",
]