# SVG

Render SVG markup with optional sanitization.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <svg viewBox="0 0 120 32" width="120" height="32" aria-hidden="true">
      <rect x="0" y="4" width="120" height="24" fill="currentColor" opacity="0.1"></rect>
      <circle cx="16" cy="16" r="10" fill="currentColor"></circle>
      <text x="34" y="20" font-size="12">FastStrap</text>
    </svg>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Svg

Svg(
    "<svg viewBox='0 0 120 32' width='120' height='32'>...</svg>",
)
```
  </div>
</div>

---

## Sanitization

Sanitization is enabled by default and uses `bleach`. Install the optional extras:

```bash
pip install "faststrap[markdown]"
```

To allow raw SVG as-is, disable sanitization:

```python
Svg(svg_text, sanitize=False)
```

You can also pre-sanitize SVG strings with `render_svg` if you want to reuse output.

---

## Theming

Use `currentColor` inside your SVG to inherit text color and automatically adapt to light and dark themes.

---

## Security Notes

Only disable sanitization for trusted SVG markup. Treat user-provided SVG as untrusted input.

---

## API Reference

::: faststrap.components.display.svg.Svg
    options:
        show_source: true
        heading_level: 4
