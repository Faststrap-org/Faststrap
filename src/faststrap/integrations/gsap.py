"""Optional GSAP motion integration.

The integration is CDN-first and opt-in. Core Faststrap keeps using `Fx` for
zero-JS effects; this module is for projects that explicitly want richer motion.
"""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, NotStr, Script

from ..core.base import merge_classes
from ..utils.attrs import convert_attrs

GSAP_VERSION = "3.12.5"
GSAP_CDN_URL = f"https://cdn.jsdelivr.net/npm/gsap@{GSAP_VERSION}/dist/gsap.min.js"

GsapPreset = Literal[
    "fade",
    "fade-up",
    "fade-down",
    "slide-left",
    "slide-right",
    "scale",
    "pop",
]
MotionPreset = GsapPreset

VALID_GSAP_PRESETS = {
    "fade",
    "fade-up",
    "fade-down",
    "slide-left",
    "slide-right",
    "scale",
    "pop",
}

GSAP_INIT_SCRIPT = """
(() => {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const presets = {
    fade: { opacity: 0 },
    "fade-up": { opacity: 0, y: 24 },
    "fade-down": { opacity: 0, y: -24 },
    "slide-left": { opacity: 0, x: 32 },
    "slide-right": { opacity: 0, x: -32 },
    scale: { opacity: 0, scale: 0.96 },
    pop: { opacity: 0, scale: 0.92, y: 8 }
  };

  const readNumber = (value, fallback) => {
    if (value === undefined || value === null || value === "") return fallback;
    const parsed = Number(value);
    return Number.isFinite(parsed) ? parsed : fallback;
  };

  const init = (scope = document) => {
    if (!window.gsap || reducedMotion.matches) return;

    scope.querySelectorAll("[data-fs-gsap]").forEach((element) => {
      if (element.dataset.fsGsapInit === "true") return;
      element.dataset.fsGsapInit = "true";

      const presetName = element.dataset.fsGsap || "fade-up";
      const preset = presets[presetName] || presets["fade-up"];
      const vars = {
        ...preset,
        duration: readNumber(element.dataset.fsGsapDuration, 0.45),
        delay: readNumber(element.dataset.fsGsapDelay, 0),
        ease: element.dataset.fsGsapEase || "power2.out",
        clearProps: "transform,opacity"
      };

      const stagger = readNumber(element.dataset.fsGsapStagger, 0);
      if (stagger > 0 && element.children.length > 0) {
        window.gsap.from(element.children, { ...vars, stagger });
      } else {
        window.gsap.from(element, vars);
      }
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => init(document));
  } else {
    init(document);
  }

  if (window.FaststrapHtmx) {
    window.FaststrapHtmx.onSwap((event, elt) => init(elt || document));
  } else {
    document.addEventListener("htmx:afterSwap", (event) => init(event.target));
  }
  window.FaststrapGsap = { init };
})();
"""


def _validate_preset(preset: str) -> None:
    if preset not in VALID_GSAP_PRESETS:
        allowed = ", ".join(sorted(VALID_GSAP_PRESETS))
        msg = f"Unknown GSAP preset {preset!r}. Expected one of: {allowed}."
        raise ValueError(msg)


def gsap_assets(
    *,
    version: str = GSAP_VERSION,
    cdn_url: str | None = None,
    include_init: bool = True,
    defer: bool = True,
) -> tuple[Any, ...]:
    """Return script tags required by the Faststrap GSAP integration."""
    source = cdn_url or f"https://cdn.jsdelivr.net/npm/gsap@{version}/dist/gsap.min.js"
    assets: list[Any] = [Script(src=source, defer=defer)]
    if include_init:
        assets.append(Script(NotStr(GSAP_INIT_SCRIPT)))
    return tuple(assets)


