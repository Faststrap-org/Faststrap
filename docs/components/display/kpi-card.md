# KPICard

`KPICard` groups multiple related metrics inside one compact card.

## Quick Start

```python
from faststrap import KPICard

KPICard(
    "Campaign Health",
    metrics=[
        ("Leads", "1,240", "+18%", "up"),
        ("CAC", "$42", "-6%", "up"),
        ("Churn", "2.1%", "+0.4%", "down"),
    ],
    columns=3,
)
```

## Metric Tuple Format

Each metric must include at least `(label, value)`.

```python
("Revenue", "$82k")
("Revenue", "$82k", "+12%", "up")
```

The optional fourth value must be one of `up`, `down`, or `neutral`. Unknown values are treated as `neutral`.

## Usage Scenarios

### Dashboard Grid

```python
DashboardGrid(
    KPICard(
        "Revenue",
        [
            ("Today", "$4,200", "+3.2%", "up"),
            ("MTD", "$82k", "+12%", "up"),
            ("Customers", "1,247", "+8%", "up"),
        ],
        columns=3,
        variant="primary",
        inverse=True,
    ),
    cols=12,
)
```

### Dark Mode

```python
KPICard(
    "Server Health",
    [
        ("CPU", "42%", "-5%", "up"),
        ("Memory", "6.2 GB", "+0.3 GB", "down"),
        ("Uptime", "99.98%", "+0.01%", "up"),
    ],
    columns=3,
    inverse=True,
)
```

## Theming

`KPICard` adds the `faststrap-kpi-card` class, so you can style it with normal CSS or `theme_variant_css()`.

## Accessibility

- `KPICard` uses semantic heading markup for the title.
- Ensure sufficient color contrast for delta values, especially when using `inverse=True`.

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `title` | `str` | required | Card label. |
| `metrics` | `Sequence[Sequence[Any]]` | required | Metric tuples. |
| `columns` | `int` | `2` | Number of metric columns. Must be at least `1`. |
| `variant` | Bootstrap variant | `UNSET` | Card background variant. |
| `inverse` | `bool` | `False` | Use inverted text colors. |
| `**kwargs` | `Any` | | Extra HTML attributes. |

## API Reference

::: faststrap.components.display.stat_card.KPICard

