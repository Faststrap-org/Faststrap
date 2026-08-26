# MetricCard

`MetricCard` displays one important value with an optional delta and icon. Use it for dashboard KPIs, analytics summaries, and operational health cards.

## Quick Start

```python
from faststrap import Icon, MetricCard

MetricCard(
    "Revenue",
    "$42.8k",
    delta="+12.4%",
    delta_type="up",
    icon=Icon("graph-up"),
)
```

## Usage Scenarios

### Inline in a Row

```python
Row(
    Col(
        MetricCard(
            "Users",
            "2,847",
            delta="+18.2%",
            delta_type="up",
            variant="success",
            inverse=True,
        ),
        cols=12, cols_md=6, cols_lg=3,
    ),
    Col(
        MetricCard(
            "Bounce Rate",
            "24.3%",
            delta="-2.1%",
            delta_type="down",
            variant="danger",
        ),
        cols=12, cols_md=6, cols_lg=3,
    ),
    g=3,
)
```

### Without Icon

```python
MetricCard(
    "Orders",
    "384",
    delta="+5.1%",
    delta_type="up",
)
```

## Theming

`MetricCard` adds the `faststrap-metric-card` class, so you can style it with normal CSS or `theme_variant_css()`.

## Accessibility

- Ensure delta color differences are also visible via text or icon for color-blind users.
- Use `variant` and `inverse` consistently with your theme palette to maintain contrast ratios.

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `title` | `str` | required | Metric label. |
| `value` | `str \| int \| float` | required | Primary metric value. |
| `delta` | `str \| int \| float \| None` | `None` | Change text such as `+12%`. |
| `delta_type` | `"up" \| "down" \| "neutral"` | `"neutral"` | Delta color treatment. |
| `icon` | `Any \| None` | `None` | Optional icon or custom element. |
| `variant` | Bootstrap variant | `UNSET` | Card background variant. |
| `inverse` | `bool` | `False` | Use inverted text colors. |
| `icon_bg` | `str \| None` | `UNSET` | Icon wrapper background class. |
| `**kwargs` | `Any` | | Extra HTML attributes. |

## API Reference

::: faststrap.components.display.stat_card.MetricCard
