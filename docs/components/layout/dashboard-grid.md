# DashboardGrid

Responsive grid layout for dashboards with consistent spacing and card sizing.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div style="display: grid; gap: 1rem; grid-template-columns: repeat(3, minmax(0, 1fr));">
      <div class="card"><div class="card-body">Revenue: $12k</div></div>
      <div class="card"><div class="card-body">Users: 2,410</div></div>
      <div class="card"><div class="card-body">Trials: 312</div></div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import DashboardGrid, StatCard

DashboardGrid(
    StatCard("Revenue", "$12k"),
    StatCard("Users", "2,410"),
    cols=3,
    gap=1.5,
)
```
  </div>
</div>

---

## Auto Fit

When `cols` is not provided, the grid uses auto-fit sizing based on `min_card_width`.

```python
DashboardGrid(
    *cards,
    min_card_width=280,
)
```

---

## Dense Packing

```python
DashboardGrid(*cards, dense=True)
```

---

## API Reference

::: faststrap.components.layout.dashboard_grid.DashboardGrid
    options:
        show_source: true
        heading_level: 4
