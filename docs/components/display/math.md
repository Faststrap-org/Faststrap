# Math

`@beta`

Render LaTeX math using KaTeX, with built-in support for chemistry notation via the `mhchem` extension.

---

## Quick Start

```python
from faststrap import Math

# Inline math
Math(r"\frac{a}{b}")

# Display math
Math(r"\int_{-\infty}^{\infty} e^{-x^2} dx", display_mode=True)

# Chemistry
Math(r"\ce{2H2 + O2 -> 2H2O}")

# Physics
Math(r"F = G \frac{m_1 m_2}{r^2}")
```

---

## Features

- LaTeX math rendering via KaTeX
- Chemistry support through `mhchem` (`\ce{}`, `\cee{}`, reaction arrows)
- Inline (`<span>`) and display (`<div>`) modes
- Optional error throwing for unsupported LaTeX
- Auto-renders on page load and after HTMX swaps
- Theme-aware via `set_component_defaults()`

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `latex` | `str` | required | LaTeX math source. |
| `display_mode` | `bool` | `False` | Render as block-level display math. |
| `throw_on_error` | `bool` | `False` | Raise on unsupported LaTeX instead of rendering fallback text. |
| `renderer` | `str` | `"katex"` | Rendering backend. Currently only `"katex"` is supported. |
| `**kwargs` | `Any` | | Extra HTML attributes for the wrapper element. |

---

## Usage Examples

### Inline Math

```python
from fasthtml.common import SectionHeader
from faststrap import Math

SectionHeader(
    "Physics",
    subtitle=(
        "Newton's law: "
        + Math(r"F = G \frac{m_1 m_2}{r^2}")
        + " governs gravitational attraction."
    ),
)
```

### Display Math

```python
from faststrap import Card, Math

Card(
    Card.Header("Gaussian Integral"),
    Card.Body(
        Math(
            r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}",
            display_mode=True,
        )
    ),
)
```

### Chemistry Reactions

```python
from faststrap import Card, Math

Card(
    Card.Header("Combustion"),
    Card.Body(
        Math(r"\ce{2H2 + O2 -> 2H2O}"),
        Math(r"\Delta H = -286 \text{ kJ/mol}", display_mode=True),
    ),
)
```

### Biology Statistics

```python
Math(r"p = \frac{n}{N} \times 100", cls="text-success")
Math(r"\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i", display_mode=True)
```

### Matrices and Linear Algebra

```python
Math(
    r"A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}",
    display_mode=True,
)
```

### With Markdown Documents

`Math` components can be embedded inside `Markdown` output:

```python
from faststrap import Markdown, Math

content = Markdown(
    "# Kinematics\n"
    + Math(r"s = ut + \frac{1}{2}at^2", display_mode=True)
)
```

When using `Markdown` with LaTeX, ensure KaTeX auto-render is configured
to scan `.faststrap-markdown` containers as well as `.faststrap-math`.

---

## Subject-Specific Patterns

| Subject | Example |
|---------|---------|
| **Physics** | `Math(r"\vec{F} = m\vec{a}")` |
| **Chemistry** | `Math(r"\ce{H2SO4 + 2NaOH -> Na2SO4 + 2H2O}")` |
| **Math** | `Math(r"\frac{d}{dx}\left( x^2 \right) = 2x", display_mode=True)` |
| **Biology** | `Math(r"P(A|B) = \frac{P(B|A)P(A)}{P(B)}")` |

---

## Configuration

### Global Defaults

```python
from faststrap import set_component_defaults

set_component_defaults("Math", display_mode=True, throw_on_error=True)
```

### KaTeX CSS and JS

Faststrap does not inject KaTeX automatically. Include it in your app:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
```

Or load via `add_bootstrap()` app headers.

---

## When to Use Math vs Markdown

| Use Case | Component |
|----------|-----------|
| Inline formulas in text | `Math` |
| Display equations | `Math(display_mode=True)` |
| Full documents with formulas | `Markdown` + KaTeX auto-render |
| Chemistry reactions | `Math` with `mhchem` syntax |
| Editable math input | `MathLive` (external) |

---

## Accessibility

KaTeX output is accessible by default. For additional screen-reader support,
consider pairing with MathJax's MathML output for complex documents.

---

## API Reference

::: faststrap.components.display.math.Math
    options:
        show_source: true
        heading_level: 4
