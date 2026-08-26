# Status Badge

`StatusBadge` builds on `Badge` with semantic status names, optional icons, and optional dot indicators.

Use it anywhere a status label should read consistently across dashboards, tables, cards, and activity feeds.

## Import

```python
from faststrap import StatusBadge, BadgeGroup
```

## Basic Usage

```python
StatusBadge("Live", status="success")
StatusBadge("Pending", status="pending")
StatusBadge("Failed", status="error")
```

## Dot Style

```python
StatusBadge("Pending", status="pending", show_dot=True)
```

## Badge Groups

```python
BadgeGroup(
    StatusBadge("Live", status="success"),
    StatusBadge("Beta", status="info"),
)
```

## Usage Scenarios

### Data Table Row

```python
DataTable(
    data=[
        {"name": "Alice", "status": "active"},
        {"name": "Bob", "status": "pending"},
    ],
    columns=["name", "status"],
    render_status=lambda row: StatusBadge(
        row["status"].title(),
        status=row["status"],
    ),
)
```

### Card Footer

```python
Card(
    Card.Body("Project deployment completed."),
    Card.Footer(
        StatusBadge("Deployed", status="success"),
        StatusBadge("Reviewed", status="info"),
    ),
)
```

## Custom Icons

```python
StatusBadge(
    "Custom",
    status="warning",
    icon="lightning-fill",
    show_dot=True,
)
```

## Status Mapping

| Status | Default Variant | Default Icon |
| :--- | :--- | :--- |
| `success` | `success` | `check-circle-fill` |
| `error` | `danger` | `x-circle-fill` |
| `warning` | `warning` | `exclamation-triangle-fill` |
| `info` | `info` | `info-circle-fill` |
| `pending` | `warning` | `clock-fill` |
| `neutral` | `secondary` | none |

## Accessibility

- `StatusBadge` uses semantic color/status mapping; ensure sufficient contrast for dot indicators.
- The `pill` option increases the touch target size for mobile UIs.

## Parameters

| Param | Type | Description |
| :--- | :--- | :--- |
| `label` | `str` | Badge text. |
| `status` | `success | error | warning | info | pending | neutral` | Semantic status name. |
| `variant` | `str | None` | Bootstrap variant override. |
| `icon` | `str | None` | Bootstrap icon override. Set `""` to suppress the default icon. |
| `show_dot` | `bool` | Show a dot before the label. |
| `pill` | `bool` | Use rounded pill styling. |

::: faststrap.components.display.status_badge.StatusBadge
    options:
        show_source: true
        heading_level: 3

::: faststrap.components.display.status_badge.BadgeGroup
    options:
        show_source: true
        heading_level: 3
