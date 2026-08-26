# Grid

The `Container`, `Row`, and `Col` components implement the Bootstrap 5 responsive grid system.

## Quick Start

```python
Container(
    Row(
        Col("Column 1", span=6),
        Col("Column 2", span=6),
    )
)
```

## Usage Scenarios

### Fixed-Width Container

```python
Container(H1("Welcome"), P("Content"))
```

### Fluid Container

```python
Container(Row(...), fluid=True)
```

### Fluid Until Breakpoint

```python
Container(content, fluid="lg")
```

### Responsive Row

```python
Row(
    Col("A", span=12, cols_md=6, cols_lg=4),
    Col("B", span=12, cols_md=6, cols_lg=4),
    Col("C", span=12, cols_md=6, cols_lg=4),
)
```

### Column with Offset

```python
Col("Offset by 3", span=6, offset=3)
```

### Responsive Column Sizing

```python
Col("Content", span=12, md=6, lg=4, xl=3)
```

## Parameter Reference

### Container

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `*children` | `Any` | Required | Container content |
| `fluid` | `bool \| str` | `False` | Fluid container type (`True`/`"fluid"` for full-width, `"sm"`/`"md"`/`"lg"`/`"xl"`/`"xxl"` for fluid until breakpoint) |
| `**kwargs` | `Any` | - | Additional HTML attributes |

### Row

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `*children` | `Any` | Required | Row content (typically Col components) |
| `cols` | `int \| None` | `None` | Number of columns for all breakpoints (1-12) |
| `cols_sm` | `int \| None` | `None` | Columns for small devices (≥576px) |
| `cols_md` | `int \| None` | `None` | Columns for medium devices (≥768px) |
| `cols_lg` | `int \| None` | `None` | Columns for large devices (≥992px) |
| `cols_xl` | `int \| None` | `None` | Columns for extra large devices (≥1200px) |
| `cols_xxl` | `int \| None` | `None` | Columns for extra extra large devices (≥1400px) |
| `**kwargs` | `Any` | - | Additional HTML attributes |

### Col

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `*children` | `Any` | Required | Column content |
| `span` | `int \| bool` | `True` | Column span (1-12) or `True` for auto-width |
| `sm` | `int \| None` | `None` | Span for small devices (≥576px) |
| `md` | `int \| None` | `None` | Span for medium devices (≥768px) |
| `lg` | `int \| None` | `None` | Span for large devices (≥992px) |
| `xl` | `int \| None` | `None` | Span for extra large devices (≥1200px) |
| `xxl` | `int \| None` | `None` | Span for extra extra large devices (≥1400px) |
| `offset` | `int \| None` | `None` | Offset columns (0-11) |
| `offset_sm` | `int \| None` | `None` | Offset for small devices |
| `offset_md` | `int \| None` | `None` | Offset for medium devices |
| `offset_lg` | `int \| None` | `None` | Offset for large devices |
| `offset_xl` | `int \| None` | `None` | Offset for extra large devices |
| `offset_xxl` | `int \| None` | `None` | Offset for extra extra large devices |
| `**kwargs` | `Any` | - | Additional HTML attributes |

## Accessibility

- Grid is purely structural and does not add accessibility barriers.
- Content within columns maintains proper heading hierarchy.

## API Reference

::: faststrap.components.layout.grid.Container
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.layout.grid.Row
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.layout.grid.Col
    options:
        show_source: true
        heading_level: 4
