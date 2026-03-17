# Chart

`Chart` renders Matplotlib, Plotly, Altair, or raw SVG and HTML outputs in a single component.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <svg viewBox="0 0 220 80" width="100%" height="80" aria-hidden="true">
      <polyline fill="none" stroke="currentColor" stroke-width="2" points="0,60 40,35 80,45 120,20 160,30 220,10"></polyline>
    </svg>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import Chart

Chart(fig, backend="matplotlib")
```
  </div>
</div>

---

## Plotly and Altair

```python
Chart(fig, backend="plotly", include_js=True)
```

If your figure object exposes `to_html()`, `Chart` can render it directly.

---

## Raw SVG or HTML

Raw strings require explicit opt-in for safety:

```python
Chart("<svg>...</svg>", backend="svg", allow_unsafe_html=True)
```

---

## Backend Inference

If you pass a Matplotlib or Plotly/Altair object, `Chart` will infer the backend automatically. Raw strings always require `backend` to be specified.

---

## Sizing and Responsiveness

- `responsive=True` adds `w-100` to the wrapper.
- Use `width` and `height` for fixed sizing.

```python
Chart(fig, backend="matplotlib", width=480, height=320)
```

---

## Theming

`Chart` does not auto-theme plots. Use your chart library to set colors for dark mode and match your theme palette.

---

## Security Notes

If you render raw SVG or HTML, only use trusted content. Set `allow_unsafe_html=True` only when you control the source.

---

## API Reference

::: faststrap.components.display.chart.Chart
    options:
        show_source: true
        heading_level: 4