def add_gsap(
    app: Any,
    *,
    version: str = GSAP_VERSION,
    cdn_url: str | None = None,
    include_init: bool = True,
    defer: bool = True,
) -> None:
    """Attach GSAP assets to a FastHTML app once.

    Use this only in projects that intentionally opt into richer client-side
    motion. Core Faststrap components do not depend on GSAP.
    """
    if getattr(app, "_faststrap_gsap_loaded", False):
        return

    app.hdrs.extend(
        gsap_assets(version=version, cdn_url=cdn_url, include_init=include_init, defer=defer)
    )
    app._faststrap_gsap_loaded = True


class Gsap:
    """Python-friendly GSAP motion presets for Faststrap components."""

    fade = "fade"
    fade_up = "fade-up"
    fade_down = "fade-down"
    slide_left = "slide-left"
    slide_right = "slide-right"
    scale = "scale"
    pop = "pop"

    @staticmethod
    def attrs(
        preset: GsapPreset = "fade-up",
        *,
        duration: float | None = None,
        delay: float | None = None,
        ease: str | None = None,
        stagger: float | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Return data attributes consumed by the Faststrap GSAP runtime."""
        _validate_preset(preset)
        attrs: dict[str, Any] = {"data_fs_gsap": preset}

        if duration is not None:
            attrs["data_fs_gsap_duration"] = str(duration)
        if delay is not None:
            attrs["data_fs_gsap_delay"] = str(delay)
        if ease is not None:
            attrs["data_fs_gsap_ease"] = ease
        if stagger is not None:
            attrs["data_fs_gsap_stagger"] = str(stagger)

        attrs.update(kwargs)
        return convert_attrs(attrs)

    reveal = attrs
    reveal_attrs = attrs

    @staticmethod
    def fade_attrs(**kwargs: Any) -> dict[str, Any]:
        """Return attributes for a fade reveal."""
        return Gsap.attrs("fade", **kwargs)

    @staticmethod
    def fade_up_attrs(**kwargs: Any) -> dict[str, Any]:
        """Return attributes for a fade-up reveal."""
        return Gsap.attrs("fade-up", **kwargs)

    @staticmethod
    def fade_down_attrs(**kwargs: Any) -> dict[str, Any]:
        """Return attributes for a fade-down reveal."""
        return Gsap.attrs("fade-down", **kwargs)

    @staticmethod
    def slide_left_attrs(**kwargs: Any) -> dict[str, Any]:
        """Return attributes for a slide-left reveal."""
        return Gsap.attrs("slide-left", **kwargs)

    @staticmethod
    def slide_right_attrs(**kwargs: Any) -> dict[str, Any]:
        """Return attributes for a slide-right reveal."""
        return Gsap.attrs("slide-right", **kwargs)

    @staticmethod
    def scale_attrs(**kwargs: Any) -> dict[str, Any]:
        """Return attributes for a scale reveal."""
        return Gsap.attrs("scale", **kwargs)

    @staticmethod
    def pop_attrs(**kwargs: Any) -> dict[str, Any]:
        """Return attributes for a pop reveal."""
        return Gsap.attrs("pop", **kwargs)

    @staticmethod
    def stagger_attrs(
        preset: GsapPreset = "fade-up",
        *,
        stagger: float = 0.08,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Return attributes for revealing a container's children in sequence."""
        return Gsap.attrs(preset, stagger=stagger, **kwargs)


def GsapReveal(
    *children: Any,
    preset: GsapPreset = "fade-up",
    duration: float | None = None,
    delay: float | None = None,
    ease: str | None = None,
    stagger: float | None = None,
    **kwargs: Any,
) -> Div:
    """Wrap children in a motion-enabled container."""
    user_cls = kwargs.pop("cls", "")
    attrs = Gsap.attrs(
        preset,
        duration=duration,
        delay=delay,
        ease=ease,
        stagger=stagger,
        **kwargs,
    )
    attrs["cls"] = merge_classes("faststrap-gsap-reveal", user_cls)
    return Div(*children, **attrs)


Motion = GsapReveal
