# Dashboard Grid

The `DashboardGrid` component creates a responsive CSS grid layout ideal for dashboards and card-based interfaces.

## Quick Start

```python
DashboardGrid(
    StatCard("Revenue", "$12K", "+5%", delta_color="success"),
    StatCard("Users", "1.2K", "+12%"),
    StatCard("Orders", "456", "+3%"),
    cols=3,
)
```

## Usage Scenarios

### Auto-Fit Cards

```python
DashboardGrid(
    Card("A"),
    Card("B"),
    Card("C"),
    min_card_width=240,
)
```

### Dense Grid

```python
DashboardGrid(
    Card("A"),
    Card("B"),
    Card("C"),
    Card("D"),
    cols=2,
    dense=True,
)
```

### Custom Gap

```python
DashboardGrid(
    StatCard("CPU", "45%", "+2%"),
    StatCard("RAM", "62%", "-1%"),
    gap=2,
)
```

## Parameter Reference

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `*children` | `Any` | Required | Grid items (typically Card components) |
| `cols` | `int \| None` | UNSET | Fixed number of columns. When `None`, uses `auto-fit` with `min_card_width`. |
| `gap` | `str \| int \| float` | `1.5` | Gap between items (`"1.5rem"`, `16`, etc.) |
| `min_card_width` | `str \| int \| float` | `240` | Minimum card width for auto-fit mode |
| `dense` | `bool` | `False` | Enable dense packing (`grid-auto-flow: dense`) |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Accessibility

- Grid is purely structural.
- Content within cards maintains proper heading hierarchy.

## API Reference

::: faststrap.components.layout.dashboard_grid.DashboardGrid
    options:
        show_source: true
        heading_level: 4
