"""Stability markers for Faststrap components."""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

F = TypeVar("F", bound=Callable)


def stable(func: F) -> F:
    """
    Mark component as stable (API won't break in minor versions).

    Usage:
        @stable
        def Button(...): ...
    """
    # Use setattr to allow type checkers to see the attribute if needed
    # but primarily this is for runtime inspection/documentation
    func.__faststrap_stable__ = True  # type: ignore[attr-defined]
    func.__faststrap_stability__ = "stable"  # type: ignore[attr-defined]
    return func


def beta(func: F) -> F:
    """
    Mark component as beta (API may change in minor versions).

    Usage:
        @beta
        def NewComponent(...): ...
    """
    func.__faststrap_beta__ = True  # type: ignore[attr-defined]
    func.__faststrap_stability__ = "beta"  # type: ignore[attr-defined]
    return func


def experimental(func: F) -> F:
    """
    Mark component as experimental (API will likely change).

    Usage:
        @experimental
        def ExperimentalComp(...): ...
    """
    func.__faststrap_experimental__ = True  # type: ignore[attr-defined]
    func.__faststrap_stability__ = "experimental"  # type: ignore[attr-defined]
    return func
