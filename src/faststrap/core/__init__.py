"""Core functionality for FastStrap."""

from .assets import add_bootstrap, get_assets
from .base import BaseComponent, Component, merge_classes

__all__ = ["add_bootstrap", "get_assets", "Component", "BaseComponent", "merge_classes"]
